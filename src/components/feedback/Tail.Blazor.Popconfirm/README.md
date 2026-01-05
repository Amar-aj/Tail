# Tail.Blazor.Popconfirm

Independent NuGet package for the TailPopconfirm component.

## Installation

```bash
dotnet add package Tail.Blazor.Popconfirm
```

## Features

- Popconfirm dialog
- Click or hover trigger
- 4 placement options (Top, Bottom, Left, Right)
- Custom confirm/cancel text
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
| Title | string | "Are you sure?" | Title parameter |
| ConfirmText | string | "Confirm" | ConfirmText parameter |
| CancelText | string | "Cancel" | CancelText parameter |
| Trigger | PopconfirmTrigger | PopconfirmTrigger.Click | Trigger parameter |
| Placement | PopconfirmPlacement | PopconfirmPlacement.Top | Placement parameter |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| OnConfirm | void | OnConfirm callback |
| OnCancel | void | OnCancel callback |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailPopconfirm></TailPopconfirm>
```