using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Visualization.Models;

/// <summary>
/// Represents a node in a flowchart.
/// </summary>
public class FlowchartNode
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Label { get; set; } = string.Empty;
    public string? Type { get; set; } // rectangle, circle, diamond, etc.
    public double X { get; set; }
    public double Y { get; set; }
    public double Width { get; set; } = 120;
    public double Height { get; set; } = 60;
    public string? Color { get; set; }
    public string? Icon { get; set; }
    public RenderFragment? Content { get; set; }
    public object? Data { get; set; }
}

/// <summary>
/// Represents an edge/connection in a flowchart.
/// </summary>
public class FlowchartEdge
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string SourceNodeId { get; set; } = string.Empty;
    public string TargetNodeId { get; set; } = string.Empty;
    public string? Label { get; set; }
    public string? Color { get; set; }
    public string? Style { get; set; } // solid, dashed, dotted
    public bool Directed { get; set; } = true; // Arrow direction
    public object? Data { get; set; }
}

/// <summary>
/// Flowchart layout algorithm.
/// </summary>
public enum FlowchartLayout
{
    Manual,
    Hierarchical,
    ForceDirected,
    Grid
}

/// <summary>
/// Flowchart node type/shape.
/// </summary>
public enum FlowchartNodeType
{
    Rectangle,
    Circle,
    Diamond,
    Ellipse,
    RoundedRectangle,
    Hexagon
}

