namespace Tail.Blazor.Utils.Models;

/// <summary>
/// Image zoom mode.
/// </summary>
public enum ImageZoomMode
{
    Click,
    Hover,
    Always
}

/// <summary>
/// Lightbox transition effect.
/// </summary>
public enum LightboxTransition
{
    Fade,
    Slide,
    Zoom
}

/// <summary>
/// Represents an image in the lightbox gallery.
/// </summary>
public class LightboxImage
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Url { get; set; } = string.Empty;
    public string? ThumbnailUrl { get; set; }
    public string? Title { get; set; }
    public string? Description { get; set; }
    public string? Alt { get; set; }
}

