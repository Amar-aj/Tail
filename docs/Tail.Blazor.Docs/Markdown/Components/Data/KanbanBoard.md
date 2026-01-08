---
title: KanbanBoard
package: Tail.Blazor.KanbanBoard
category: data
namespace: Tail.Blazor.KanbanBoard
route: /components/data/kanbanboard
is_generic: false
is_missing: false
---

# KanbanBoard

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

## Namespace

```csharp
using Tail.Blazor.KanbanBoard;
```

## Basic Usage

```razor
<TailKanbanBoard>Content</TailKanbanBoard>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.KanbanBoard

<TailKanbanBoard>
    Hello, World!
</TailKanbanBoard>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailKanbanBoard Style="Sample Style">
    Combined Parameters
</TailKanbanBoard>
```

## Advanced Examples

More complex usage scenarios:

More complex usage scenarios:

##

## Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailKanbanBoard >
        Action Button
    </TailKanbanBoard>
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Columns** | `List<KanbanColumn>` | new() | Columns parameter |
| **CardTemplate** | `RenderFragment<KanbanCard>` | default! | CardTemplate parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `KanbanColumn` | `class` | KanbanColumn property |
| `Title` | `string` | Title property |
| `Cards` | `List<KanbanCard>` | Cards property |
| `KanbanCard` | `class` | KanbanCard property |
| `Id` | `string` | Id property |
| `Title` | `string` | Title property |

## Base Class

The component inherits from `TailComponentBase` (from `Tail.Blazor.Core.Base`), which provides:

- `Class` parameter for additional CSS classes
- `AdditionalAttributes` parameter for additional HTML attributes

## Dependencies

- `Tail.Blazor.Core.Base` (required)
- `Microsoft.AspNetCore.Components`
- `Microsoft.AspNetCore.Components.Web`
- `Microsoft.AspNetCore.Components`
- `Microsoft.AspNetCore.Components.Web`
- `Microsoft.AspNetCore.Components`
- `Microsoft.AspNetCore.Components.Web`

## Target Frameworks

- .NET 8
- .NET 9
- .NET 10
