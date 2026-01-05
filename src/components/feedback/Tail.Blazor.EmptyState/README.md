# Tail.Blazor.EmptyState

Independent NuGet package for the TailEmptyState component.

## Installation

```bash
dotnet add package Tail.Blazor.EmptyState
```

## Features

- Empty state display
- 3 sizes (Sm, Md, Lg)
- 3 variants (Default, Minimal, Detailed)
- Custom icon support
- Title and description
- Action button support
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
| Action | RenderFragment? | - | Action parameter |
| Title | string? | - | Title parameter |
| Description | string? | - | Description parameter |
| Size | EmptyStateSize | EmptyStateSize.Md | Size of the component |
| Variant | EmptyStateVariant | EmptyStateVariant.Default | Visual variant style for the component |
| ShowDefaultIcon | bool | true | Icon to display |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailEmptyState></TailEmptyState>
```