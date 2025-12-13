namespace Tail.Blazor.Navigation.Models;

/// <summary>
/// Scroll Spy item representing a section to track.
/// </summary>
public class ScrollSpyItem
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string TargetId { get; set; } = string.Empty; // ID of the element to scroll to
    public string Label { get; set; } = string.Empty;
    public string? Icon { get; set; }
    public int? Offset { get; set; } // Offset in pixels for scroll position
    public bool IsActive { get; set; }
}

/// <summary>
/// Scroll Spy behavior mode.
/// </summary>
public enum ScrollSpyMode
{
    Smooth, // Smooth scrolling
    Instant, // Instant jump
    Auto // Auto-detect based on browser support
}

/// <summary>
/// Scroll Spy highlight style.
/// </summary>
public enum ScrollSpyHighlightStyle
{
    Underline,
    Background,
    Border,
    Badge
}

