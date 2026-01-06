# Tail.Blazor.Chart

Independent NuGet package for the TailChart component.

## Installation

```bash
dotnet add package Tail.Blazor.Chart
```

## Features

- Multiple chart types (Line, Bar, Area, Pie)
- SVG-based rendering
- Customizable size
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Chart;
```

## Component Usage

```razor
<TailChart></TailChart>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Data** | `List<double>` | new() | Data parameter |
| **ChartType** | `ChartType` | ChartType.Line | ChartType parameter |
| **Width** | `int` | 400 | Width parameter |
| **Height** | `int` | 200 | Height parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Enums

### ChartType

```csharp
public enum ChartType
{
    Line,
    Bar,
    Area,
}
```

/// Chart type options.
///

### Tail.Blazor.Chart;.ChartType

```csharp
public enum Tail.Blazor.Chart;.ChartType
{
    Line,
    Bar,
    Area,
}
```

/// Chart type options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Chart

<TailChart />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailChart />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailChart Data="10" Width="10" Height="10" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailChart Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailChart>

@* Using Class parameter *@
<TailChart Class="my-custom-class shadow-lg">
    With Custom Class
</TailChart>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailChart  />
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

- **Package ID**: `Tail.Blazor.Chart`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
