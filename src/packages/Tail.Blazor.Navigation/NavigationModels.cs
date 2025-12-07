using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Navigation;

/// <summary>
/// Step item for TailSteps component.
/// </summary>
public class StepItem
{
    public string Title { get; set; } = "";
    public string? Description { get; set; }
    public object? Data { get; set; }
}

/// <summary>
/// Steps orientation.
/// </summary>
public enum StepsOrientation
{
    Horizontal,
    Vertical
}

/// <summary>
/// Tab item for TailTabs component.
/// </summary>
public class TabItem
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Label { get; set; } = "";
    public RenderFragment? Content { get; set; }
}

/// <summary>
/// Tab variant styles.
/// </summary>
public enum TabVariant
{
    Default,
    Underline,
    Pills
}

/// <summary>
/// Tab size options.
/// </summary>
public enum TabSize
{
    Sm,
    Md,
    Lg
}

/// <summary>
/// Tab position.
/// </summary>
public enum TabPosition
{
    Top,
    Bottom,
    Left,
    Right
}

/// <summary>
/// Accordion variant styles.
/// </summary>
public enum AccordionVariant
{
    Default,
    Bordered,
    Flush
}

/// <summary>
/// Sidebar position.
/// </summary>
public enum SidebarPosition
{
    Left,
    Right
}

/// <summary>
/// Menu variant styles.
/// </summary>
public enum MenuVariant
{
    Default,
    Compact,
    Expanded
}

/// <summary>
/// Breadcrumb item.
/// </summary>
public class BreadcrumbItem
{
    public string Text { get; set; } = "";
    public string? Href { get; set; }
    public object? Data { get; set; }
}

/// <summary>
/// Carousel slide.
/// </summary>
public class CarouselSlide
{
    public RenderFragment Content { get; set; } = default!;
    public object? Data { get; set; }
}

