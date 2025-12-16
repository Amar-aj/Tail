namespace Tail.Blazor.Tree;

/// <summary>
/// Tree node item model.
/// </summary>
public class TreeNodeItem
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Label { get; set; } = string.Empty;
    public List<TreeNodeItem> Children { get; set; } = new();
    public bool IsExpanded { get; set; }
}

