---
title: ArcGauge
package: Tail.Blazor.ArcGauge
category: visualization
namespace: Tail.Blazor.ArcGauge
route: /components/visualization/arcgauge
is_generic: false
is_missing: false
---

# ArcGauge

Independent NuGet package for the TailArcGauge component.

## Installation

```bash
dotnet add package Tail.Blazor.ArcGauge
```

## Features

- Arc gauge visualization
- Percentage display
- Customizable size
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ArcGauge;
```

## Basic Usage

```razor
<TailArcGauge />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ArcGauge

<TailArcGauge />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailArcGauge Size="12">Small</TailArcGauge>
<TailArcGauge Size="16">Medium</TailArcGauge>
<TailArcGauge Size="24">Large</TailArcGauge>
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailArcGauge Value="10" StrokeWidth="10" ShowLabel="true" Style="Sample Style" />
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
    <TailArcGauge  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `int` | - | Current value of the component |
| **Size** | `int` | 200 | Size of the component |
| **StrokeWidth** | `int` | 20 | StrokeWidth parameter |
| **ShowLabel** | `bool` | true | Label text for the component |
| **Style** | `string?` | - | Additional CSS styles |

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
