# Tail.Blazor.FloatingActionMenu

Independent NuGet package for the TailFloatingActionMenu component.

## Installation

```bash
dotnet add package Tail.Blazor.FloatingActionMenu
```

## Features

- Floating action menu
- Expandable menu items
- 4 position options
- Icon support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Items | List<FloatingActionMenuItem> | new() | Data items collection |
| Position | FloatingActionMenuPosition | FloatingActionMenuPosition.BottomRight | Position parameter |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| OnItemClick | FloatingActionMenuItem | Raised when component is clicked |

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| FloatingActionMenuItem | class | FloatingActionMenuItem property |
| Label | string | Label property |
| Icon | RenderFragment? | Icon property |
| OnClick | EventCallback | OnClick property |
| FloatingActionMenuPosition | enum | FloatingActionMenuPosition property |

## Methods

No additional public methods.

## Examples

```razor
<TailFloatingActionMenu></TailFloatingActionMenu>
```