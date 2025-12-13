namespace Tail.Blazor.Visualization.Models;

/// <summary>
/// Represents a task in a Gantt chart.
/// </summary>
public class GanttTask
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Name { get; set; } = string.Empty;
    public DateTime StartDate { get; set; }
    public DateTime EndDate { get; set; }
    public double Progress { get; set; } = 0; // 0-100
    public string? Color { get; set; }
    public List<string> Dependencies { get; set; } = new(); // IDs of tasks this depends on
    public bool IsMilestone { get; set; } = false;
    public string? Resource { get; set; }
    public int Row { get; set; } // Row position in the chart
    public object? Data { get; set; } // Custom data
}

/// <summary>
/// Represents a milestone in a Gantt chart.
/// </summary>
public class GanttMilestone
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Name { get; set; } = string.Empty;
    public DateTime Date { get; set; }
    public string? Color { get; set; }
    public string? Icon { get; set; }
}

/// <summary>
/// Gantt chart view mode.
/// </summary>
public enum GanttViewMode
{
    Day,
    Week,
    Month
}

