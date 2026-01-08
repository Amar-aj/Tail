---
title: ContextMenu
package: Tail.Blazor.ContextMenu
category: navigation
namespace: Tail.Blazor.ContextMenu
route: /components/navigation/contextmenu
is_generic: false
is_missing: false
---

# ContextMenu

Independent NuGet package for the TailContextMenu component.

## Installation

```bash
dotnet add package Tail.Blazor.ContextMenu
```

## Features

- Right-click context menu
- Menu items with actions
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ContextMenu;
```

## Basic Usage

```razor
<TailContextMenu>Content</TailContextMenu>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ContextMenu

<TailContextMenu>
    Hello, World!
</TailContextMenu>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailContextMenu OnItemClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailContextMenu>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailContextMenu OnItemClick="HandleOnItemClick">
    Click Me
</TailContextMenu>

@code {
    private void HandleOnItemClick(Tail.Blazor.ContextMenu.ContextMenuItem args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailContextMenu Style="Sample Style">
    Combined Parameters
</TailContextMenu>
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
    <TailContextMenu OnItemClick="HandleAction">
        Action Button
    </TailContextMenu>
</div>

@code {
    private void HandleAction(ContextMenuItem args)
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
| **Items** | `List<ContextMenuItem>` | new() | Data items collection |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnItemClick** | `EventCallback<ContextMenuItem>` | Raised when component is clicked |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `ContextMenuItem` | `class` | ContextMenuItem property |
| `Label` | `string` | Label property |
| `OnClick` | `EventCallback` | OnClick property |

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
