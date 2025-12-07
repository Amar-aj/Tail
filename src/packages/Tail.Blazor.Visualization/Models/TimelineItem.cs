using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Visualization.Models;

/// <summary>
/// Represents an item in a timeline.
/// </summary>
public class TimelineItem
{
    /// <summary>
    /// Title of the timeline item.
    /// </summary>
    public string Title { get; set; } = string.Empty;
    
    /// <summary>
    /// Description or content.
    /// </summary>
    public string? Description { get; set; }
    
    /// <summary>
    /// Date/time of the event.
    /// </summary>
    public DateTime? Date { get; set; }
    
    /// <summary>
    /// Time string (formatted).
    /// </summary>
    public string? Time { get; set; }
    
    /// <summary>
    /// Status of the item.
    /// </summary>
    public Tail.Blazor.Core.Enums.TimelineStatus Status { get; set; }
    
    /// <summary>
    /// Optional icon.
    /// </summary>
    public string? Icon { get; set; }
    
    /// <summary>
    /// Optional color.
    /// </summary>
    public string? Color { get; set; }
    
    /// <summary>
    /// Optional custom content.
    /// </summary>
    public RenderFragment? Content { get; set; }
}
