# Tail.Blazor.AutoComplete

Independent NuGet package for the TailAutoComplete component.

## Installation

```bash
dotnet add package Tail.Blazor.AutoComplete
```

## Features

- Autocomplete with suggestions dropdown
- Real-time filtering
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
| Value | string? | - | Current value of the component |
| Items | List<string>? | - | Data items collection |
| Size | AutoCompleteSize | AutoCompleteSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| Placeholder | string? | - | Placeholder text |
| Disabled | bool | - | Whether the component is disabled |
| MinChars | int | 1 | Minimum value constraint |
| MaxItems | int | 10 | Maximum value constraint |
| IsLoading | bool | - | Whether the component is in loading state |
| ItemTemplate | RenderFragment<string>? | - | ItemTemplate parameter |
| AriaLabel | string? | - | Label text for the component |
| Tooltip | string? | - | Tooltip parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| ValueChanged | string? | Raised when value changes |
| OnItemSelected | string | Raised with string value |
| OnSearch | string | Raised with string value |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailAutoComplete></TailAutoComplete>
```