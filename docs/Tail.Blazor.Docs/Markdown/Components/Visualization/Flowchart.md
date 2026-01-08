---
title: Flowchart
package: Tail.Blazor.Flowchart
category: visualization
namespace: Tail.Blazor.Flowchart
route: /components/visualization/flowchart
is_generic: false
is_missing: false
---

# Flowchart

Independent NuGet package for the TailFlowchart component.

## Installation

```bash
dotnet add package Tail.Blazor.Flowchart
```

## Features

- Flowchart visualization
- Nodes and connections
- SVG-based rendering
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Flowchart;
```

## Basic Usage

```razor
<TailFlowchart />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Flowchart

<TailFlowchart />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailFlowchart Width="10" Height="10" Style="Sample Style" />
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
    <TailFlowchart  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Nodes** | `List<FlowchartNode>` | new() | Nodes parameter |
| **Connections** | `List<FlowchartConnection>` | new() | Connections parameter |
| **Width** | `int` | 800 | Width parameter |
| **Height** | `int` | 600 | Height parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `FlowchartNode` | `class` | FlowchartNode property |
| `Id` | `string` | Id property |
| `Label` | `string` | Label property |
| `X` | `double` | X property |
| `Y` | `double` | Y property |
| `FlowchartConnection` | `class` | FlowchartConnection property |
| `FromId` | `string` | FromId property |
| `ToId` | `string` | ToId property |
| `FromX` | `double` | FromX property |
| `FromY` | `double` | FromY property |
| `ToX` | `double` | ToX property |
| `ToY` | `double` | ToY property |

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
