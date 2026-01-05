# Tail.Blazor.Scheduler

Independent NuGet package for the TailScheduler component.

## Installation

```bash
dotnet add package Tail.Blazor.Scheduler
```

## Features

- Calendar scheduler
- Event display
- Month view
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| CurrentDate | DateTime | DateTime.Now | CurrentDate parameter |
| Events | List<SchedulerEvent> | new() | Events parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| CalendarDay | class | CalendarDay property |
| Date | DateTime | Date property |
| Day | int | Day property |
| Events | List<SchedulerEvent> | Events property |
| SchedulerEvent | class | SchedulerEvent property |
| Date | DateTime | Date property |
| Title | string | Title property |

## Methods

No additional public methods.

## Examples

```razor
<TailScheduler></TailScheduler>
```