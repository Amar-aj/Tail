# Tail.Blazor.Mask

Independent NuGet package for the TailMask component.

## Installation

```bash
dotnet add package Tail.Blazor.Mask
```

## Features

- Input masking (phone, credit card, etc.)
- Custom mask patterns
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
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
| Mask | string | "(###) ###-####" | Mask parameter |
| Size | MaskSize | MaskSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| Placeholder | string? | - | Placeholder text |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Required | bool | - | Whether the component is required |
| Disabled | bool | - | Whether the component is disabled |
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
<TailMask></TailMask>
```