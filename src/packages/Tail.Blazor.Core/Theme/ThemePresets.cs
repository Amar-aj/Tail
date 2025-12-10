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
/// Complete color scheme for a theme with enhanced UI/UX variables
/// </summary>
public class ThemeColors
{
    // Primary colors
    public string Primary { get; set; } = "#3b82f6";
    public string Secondary { get; set; } = "#8b5cf6";
    public string Accent { get; set; } = "#ec4899";
    
    // State colors
    public string Success { get; set; } = "#10b981";
    public string Warning { get; set; } = "#f59e0b";
    public string Danger { get; set; } = "#ef4444";
    public string Info { get; set; } = "#3b82f6";
    
    // Background & Surface colors
    public string Background { get; set; } = "#ffffff";
    public string Surface { get; set; } = "#f9fafb";
    public string Surface2 { get; set; } = "#f3f4f6";  // NEW: Secondary surface
    public string Surface3 { get; set; } = "#e5e7eb";  // NEW: Tertiary surface
    
    // Text colors
    public string TextPrimary { get; set; } = "#111827";
    public string TextSecondary { get; set; } = "#6b7280";
    public string TextMuted { get; set; } = "#9ca3af";  // NEW: Muted text
    
    // Border & Divider
    public string Border { get; set; } = "#e5e7eb";
    public string Divider { get; set; } = "#d1d5db";  // NEW: Divider lines
    
    // Shadows
    public string ShadowSm { get; set; } = "0 1px 2px 0 rgba(0, 0, 0, 0.05)";  // NEW
    public string ShadowMd { get; set; } = "0 4px 6px -1px rgba(0, 0, 0, 0.1)";  // NEW
    public string ShadowLg { get; set; } = "0 10px 15px -3px rgba(0, 0, 0, 0.1)";  // NEW
    
    // Border Radius
    public string RadiusSm { get; set; } = "0.25rem";  // NEW: 4px
    public string RadiusMd { get; set; } = "0.375rem";  // NEW: 6px
    public string RadiusLg { get; set; } = "0.5rem";  // NEW: 8px
    
    // Transitions
    public string TransitionFast { get; set; } = "150ms cubic-bezier(0.4, 0, 0.2, 1)";  // NEW
    public string TransitionNormal { get; set; } = "200ms cubic-bezier(0.4, 0, 0.2, 1)";  // NEW
}

