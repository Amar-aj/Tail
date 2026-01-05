# Tail.Blazor.Tour

Independent NuGet package for the TailTour component.

## Installation

```bash
dotnet add package Tail.Blazor.Tour
```

## Features

- Interactive tour/walkthrough
- Step-by-step navigation
- Spotlight overlay
- Custom tooltip placement
- Previous/Next navigation
- Finish tour callback
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Steps | List<TourStep> | new() | Step value for numeric inputs |
| IsActive | bool | - | IsActive parameter |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| OnTourComplete | void | OnTourComplete callback |

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| TourStep | class | TourStep property |
| Id | string | Id property |
| Title | string | Title property |
| Content | string? | Content property |
| TargetSelector | string? | TargetSelector property |
| Placement | TourTooltipPlacement | Placement property |
| TourTooltipPlacement | enum | TourTooltipPlacement property |

## Methods

No additional public methods.

## Examples

```razor
<TailTour></TailTour>
```