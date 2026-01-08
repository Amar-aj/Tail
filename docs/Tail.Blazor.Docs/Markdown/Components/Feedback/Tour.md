---
title: Tour
package: Tail.Blazor.Tour
category: feedback
namespace: Tail.Blazor.Tour
route: /components/feedback/tour
is_generic: false
is_missing: false
---

# Tour

Independent NuGet package for the TailTour component.

## Installation

```bash
dotnet add package Tail.Blazor.Tour
```

## Features

- Interactive tour/walkthrough
- Step-by-step navigation
- Spotlight overlay
- Custom tooltip placement
- Previous/Next navigation
- Finish tour callback
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Tour;
```

## Basic Usage

```razor
<TailTour />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Tour

<TailTour />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailTour OnTourComplete="() => Console.WriteLine("Clicked")">
    Click Me
</TailTour>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailTour OnTourComplete="HandleOnTourComplete">
    Click Me
</TailTour>

@code {
    private void HandleOnTourComplete()
    {
        // Handle the event
        Console.WriteLine("Event triggered");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailTour IsActive="true" Style="Sample Style" />
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
    <TailTour OnTourComplete="HandleAction" />
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
| **Steps** | `List<TourStep>` | new() | Step value for numeric inputs |
| **IsActive** | `bool` | - | IsActive parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnTourComplete** | `EventCallback` | OnTourComplete callback |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `TourStep` | `class` | TourStep property |
| `Id` | `string` | Id property |
| `Title` | `string` | Title property |
| `Content` | `string?` | Content property |
| `TargetSelector` | `string?` | TargetSelector property |
| `Placement` | `TourTooltipPlacement` | Placement property |
| `TourTooltipPlacement` | `enum` | TourTooltipPlacement property |

### Enums

#### TourTooltipPlacement

```csharp
public enum TourTooltipPlacement
{
    Auto,
    Top,
    Bottom,
    Left,
}
```

/// Tour tooltip placement.
///

#### Tail.Blazor.Tour;.TourTooltipPlacement

```csharp
public enum Tail.Blazor.Tour;.TourTooltipPlacement
{
    Auto,
    Top,
    Bottom,
    Left,
}
```

/// Tour tooltip placement.
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
