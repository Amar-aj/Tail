using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Navigation.Models;

/// <summary>
/// Represents a step in a step indicator.
/// </summary>
public class StepItem
{
    /// <summary>
    /// Title of the step.
    /// </summary>
    public string Title { get; set; } = string.Empty;
    
    /// <summary>
    /// Optional description.
    /// </summary>
    public string? Description { get; set; }
    
    /// <summary>
    /// Whether this step is completed.
    /// </summary>
    public bool IsCompleted { get; set; }
    
    /// <summary>
    /// Whether this step is the current step.
    /// </summary>
    public bool IsCurrent { get; set; }
    
    /// <summary>
    /// Optional icon.
    /// </summary>
    public string? Icon { get; set; }
}

/// <summary>
/// Represents a breadcrumb item.
/// </summary>
public class BreadcrumbItem
{
    /// <summary>
    /// Display text.
    /// </summary>
    public string Text { get; set; } = string.Empty;
    
    /// <summary>
    /// Optional link URL.
    /// </summary>
    public string? Href { get; set; }
    
    /// <summary>
    /// Whether this is the current/active item.
    /// </summary>
    public bool IsActive { get; set; }
    
    /// <summary>
    /// Optional icon.
    /// </summary>
    public string? Icon { get; set; }
}

/// <summary>
/// Represents a carousel slide.
/// </summary>
public class CarouselSlide
{
    /// <summary>
    /// Image URL.
    /// </summary>
    public string? ImageUrl { get; set; }
    
    /// <summary>
    /// Alt text for image.
    /// </summary>
    public string? AltText { get; set; }
    
    /// <summary>
    /// Optional caption.
    /// </summary>
    public string? Caption { get; set; }
    
    /// <summary>
    /// Optional link.
    /// </summary>
    public string? Link { get; set; }
    
    /// <summary>
    /// Custom content (if not using image).
    /// </summary>
    public RenderFragment? Content { get; set; }
}

/// <summary>
/// Represents a tab item.
/// </summary>
public class TabItem
{
    /// <summary>
    /// Tab title/label.
    /// </summary>
    public string Title { get; set; } = string.Empty;
    
    /// <summary>
    /// Alias for Title (for compatibility).
    /// </summary>
    public string Label
    {
        get => Title;
        set => Title = value;
    }
    
    /// <summary>
    /// Tab content.
    /// </summary>
    public RenderFragment? Content { get; set; }
    
    /// <summary>
    /// Optional icon.
    /// </summary>
    public string? Icon { get; set; }
    
    /// <summary>
    /// Whether this tab is disabled.
    /// </summary>
    public bool Disabled { get; set; }
    
    /// <summary>
    /// Optional badge text.
    /// </summary>
    public string? Badge { get; set; }
}
