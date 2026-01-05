# Tail.Blazor.ListView

Independent NuGet package for the TailListView component.

## Installation

```bash
dotnet add package Tail.Blazor.ListView
```

## Features

- List view with items
- Custom item template
- Hover effects
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

| Name | Description |
| --- | --- |
| T | Generic type parameter for typed data |

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Items | List<T> | new() | Data items collection |
| ItemTemplate | RenderFragment<T> | default! | ItemTemplate parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailListView></TailListView>
```