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

## Namespace

```csharp
using Tail.Blazor.KanbanBoard;
```

## Component Usage

```razor
<TailKanbanBoard></TailKanbanBoard>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Columns** | `List<KanbanColumn>` | new() | Columns parameter |
| **CardTemplate** | `RenderFragment<KanbanCard>` | default! | CardTemplate parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.KanbanBoard

<TailKanbanBoard>
    Hello, World!
</TailKanbanBoard>
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailKanbanBoard>Content</TailKanbanBoard>
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailKanbanBoard Style="Sample Style">
    Combined Parameters
</TailKanbanBoard>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailKanbanBoard Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailKanbanBoard>

@* Using Class parameter *@
<TailKanbanBoard Class="my-custom-class shadow-lg">
    With Custom Class
</TailKanbanBoard>
```

### Real-World Example

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

## Package Information

- **Package ID**: `Tail.Blazor.KanbanBoard`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
