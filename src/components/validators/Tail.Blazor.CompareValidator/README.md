# Tail.Blazor.CompareValidator

Independent NuGet package for the TailCompareValidator component.

## Installation

```bash
dotnet add package Tail.Blazor.CompareValidator
```

## Features

- Value comparison validation
- 4 operators (Equal, NotEqual, GreaterThan, LessThan)
- Custom error message
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
| CompareTo | string? | - | CompareTo parameter |
| Operator | CompareOperator | CompareOperator.Equal | Operator parameter |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailCompareValidator></TailCompareValidator>
```