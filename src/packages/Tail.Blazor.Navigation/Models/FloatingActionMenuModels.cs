using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Navigation.Models;

/// <summary>
/// Represents a sub-action in a floating action menu.
/// </summary>
public class FloatingActionItem
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Label { get; set; } = string.Empty;
    public string? Icon { get; set; }
    public EventCallback OnClick { get; set; }
    public bool Disabled { get; set; }
    public string? Color { get; set; }
    public object? Data { get; set; }
}

/// <summary>
/// Floating action menu placement.
/// </summary>
public enum FloatingActionPlacement
{
    BottomRight,
    BottomLeft,
    TopRight,
    TopLeft,
    BottomCenter,
    TopCenter
}

/// <summary>
/// Floating action menu direction for sub-actions.
/// </summary>
public enum FloatingActionDirection
{
    Up,
    Down,
    Left,
    Right
}

