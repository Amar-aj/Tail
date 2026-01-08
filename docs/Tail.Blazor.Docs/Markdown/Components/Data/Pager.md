---
title: Pager
package: Tail.Blazor.Pager
category: data
namespace: Tail.Blazor.Pager
route: /components/data/pager
is_generic: false
is_missing: false
---

# Pager

Independent NuGet package for the TailPager component.

## Installation

```bash
dotnet add package Tail.Blazor.Pager
```

## Features

- Page navigation
- Item count display
- Previous/Next buttons
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Pager;
```

## Basic Usage

```razor
<TailPager />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Pager

<TailPager />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailPager CurrentPageChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailPager>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailPager Size="12">Small</TailPager>
<TailPager Size="16">Medium</TailPager>
<TailPager Size="24">Large</TailPager>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailPager CurrentPageChanged="HandleCurrentPageChanged">
    Click Me
</TailPager>

@code {
    private void HandleCurrentPageChanged(int args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailPager CurrentPage="10" TotalPages="10" TotalItems="10" Style="Sample Style" />
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
    <TailPager CurrentPageChanged="HandleAction" />
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
| **CurrentPage** | `int` | 1 | CurrentPage parameter |
| **TotalPages** | `int` | 1 | TotalPages parameter |
| **TotalItems** | `int` | - | Data items collection |
| **PageSize** | `int` | 10 | Size of the component |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **CurrentPageChanged** | `EventCallback<int>` | Raised when value changes |

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
