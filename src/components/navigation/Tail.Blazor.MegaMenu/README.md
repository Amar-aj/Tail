# Tail.Blazor.MegaMenu

Independent NuGet package for the TailMegaMenu component.

## Installation

```bash
dotnet add package Tail.Blazor.MegaMenu
```

## Features

- Mega menu with multiple columns
- Hover activation
- Section organization
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Trigger | RenderFragment? | - | Trigger parameter |
| Sections | List<MegaMenuSection> | new() | Sections parameter |
| Columns | int | 3 | Columns parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| MegaMenuSection | class | MegaMenuSection property |
| Title | string? | Title property |
| Items | List<MegaMenuItem> | Items property |
| MegaMenuItem | class | MegaMenuItem property |
| Label | string | Label property |
| Href | string? | Href property |

## Methods

No additional public methods.

## Examples

```razor
<TailMegaMenu></TailMegaMenu>
```