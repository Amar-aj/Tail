# Tail.Blazor.Sidebar

Independent NuGet package for the TailSidebar component.

## Installation

```bash
dotnet add package Tail.Blazor.Sidebar
```

## Features

- Collapsible sidebar
- Left/right positioning
- Header and footer support
- Smooth collapse animation
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
| Header | RenderFragment? | - | Header parameter |
| Footer | RenderFragment? | - | Footer parameter |
| IsCollapsed | bool | - | IsCollapsed parameter |
| IsCollapsible | bool | true | IsCollapsible parameter |
| Position | SidebarPosition | SidebarPosition.Left | Position parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailSidebar></TailSidebar>
```