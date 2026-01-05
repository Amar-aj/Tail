# Tail.Blazor.Carousel

Independent NuGet package for the TailCarousel component.

## Installation

```bash
dotnet add package Tail.Blazor.Carousel
```

## Features

- Image/content carousel
- Previous/Next controls
- Indicator dots
- Auto-play option
- Smooth transitions
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Items | List<RenderFragment> | new() | Data items collection |
| CurrentIndex | int | - | CurrentIndex parameter |
| ShowControls | bool | true | ShowControls parameter |
| ShowIndicators | bool | true | ShowIndicators parameter |
| AutoPlay | bool | - | AutoPlay parameter |
| AutoPlayInterval | int | 3000 | AutoPlayInterval parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| Dispose | void | Dispose property |

## Methods

No additional public methods.

## Examples

```razor
<TailCarousel></TailCarousel>
```