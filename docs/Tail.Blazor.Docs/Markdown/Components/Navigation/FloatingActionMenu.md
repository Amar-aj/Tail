---
title: FloatingActionMenu
package: Tail.Blazor.FloatingActionMenu
category: navigation
namespace: Tail.Blazor.FloatingActionMenu
route: /components/navigation/floatingactionmenu
is_generic: false
is_missing: false
---

# FloatingActionMenu

Independent NuGet package for the TailFloatingActionMenu component.

## Installation

```bash
dotnet add package Tail.Blazor.FloatingActionMenu
```

## Features

- Floating action menu
- Expandable menu items
- 4 position options
- Icon support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.FloatingActionMenu;
```

## Basic Usage

```razor
<TailFloatingActionMenu />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.FloatingActionMenu

<TailFloatingActionMenu />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailFloatingActionMenu OnItemClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailFloatingActionMenu>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailFloatingActionMenu OnItemClick="HandleOnItemClick">
    Click Me
</TailFloatingActionMenu>

@code {
    private void HandleOnItemClick(Tail.Blazor.FloatingActionMenu.FloatingActionMenuItem args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailFloatingActionMenu Style="Sample Style" />
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
    <TailFloatingActionMenu OnItemClick="HandleAction" />
</div>

@code {
    private void HandleAction(FloatingActionMenuItem args)
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
| **Items** | `List<FloatingActionMenuItem>` | new() | Data items collection |
| **Position** | `FloatingActionMenuPosition` | FloatingActionMenuPosition.BottomRight | Position parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnItemClick** | `EventCallback<FloatingActionMenuItem>` | Raised when component is clicked |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `FloatingActionMenuItem` | `class` | FloatingActionMenuItem property |
| `Label` | `string` | Label property |
| `Icon` | `RenderFragment?` | Icon property |
| `OnClick` | `EventCallback` | OnClick property |
| `FloatingActionMenuPosition` | `enum` | FloatingActionMenuPosition property |

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
