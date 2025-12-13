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

/// <summary>
/// Context menu item.
/// </summary>
public class ContextMenuItem
{
    public string Text { get; set; } = string.Empty;
    public string? Icon { get; set; }
    public string? Shortcut { get; set; }
    public bool IsDivider { get; set; }
    public bool IsSection { get; set; }
    public bool Disabled { get; set; }
    public List<ContextMenuItem> Children { get; set; } = new();
    public bool HasChildren => Children != null && Children.Any();
    public EventCallback OnClick { get; set; }
}

/// <summary>
/// Context menu position.
/// </summary>
public enum ContextMenuPosition
{
    Auto,
    Top,
    Bottom,
    Left,
    Right
}

/// <summary>
/// Command palette item.
/// </summary>
public class CommandPaletteItem
{
    /// <summary>
    /// Unique identifier for the command.
    /// </summary>
    public string Id { get; set; } = Guid.NewGuid().ToString();
    
    /// <summary>
    /// Display text for the command.
    /// </summary>
    public string Text { get; set; } = string.Empty;
    
    /// <summary>
    /// Optional description or subtitle.
    /// </summary>
    public string? Description { get; set; }
    
    /// <summary>
    /// Optional icon (emoji or text).
    /// </summary>
    public string? Icon { get; set; }
    
    /// <summary>
    /// Optional keyboard shortcut display (e.g., "Ctrl+K").
    /// </summary>
    public string? Shortcut { get; set; }
    
    /// <summary>
    /// Optional category/group for grouping commands.
    /// </summary>
    public string? Category { get; set; }
    
    /// <summary>
    /// Keywords for search (if different from Text).
    /// </summary>
    public List<string> Keywords { get; set; } = new();
    
    /// <summary>
    /// Indicates if the command is disabled.
    /// </summary>
    public bool Disabled { get; set; }
    
    /// <summary>
    /// Action to perform when the command is selected.
    /// </summary>
    public EventCallback OnExecute { get; set; }
    
    /// <summary>
    /// Optional data associated with the command.
    /// </summary>
    public object? Data { get; set; }
}

/// <summary>
/// Command palette placement.
/// </summary>
public enum CommandPalettePlacement
{
    /// <summary>
    /// Center of the screen.
    /// </summary>
    Center,
    /// <summary>
    /// Top of the screen.
    /// </summary>
    Top,
    /// <summary>
    /// Bottom of the screen.
    /// </summary>
    Bottom
}

