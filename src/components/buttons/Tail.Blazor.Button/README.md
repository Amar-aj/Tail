# Tail.Blazor.Button

Independent NuGet package for the TailButton component.

## Installation

```bash
dotnet add package Tail.Blazor.Button
```

## Features

- 9 variants (Primary, Success, Warning, Danger, Info, Outline, Soft, Ghost, Link)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Loading states
- Icon support (start/end)
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
| LoadingText | string? | - | Whether the component is in loading state |
| ShowDefaultLoadingText | bool | false | Whether the component is in loading state |
| DefaultLoadingText | string | "Loading..." | Whether the component is in loading state |
| Type | string | "button" | Type parameter |
| StopPropagation | bool | - | StopPropagation parameter |
| IconStart | RenderFragment? | - | Icon to display |
| IconEnd | RenderFragment? | - | Icon to display |
| Style | string? | - | Additional CSS styles |
| Tooltip | string? | - | Tooltip parameter |
| EnableRipple | bool | true | EnableRipple parameter |
| FullWidth | bool | false | FullWidth parameter |
| AnimationDuration | string | "duration-200" | AnimationDuration parameter |
| AriaLabel | string? | - | Label text for the component |
| AutoFocus | bool | false | AutoFocus parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| OnClick | MouseEventArgs | Raised when component is clicked |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailButton></TailButton>
```