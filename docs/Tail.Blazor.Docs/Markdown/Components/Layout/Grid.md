---
title: Grid
package: Tail.Blazor.Grid
category: layout
namespace: Tail.Blazor.Grid
route: /components/layout/grid
is_generic: false
is_missing: false
---

# Grid

Independent NuGet package for the TailGrid component.

## Installation

```bash
dotnet add package Tail.Blazor.Grid
```

## Features

- Responsive grid system
- Customizable columns
- Gap spacing
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Grid;
```

## Basic Usage

```razor
<TailGrid>Content</TailGrid>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Grid

<TailGrid>
    Hello, World!
</TailGrid>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailGrid Columns="10" Gap="10" Style="Sample Style">
    Combined Parameters
</TailGrid>
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
    <TailGrid >
        Action Button
    </TailGrid>
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Columns** | `int` | 12 | Columns parameter |
| **Gap** | `int` | 4 | Gap parameter |
| **Style** | `string?` | - | Additional CSS styles |

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
