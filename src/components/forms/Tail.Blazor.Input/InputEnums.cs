namespace Tail.Blazor.Input;

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
    DateTimeLocal,
    Time,
    Month,
    Week
}

/// <summary>
/// Input size options.
/// </summary>
public enum InputSize
{
    Xs,
    Sm,
    Md,
    Lg,
    Xl
}

/// <summary>
/// Input variant options (visual style).
/// </summary>
public enum InputVariant
{
    /// <summary>
    /// Standard variant with border.
    /// </summary>
    Standard,
    /// <summary>
    /// Outlined variant with border and transparent background.
    /// </summary>
    Outlined,
    /// <summary>
    /// Filled variant with background color.
    /// </summary>
    Filled
}

