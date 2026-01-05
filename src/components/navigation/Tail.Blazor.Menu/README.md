# Tail.Blazor.Menu

Independent NuGet package for the TailMenu component.

## Installation

```bash
dotnet add package Tail.Blazor.Menu
```

## Features

- Menu container
- 3 variants (Default, Vertical, Horizontal)
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
| HeaderTemplate | RenderFragment? | - | HeaderTemplate parameter |
| FooterTemplate | RenderFragment? | - | FooterTemplate parameter |
| Variant | MenuVariant | MenuVariant.Default | Visual variant style for the component |
| Orientation | MenuOrientation | MenuOrientation.Vertical | Orientation parameter |
| Align | MenuAlign | MenuAlign.Start | Align parameter |
| Dense | bool | false | Dense parameter |
| HoverBackground | string? | "var(--color-surface-hover)" | HoverBackground parameter |
| HoverTextColor | string? | "var(--color-text-primary)" | Color scheme for the component |
| ActiveBackground | string? | "var(--color-primary)" | ActiveBackground parameter |
| ActiveTextColor | string? | "var(--color-text-on-primary, #ffffff)" | Color scheme for the component |
| AriaLabel | string? | "Main menu" | Label text for the component |
| Style | string? | - | Additional CSS styles |
| ItemClass | string? | - | Additional CSS classes |
| AnimationDuration | int | 200 | AnimationDuration parameter |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| MenuOrientation | enum | MenuOrientation property |
| MenuAlign | enum | MenuAlign property |

## Methods

No additional public methods.

## Examples

```razor
<TailMenu></TailMenu>
```