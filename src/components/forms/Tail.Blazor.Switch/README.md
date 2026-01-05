# Tail.Blazor.Switch

Independent NuGet package for the TailSwitch component.

## Installation

```bash
dotnet add package Tail.Blazor.Switch
```

## Features

- Toggle switch design
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Custom content support
- Validation error display
- Disabled state
- Smooth animations
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| IsChecked | bool | - | IsChecked parameter |
| Size | SwitchSize | SwitchSize.Md | Size of the component |
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
<TailSwitch></TailSwitch>
```