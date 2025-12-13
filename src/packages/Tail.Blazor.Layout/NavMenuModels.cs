namespace Tail.Blazor.Layout;

/// <summary>
/// Navigation menu item.
/// </summary>
public class NavMenuItem
{
    /// <summary>
    /// Link URL.
    /// </summary>
    public string? Href { get; set; }
    
    /// <summary>
    /// Display text.
    /// </summary>
    public string Text { get; set; } = string.Empty;
    
    /// <summary>
    /// Optional icon (emoji or text).
    /// </summary>
    public string? Icon { get; set; }
    
    /// <summary>
    /// Optional badge.
    /// </summary>
    public NavMenuBadge? Badge { get; set; }
    
    /// <summary>
    /// Whether this is a section header.
    /// </summary>
    public bool IsSection { get; set; }
    
    /// <summary>
    /// Whether this is a divider.
    /// </summary>
    public bool IsDivider { get; set; }
    
    /// <summary>
    /// Whether this item is disabled.
    /// </summary>
    public bool Disabled { get; set; }
    
    /// <summary>
    /// Whether to use exact match for active state.
    /// </summary>
    public bool ExactMatch { get; set; } = false;
    
    /// <summary>
    /// Child menu items for expandable menus.
    /// </summary>
    public List<NavMenuItem> Children { get; set; } = new();
    
    /// <summary>
    /// Whether this item is expanded (for items with children).
    /// </summary>
    public bool IsExpanded { get; set; } = false;
    
    /// <summary>
    /// Whether this item can be expanded (has children).
    /// </summary>
    public bool HasChildren => Children != null && Children.Any();
}

/// <summary>
/// Navigation menu badge.
/// </summary>
public class NavMenuBadge
{
    /// <summary>
    /// Badge text.
    /// </summary>
    public string Text { get; set; } = string.Empty;
    
    /// <summary>
    /// Badge variant.
    /// </summary>
    public NavMenuBadgeVariant Variant { get; set; } = NavMenuBadgeVariant.Default;
}

/// <summary>
/// Navigation menu variant.
/// </summary>
public enum NavMenuVariant
{
    Default,
    Pills,
    Underline
}

/// <summary>
/// Navigation menu size.
/// </summary>
public enum NavMenuSize
{
    Sm,
    Md,
    Lg
}

/// <summary>
/// Navigation menu badge variant.
/// </summary>
public enum NavMenuBadgeVariant
{
    Default,
    Primary,
    Success,
    Warning,
    Danger
}

