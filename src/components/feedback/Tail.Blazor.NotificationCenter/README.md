# Tail.Blazor.NotificationCenter

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

## Component Usage

```razor
<TailNotificationCenter></TailNotificationCenter>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Notifications** | `List<NotificationItem>` | new() | Notifications parameter |
| **Placement** | `NotificationCenterPlacement` | NotificationCenterPlacement.TopRight | Placement parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **OnNotificationClick** | `EventCallback<NotificationItem>` | Raised when component is clicked |

## Enums

### NotificationCenterPlacement

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

### Tail.Blazor.NotificationCenter;.NotificationCenterPlacement

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

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.NotificationCenter

<TailNotificationCenter />
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailNotificationCenter OnNotificationClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailNotificationCenter>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailNotificationCenter />
```

### Event Handling

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

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailNotificationCenter Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailNotificationCenter Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailNotificationCenter>

@* Using Class parameter *@
<TailNotificationCenter Class="my-custom-class shadow-lg">
    With Custom Class
</TailNotificationCenter>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailNotificationCenter Type="submit">
        Submit Form
    </TailNotificationCenter>
</EditForm>

@code {
    private MyModel model = new();
    
    private void HandleSubmit()
    {
        // Process form submission
        Console.WriteLine("Form submitted successfully");
    }
}
```

### Real-World Example

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

## Package Information

- **Package ID**: `Tail.Blazor.NotificationCenter`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
