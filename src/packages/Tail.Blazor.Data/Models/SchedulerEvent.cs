namespace Tail.Blazor.Data.Models;

/// <summary>
/// Scheduler event item.
/// </summary>
public class SchedulerEvent
{
    /// <summary>
    /// Unique identifier for the event.
    /// </summary>
    public string Id { get; set; } = Guid.NewGuid().ToString();
    
    /// <summary>
    /// Event title.
    /// </summary>
    public string Title { get; set; } = "";
    
    /// <summary>
    /// Event start time.
    /// </summary>
    public DateTime Start { get; set; }
    
    /// <summary>
    /// Event end time.
    /// </summary>
    public DateTime End { get; set; }
    
    /// <summary>
    /// Optional event description.
    /// </summary>
    public string? Description { get; set; }
    
    /// <summary>
    /// Optional color for the event.
    /// </summary>
    public string? Color { get; set; }
    
    /// <summary>
    /// Whether this is an all-day event.
    /// </summary>
    public bool AllDay { get; set; }
    
    /// <summary>
    /// Additional data associated with the event.
    /// </summary>
    public object? Data { get; set; }
}

