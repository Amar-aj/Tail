namespace Tail.Blazor.Core.Theme;

/// <summary>
/// Predefined theme presets with light and dark mode variations
/// </summary>
public class ThemePreset
{
    public string Name { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public ThemeColors Light { get; set; } = new();
    public ThemeColors Dark { get; set; } = new();
}

/// <summary>
/// Color scheme for a theme
/// </summary>
public class ThemeColors
{
    public string Primary { get; set; } = "#3b82f6";
    public string Secondary { get; set; } = "#8b5cf6";
    public string Accent { get; set; } = "#ec4899";
    public string Success { get; set; } = "#10b981";
    public string Warning { get; set; } = "#f59e0b";
    public string Danger { get; set; } = "#ef4444";
    public string Info { get; set; } = "#3b82f6";
    public string Background { get; set; } = "#ffffff";
    public string Surface { get; set; } = "#f9fafb";
    public string TextPrimary { get; set; } = "#111827";
    public string TextSecondary { get; set; } = "#6b7280";
    public string Border { get; set; } = "#e5e7eb";
}

/// <summary>
/// Built-in theme presets
/// </summary>
public static class ThemePresets
{
    public static ThemePreset Ocean => new()
    {
        Name = "Ocean",
        Description = "Cool blue ocean vibes",
        Light = new ThemeColors
        {
            Primary = "#0ea5e9",
            Secondary = "#06b6d4",
            Accent = "#8b5cf6",
            Background = "#ffffff",
            Surface = "#f0f9ff",
            TextPrimary = "#0c4a6e",
            TextSecondary = "#475569",
            Border = "#bae6fd"
        },
        Dark = new ThemeColors
        {
            Primary = "#38bdf8",
            Secondary = "#22d3ee",
            Accent = "#a78bfa",
            Background = "#0c1821",
            Surface = "#1e293b",
            TextPrimary = "#f0f9ff",
            TextSecondary = "#cbd5e1",
            Border = "#334155"
        }
    };

    public static ThemePreset Forest => new()
    {
        Name = "Forest",
        Description = "Natural green forest theme",
        Light = new ThemeColors
        {
            Primary = "#10b981",
            Secondary = "#059669",
            Accent = "#f59e0b",
            Background = "#ffffff",
            Surface = "#f0fdf4",
            TextPrimary = "#064e3b",
            TextSecondary = "#475569",
            Border = "#bbf7d0"
        },
        Dark = new ThemeColors
        {
            Primary = "#34d399",
            Secondary = "#10b981",
            Accent = "#fbbf24",
            Background = "#0a1f0f",
            Surface = "#1e3a2a",
            TextPrimary = "#d1fae5",
            TextSecondary = "#a7f3d0",
            Border = "#065f46"
        }
    };

    public static ThemePreset Sunset => new()
    {
        Name = "Sunset",
        Description = "Warm sunset colors",
        Light = new ThemeColors
        {
            Primary = "#f97316",
            Secondary = "#f59e0b",
            Accent = "#ec4899",
            Background = "#ffffff",
            Surface = "#fff7ed",
            TextPrimary = "#7c2d12",
            TextSecondary = "#78350f",
            Border = "#fed7aa"
        },
        Dark = new ThemeColors
        {
            Primary = "#fb923c",
            Secondary = "#fbbf24",
            Accent = "#f472b6",
            Background = "#1a0f0a",
            Surface = "#3a2618",
            TextPrimary = "#ffedd5",
            TextSecondary = "#fed7aa",
            Border = "#78350f"
        }
    };

    public static ThemePreset Purple => new()
    {
        Name = "Purple Haze",
        Description = "Rich purple gradient theme",
        Light = new ThemeColors
        {
            Primary = "#8b5cf6",
            Secondary = "#a78bfa",
            Accent = "#ec4899",
            Background = "#ffffff",
            Surface = "#faf5ff",
            TextPrimary = "#581c87",
            TextSecondary = "#6b7280",
            Border = "#e9d5ff"
        },
        Dark = new ThemeColors
        {
            Primary = "#a78bfa",
            Secondary = "#c4b5fd",
            Accent = "#f472b6",
            Background = "#1a0f2e",
            Surface = "#2e1a47",
            TextPrimary = "#f3e8ff",
            TextSecondary = "#ddd6fe",
            Border = "#581c87"
        }
    };

    public static ThemePreset Midnight => new()
    {
        Name = "Midnight",
        Description = "Deep blue midnight theme",
        Light = new ThemeColors
        {
            Primary = "#3b82f6",
            Secondary = "#6366f1",
            Accent = "#06b6d4",
            Background = "#ffffff",
            Surface = "#eff6ff",
            TextPrimary = "#1e3a8a",
            TextSecondary = "#475569",
            Border = "#bfdbfe"
        },
        Dark = new ThemeColors
        {
            Primary = "#60a5fa",
            Secondary = "#818cf8",
            Accent = "#22d3ee",
            Background = "#0f1419",
            Surface = "#1e293b",
            TextPrimary = "#dbeafe",
            TextSecondary = "#93c5fd",
            Border = "#1e3a8a"
        }
    };

    public static List<ThemePreset> All => new()
    {
        Ocean,
        Forest,
        Sunset,
        Purple,
        Midnight
    };
}