/// <summary>
/// Built-in theme presets with enhanced color schemes
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
            Success = "#10b981",
            Warning = "#f59e0b",
            Danger = "#ef4444",
            Info = "#0ea5e9",
            Background = "#ffffff",
            Surface = "#f0f9ff",
            Surface2 = "#e0f2fe",
            Surface3 = "#bae6fd",
            TextPrimary = "#0c4a6e",
            TextSecondary = "#475569",
            TextMuted = "#64748b",
            Border = "#bae6fd",
            Divider = "#7dd3fc"
        },
        Dark = new ThemeColors
        {
            Primary = "#38bdf8",
            Secondary = "#22d3ee",
            Accent = "#a78bfa",
            Success = "#34d399",
            Warning = "#fbbf24",
            Danger = "#f87171",
            Info = "#38bdf8",
            Background = "#0c1821",
            Surface = "#1e293b",
            Surface2 = "#334155",
            Surface3 = "#475569",
            TextPrimary = "#f0f9ff",
            TextSecondary = "#cbd5e1",
            TextMuted = "#94a3b8",
            Border = "#334155",
            Divider = "#475569",
            ShadowSm = "0 1px 2px 0 rgba(0, 0, 0, 0.3)",
            ShadowMd = "0 4px 6px -1px rgba(0, 0, 0, 0.4)",
            ShadowLg = "0 10px 15px -3px rgba(0, 0, 0, 0.5)"
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
            Success = "#10b981",
            Warning = "#f59e0b",
            Danger = "#ef4444",
            Info = "#06b6d4",
            Background = "#ffffff",
            Surface = "#f0fdf4",
            Surface2 = "#dcfce7",
            Surface3 = "#bbf7d0",
            TextPrimary = "#064e3b",
            TextSecondary = "#475569",
            TextMuted = "#64748b",
            Border = "#bbf7d0",
            Divider = "#86efac"
        },
        Dark = new ThemeColors
        {
            Primary = "#34d399",
            Secondary = "#10b981",
            Accent = "#fbbf24",
            Success = "#34d399",
            Warning = "#fbbf24",
            Danger = "#f87171",
            Info = "#22d3ee",
            Background = "#0a1f0f",
            Surface = "#1e3a2a",
            Surface2 = "#2d5a42",
            Surface3 = "#3d7a5a",
            TextPrimary = "#d1fae5",
            TextSecondary = "#a7f3d0",
            TextMuted = "#6ee7b7",
            Border = "#065f46",
            Divider = "#047857",
            ShadowSm = "0 1px 2px 0 rgba(0, 0, 0, 0.3)",
            ShadowMd = "0 4px 6px -1px rgba(0, 0, 0, 0.4)",
            ShadowLg = "0 10px 15px -3px rgba(0, 0, 0, 0.5)"
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
            Success = "#10b981",
            Warning = "#f59e0b",
            Danger = "#ef4444",
            Info = "#06b6d4",
            Background = "#ffffff",
            Surface = "#fff7ed",
            Surface2 = "#ffedd5",
            Surface3 = "#fed7aa",
            TextPrimary = "#7c2d12",
            TextSecondary = "#78350f",
            TextMuted = "#92400e",
            Border = "#fed7aa",
            Divider = "#fdba74"
        },
        Dark = new ThemeColors
        {
            Primary = "#fb923c",
            Secondary = "#fbbf24",
            Accent = "#f472b6",
            Success = "#34d399",
            Warning = "#fbbf24",
            Danger = "#f87171",
            Info = "#22d3ee",
            Background = "#1a0f0a",
            Surface = "#3a2618",
            Surface2 = "#5a3d28",
            Surface3 = "#7a5438",
            TextPrimary = "#ffedd5",
            TextSecondary = "#fed7aa",
            TextMuted = "#fdba74",
            Border = "#78350f",
            Divider = "#92400e",
            ShadowSm = "0 1px 2px 0 rgba(0, 0, 0, 0.3)",
            ShadowMd = "0 4px 6px -1px rgba(0, 0, 0, 0.4)",
            ShadowLg = "0 10px 15px -3px rgba(0, 0, 0, 0.5)"
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
            Success = "#10b981",
            Warning = "#f59e0b",
            Danger = "#ef4444",
            Info = "#06b6d4",
            Background = "#ffffff",
            Surface = "#faf5ff",
            Surface2 = "#f3e8ff",
            Surface3 = "#e9d5ff",
            TextPrimary = "#581c87",
            TextSecondary = "#6b7280",
            TextMuted = "#9ca3af",
            Border = "#e9d5ff",
            Divider = "#d8b4fe"
        },
        Dark = new ThemeColors
        {
            Primary = "#a78bfa",
            Secondary = "#c4b5fd",
            Accent = "#f472b6",
            Success = "#34d399",
            Warning = "#fbbf24",
            Danger = "#f87171",
            Info = "#22d3ee",
            Background = "#1a0f2e",
            Surface = "#2e1a47",
            Surface2 = "#422861",
            Surface3 = "#56367b",
            TextPrimary = "#f3e8ff",
            TextSecondary = "#ddd6fe",
            TextMuted = "#c4b5fd",
            Border = "#581c87",
            Divider = "#6d28d9",
            ShadowSm = "0 1px 2px 0 rgba(0, 0, 0, 0.3)",
            ShadowMd = "0 4px 6px -1px rgba(0, 0, 0, 0.4)",
            ShadowLg = "0 10px 15px -3px rgba(0, 0, 0, 0.5)"
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
            Success = "#10b981",
            Warning = "#f59e0b",
            Danger = "#ef4444",
            Info = "#3b82f6",
            Background = "#ffffff",
            Surface = "#eff6ff",
            Surface2 = "#dbeafe",
            Surface3 = "#bfdbfe",
            TextPrimary = "#1e3a8a",
            TextSecondary = "#475569",
            TextMuted = "#64748b",
            Border = "#bfdbfe",
            Divider = "#93c5fd"
        },
        Dark = new ThemeColors
        {
            Primary = "#60a5fa",
            Secondary = "#818cf8",
            Accent = "#22d3ee",
            Success = "#34d399",
            Warning = "#fbbf24",
            Danger = "#f87171",
            Info = "#60a5fa",
            Background = "#0f1419",
            Surface = "#1e293b",
            Surface2 = "#334155",
            Surface3 = "#475569",
            TextPrimary = "#dbeafe",
            TextSecondary = "#93c5fd",
            TextMuted = "#60a5fa",
            Border = "#1e3a8a",
            Divider = "#1e40af",
            ShadowSm = "0 1px 2px 0 rgba(0, 0, 0, 0.3)",
            ShadowMd = "0 4px 6px -1px rgba(0, 0, 0, 0.4)",
            ShadowLg = "0 10px 15px -3px rgba(0, 0, 0, 0.5)"
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
