# Tail.Blazor.ContextMenu

Independent NuGet package for the TailContextMenu component.

## Installation

```bash
dotnet add package Tail.Blazor.ContextMenu
```

## Features

- Right-click context menu
- Menu items with actions
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
| Items | List<ContextMenuItem> | new() | Data items collection |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| OnItemClick | ContextMenuItem | Raised when component is clicked |

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| ContextMenuItem | class | ContextMenuItem property |
| Label | string | Label property |
| OnClick | EventCallback | OnClick property |

## Methods

No additional public methods.

## Examples

```razor
<TailContextMenu></TailContextMenu>
```