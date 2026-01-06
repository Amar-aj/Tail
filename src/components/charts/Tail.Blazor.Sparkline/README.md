# Tail.Blazor.Sparkline

Independent NuGet package for the TailSparkline component.

## Installation

```bash
dotnet add package Tail.Blazor.Sparkline
```

## Features

- Mini sparkline chart
- Inline data visualization
- SVG-based rendering
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Sparkline;
```

## Component Usage

```razor
<TailSparkline></TailSparkline>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Data** | `List<double>` | new() | Data parameter |
| **Width** | `int` | 100 | Width parameter |
| **Height** | `int` | 30 | Height parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Sparkline

<TailSparkline />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailSparkline />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailSparkline Data="10" Width="10" Height="10" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailSparkline Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailSparkline>

@* Using Class parameter *@
<TailSparkline Class="my-custom-class shadow-lg">
    With Custom Class
</TailSparkline>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailSparkline  />
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

- **Package ID**: `Tail.Blazor.Sparkline`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
