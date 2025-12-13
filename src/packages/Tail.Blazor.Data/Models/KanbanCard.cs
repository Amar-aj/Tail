namespace Tail.Blazor.Data.Models;

/// <summary>
/// Represents a card in a Kanban board.
/// </summary>
public class KanbanCard
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Title { get; set; } = string.Empty;
    public string? Description { get; set; }
    public string ColumnId { get; set; } = string.Empty;
    public int Order { get; set; }
    public string? Color { get; set; }
    public List<string> Tags { get; set; } = new();
    public Dictionary<string, object>? Metadata { get; set; }
    public object? Data { get; set; } // For custom data
}

