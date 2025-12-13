using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Feedback;

/// <summary>
/// Service for managing notifications in the notification center.
/// </summary>
public class NotificationService
{
    private readonly List<NotificationCenterItem> _notifications = new();
    
    /// <summary>
    /// Event raised when notifications change.
    /// </summary>
    public event Action? OnNotificationsChanged;
    
    /// <summary>
    /// Gets all notifications.
    /// </summary>
    public IReadOnlyList<NotificationCenterItem> Notifications => _notifications.AsReadOnly();
    
    /// <summary>
    /// Gets unread notification count.
    /// </summary>
    public int UnreadCount => _notifications.Count(n => !n.IsRead);
    
    /// <summary>
    /// Gets notifications grouped by category.
    /// </summary>
    public Dictionary<string, List<NotificationCenterItem>> GetGroupedNotifications()
    {
        return _notifications
            .GroupBy(n => n.Category ?? "Other")
            .ToDictionary(g => g.Key, g => g.ToList());
    }
    
    /// <summary>
    /// Adds a new notification.
    /// </summary>
    public void AddNotification(NotificationCenterItem notification)
    {
        _notifications.Insert(0, notification); // Add to beginning
        OnNotificationsChanged?.Invoke();
    }
    
    /// <summary>
    /// Adds a new notification with convenience parameters.
    /// </summary>
    public void AddNotification(string title, string? message = null, ToastVariant variant = ToastVariant.Info, string? category = null, string? icon = null)
    {
        var notification = new NotificationCenterItem
        {
            Title = title,
            Message = message,
            Variant = variant,
            Category = category,
            Icon = icon,
            Timestamp = DateTime.Now
        };
        
        AddNotification(notification);
    }
    
    /// <summary>
    /// Marks a notification as read.
    /// </summary>
    public void MarkAsRead(string notificationId)
    {
        var notification = _notifications.FirstOrDefault(n => n.Id == notificationId);
        if (notification != null && !notification.IsRead)
        {
            notification.IsRead = true;
            OnNotificationsChanged?.Invoke();
        }
    }
    
    /// <summary>
    /// Marks all notifications as read.
    /// </summary>
    public void MarkAllAsRead()
    {
        foreach (var notification in _notifications.Where(n => !n.IsRead))
        {
            notification.IsRead = true;
        }
        OnNotificationsChanged?.Invoke();
    }
    
    /// <summary>
    /// Removes a notification.
    /// </summary>
    public void RemoveNotification(string notificationId)
    {
        var notification = _notifications.FirstOrDefault(n => n.Id == notificationId);
        if (notification != null)
        {
            _notifications.Remove(notification);
            OnNotificationsChanged?.Invoke();
        }
    }
    
    /// <summary>
    /// Clears all notifications.
    /// </summary>
    public void ClearAll()
    {
        _notifications.Clear();
        OnNotificationsChanged?.Invoke();
    }
    
    /// <summary>
    /// Clears read notifications.
    /// </summary>
    public void ClearRead()
    {
        _notifications.RemoveAll(n => n.IsRead);
        OnNotificationsChanged?.Invoke();
    }
}

