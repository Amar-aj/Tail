# Tail.Blazor.FAB

Independent NuGet package for the TailFAB (Floating Action Button) component.

## Installation

```bash
dotnet add package Tail.Blazor.FAB
```

## Features

- 4 positions (TopLeft, TopRight, BottomLeft, BottomRight)
- Fixed positioning
- Circular design
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
| Position | FABPosition | FABPosition.BottomRight | Position parameter |
| Disabled | bool | - | Whether the component is disabled |
| IsLoading | bool | - | Whether the component is in loading state |
| Type | string | "button" | Type parameter |
| Style | string? | - | Additional CSS styles |
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
<TailFAB></TailFAB>
```