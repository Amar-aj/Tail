---
title: Chart
package: Tail.Blazor.Chart
category: charts
namespace: Tail.Blazor.Chart
route: /components/charts/chart
is_generic: false
is_missing: false
---

# Chart

Independent NuGet package for the TailChart component.

## Installation

```bash
dotnet add package Tail.Blazor.Chart
```

## Features

- Multiple chart types (Line, Bar, Area, Pie)
- SVG-based rendering
- Customizable size
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Chart;
```

## Basic Usage

```razor
<TailChart />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Chart

<TailChart />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailChart Data="10" Width="10" Height="10" Style="Sample Style" />
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
    <TailChart  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Data** | `List<double>` | new() | Data parameter |
| **ChartType** | `ChartType` | ChartType.Line | ChartType parameter |
| **Width** | `int` | 400 | Width parameter |
| **Height** | `int` | 200 | Height parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Enums

#### ChartType

```csharp
public enum ChartType
{
    Line,
    Bar,
    Area,
}
```

/// Chart type options.
///

#### Tail.Blazor.Chart;.ChartType

```csharp
public enum Tail.Blazor.Chart;.ChartType
{
    Line,
    Bar,
    Area,
}
```

/// Chart type options.
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
