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

