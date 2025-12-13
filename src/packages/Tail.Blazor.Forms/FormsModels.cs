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
    Danger
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
/// Date range preset for quick selection.
/// </summary>
public class DateRangePreset
{
    /// <summary>
    /// Preset label.
    /// </summary>
    public string Label { get; set; } = string.Empty;
    
    /// <summary>
    /// Function that returns the date range (Start, End).
    /// </summary>
    public Func<(DateTime Start, DateTime End)> GetRange { get; set; } = null!;
}

/// <summary>
/// Currency symbol position.
/// </summary>
public enum CurrencySymbolPosition
{
    Left,
    Right
}

/// <summary>
/// Country code information.
/// </summary>
public class CountryCode
{
    public string Code { get; set; } = string.Empty;
    public string Flag { get; set; } = string.Empty;
    public string Country { get; set; } = string.Empty;
}

/// <summary>
/// Password strength level.
/// </summary>
public enum PasswordStrength
{
    VeryWeak,
    Weak,
    Fair,
    Good,
    Strong
}

/// <summary>
/// Password requirement type.
/// </summary>
public enum PasswordRequirementType
{
    Length,
    Uppercase,
    Lowercase,
    Number,
    Special
}

/// <summary>
/// Password requirement.
/// </summary>
public class PasswordRequirement
{
    public PasswordRequirementType Type { get; set; }
    public string Description { get; set; } = string.Empty;
    public int? MinLength { get; set; }
}

/// <summary>
/// Rich text editor toolbar item.
/// </summary>
public class RichTextEditorToolbarItem
{
    /// <summary>
    /// Item identifier/command.
    /// </summary>
    public string Command { get; set; } = string.Empty;
    
    /// <summary>
    /// Display icon or text.
    /// </summary>
    public string Icon { get; set; } = string.Empty;
    
    /// <summary>
    /// Tooltip text.
    /// </summary>
    public string? Tooltip { get; set; }
    
    /// <summary>
    /// Optional value for commands that require it (e.g., font size, color).
    /// </summary>
    public string? Value { get; set; }
    
    /// <summary>
    /// Indicates if the item is a separator.
    /// </summary>
    public bool IsSeparator { get; set; }
    
    /// <summary>
    /// Indicates if the item is disabled.
    /// </summary>
    public bool Disabled { get; set; }
}

/// <summary>
/// Rich text editor size options.
/// </summary>
public enum RichTextEditorSize
{
    Sm,
    Md,
    Lg
}

/// <summary>
/// Rich text editor variant styles.
/// </summary>
public enum RichTextEditorVariant
{
    Default,
    Outline,
    Filled
}

