namespace Tail.Blazor.ResponsiveLayout;

/// <summary>
/// Layout mode for responsive layout component.
/// </summary>
public enum LayoutMode
{
    /// <summary>
    /// Drawer on the left side.
    /// </summary>
    DrawerLeft,
    
    /// <summary>
    /// Drawer on the right side.
    /// </summary>
    DrawerRight,
    
    /// <summary>
    /// Fixed sidebar on the left.
    /// </summary>
    FixedLeft,
    
    /// <summary>
    /// Fixed sidebar on the right.
    /// </summary>
    FixedRight,
    
    /// <summary>
    /// No sidebar, full width.
    /// </summary>
    FullWidth
}

/// <summary>
/// Density mode for responsive layout component.
/// </summary>
public enum DensityMode
{
    /// <summary>
    /// Compact spacing.
    /// </summary>
    Compact,
    
    /// <summary>
    /// Normal spacing.
    /// </summary>
    Normal,
    
    /// <summary>
    /// Comfortable spacing.
    /// </summary>
    Comfortable
}

/// <summary>
/// Responsive layout breakpoint.
/// </summary>
public enum ResponsiveLayoutBreakpoint
{
    /// <summary>
    /// Small breakpoint.
    /// </summary>
    Sm,
    
    /// <summary>
    /// Medium breakpoint.
    /// </summary>
    Md,
    
    /// <summary>
    /// Large breakpoint.
    /// </summary>
    Lg,
    
    /// <summary>
    /// Extra large breakpoint.
    /// </summary>
    Xl
}
