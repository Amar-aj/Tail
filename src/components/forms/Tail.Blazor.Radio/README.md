# Tail.Blazor.Radio

Independent NuGet package for the TailRadio component.

## Installation

```bash
dotnet add package Tail.Blazor.Radio
```

## Features

- Radio button input
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Group name support
- Label support
- Custom content support
- Validation error display
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
| GroupName | string? | - | GroupName parameter |
| IsChecked | bool | - | IsChecked parameter |
| Size | RadioSize | RadioSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| ChildContent | RenderFragment? | - | ChildContent parameter |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Disabled | bool | - | Whether the component is disabled |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| IsCheckedChanged | bool | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailRadio></TailRadio>
```