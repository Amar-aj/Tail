using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Data.Models;

/// <summary>
/// Represents an item in a list view.
/// </summary>
public class ListItem
{
    /// <summary>
    /// Unique identifier.
    /// </summary>
    public string Id { get; set; } = string.Empty;
    
    /// <summary>
    /// Title or primary text.
    /// </summary>
    public string Title { get; set; } = string.Empty;
    
    /// <summary>
    /// Subtitle or secondary text.
    /// </summary>
    public string? Subtitle { get; set; }
    
    /// <summary>
    /// Optional description.
    /// </summary>
    public string? Description { get; set; }
    
    /// <summary>
    /// Optional icon.
    /// </summary>
    public string? Icon { get; set; }
    
    /// <summary>
    /// Optional image URL.
    /// </summary>
    public string? ImageUrl { get; set; }
    
    /// <summary>
    /// Optional custom content.
    /// </summary>
    public RenderFragment? Content { get; set; }
    
    /// <summary>
    /// Whether this item is selected.
    /// </summary>
    public bool IsSelected { get; set; }
    
    /// <summary>
    /// Whether this item is disabled.
    /// </summary>
    public bool IsDisabled { get; set; }
    
    /// <summary>
    /// Optional metadata.
    /// </summary>
    public Dictionary<string, object>? Metadata { get; set; }
}
