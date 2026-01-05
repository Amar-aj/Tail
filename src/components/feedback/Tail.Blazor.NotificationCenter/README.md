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

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Notifications | List<NotificationItem> | new() | Notifications parameter |
| Placement | NotificationCenterPlacement | NotificationCenterPlacement.TopRight | Placement parameter |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| OnNotificationClick | NotificationItem | Raised when component is clicked |

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| NotificationItem | class | NotificationItem property |
| Id | string | Id property |
| Title | string | Title property |
| Message | string? | Message property |
| Variant | ToastVariant | Variant property |
| Icon | string? | Icon property |
| Timestamp | DateTime | Timestamp property |
| IsRead | bool | IsRead property |
| Dismissible | bool | Dismissible property |
| ToastVariant | enum | ToastVariant property |

## Methods

No additional public methods.

## Examples

```razor
<TailNotificationCenter></TailNotificationCenter>
```