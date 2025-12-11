using Microsoft.AspNetCore.Components.Forms;

namespace Tail.Blazor.Forms;

/// <summary>
/// Input type options.
/// </summary>
public enum InputType
{
    Text,
    Password,
    Email,
    Number,
    Tel,
    Url,
    Search,
    Date,
    Time,
    DateTimeLocal,
    Month,
    Week
}

/// <summary>
/// Input size options.
/// </summary>
public enum InputSize
{
    Sm,
    Md,
    Lg
}

/// <summary>
/// Select item for dropdowns.
/// </summary>
public class SelectItem
{
    public string? Value { get; set; }
    public string? Text { get; set; }
    public bool Disabled { get; set; }
}

/// <summary>
/// Checkbox size options.
/// </summary>
public enum CheckboxSize
{
    Sm,
    Md,
    Lg
}

/// <summary>
/// Checkbox variant styles.
/// </summary>
public enum CheckboxVariant
{
    Primary,
    Success,
    Warning,
    Danger
}

/// <summary>
/// Switch size options.
/// </summary>
public enum SwitchSize
{
    Sm,
    Md,
    Lg
}

/// <summary>
/// Switch variant styles.
/// </summary>
public enum SwitchVariant
{
    Primary,
    Success,
    Warning,
    Danger,
    Emoji
}

/// <summary>
/// Slider variant styles.
/// </summary>
public enum SliderVariant
{
    Primary,
    Success,
    Warning,
    Danger
}

/// <summary>
/// Slider size options.
/// </summary>
public enum SliderSize
{
    Sm,
    Md,
    Lg
}

/// <summary>
/// Rating size options.
/// </summary>
public enum RatingSize
{
    Sm,
    Md,
    Lg,
    Xl
}

/// <summary>
/// Rating color options.
/// </summary>
public enum RatingColor
{
    Yellow,
    Orange,
    Red,
    Pink,
    Purple
}

/// <summary>
/// Radio group orientation.
/// </summary>
public enum RadioGroupOrientation
{
    Vertical,
    Horizontal
}

/// <summary>
/// Radio size options.
/// </summary>
public enum RadioSize
{
    Sm,
    Md,
    Lg
}

/// <summary>
/// Radio variant styles.
/// </summary>
public enum RadioVariant
{
    Primary,
    Success,
    Warning,
    Danger
}

/// <summary>
/// Hour format for time picker (12-hour or 24-hour).
/// </summary>
public enum HourFormat
{
    Format12,
    Format24
}

/// <summary>
/// Date picker view mode.
/// </summary>
public enum DatePickerView
{
    Calendar,
    Month,
    Year
}

/// <summary>
/// Date selection mode.
/// </summary>
public enum DateSelectionMode
{
    Single,
    Multiple,
    Range
}

/// <summary>
/// File upload item with custom name support.
/// </summary>
public class FileUploadItem
{
    public IBrowserFile File { get; set; } = null!;
    public string CustomName { get; set; } = string.Empty;
    public string PreviewUrl { get; set; } = string.Empty;
    public bool IsImage { get; set; }
    public string FileType { get; set; } = string.Empty;
    public bool EditingName { get; set; }
    
    public FileUploadItem(IBrowserFile file)
    {
        File = file;
        CustomName = file.Name;
        FileType = GetFileType(file.ContentType, file.Name);
        IsImage = file.ContentType.StartsWith("image/", StringComparison.OrdinalIgnoreCase);
    }
    
    private string GetFileType(string contentType, string fileName)
    {
        if (contentType.StartsWith("image/", StringComparison.OrdinalIgnoreCase))
            return "image";
        if (contentType == "application/pdf")
            return "pdf";
        if (contentType.Contains("word", StringComparison.OrdinalIgnoreCase) || 
            fileName.EndsWith(".doc", StringComparison.OrdinalIgnoreCase) ||
            fileName.EndsWith(".docx", StringComparison.OrdinalIgnoreCase))
            return "word";
        if (contentType.Contains("excel", StringComparison.OrdinalIgnoreCase) ||
            fileName.EndsWith(".xls", StringComparison.OrdinalIgnoreCase) ||
            fileName.EndsWith(".xlsx", StringComparison.OrdinalIgnoreCase))
            return "excel";
        if (contentType.Contains("text", StringComparison.OrdinalIgnoreCase))
            return "text";
        if (contentType.Contains("video", StringComparison.OrdinalIgnoreCase))
            return "video";
        if (contentType.Contains("audio", StringComparison.OrdinalIgnoreCase))
            return "audio";
        return "file";
    }
}

