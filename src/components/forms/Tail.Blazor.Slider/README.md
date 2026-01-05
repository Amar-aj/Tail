# Tail.Blazor.Slider

Independent NuGet package for the TailSlider component.

## Installation

```bash
dotnet add package Tail.Blazor.Slider
```

## Features

- Range input with min/max/step
- 3 sizes (Sm, Md, Lg)
- 4 variants (Primary, Success, Warning, Danger)
- Label support
- Value display
- Min/max labels
- Help text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Value | double | - | Current value of the component |
| Min | double | 0 | Minimum value constraint |
| Max | double | 100 | Maximum value constraint |
| Step | double | 1 | Step value for numeric inputs |
| Size | SliderSize | SliderSize.Md | Size of the component |
| Variant | SliderVariant | SliderVariant.Primary | Visual variant style for the component |
| Label | string? | - | Label text for the component |
| HelpText | string? | - | HelpText parameter |
| ShowValue | bool | - | Current value of the component |
| ShowLabels | bool | - | Label text for the component |
| Disabled | bool | - | Whether the component is disabled |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| ValueChanged | double | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailSlider></TailSlider>
```