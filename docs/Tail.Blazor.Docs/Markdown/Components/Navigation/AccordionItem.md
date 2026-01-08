---
title: AccordionItem
package: Tail.Blazor.AccordionItem
category: navigation
namespace: Tail.Blazor.AccordionItem
route: /components/navigation/accordionitem
is_generic: false
is_missing: false
---

# AccordionItem

Independent NuGet package for the TailAccordionItem component.

## Installation

```bash
dotnet add package Tail.Blazor.AccordionItem
```

## Features

- Individual accordion item
- Expand/collapse animation
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.AccordionItem;
```

## Basic Usage

```razor
<TailAccordionItem>Content</TailAccordionItem>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.AccordionItem

<TailAccordionItem>
    Hello, World!
</TailAccordionItem>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailAccordionItem IsExpandedChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailAccordionItem>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailAccordionItem IsExpandedChanged="HandleIsExpandedChanged">
    Click Me
</TailAccordionItem>

@code {
    private void HandleIsExpandedChanged(bool args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailAccordionItem Title="Sample Title" IsExpanded="true" Style="Sample Style">
    Combined Parameters
</TailAccordionItem>
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
    <TailAccordionItem IsExpandedChanged="HandleAction">
        Action Button
    </TailAccordionItem>
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
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Title** | `string` | string.Empty | Title parameter |
| **IsExpanded** | `bool` | - | IsExpanded parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **IsExpandedChanged** | `EventCallback<bool>` | Raised when value changes |

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
