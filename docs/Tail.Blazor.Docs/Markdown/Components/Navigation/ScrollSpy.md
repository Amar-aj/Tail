---
title: ScrollSpy
package: Tail.Blazor.ScrollSpy
category: navigation
namespace: Tail.Blazor.ScrollSpy
route: /components/navigation/scrollspy
is_generic: false
is_missing: false
---

# ScrollSpy

Independent NuGet package for the TailScrollSpy component.

## Installation

```bash
dotnet add package Tail.Blazor.ScrollSpy
```

## Features

- Scroll spy navigation
- Active section highlighting
- Left/right positioning
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ScrollSpy;
```

## Basic Usage

```razor
<TailScrollSpy />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ScrollSpy

<TailScrollSpy />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailScrollSpy OnItemClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailScrollSpy>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailScrollSpy OnItemClick="HandleOnItemClick">
    Click Me
</TailScrollSpy>

@code {
    private void HandleOnItemClick(Tail.Blazor.ScrollSpy.ScrollSpyItem args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailScrollSpy ActiveId="Sample ActiveId" Style="Sample Style" />
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
    <TailScrollSpy OnItemClick="HandleAction" />
</div>

@code {
    private void HandleAction(ScrollSpyItem args)
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
| **Items** | `List<ScrollSpyItem>` | new() | Data items collection |
| **ActiveId** | `string?` | - | ActiveId parameter |
| **Position** | `ScrollSpyPosition` | ScrollSpyPosition.Left | Position parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnItemClick** | `EventCallback<ScrollSpyItem>` | Raised when component is clicked |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `ScrollSpyItem` | `class` | ScrollSpyItem property |
| `Id` | `string` | Id property |
| `Label` | `string` | Label property |
| `Href` | `string?` | Href property |
| `ScrollSpyPosition` | `enum` | ScrollSpyPosition property |

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
