# Tail.Blazor.KanbanBoard

Independent NuGet package for the TailKanbanBoard component.

## Installation

```bash
dotnet add package Tail.Blazor.KanbanBoard
```

## Features

- Kanban board
- Multiple columns
- Custom card template
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Columns | List<KanbanColumn> | new() | Columns parameter |
| CardTemplate | RenderFragment<KanbanCard> | default! | CardTemplate parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| KanbanColumn | class | KanbanColumn property |
| Title | string | Title property |
| Cards | List<KanbanCard> | Cards property |
| KanbanCard | class | KanbanCard property |
| Id | string | Id property |
| Title | string | Title property |

## Methods

No additional public methods.

## Examples

```razor
<TailKanbanBoard></TailKanbanBoard>
```