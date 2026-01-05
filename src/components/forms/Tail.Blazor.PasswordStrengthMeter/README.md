# Tail.Blazor.PasswordStrengthMeter

Independent NuGet package for the TailPasswordStrengthMeter component.

## Installation

```bash
dotnet add package Tail.Blazor.PasswordStrengthMeter
```

## Features

- Password input with strength meter
- Show/hide password toggle
- Real-time strength calculation
- Visual strength indicator (5 levels)
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
| Value | string? | - | Current value of the component |
| Size | PasswordStrengthMeterSize | PasswordStrengthMeterSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| Placeholder | string? | - | Placeholder text |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Required | bool | - | Whether the component is required |
| Disabled | bool | - | Whether the component is disabled |
| ShowStrengthMeter | bool | true | ShowStrengthMeter parameter |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| ValueChanged | string? | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailPasswordStrengthMeter></TailPasswordStrengthMeter>
```