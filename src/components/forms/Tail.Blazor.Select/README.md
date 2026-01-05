# Tail.Blazor.Select

Independent NuGet package for the TailSelect component.

## Installation

```bash
dotnet add package Tail.Blazor.Select
```

## Features

- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label and help text support
- Placeholder option
- Items list support
- Custom option content
- Validation error display
- Required field indicator
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
| Size | SelectSize | SelectSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| Placeholder | string? | - | Placeholder text |
| HelpText | string? | - | HelpText parameter |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Required | bool | - | Whether the component is required |
| Disabled | bool | - | Whether the component is disabled |
| Items | List<SelectItem>? | - | Data items collection |
| ChildContent | RenderFragment? | - | ChildContent parameter |
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
<TailSelect></TailSelect>
```