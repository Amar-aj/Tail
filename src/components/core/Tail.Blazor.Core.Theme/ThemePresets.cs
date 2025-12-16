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
    public string Surface2 { get; set; } = "#f3f4f6";
    public string Surface3 { get; set; } = "#e5e7eb";
    public string TextPrimary { get; set; } = "#111827";
    public string TextSecondary { get; set; } = "#6b7280";
    public string TextMuted { get; set; } = "#9ca3af";
    public string Border { get; set; } = "#e5e7eb";
    public string Divider { get; set; } = "#d1d5db";
    public string ShadowSm { get; set; } = "0 1px 2px 0 rgba(0, 0, 0, 0.05)";
    public string ShadowMd { get; set; } = "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)";
    public string ShadowLg { get; set; } = "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)";
    public string RadiusSm { get; set; } = "0.25rem";
    public string RadiusMd { get; set; } = "0.5rem";
    public string RadiusLg { get; set; } = "0.75rem";
    public string TransitionFast { get; set; } = "150ms";
    public string TransitionNormal { get; set; } = "300ms";
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
            Surface2 = "#e0f2fe",
            Surface3 = "#bae6fd",
            TextPrimary = "#0c4a6e",
            TextSecondary = "#475569",
            TextMuted = "#64748b",
            Border = "#bae6fd",
            Divider = "#94a3b8"
        },
        Dark = new ThemeColors
        {
            Primary = "#38bdf8",
            Secondary = "#22d3ee",
            Accent = "#a78bfa",
            Background = "#0c1821",
            Surface = "#1e293b",
            Surface2 = "#334155",
            Surface3 = "#475569",
            TextPrimary = "#f0f9ff",
            TextSecondary = "#cbd5e1",
            TextMuted = "#94a3b8",
            Border = "#334155",
            Divider = "#475569"
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
            Surface2 = "#dcfce7",
            Surface3 = "#bbf7d0",
            TextPrimary = "#064e3b",
            TextSecondary = "#475569",
            TextMuted = "#64748b",
            Border = "#bbf7d0",
            Divider = "#94a3b8"
        },
        Dark = new ThemeColors
        {
            Primary = "#34d399",
            Secondary = "#10b981",
            Accent = "#fbbf24",
            Background = "#0a1f0f",
            Surface = "#1e3a2a",
            Surface2 = "#065f46",
            Surface3 = "#047857",
            TextPrimary = "#d1fae5",
            TextSecondary = "#a7f3d0",
            TextMuted = "#6ee7b7",
            Border = "#065f46",
            Divider = "#047857"
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
            Surface2 = "#ffedd5",
            Surface3 = "#fed7aa",
            TextPrimary = "#7c2d12",
            TextSecondary = "#78350f",
            TextMuted = "#a16207",
            Border = "#fed7aa",
            Divider = "#fbbf24"
        },
        Dark = new ThemeColors
        {
            Primary = "#fb923c",
            Secondary = "#fbbf24",
            Accent = "#f472b6",
            Background = "#1a0f0a",
            Surface = "#3a2618",
            Surface2 = "#78350f",
            Surface3 = "#92400e",
            TextPrimary = "#ffedd5",
            TextSecondary = "#fed7aa",
            TextMuted = "#fcd34d",
            Border = "#78350f",
            Divider = "#92400e"
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
            Surface2 = "#f3e8ff",
            Surface3 = "#e9d5ff",
            TextPrimary = "#581c87",
            TextSecondary = "#6b7280",
            TextMuted = "#9ca3af",
            Border = "#e9d5ff",
            Divider = "#d1d5db"
        },
        Dark = new ThemeColors
        {
            Primary = "#a78bfa",
            Secondary = "#c4b5fd",
            Accent = "#f472b6",
            Background = "#1a0f2e",
            Surface = "#2e1a47",
            Surface2 = "#4c1d95",
            Surface3 = "#581c87",
            TextPrimary = "#f3e8ff",
            TextSecondary = "#ddd6fe",
            TextMuted = "#c4b5fd",
            Border = "#581c87",
            Divider = "#6b21a8"
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
            Surface2 = "#dbeafe",
            Surface3 = "#bfdbfe",
            TextPrimary = "#1e3a8a",
            TextSecondary = "#475569",
            TextMuted = "#64748b",
            Border = "#bfdbfe",
            Divider = "#94a3b8"
        },
        Dark = new ThemeColors
        {
            Primary = "#60a5fa",
            Secondary = "#818cf8",
            Accent = "#22d3ee",
            Background = "#0f1419",
            Surface = "#1e293b",
            Surface2 = "#334155",
            Surface3 = "#475569",
            TextPrimary = "#dbeafe",
            TextSecondary = "#93c5fd",
            TextMuted = "#64748b",
            Border = "#1e3a8a",
            Divider = "#334155"
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
