---
title: Pagination
package: Tail.Blazor.Pagination
category: navigation
namespace: Tail.Blazor.Pagination
route: /components/navigation/pagination
is_generic: false
is_missing: false
---

# Pagination

Independent NuGet package for the TailPagination component.

## Installation

```bash
dotnet add package Tail.Blazor.Pagination
```

## Features

- Page navigation
- Previous/Next buttons
- Page number buttons
- Ellipsis for large page counts
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Pagination;
```

## Basic Usage

```razor
<TailPagination />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Pagination

<TailPagination />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailPagination CurrentPageChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailPagination>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailPagination CurrentPageChanged="HandleCurrentPageChanged">
    Click Me
</TailPagination>

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
<TailPagination CurrentPage="10" TotalPages="10" VisiblePages="10" Style="Sample Style" />
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
    <TailPagination CurrentPageChanged="HandleAction" />
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
| **VisiblePages** | `int` | 5 | Whether the component is visible |
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
