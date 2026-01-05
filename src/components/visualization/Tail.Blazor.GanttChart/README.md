# Tail.Blazor.GanttChart

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

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Tasks | List<GanttTask> | new() | Tasks parameter |
| StartDate | DateTime | DateTime.Now | StartDate parameter |
| EndDate | DateTime | DateTime.Now.AddDays(30) | EndDate parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| GanttTask | class | GanttTask property |
| Name | string | Name property |
| StartDate | DateTime | StartDate property |
| EndDate | DateTime | EndDate property |

## Methods

No additional public methods.

## Examples

```razor
<TailGanttChart></TailGanttChart>
```