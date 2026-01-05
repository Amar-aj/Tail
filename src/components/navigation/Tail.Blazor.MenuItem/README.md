# Tail.Blazor.MenuItem

Independent NuGet package for the TailMenuItem component.

## Installation

```bash
dotnet add package Tail.Blazor.MenuItem
```

## Features

- Menu item with link
- Icon support
- Badge support
- Active state
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
| Icon | RenderFragment? | - | Icon to display |
| Badge | RenderFragment? | - | Badge parameter |
| Href | string? | "#" | Href parameter |
| IsActive | bool | - | IsActive parameter |
| Target | string? | - | Target parameter |
| Disabled | bool | false | Whether the component is disabled |
| PreventDefault | bool | true | PreventDefault parameter |
| Style | string? | - | Additional CSS styles |
| ItemClass | string? | - | Additional CSS classes |
| Bordered | bool | false | Bordered parameter |
| Shadow | ShadowLevel | ShadowLevel.None | Shadow parameter |
| Underline | bool | false | Underline parameter |
| BorderColor | string? | - | Color scheme for the component |

## Events

| Event | Type | Description |
| --- | --- | --- |
| OnClick | MenuItemClickArgs | Raised when component is clicked |

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| ShadowLevel | enum | ShadowLevel property |
| MenuItemClickArgs | record | MenuItemClickArgs property |

## Methods

No additional public methods.

## Examples

```razor
<TailMenuItem></TailMenuItem>
```