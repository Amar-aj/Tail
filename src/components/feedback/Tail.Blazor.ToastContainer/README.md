# Tail.Blazor.ToastContainer

Independent NuGet package for the TailToastContainer component.

## Installation

```bash
dotnet add package Tail.Blazor.ToastContainer
```

## Features

- Toast container with positioning
- 6 positions (TopLeft, TopRight, TopCenter, BottomLeft, BottomRight, BottomCenter)
- Max toasts limit
- Programmatic toast display
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Position | ToastPosition | ToastPosition.TopRight | Position parameter |
| MaxToasts | int | 5 | Maximum value constraint |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| ShowToast | void | ShowToast property |
| ToastItem | class | ToastItem property |
| Message | string | Message property |
| Title | string? | Title property |
| Variant | ToastVariant | Variant property |
| Dismissible | bool | Dismissible property |
| AutoDismissAfter | int? | AutoDismissAfter property |

## Methods

No additional public methods.

## Examples

```razor
<TailToastContainer></TailToastContainer>
```