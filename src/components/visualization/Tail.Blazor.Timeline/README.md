# Tail.Blazor.Timeline

Independent NuGet package for the TailTimeline component.

## Installation

```bash
dotnet add package Tail.Blazor.Timeline
```

## Features

- Timeline visualization
- Title and description
- Timestamp display
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Items | List<TimelineItem> | new() | Data items collection |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| TimelineItem | class | TimelineItem property |
| Title | string | Title property |
| Description | string? | Description property |
| Timestamp | DateTime? | Timestamp property |

## Methods

No additional public methods.

## Examples

```razor
<TailTimeline></TailTimeline>
```