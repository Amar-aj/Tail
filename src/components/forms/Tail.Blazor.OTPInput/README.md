# Tail.Blazor.OTPInput

Independent NuGet package for the TailOTPInput component.

## Installation

```bash
dotnet add package Tail.Blazor.OTPInput
```

## Features

- One-time password input
- Multiple digit inputs
- Customizable length (default 6)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Help text
- Auto-focus next input
- Paste support
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
| Length | int | 6 | Length parameter |
| Size | OTPInputSize | OTPInputSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| HelpText | string? | - | HelpText parameter |
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
<TailOTPInput></TailOTPInput>
```