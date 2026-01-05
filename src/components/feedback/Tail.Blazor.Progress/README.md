# Tail.Blazor.Progress

Independent NuGet package for the TailProgress component.

## Installation

```bash
dotnet add package Tail.Blazor.Progress
```

## Features

- Progress bar with percentage
- 5 variants (Primary, Success, Warning, Danger, Info)
- 4 sizes (Sm, Md, Lg, Xl)
- Label support (inside/outside)
- Animation option
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
| Variant | ProgressVariant | ProgressVariant.Primary | Visual variant style for the component |
| Size | ProgressSize | ProgressSize.Md | Size of the component |
| ShowLabel | bool | - | Label text for the component |
| LabelPosition | ProgressLabelPosition | ProgressLabelPosition.Outside | Label text for the component |
| Label | string? | - | Label text for the component |
| Animated | bool | - | Animated parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailProgress></TailProgress>
```