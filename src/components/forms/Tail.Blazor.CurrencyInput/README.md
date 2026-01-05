# Tail.Blazor.CurrencyInput

Independent NuGet package for the TailCurrencyInput component.

## Installation

```bash
dotnet add package Tail.Blazor.CurrencyInput
```

## Features

- Currency input with symbol
- Left or right symbol position
- Custom currency symbol
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
| Value | decimal? | - | Current value of the component |
| CurrencySymbol | string | "$" | CurrencySymbol parameter |
| SymbolPosition | CurrencySymbolPosition | CurrencySymbolPosition.Left | SymbolPosition parameter |
| Size | CurrencyInputSize | CurrencyInputSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| Placeholder | string? | - | Placeholder text |
| Disabled | bool | - | Whether the component is disabled |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| ValueChanged | decimal? | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailCurrencyInput></TailCurrencyInput>
```