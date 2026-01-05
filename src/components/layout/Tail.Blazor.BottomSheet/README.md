# Tail.Blazor.BottomSheet

Independent NuGet package for the TailBottomSheet component.

## Installation

```bash
dotnet add package Tail.Blazor.BottomSheet
```

## Features

- Bottom sheet modal
- 4 sizes (Sm, Md, Lg, Full)
- Backdrop click to close
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| IsVisible | bool | - | Whether the component is visible |
| ChildContent | RenderFragment? | - | ChildContent parameter |
| Size | BottomSheetSize | BottomSheetSize.Md | Size of the component |
| CloseOnBackdropClick | bool | true | Event callback raised when clicked |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| IsVisibleChanged | bool | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailBottomSheet></TailBottomSheet>
```