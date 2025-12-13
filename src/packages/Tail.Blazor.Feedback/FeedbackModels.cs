using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Feedback;

/// <summary>
/// Alert variant styles.
/// </summary>
public enum AlertVariant
{
    Success,
    Warning,
    Danger,
    Info
}

/// <summary>
/// Badge variant styles.
/// </summary>
public enum BadgeVariant
{
    Primary,
    Success,
    Warning,
    Danger,
    Info,
    Gray
}

/// <summary>
/// Badge size options.
/// </summary>
public enum BadgeSize
{
    Sm,
    Md,
    Lg
}

/// <summary>
/// Spinner size options.
/// </summary>
public enum SpinnerSize
{
    Sm,
    Md,
    Lg,
    Xl
}

/// <summary>
/// Spinner color options.
/// </summary>
public enum SpinnerColor
{
    Primary,
    Success,
    Warning,
    Danger,
    White,
    Gray
}

/// <summary>
/// Progress variant styles.
/// </summary>
public enum ProgressVariant
{
    Primary,
    Success,
    Warning,
    Danger,
    Info
}

/// <summary>
/// Progress size options.
/// </summary>
public enum ProgressSize
{
    Sm,
    Md,
    Lg,
    Xl
}

/// <summary>
/// Progress label position.
/// </summary>
public enum ProgressLabelPosition
{
    Inside,
    Outside
}

/// <summary>
/// Skeleton type options.
/// </summary>
public enum SkeletonType
{
    Text,
    Circle,
    Rectangle,
    Custom
}

/// <summary>
/// Dialog size options.
/// </summary>
public enum DialogSize
{
    Sm,
    Md,
    Lg,
    Xl,
    Xxl,
    Full
}

/// <summary>
/// Toast variant styles.
/// </summary>
public enum ToastVariant
{
    Success,
    Warning,
    Error,
    Info
}

/// <summary>
/// Toast position options.
/// </summary>
public enum ToastPosition
{
    TopLeft,
    TopRight,
    TopCenter,
    BottomLeft,
    BottomRight,
    BottomCenter
}

/// <summary>
/// Popconfirm trigger type.
/// </summary>
public enum PopconfirmTrigger
{
    Click,
    Hover
}

/// <summary>
/// Popconfirm placement.
/// </summary>
public enum PopconfirmPlacement
{
    Top,
    Bottom,
    Left,
    Right
}

/// <summary>
/// Empty state size.
/// </summary>
public enum EmptyStateSize
{
    Sm,
    Md,
    Lg
}

/// <summary>
/// Empty state variant.
/// </summary>
public enum EmptyStateVariant
{
    Default,
    Minimal,
    Detailed
}

/// <summary>
/// Confetti shape type.
/// </summary>
public enum ConfettiShape
{
    Circle,
    Rectangle,
    Star,
    Mixed
}

/// <summary>
/// Notification center item.
/// </summary>
public class NotificationCenterItem
{
    /// <summary>
    /// Unique identifier for the notification.
    /// </summary>
    public string Id { get; set; } = Guid.NewGuid().ToString();
    
    /// <summary>
    /// Notification title.
    /// </summary>
    public string Title { get; set; } = string.Empty;
    
    /// <summary>
    /// Notification message/description.
    /// </summary>
    public string? Message { get; set; }
    
    /// <summary>
    /// Notification variant/type.
    /// </summary>
    public ToastVariant Variant { get; set; } = ToastVariant.Info;
    
    /// <summary>
    /// Optional icon (emoji or text).
    /// </summary>
    public string? Icon { get; set; }
    
    /// <summary>
    /// Timestamp when the notification was created.
    /// </summary>
    public DateTime Timestamp { get; set; } = DateTime.Now;
    
    /// <summary>
    /// Indicates if the notification has been read.
    /// </summary>
    public bool IsRead { get; set; }
    
    /// <summary>
    /// Optional category/group for grouping notifications.
    /// </summary>
    public string? Category { get; set; }
    
    /// <summary>
    /// Optional action buttons.
    /// </summary>
    public List<NotificationAction> Actions { get; set; } = new();
    
    /// <summary>
    /// Optional data associated with the notification.
    /// </summary>
    public object? Data { get; set; }
    
    /// <summary>
    /// Indicates if the notification can be dismissed.
    /// </summary>
    public bool Dismissible { get; set; } = true;
}

/// <summary>
/// Notification action button.
/// </summary>
public class NotificationAction
{
    /// <summary>
    /// Action label/text.
    /// </summary>
    public string Label { get; set; } = string.Empty;
    
    /// <summary>
    /// Action callback.
    /// </summary>
    public EventCallback OnClick { get; set; }
    
    /// <summary>
    /// Action variant/style.
    /// </summary>
    public NotificationActionVariant Variant { get; set; } = NotificationActionVariant.Primary;
}

/// <summary>
/// Notification action variant.
/// </summary>
public enum NotificationActionVariant
{
    Primary,
    Secondary,
    Success,
    Warning,
    Danger
}

/// <summary>
/// Notification center placement.
/// </summary>
public enum NotificationCenterPlacement
{
    TopRight,
    TopLeft,
    BottomRight,
    BottomLeft
}

/// <summary>
/// Tour step for walkthrough.
/// </summary>
public class TourStep
{
    /// <summary>
    /// Unique identifier for the step.
    /// </summary>
    public string Id { get; set; } = Guid.NewGuid().ToString();
    
    /// <summary>
    /// Step title.
    /// </summary>
    public string Title { get; set; } = string.Empty;
    
    /// <summary>
    /// Step description/content.
    /// </summary>
    public string? Content { get; set; }
    
    /// <summary>
    /// CSS selector or element ID to highlight.
    /// </summary>
    public string? TargetSelector { get; set; }
    
    /// <summary>
    /// Tooltip placement relative to target.
    /// </summary>
    public TourTooltipPlacement Placement { get; set; } = TourTooltipPlacement.Auto;
    
    /// <summary>
    /// Optional image or illustration.
    /// </summary>
    public string? Image { get; set; }
    
    /// <summary>
    /// Optional data associated with the step.
    /// </summary>
    public object? Data { get; set; }
}

/// <summary>
/// Tour tooltip placement.
/// </summary>
public enum TourTooltipPlacement
{
    Auto,
    Top,
    Bottom,
    Left,
    Right,
    TopLeft,
    TopRight,
    BottomLeft,
    BottomRight
}

/// <summary>
/// Tour highlight style.
/// </summary>
public enum TourHighlightStyle
{
    /// <summary>
    /// Spotlight effect with dark overlay.
    /// </summary>
    Spotlight,
    /// <summary>
    /// Border highlight only.
    /// </summary>
    Border,
    /// <summary>
    /// Background highlight.
    /// </summary>
    Background
}

/// <summary>
/// Element dimensions for tour positioning.
/// </summary>
public class TourElementDimensions
{
    public double Width { get; set; }
    public double Height { get; set; }
    public double Top { get; set; }
    public double Left { get; set; }
}

