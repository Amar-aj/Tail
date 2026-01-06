# Tail.Blazor.Tree

Independent NuGet package for the TailTree component.

## Installation

```bash
dotnet add package Tail.Blazor.Tree
```

## Features

- Tree view component
- Expandable nodes
- Hierarchical structure
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Tree;
```

## Component Usage

```razor
<TailTree></TailTree>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Nodes** | `List<TreeNodeItem>` | new() | Nodes parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Tree

<TailTree />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailTree />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailTree Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailTree Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailTree>

@* Using Class parameter *@
<TailTree Class="my-custom-class shadow-lg">
    With Custom Class
</TailTree>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailTree  />
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

- **Package ID**: `Tail.Blazor.Tree`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
