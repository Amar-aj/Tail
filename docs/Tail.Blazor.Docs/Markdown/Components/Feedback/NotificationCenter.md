---
title: NotificationCenter
package: Tail.Blazor.NotificationCenter
category: feedback
namespace: Tail.Blazor.NotificationCenter
route: /components/feedback/notificationcenter
is_generic: false
is_missing: false
---

# NotificationCenter

Independent NuGet package for the TailNotificationCenter component.

## Installation

```bash
dotnet add package Tail.Blazor.NotificationCenter
```

## Features

- Notification center with list
- 4 placement options
- Read/unread states
- Mark all as read
- Dismissible notifications
- Timestamp display
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.NotificationCenter;
```

## Basic Usage

```razor
<TailNotificationCenter />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.NotificationCenter

<TailNotificationCenter />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailNotificationCenter OnNotificationClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailNotificationCenter>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailNotificationCenter OnNotificationClick="HandleOnNotificationClick">
    Click Me
</TailNotificationCenter>

@code {
    private void HandleOnNotificationClick(Tail.Blazor.NotificationCenter.NotificationItem args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailNotificationCenter Style="Sample Style" />
```

## Advanced Examples

More complex usage scenarios:

More complex usage scenarios:

##

## Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailNotificationCenter OnNotificationClick="HandleAction" />
</div>

@code {
    private void HandleAction(NotificationItem args)
    {
        // Perform action
        Console.WriteLine("Action executed");
    }
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Notifications** | `List<NotificationItem>` | new() | Notifications parameter |
| **Placement** | `NotificationCenterPlacement` | NotificationCenterPlacement.TopRight | Placement parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnNotificationClick** | `EventCallback<NotificationItem>` | Raised when component is clicked |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `NotificationItem` | `class` | NotificationItem property |
| `Id` | `string` | Id property |
| `Title` | `string` | Title property |
| `Message` | `string?` | Message property |
| `Variant` | `ToastVariant` | Variant property |
| `Icon` | `string?` | Icon property |
| `Timestamp` | `DateTime` | Timestamp property |
| `IsRead` | `bool` | IsRead property |
| `Dismissible` | `bool` | Dismissible property |
| `ToastVariant` | `enum` | ToastVariant property |

### Enums

#### NotificationCenterPlacement

```csharp
public enum NotificationCenterPlacement
{
    TopRight,
    TopLeft,
    BottomRight,
}
```

/// Notification center placement.
///

#### Tail.Blazor.NotificationCenter;.NotificationCenterPlacement

```csharp
public enum Tail.Blazor.NotificationCenter;.NotificationCenterPlacement
{
    TopRight,
    TopLeft,
    BottomRight,
}
```

/// Notification center placement.
///

## Base Class

The component inherits from `TailComponentBase` (from `Tail.Blazor.Core.Base`), which provides:

- `Class` parameter for additional CSS classes
- `AdditionalAttributes` parameter for additional HTML attributes

## Dependencies

- `Tail.Blazor.Core.Base` (required)
- `Microsoft.AspNetCore.Components`
- `Microsoft.AspNetCore.Components.Web`
- `Microsoft.AspNetCore.Components`
- `Microsoft.AspNetCore.Components.Web`
- `Microsoft.AspNetCore.Components`
- `Microsoft.AspNetCore.Components.Web`

## Target Frameworks

- .NET 8
- .NET 9
- .NET 10
