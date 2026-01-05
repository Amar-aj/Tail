# Tail.Blazor.ColorPicker

Independent NuGet package for the TailColorPicker component.

## Installation

```bash
dotnet add package Tail.Blazor.ColorPicker
```

## Features

- Color picker with visual selector
- Hex color input
- Color preview
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Help text
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
| Size | ColorPickerSize | ColorPickerSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| HelpText | string? | - | HelpText parameter |
| ShowPreview | bool | true | ShowPreview parameter |
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
<TailColorPicker></TailColorPicker>
```