using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Core;

/// <summary>
/// Base class for all Tail.Blazor components.
/// Provides common functionality for lightweight, high-performance components.
/// </summary>
public abstract class TailComponentBase : ComponentBase
{
    /// <summary>
    /// Additional CSS classes to apply to the component.
    /// </summary>
    [Parameter]
    public string? Class { get; set; }

    /// <summary>
    /// Additional attributes to apply to the component.
    /// </summary>
    [Parameter(CaptureUnmatchedValues = true)]
    public Dictionary<string, object>? AdditionalAttributes { get; set; }

    /// <summary>
    /// Gets the combined CSS classes for the component.
    /// </summary>
    protected virtual string? CssClass => Class;

    /// <summary>
    /// Determines if the component should render.
    /// Override to implement custom render logic for performance optimization.
    /// </summary>
    protected override bool ShouldRender()
    {
        return base.ShouldRender();
    }
}

