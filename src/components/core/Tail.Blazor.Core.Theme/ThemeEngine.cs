using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Core.Theme;

/// <summary>
/// Theme engine for Tail.Blazor with support for dynamic colors, gradients, and custom themes.
/// </summary>
public class ThemeEngine
{
    private readonly Dictionary<string, string> _cssVariables = new();
    private ThemeMode _currentMode = ThemeMode.Light;
    private ThemePalette _currentPalette = ThemePalette.Default;

    /// <summary>
    /// Gets or sets the current theme mode.
    /// </summary>
    public ThemeMode Mode
    {
        get => _currentMode;
        set
        {
            _currentMode = value;
            UpdateTheme();
        }
    }

    /// <summary>
    /// Gets or sets the current theme palette.
    /// </summary>
    public ThemePalette Palette
    {
        get => _currentPalette;
        set
        {
            _currentPalette = value;
            UpdateTheme();
        }
    }

    /// <summary>
    /// Gets or sets custom primary color.
    /// </summary>
    public string? PrimaryColor { get; set; }

    /// <summary>
    /// Gets or sets custom secondary color.
    /// </summary>
    public string? SecondaryColor { get; set; }

    /// <summary>
    /// Gets or sets custom accent color.
    /// </summary>
    public string? AccentColor { get; set; }

    /// <summary>
    /// Gets or sets whether to use gradients.
    /// </summary>
    public bool UseGradients { get; set; } = true;

    /// <summary>
    /// Gets or sets gradient direction (e.g., "to-r", "to-br", "to-r").
    /// </summary>
    public string GradientDirection { get; set; } = "to-r";

    /// <summary>
    /// Gets CSS variables as a dictionary.
    /// </summary>
    public Dictionary<string, string> GetCssVariables()
    {
        return new Dictionary<string, string>(_cssVariables);
    }

    /// <summary>
    /// Gets CSS variables as a style string.
    /// </summary>
    public string GetCssVariablesString()
    {
        return string.Join("; ", _cssVariables.Select(kvp => $"--{kvp.Key}: {kvp.Value}"));
    }

    /// <summary>
    /// Sets a custom CSS variable.
    /// </summary>
    public void SetVariable(string name, string value)
    {
        _cssVariables[name] = value;
    }

    /// <summary>
    /// Gets a CSS variable value.
    /// </summary>
    public string? GetVariable(string name)
    {
        return _cssVariables.TryGetValue(name, out var value) ? value : null;
    }

    /// <summary>
    /// Applies a custom color palette.
    /// </summary>
    public void ApplyPalette(CustomColorPalette palette)
    {
        PrimaryColor = palette.Primary;
        SecondaryColor = palette.Secondary;
        AccentColor = palette.Accent;
        UpdateTheme();
    }

    /// <summary>
    /// Applies a gradient theme.
    /// </summary>
    public void ApplyGradientTheme(string primaryStart, string primaryEnd, string? secondaryStart = null, string? secondaryEnd = null)
    {
        UseGradients = true;
        SetVariable("primary-gradient-start", primaryStart);
        SetVariable("primary-gradient-end", primaryEnd);
        if (secondaryStart != null && secondaryEnd != null)
        {
            SetVariable("secondary-gradient-start", secondaryStart);
            SetVariable("secondary-gradient-end", secondaryEnd);
        }
        UpdateTheme();
    }

    private void UpdateTheme()
    {
        var colors = GetColorPalette();
        
        // Base colors
        SetVariable("primary", colors.Primary);
        SetVariable("primary-dark", colors.PrimaryDark);
        SetVariable("primary-light", colors.PrimaryLight);
        SetVariable("secondary", colors.Secondary);
        SetVariable("accent", colors.Accent);
        
        // Background colors
        SetVariable("bg-primary", _currentMode == ThemeMode.Dark ? "#1a1a1a" : "#ffffff");
        SetVariable("bg-secondary", _currentMode == ThemeMode.Dark ? "#2a2a2a" : "#f5f5f5");
        SetVariable("bg-tertiary", _currentMode == ThemeMode.Dark ? "#3a3a3a" : "#e5e5e5");
        
        // Text colors
        SetVariable("text-primary", _currentMode == ThemeMode.Dark ? "#ffffff" : "#1a1a1a");
        SetVariable("text-secondary", _currentMode == ThemeMode.Dark ? "#b0b0b0" : "#6b6b6b");
        SetVariable("text-muted", _currentMode == ThemeMode.Dark ? "#808080" : "#9b9b9b");
        
        // Border colors
        SetVariable("border-color", _currentMode == ThemeMode.Dark ? "#404040" : "#e0e0e0");
        
        // Gradient support
        if (UseGradients && PrimaryColor != null)
        {
            var gradientEnd = DarkenColor(PrimaryColor, 0.2);
            SetVariable("primary-gradient", $"linear-gradient({GradientDirection}, {PrimaryColor}, {gradientEnd})");
        }
        
        // State colors
        SetVariable("success", "#10b981");
        SetVariable("warning", "#f59e0b");
        SetVariable("danger", "#ef4444");
        SetVariable("info", "#3b82f6");
    }

