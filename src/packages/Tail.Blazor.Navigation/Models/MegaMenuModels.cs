using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Navigation.Models;

/// <summary>
/// Represents a column in a mega menu.
/// </summary>
public class MegaMenuColumn
{
    public string Title { get; set; } = string.Empty;
    public string? Icon { get; set; }
    public List<MegaMenuItem> Items { get; set; } = new();
    public RenderFragment? CustomContent { get; set; }
    public int Width { get; set; } = 1; // Relative width (1 = default, 2 = double, etc.)
}

/// <summary>
/// Represents an item in a mega menu column.
/// </summary>
public class MegaMenuItem
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Text { get; set; } = string.Empty;
    public string? Description { get; set; }
    public string? Icon { get; set; }
    public string? Href { get; set; }
    public string? ImageUrl { get; set; }
    public string? Badge { get; set; }
    public bool IsNew { get; set; }
    public bool IsHot { get; set; }
    public EventCallback OnClick { get; set; }
    public bool Disabled { get; set; }
}

/// <summary>
/// Mega menu placement.
/// </summary>
public enum MegaMenuPlacement
{
    Bottom,
    Top
}

/// <summary>
/// Mega menu alignment.
/// </summary>
public enum MegaMenuAlignment
{
    Left,
    Center,
    Right,
    FullWidth
}

