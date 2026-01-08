---
title: PivotDataGrid
package: Tail.Blazor.PivotDataGrid
category: data
namespace: Tail.Blazor.PivotDataGrid
route: /components/data/pivotdatagrid
is_generic: false
is_missing: false
---

# PivotDataGrid

Independent NuGet package for the TailPivotDataGrid component.

## Installation

```bash
dotnet add package Tail.Blazor.PivotDataGrid
```

## Features

- Pivot table
- Row and column headers
- Data aggregation
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.PivotDataGrid;
```

## Basic Usage

```razor
<TailPivotDataGrid />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.PivotDataGrid

<TailPivotDataGrid />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailPivotDataGrid RowHeader="Sample RowHeader" Columns="Sample Columns" Style="Sample Style" />
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
    <TailPivotDataGrid  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **RowHeader** | `string` | "Row" | RowHeader parameter |
| **Columns** | `List<string>` | new() | Columns parameter |
| **Rows** | `List<PivotRow>` | new() | Rows parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `PivotRow` | `class` | PivotRow property |
| `Key` | `string` | Key property |
| `string` | `Dictionary<string,` | string property |

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
