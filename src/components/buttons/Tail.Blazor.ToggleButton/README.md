# Tail.Blazor.ToggleButton

Independent NuGet package for the TailToggleButton component.

## Installation

```bash
dotnet add package Tail.Blazor.ToggleButton
```

## Features

- Toggle on/off states
- Visual feedback for toggled state
- 9 variants
- 5 sizes
- Disabled states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| ChildContent | RenderFragment? | - | ChildContent parameter |
| ToggledContent | RenderFragment? | - | ToggledContent parameter |
| Variant | ButtonVariant | ButtonVariant.Primary | Visual variant style for the component |
| Size | ButtonSize | ButtonSize.Md | Size of the component |
| Disabled | bool | - | Whether the component is disabled |
| IsToggled | bool | - | IsToggled parameter |
| AriaLabel | string? | - | Label text for the component |
| Tooltip | string? | - | Tooltip parameter |
| Type | string | "button" | Type parameter |
| AutoFocus | bool | false | AutoFocus parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| IsToggledChanged | bool | Raised when value changes |
| OnClick | MouseEventArgs | Raised when component is clicked |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailToggleButton></TailToggleButton>
```