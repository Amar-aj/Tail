using Microsoft.JSInterop;
using System.Text.Json;

namespace Tail.Blazor.Core.Theme;

/// <summary>
/// Service for managing theme settings with localStorage persistence
/// </summary>
public class ThemeService
{
    private readonly IJSRuntime _jsRuntime;
    private const string THEME_KEY = "tail-blazor-theme-settings";
    
    public event Action? OnThemeChanged;
    
    public ThemeSettings CurrentSettings { get; private set; } = new();

    public ThemeService(IJSRuntime jsRuntime)
    {
        _jsRuntime = jsRuntime;
    }

    /// <summary>
    /// Load theme settings from localStorage
    /// </summary>
    public async Task<ThemeSettings> LoadThemeAsync()
    {
        try
        {
            var json = await _jsRuntime.InvokeAsync<string>("localStorage.getItem", THEME_KEY);
            if (!string.IsNullOrEmpty(json))
            {
                CurrentSettings = JsonSerializer.Deserialize<ThemeSettings>(json) ?? new ThemeSettings();
            }
            else
            {
                // Default to Ocean theme, Light mode
                CurrentSettings = new ThemeSettings
                {
                    PresetName = "Ocean",
                    Mode = "Light",
                    Colors = ThemePresets.Ocean.Light
                };
                await SaveThemeAsync();
            }
        }
        catch
        {
            CurrentSettings = new ThemeSettings
            {
                PresetName = "Ocean",
                Mode = "Light",
                Colors = ThemePresets.Ocean.Light
            };
        }

        return CurrentSettings;
    }

    /// <summary>
    /// Save theme settings to localStorage
    /// </summary>
    public async Task SaveThemeAsync()
    {
        try
        {
            var json = JsonSerializer.Serialize(CurrentSettings);
            await _jsRuntime.InvokeVoidAsync("localStorage.setItem", THEME_KEY, json);
            OnThemeChanged?.Invoke();
        }
        catch
        {
            // Handle error silently
        }
    }

    /// <summary>
    /// Apply a predefined theme preset
    /// </summary>
    public async Task ApplyPresetAsync(string presetName, string mode = "Light")
    {
        CurrentSettings.PresetName = presetName;
        CurrentSettings.Mode = mode;
        CurrentSettings.IsCustom = false;
        
        // Get the preset colors
        var preset = ThemePresets.All.FirstOrDefault(p => p.Name == presetName);
        if (preset != null)
        {
            var colors = mode == "Dark" ? preset.Dark : preset.Light;
            CurrentSettings.Colors = colors;
        }

        await SaveThemeAsync();
        await ApplyThemeToDocumentAsync();
    }

    /// <summary>
    /// Apply custom theme colors
    /// </summary>
    public async Task ApplyCustomThemeAsync(ThemeColors colors, string mode = "Light")
    {
        CurrentSettings.IsCustom = true;
        CurrentSettings.Mode = mode;
        CurrentSettings.PresetName = "Custom";
        CurrentSettings.Colors = colors;

        await SaveThemeAsync();
        await ApplyThemeToDocumentAsync();
    }

    /// <summary>
    /// Toggle between light and dark mode
    /// </summary>
    public async Task ToggleModeAsync()
    {
        CurrentSettings.Mode = CurrentSettings.Mode == "Light" ? "Dark" : "Light";
        
        if (!CurrentSettings.IsCustom)
        {
            // Reload preset colors for new mode
            var preset = ThemePresets.All.FirstOrDefault(p => p.Name == CurrentSettings.PresetName);
            if (preset != null)
            {
                CurrentSettings.Colors = CurrentSettings.Mode == "Dark" ? preset.Dark : preset.Light;
            }
        }

        await SaveThemeAsync();
        await ApplyThemeToDocumentAsync();
    }

    /// <summary>
    /// Apply theme to document root element
    /// </summary>
    private async Task ApplyThemeToDocumentAsync()
    {
        try
        {
            var isDark = CurrentSettings.Mode == "Dark";
            var colors = CurrentSettings.Colors;

            // Create JavaScript to apply theme
            var script = $@"
                (function() {{
                    const root = document.documentElement;
                    
                    // Toggle dark class
                    if ({(isDark ? "true" : "false")}) {{
                        root.classList.add('dark');
                    }} else {{
                        root.classList.remove('dark');
                    }}
                    
                    // Apply CSS variables
                    root.style.setProperty('--color-primary', '{colors.Primary}');
                    root.style.setProperty('--color-secondary', '{colors.Secondary}');
                    root.style.setProperty('--color-accent', '{colors.Accent}');
                    root.style.setProperty('--color-success', '{colors.Success}');
                    root.style.setProperty('--color-warning', '{colors.Warning}');
                    root.style.setProperty('--color-danger', '{colors.Danger}');
                    root.style.setProperty('--color-info', '{colors.Info}');
                    root.style.setProperty('--color-background', '{colors.Background}');
                    root.style.setProperty('--color-surface', '{colors.Surface}');
                    root.style.setProperty('--color-text-primary', '{colors.TextPrimary}');
                    root.style.setProperty('--color-text-secondary', '{colors.TextSecondary}');
                    root.style.setProperty('--color-border', '{colors.Border}');
                    
                    // Also update body background
                    document.body.style.backgroundColor = '{colors.Background}';
                    document.body.style.color = '{colors.TextPrimary}';
                    
                    console.log('Theme applied: {CurrentSettings.PresetName} - {CurrentSettings.Mode}');
                }})();
            ";

            await _jsRuntime.InvokeVoidAsync("eval", script);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error applying theme: {ex.Message}");
        }
    }

    /// <summary>
    /// Get all available theme presets
    /// </summary>
    public List<ThemePreset> GetPresets()
    {
        return ThemePresets.All;
    }

    /// <summary>
    /// Initialize theme on app startup
    /// </summary>
    public async Task InitializeAsync()
    {
        await LoadThemeAsync();
        await ApplyThemeToDocumentAsync();
    }
}

/// <summary>
/// Theme settings stored in localStorage
/// </summary>
public class ThemeSettings
{
    public string PresetName { get; set; } = "Ocean";
    public string Mode { get; set; } = "Light";
    public bool IsCustom { get; set; } = false;
    public ThemeColors Colors { get; set; } = ThemePresets.Ocean.Light;
}
