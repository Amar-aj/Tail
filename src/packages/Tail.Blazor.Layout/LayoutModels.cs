namespace Tail.Blazor.Layout;

/// <summary>
/// Panel variant styles.
/// </summary>
public enum PanelVariant
{
    Default,
    Success,
    Warning,
    Danger,
    Info
}

/// <summary>
/// Grid gap options.
/// </summary>
public enum GridGap
{
    None,
    Sm,
    Md,
    Lg,
    Xl
}

/// <summary>
/// Container size options.
/// </summary>
public enum ContainerSize
{
    Default,
    Sm,
    Md,
    Lg,
    Xl,
    Xxl,
    Full
}

/// <summary>
/// Divider orientation.
/// </summary>
public enum DividerOrientation
{
    Horizontal,
    Vertical
}

/// <summary>
/// Layout mode for responsive layout.
/// </summary>
public enum LayoutMode
{
    /// <summary>
    /// Drawer left with top appbar (drawer below appbar).
    /// </summary>
    DrawerLeft,
    /// <summary>
    /// Top appbar with clipped drawer (appbar overlaps drawer).
    /// </summary>
    ClippedDrawer,
    /// <summary>
    /// Appbar only (no drawer/sidebar).
    /// </summary>
    AppbarOnly
}

/// <summary>
/// Density mode for layout components.
/// </summary>
public enum DensityMode
{
    /// <summary>
    /// Normal density with standard spacing.
    /// </summary>
    Normal,
    /// <summary>
    /// Dense mode with reduced spacing.
    /// </summary>
    Dense,
    /// <summary>
    /// Compact mode with minimal spacing.
    /// </summary>
    Compact
}

/// <summary>
/// Split pane orientation.
/// </summary>
public enum SplitPaneOrientation
{
    Horizontal,
    Vertical
}

/// <summary>
/// Bottom sheet size.
/// </summary>
public enum BottomSheetSize
{
    Sm,
    Md,
    Lg,
    Full
}

/// <summary>
/// Docking panel state.
/// </summary>
public enum DockingPanelState
{
    Docked,
    Floating,
    Tabbed
}

/// <summary>
/// Docking position.
/// </summary>
public enum DockingPosition
{
    Left,
    Right,
    Top,
    Bottom,
    Center,
    Floating
}

