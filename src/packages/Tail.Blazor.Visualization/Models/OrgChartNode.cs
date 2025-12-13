namespace Tail.Blazor.Visualization.Models;

/// <summary>
/// Represents a node in an organization chart.
/// </summary>
public class OrgChartNode
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Name { get; set; } = string.Empty;
    public string? Title { get; set; }
    public string? Avatar { get; set; }
    public string? Icon { get; set; }
    public string? Department { get; set; }
    public List<OrgChartNode> Children { get; set; } = new();
    public string? Color { get; set; }
    public object? Data { get; set; } // Custom data
}

/// <summary>
/// Organization chart layout direction.
/// </summary>
public enum OrgChartLayout
{
    TopDown,
    BottomUp,
    LeftRight,
    RightLeft
}

