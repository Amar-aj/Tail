# Tail.Blazor.Rating

Independent NuGet package for the TailRating component.

## Installation

```bash
dotnet add package Tail.Blazor.Rating
```

## Features

- Star rating system
- Customizable max rating (default 5)
- 4 sizes (Sm, Md, Lg, Xl)
- 5 colors (Yellow, Orange, Red, Pink, Purple)
- Hover effects
- Value display
- Disabled and readonly states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Value | int | - | Current value of the component |
| MaxRating | int | 5 | Maximum value constraint |
| Size | RatingSize | RatingSize.Md | Size of the component |
| Color | RatingColor | RatingColor.Yellow | Color scheme for the component |
| ShowValue | bool | - | Current value of the component |
| Disabled | bool | - | Whether the component is disabled |
| ReadOnly | bool | - | Whether the component is read-only |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| ValueChanged | int | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailRating></TailRating>
```