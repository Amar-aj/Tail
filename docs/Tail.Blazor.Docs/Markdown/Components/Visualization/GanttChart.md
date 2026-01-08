---
title: GanttChart
package: Tail.Blazor.GanttChart
category: visualization
namespace: Tail.Blazor.GanttChart
route: /components/visualization/ganttchart
is_generic: false
is_missing: false
---

# GanttChart

Independent NuGet package for the TailGanttChart component.

## Installation

```bash
dotnet add package Tail.Blazor.GanttChart
```

## Features

- Gantt chart visualization
- Task timeline display
- Date range support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.GanttChart;
```

## Basic Usage

```razor
<TailGanttChart />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.GanttChart

<TailGanttChart />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailGanttChart Style="Sample Style" />
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
    <TailGanttChart  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Tasks** | `List<GanttTask>` | new() | Tasks parameter |
| **StartDate** | `DateTime` | DateTime.Now | StartDate parameter |
| **EndDate** | `DateTime` | DateTime.Now.AddDays(30) | EndDate parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `GanttTask` | `class` | GanttTask property |
| `Name` | `string` | Name property |
| `StartDate` | `DateTime` | StartDate property |
| `EndDate` | `DateTime` | EndDate property |

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