    private ColorPalette GetColorPalette()
    {
        if (PrimaryColor != null || SecondaryColor != null)
        {
            return new ColorPalette
            {
                Primary = PrimaryColor ?? "#3b82f6",
                PrimaryDark = DarkenColor(PrimaryColor ?? "#3b82f6", 0.2),
                PrimaryLight = LightenColor(PrimaryColor ?? "#3b82f6", 0.2),
                Secondary = SecondaryColor ?? "#8b5cf6",
                Accent = AccentColor ?? "#ec4899"
            };
        }

        return _currentPalette switch
        {
            ThemePalette.Blue => new ColorPalette { Primary = "#3b82f6", PrimaryDark = "#2563eb", PrimaryLight = "#60a5fa", Secondary = "#8b5cf6", Accent = "#ec4899" },
            ThemePalette.Green => new ColorPalette { Primary = "#10b981", PrimaryDark = "#059669", PrimaryLight = "#34d399", Secondary = "#06b6d4", Accent = "#f59e0b" },
            ThemePalette.Purple => new ColorPalette { Primary = "#8b5cf6", PrimaryDark = "#7c3aed", PrimaryLight = "#a78bfa", Secondary = "#ec4899", Accent = "#f59e0b" },
            ThemePalette.Red => new ColorPalette { Primary = "#ef4444", PrimaryDark = "#dc2626", PrimaryLight = "#f87171", Secondary = "#f59e0b", Accent = "#ec4899" },
            ThemePalette.Orange => new ColorPalette { Primary = "#f59e0b", PrimaryDark = "#d97706", PrimaryLight = "#fbbf24", Secondary = "#ef4444", Accent = "#ec4899" },
            _ => new ColorPalette { Primary = "#3b82f6", PrimaryDark = "#2563eb", PrimaryLight = "#60a5fa", Secondary = "#8b5cf6", Accent = "#ec4899" }
        };
    }

    private static string DarkenColor(string hex, double amount)
    {
        var rgb = HexToRgb(hex);
        return RgbToHex(
            Math.Max(0, rgb.r - (int)(rgb.r * amount)),
            Math.Max(0, rgb.g - (int)(rgb.g * amount)),
            Math.Max(0, rgb.b - (int)(rgb.b * amount))
        );
    }

    private static string LightenColor(string hex, double amount)
    {
        var rgb = HexToRgb(hex);
        return RgbToHex(
            Math.Min(255, rgb.r + (int)((255 - rgb.r) * amount)),
            Math.Min(255, rgb.g + (int)((255 - rgb.g) * amount)),
            Math.Min(255, rgb.b + (int)((255 - rgb.b) * amount))
        );
    }

    private static (int r, int g, int b) HexToRgb(string hex)
    {
        hex = hex.TrimStart('#');
        if (hex.Length == 3)
            hex = $"{hex[0]}{hex[0]}{hex[1]}{hex[1]}{hex[2]}{hex[2]}";
        return (
            Convert.ToInt32(hex.Substring(0, 2), 16),
            Convert.ToInt32(hex.Substring(2, 2), 16),
            Convert.ToInt32(hex.Substring(4, 2), 16)
        );
    }

    private static string RgbToHex(int r, int g, int b)
    {
        return $"#{r:X2}{g:X2}{b:X2}";
    }
}

public enum ThemeMode
{
    Light,
    Dark,
    Custom
}

public enum ThemePalette
{
    Default,
    Blue,
    Green,
    Purple,
    Red,
    Orange
}

public class CustomColorPalette
{
    public string Primary { get; set; } = "#3b82f6";
    public string Secondary { get; set; } = "#8b5cf6";
    public string Accent { get; set; } = "#ec4899";
}

internal class ColorPalette
{
    public string Primary { get; set; } = "#3b82f6";
    public string PrimaryDark { get; set; } = "#2563eb";
    public string PrimaryLight { get; set; } = "#60a5fa";
    public string Secondary { get; set; } = "#8b5cf6";
    public string Accent { get; set; } = "#ec4899";
}

