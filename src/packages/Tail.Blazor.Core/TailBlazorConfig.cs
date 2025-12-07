namespace Tail.Blazor.Core;

/// <summary>
/// Configuration options for Tail.Blazor.
/// </summary>
public class TailBlazorConfig
{
    /// <summary>
    /// Gets or sets the theme mode (Light, Dark, or Custom).
    /// </summary>
    public ThemeMode ThemeMode { get; set; } = ThemeMode.Light;

    /// <summary>
    /// Gets or sets whether to use Tailwind Play CDN (default) or local build.
    /// </summary>
    public bool UsePlayCdn { get; set; } = true;

    /// <summary>
    /// Gets or sets the Tailwind CSS version to use with Play CDN.
    /// </summary>
    public string TailwindVersion { get; set; } = "3.4.0";
}

/// <summary>
/// Theme mode options.
/// </summary>
public enum ThemeMode
{
    Light,
    Dark,
    Custom
}

