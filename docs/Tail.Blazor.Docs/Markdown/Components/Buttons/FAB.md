---
title: FAB
package: Tail.Blazor.FAB
category: buttons
namespace: Tail.Blazor.FAB
route: /components/buttons/fab
is_generic: false
is_missing: false
---

# FAB

Independent NuGet package for the TailFAB (Floating Action Button) component.

## Installation

```bash
dotnet add package Tail.Blazor.FAB
```

## Features

- 4 positions (TopLeft, TopRight, BottomLeft, BottomRight)
- Fixed positioning
- Circular design
- Loading states
- Disabled states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.FAB;
```

## Basic Usage

```razor
<TailFAB>Content</TailFAB>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.FAB

<TailFAB>
    Hello, World!
</TailFAB>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailFAB OnClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailFAB>
```

**Disabled State**

```razor
<TailFAB Disabled="true">
    Disabled
</TailFAB>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailFAB Disabled="true">Disabled</TailFAB>

@* Loading state *@
<TailFAB IsLoading="true">Loading...</TailFAB>

@* Both disabled and loading *@
<TailFAB Disabled="true" IsLoading="true">Processing</TailFAB>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailFAB OnClick="HandleOnClick">
    Click Me
</TailFAB>

@code {
    private void HandleOnClick(MouseEventArgs args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailFAB Type="Sample Type">
    Combined Parameters
</TailFAB>
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
    <TailFAB OnClick="HandleAction">
        Action Button
    </TailFAB>
</div>

@code {
    private void HandleAction(MouseEventArgs args)
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
| **Position** | `FABPosition` | FABPosition.BottomRight | Position parameter |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **IsLoading** | `bool` | - | Whether the component is in loading state |
| **Type** | `string` | "button" | Type parameter |
| **Style** | `string?` | - | Additional CSS styles |
| **AutoFocus** | `bool` | false | AutoFocus parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnClick** | `EventCallback<MouseEventArgs>` | Raised when component is clicked |

### Enums

#### FABPosition

```csharp
public enum FABPosition
{
    TopLeft,
    TopRight,
    BottomLeft,
}
```

/// Floating Action Button position options.
///

#### Tail.Blazor.FAB;.FABPosition

```csharp
public enum Tail.Blazor.FAB;.FABPosition
{
    TopLeft,
    TopRight,
    BottomLeft,
}
```

/// Floating Action Button position options.
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
