using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Layout;

/// <summary>
/// Represents a dockable panel in the docking layout.
/// </summary>
public class DockingPanel
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Title { get; set; } = string.Empty;
    public string? Icon { get; set; }
    public RenderFragment? Content { get; set; }
    public DockingPanelState State { get; set; } = DockingPanelState.Docked;
    public DockingPosition Position { get; set; } = DockingPosition.Center;
    public bool Closable { get; set; } = true;
    public bool Floatable { get; set; } = true;
    public bool Dockable { get; set; } = true;
    public int Order { get; set; }
    public bool IsActive { get; set; }
    public object? Data { get; set; }
}

/// <summary>
/// Represents a docking group (tabbed panels).
/// </summary>
public class DockingGroup
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public List<DockingPanel> Panels { get; set; } = new();
    public DockingPosition Position { get; set; } = DockingPosition.Center;
    public string? ActivePanelId { get; set; }
}

