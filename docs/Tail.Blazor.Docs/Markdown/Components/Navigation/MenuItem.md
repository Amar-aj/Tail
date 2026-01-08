---
title: MenuItem
package: Tail.Blazor.MenuItem
category: navigation
namespace: Tail.Blazor.MenuItem
route: /components/navigation/menuitem
is_generic: false
is_missing: false
---

# MenuItem

Independent NuGet package for the TailMenuItem component.

## Installation

```bash
dotnet add package Tail.Blazor.MenuItem
```

## Features

- Menu item with link
- Icon support
- Badge support
- Active state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.MenuItem;
```

## Basic Usage

```razor
<TailMenuItem>Content</TailMenuItem>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.MenuItem

<TailMenuItem>
    Hello, World!
</TailMenuItem>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailMenuItem OnClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailMenuItem>
```

**Disabled State**

```razor
<TailMenuItem Disabled="true">
    Disabled
</TailMenuItem>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailMenuItem Disabled="true">Disabled</TailMenuItem>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailMenuItem OnClick="HandleOnClick">
    Click Me
</TailMenuItem>

@code {
    private void HandleOnClick(Tail.Blazor.MenuItem.MenuItemClickArgs args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailMenuItem Href="Sample Href" IsActive="true">
    Combined Parameters
</TailMenuItem>
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
    <TailMenuItem OnClick="HandleAction">
        Action Button
    </TailMenuItem>
</div>

@code {
    private void HandleAction(MenuItemClickArgs args)
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
| **Icon** | `RenderFragment?` | - | Icon to display |
| **Badge** | `RenderFragment?` | - | Badge parameter |
| **Href** | `string?` | "#" | Href parameter |
| **IsActive** | `bool` | - | IsActive parameter |
| **Target** | `string?` | - | Target parameter |
| **Disabled** | `bool` | false | Whether the component is disabled |
| **PreventDefault** | `bool` | true | PreventDefault parameter |
| **Style** | `string?` | - | Additional CSS styles |
| **ItemClass** | `string?` | - | Additional CSS classes |
| **Bordered** | `bool` | false | Bordered parameter |
| **Shadow** | `ShadowLevel` | ShadowLevel.None | Shadow parameter |
| **Underline** | `bool` | false | Underline parameter |
| **BorderColor** | `string?` | - | Color scheme for the component |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnClick** | `EventCallback<MenuItemClickArgs>` | Raised when component is clicked |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `ShadowLevel` | `enum` | ShadowLevel property |
| `MenuItemClickArgs` | `record` | MenuItemClickArgs property |

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
