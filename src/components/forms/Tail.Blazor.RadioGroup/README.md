# Tail.Blazor.RadioGroup

Independent NuGet package for the TailRadioGroup component.

## Installation

```bash
dotnet add package Tail.Blazor.RadioGroup
```

## Features

- Radio button grouping
- Vertical and horizontal orientations
- Label support
- Help text support
- Validation error display
- Required field indicator
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
| Label | string? | - | Label text for the component |
| HelpText | string? | - | HelpText parameter |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Required | bool | - | Whether the component is required |
| Orientation | RadioGroupOrientation | RadioGroupOrientation.Vertical | Orientation parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailRadioGroup></TailRadioGroup>
```