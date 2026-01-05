# Tail.Blazor.TimePicker

Independent NuGet package for the TailTimePicker component.

## Installation

```bash
dotnet add package Tail.Blazor.TimePicker
```

## Features

- Time input with picker
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Validation error display
- Required field indicator
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
| Value | TimeSpan? | - | Current value of the component |
| Size | TimePickerSize | TimePickerSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Required | bool | - | Whether the component is required |
| Disabled | bool | - | Whether the component is disabled |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| ValueChanged | TimeSpan? | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailTimePicker></TailTimePicker>
```