# Tail.Blazor.IconButton

Independent NuGet package for the TailIconButton component.

## Installation

```bash
dotnet add package Tail.Blazor.IconButton
```

## Features

- Icon-only button design
- 9 variants (Primary, Success, Warning, Danger, Info, Outline, Soft, Ghost, Link)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Loading states
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
| Variant | ButtonVariant | ButtonVariant.Primary | Visual variant style for the component |
| Size | ButtonSize | ButtonSize.Md | Size of the component |
| Disabled | bool | - | Whether the component is disabled |
| IsLoading | bool | - | Whether the component is in loading state |
| Type | string | "button" | Type parameter |
| StopPropagation | bool | - | StopPropagation parameter |
| Style | string? | - | Additional CSS styles |
| AriaLabel | string? | - | Label text for the component |
| Tooltip | string? | - | Tooltip parameter |
| Shape | ButtonShape | ButtonShape.Square | Shape parameter |
| AutoFocus | bool | false | AutoFocus parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| OnClick | MouseEventArgs | Raised when component is clicked |

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| ButtonShape | enum | ButtonShape property |

## Methods

No additional public methods.

## Examples

```razor
<TailIconButton></TailIconButton>
```