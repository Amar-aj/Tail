# Tail.Blazor.KanbanBoard

Independent NuGet package for the TailKanbanBoard component.

## Installation

```bash
dotnet add package Tail.Blazor.KanbanBoard
```

## Usage

```razor
@using Tail.Blazor.KanbanBoard

<TailKanbanBoard Columns="@kanbanColumns">
    <CardTemplate>
        <div>@context.Title</div>
    </CardTemplate>
</TailKanbanBoard>
```

## Features

- Kanban board
- Multiple columns
- Custom card template
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~5 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

