# Tail.Blazor.ProgressBarCircular

Independent NuGet package for the TailProgressBarCircular component.

## Installation

```bash
dotnet add package Tail.Blazor.ProgressBarCircular
```

## Features

- Circular progress indicator
- Customizable size
- 5 variants (Primary, Success, Warning, Danger, Info)
- Label support
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
| Size | int | 100 | Size of the component |
| StrokeWidth | int | 8 | StrokeWidth parameter |
| Variant | ProgressBarCircularVariant | ProgressBarCircularVariant.Primary | Visual variant style for the component |
| ShowLabel | bool | true | Label text for the component |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailProgressBarCircular></TailProgressBarCircular>
```