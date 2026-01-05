# Tail.Blazor.ButtonGroup

Independent NuGet package for the TailButtonGroup component.

## Installation

```bash
dotnet add package Tail.Blazor.ButtonGroup
```

## Features

- Horizontal and vertical layouts
- Seamless button grouping
- Rounded corners
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
| Vertical | bool | - | Vertical parameter |
| Spacing | ButtonGroupSpacing | ButtonGroupSpacing.None | Spacing parameter |
| Size | ButtonGroupSize | ButtonGroupSize.Md | Size of the component |
| BorderRadius | ButtonGroupBorderRadius | ButtonGroupBorderRadius.Md | BorderRadius parameter |
| Attached | bool | true | Attached parameter |
| ShowBorder | bool | true | ShowBorder parameter |
| ShowShadow | bool | false | ShowShadow parameter |
| Style | string? | - | Additional CSS styles |
| Disabled | bool | false | Whether the component is disabled |
| AriaLabel | string? | - | Label text for the component |
| AnimationDuration | string | "duration-200" | AnimationDuration parameter |
| ResponsiveVertical | bool | false | ResponsiveVertical parameter |
| Variant | string? | - | Visual variant style for the component |

## Events

No events exposed.

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailButtonGroup></TailButtonGroup>
```