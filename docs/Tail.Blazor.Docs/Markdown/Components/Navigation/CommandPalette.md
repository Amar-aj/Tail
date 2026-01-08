---
title: CommandPalette
package: Tail.Blazor.CommandPalette
category: navigation
namespace: Tail.Blazor.CommandPalette
route: /components/navigation/commandpalette
is_generic: false
is_missing: false
---

# CommandPalette

Independent NuGet package for the TailCommandPalette component.

## Installation

```bash
dotnet add package Tail.Blazor.CommandPalette
```

## Features

- Command palette (Cmd+K style)
- Search/filter commands
- Keyboard navigation
- Shortcut display
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.CommandPalette;
```

## Basic Usage

```razor
<TailCommandPalette />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.CommandPalette

<TailCommandPalette />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailCommandPalette IsVisibleChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailCommandPalette>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailCommandPalette IsVisibleChanged="HandleIsVisibleChanged">
    Click Me
</TailCommandPalette>

@code {
    private void HandleIsVisibleChanged(bool args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailCommandPalette IsVisible="true" Placeholder="Sample Placeholder" Style="Sample Style" />
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
    <TailCommandPalette IsVisibleChanged="HandleAction" />
</div>

@code {
    private void HandleAction(bool args)
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
| **IsVisible** | `bool` | - | Whether the component is visible |
| **Commands** | `List<CommandItem>` | new() | Commands parameter |
| **Placeholder** | `string` | "Type a command or search..." | Placeholder text |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **IsVisibleChanged** | `EventCallback<bool>` | Raised when value changes |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `CommandItem` | `class` | CommandItem property |
| `Label` | `string` | Label property |
| `Description` | `string?` | Description property |
| `Shortcut` | `string?` | Shortcut property |
| `OnExecute` | `EventCallback` | OnExecute property |

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
