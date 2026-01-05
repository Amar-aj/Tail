# Tail.Blazor.MultiSelect

Independent NuGet package for the TailMultiSelect component.

## Installation

```bash
dotnet add package Tail.Blazor.MultiSelect
```

## Features

- Multi-selection dropdown
- Tag display for selected items
- Search functionality (can be added)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
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
| SelectedValues | List<string>? | - | Current value of the component |
| Items | List<MultiSelectItem>? | - | Data items collection |
| Size | MultiSelectSize | MultiSelectSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| Placeholder | string? | - | Placeholder text |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Required | bool | - | Whether the component is required |
| Disabled | bool | - | Whether the component is disabled |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| SelectedValuesChanged | List<string> | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailMultiSelect></TailMultiSelect>
```