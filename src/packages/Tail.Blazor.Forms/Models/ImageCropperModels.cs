namespace Tail.Blazor.Forms.Models;

/// <summary>
/// Image cropper aspect ratio preset.
/// </summary>
public class AspectRatio
{
    public string Name { get; set; } = string.Empty;
    public double Ratio { get; set; } // width / height
    public bool Locked { get; set; } = false;
}

/// <summary>
/// Image cropper view mode.
/// </summary>
public enum ImageCropperViewMode
{
    Normal,
    Crop,
    Preview
}

/// <summary>
/// Image cropper zoom mode.
/// </summary>
public enum ImageCropperZoomMode
{
    Free,
    Fit,
    Fill
}

