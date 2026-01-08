---
title: Rating
package: Tail.Blazor.Rating
category: forms
namespace: Tail.Blazor.Rating
route: /components/forms/rating
is_generic: false
is_missing: false
---

# Rating

Independent NuGet package for the TailRating component.

## Installation

```bash
dotnet add package Tail.Blazor.Rating
```

## Features

- Star rating system
- Customizable max rating (default 5)
- 4 sizes (Sm, Md, Lg, Xl)
- 5 colors (Yellow, Orange, Red, Pink, Purple)
- Hover effects
- Value display
- Disabled and readonly states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Rating;
```

## Basic Usage

```razor
<TailRating />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Rating

<TailRating />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailRating Size="RatingSize.Md">
    Medium Size
</TailRating>
```

**With Click Handler**

```razor
<TailRating ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailRating>
```

**Disabled State**

```razor
<TailRating Disabled="true">
    Disabled
</TailRating>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailRating Size="RatingSize.Sm">Sm</TailRating>
<TailRating Size="RatingSize.Md">Md</TailRating>
<TailRating Size="RatingSize.Lg">Lg</TailRating>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailRating Disabled="true">Disabled</TailRating>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailRating ValueChanged="HandleValueChanged">
    Click Me
</TailRating>

@code {
    private void HandleValueChanged(int args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailRating Size="RatingSize.Md" Value="10" MaxRating="10" ShowValue="true" />
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
    <TailRating Size="RatingSize.Md" ValueChanged="HandleAction" />
</div>

@code {
    private void HandleAction(int args)
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
| **Value** | `int` | - | Current value of the component |
| **MaxRating** | `int` | 5 | Maximum value constraint |
| **Size** | `RatingSize` | RatingSize.Md | Size of the component |
| **Color** | `RatingColor` | RatingColor.Yellow | Color scheme for the component |
| **ShowValue** | `bool` | - | Current value of the component |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **ReadOnly** | `bool` | - | Whether the component is read-only |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<int>` | Raised when value changes |

### Enums

#### RatingSize

```csharp
public enum RatingSize
{
    Sm,
    Md,
    Lg,
}
```

/// Rating size options.
///

#### Tail.Blazor.Rating;.RatingSize

```csharp
public enum Tail.Blazor.Rating;.RatingSize
{
    Sm,
    Md,
    Lg,
}
```

/// Rating size options.
///

#### RatingColor

```csharp
public enum RatingColor
{
    Yellow,
    Orange,
    Red,
    Pink,
}
```

/// Rating color options.
///

#### Tail.Blazor.Rating;.RatingColor

```csharp
public enum Tail.Blazor.Rating;.RatingColor
{
    Yellow,
    Orange,
    Red,
    Pink,
}
```

/// Rating color options.
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
