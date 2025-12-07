namespace Tail.Blazor.Forms.Models;

/// <summary>
/// Represents an item in a select dropdown.
/// </summary>
/// <typeparam name="TValue">The type of the value.</typeparam>
public class SelectItem<TValue>
{
    /// <summary>
    /// Display text.
    /// </summary>
    public string Text { get; set; } = string.Empty;
    
    /// <summary>
    /// The value.
    /// </summary>
    public TValue? Value { get; set; }
    
    /// <summary>
    /// Whether this item is disabled.
    /// </summary>
    public bool Disabled { get; set; }
    
    /// <summary>
    /// Optional group name.
    /// </summary>
    public string? Group { get; set; }
}

/// <summary>
/// Non-generic select item.
/// </summary>
public class SelectItem : SelectItem<string>
{
}
