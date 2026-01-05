# Tail.Blazor.Numeric

Independent NuGet package for the TailNumeric component.

## Installation

```bash
dotnet add package Tail.Blazor.Numeric
```

## Features

- Numeric input with increment/decrement buttons
- Min/max constraints
- Custom step value
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
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
| Value | decimal | - | Current value of the component |
| Min | decimal | decimal.MinValue | Minimum value constraint |
| Max | decimal | decimal.MaxValue | Maximum value constraint |
| Step | decimal | 1 | Step value for numeric inputs |
| Size | NumericSize | NumericSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| Disabled | bool | - | Whether the component is disabled |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| ValueChanged | decimal | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailNumeric></TailNumeric>
```