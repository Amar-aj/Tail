# Tail.Blazor.Checkbox

Independent NuGet package for the TailCheckbox component.

## Installation

```bash
dotnet add package Tail.Blazor.Checkbox
```

## Features

- 5 sizes (Xs, Sm, Md, Lg, Xl)
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
| IsChecked | bool | - | IsChecked parameter |
| Size | CheckboxSize | CheckboxSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| ChildContent | RenderFragment? | - | ChildContent parameter |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Disabled | bool | - | Whether the component is disabled |
| IsIndeterminate | bool | - | Minimum value constraint |
| CustomCheckIcon | RenderFragment? | - | Icon to display |
| AriaLabel | string? | - | Label text for the component |
| Tooltip | string? | - | Tooltip parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| IsCheckedChanged | bool | Raised when value changes |
| OnCheckedChanged | bool | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailCheckbox></TailCheckbox>
```