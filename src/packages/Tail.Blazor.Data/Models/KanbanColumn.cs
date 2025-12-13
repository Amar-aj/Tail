namespace Tail.Blazor.Data.Models;

/// <summary>
/// Represents a column in a Kanban board.
/// </summary>
public class KanbanColumn
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Title { get; set; } = string.Empty;
    public string? Color { get; set; }
    public int MaxCards { get; set; } = 0; // 0 = unlimited
    public bool AllowDrop { get; set; } = true;
    public int Order { get; set; }
}

