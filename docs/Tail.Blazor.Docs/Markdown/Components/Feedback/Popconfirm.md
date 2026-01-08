---
title: Popconfirm
package: Tail.Blazor.Popconfirm
category: feedback
namespace: Tail.Blazor.Popconfirm
route: /components/feedback/popconfirm
is_generic: false
is_missing: false
---

# Popconfirm

Independent NuGet package for the TailPopconfirm component.

## Installation

```bash
dotnet add package Tail.Blazor.Popconfirm
```

## Features

- Popconfirm dialog
- Click or hover trigger
- 4 placement options (Top, Bottom, Left, Right)
- Custom confirm/cancel text
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Popconfirm;
```

## Basic Usage

```razor
<TailPopconfirm>Content</TailPopconfirm>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Popconfirm

<TailPopconfirm>
    Hello, World!
</TailPopconfirm>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailPopconfirm OnConfirm="() => Console.WriteLine("Clicked")">
    Click Me
</TailPopconfirm>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailPopconfirm OnConfirm="HandleOnConfirm">
    Click Me
</TailPopconfirm>

@code {
    private void HandleOnConfirm()
    {
        // Handle the event
        Console.WriteLine("Event triggered");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailPopconfirm Title="Sample Title" ConfirmText="Sample ConfirmText" CancelText="Sample CancelText">
    Combined Parameters
</TailPopconfirm>
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
    <TailPopconfirm OnConfirm="HandleAction">
        Action Button
    </TailPopconfirm>
</div>

@code {
    private void HandleAction()
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
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Title** | `string` | "Are you sure?" | Title parameter |
| **ConfirmText** | `string` | "Confirm" | ConfirmText parameter |
| **CancelText** | `string` | "Cancel" | CancelText parameter |
| **Trigger** | `PopconfirmTrigger` | PopconfirmTrigger.Click | Trigger parameter |
| **Placement** | `PopconfirmPlacement` | PopconfirmPlacement.Top | Placement parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnConfirm** | `EventCallback` | OnConfirm callback |
| **OnCancel** | `EventCallback` | OnCancel callback |

### Enums

#### PopconfirmTrigger

```csharp
public enum PopconfirmTrigger
{
    Click,
}
```

/// Popconfirm trigger type.
///

#### Tail.Blazor.Popconfirm;.PopconfirmTrigger

```csharp
public enum Tail.Blazor.Popconfirm;.PopconfirmTrigger
{
    Click,
}
```

/// Popconfirm trigger type.
///

#### PopconfirmPlacement

```csharp
public enum PopconfirmPlacement
{
    Top,
    Bottom,
    Left,
}
```

/// Popconfirm placement.
///

#### Tail.Blazor.Popconfirm;.PopconfirmPlacement

```csharp
public enum Tail.Blazor.Popconfirm;.PopconfirmPlacement
{
    Top,
    Bottom,
    Left,
}
```

/// Popconfirm placement.
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
