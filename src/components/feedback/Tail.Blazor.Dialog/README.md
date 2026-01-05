# Tail.Blazor.Dialog

Independent NuGet package for the TailDialog component.

## Installation

```bash
dotnet add package Tail.Blazor.Dialog
```

## Features

- Modal dialog with backdrop
- 6 sizes (Sm, Md, Lg, Xl, Xxl, Full)
- Title and footer support
- Close button option
- Close on backdrop click
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
| Footer | RenderFragment? | - | Footer parameter |
| Title | string? | - | Title parameter |
| Size | DialogSize | DialogSize.Md | Size of the component |
| ShowCloseButton | bool | true | ShowCloseButton parameter |
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
<TailDialog></TailDialog>
```