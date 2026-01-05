# Tail.Blazor.Chart

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

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Data | List<double> | new() | Data parameter |
| ChartType | ChartType | ChartType.Line | ChartType parameter |
| Width | int | 400 | Width parameter |
| Height | int | 200 | Height parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailChart></TailChart>
```