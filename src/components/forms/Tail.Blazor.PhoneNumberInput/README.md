# Tail.Blazor.PhoneNumberInput

Independent NuGet package for the TailPhoneNumberInput component.

## Installation

```bash
dotnet add package Tail.Blazor.PhoneNumberInput
```

## Features

- Phone number input with country code selector
- Country code dropdown
- Phone number formatting
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
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
| PhoneNumber | string? | - | PhoneNumber parameter |
| SelectedCountryCode | string | "+1" | SelectedCountryCode parameter |
| Size | PhoneNumberInputSize | PhoneNumberInputSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| Placeholder | string? | - | Placeholder text |
| Disabled | bool | - | Whether the component is disabled |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| PhoneNumberChanged | string? | Raised when value changes |
| SelectedCountryCodeChanged | string | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailPhoneNumberInput></TailPhoneNumberInput>
```