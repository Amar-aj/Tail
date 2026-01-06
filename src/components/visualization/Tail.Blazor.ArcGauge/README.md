# Tail.Blazor.ArcGauge

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

## Component Usage

```razor
<TailArcGauge></TailArcGauge>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `int` | - | Current value of the component |
| **Size** | `int` | 200 | Size of the component |
| **StrokeWidth** | `int` | 20 | StrokeWidth parameter |
| **ShowLabel** | `bool` | true | Label text for the component |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ArcGauge

<TailArcGauge />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailArcGauge />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailArcGauge Value="10" StrokeWidth="10" ShowLabel="true" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailArcGauge Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailArcGauge>

@* Using Class parameter *@
<TailArcGauge Class="my-custom-class shadow-lg">
    With Custom Class
</TailArcGauge>
```

#### Accessibility

```razor
@* Accessible component with ARIA label and tooltip *@
<TailArcGauge ShowLabel="Primary action button">
    Accessible Button
</TailArcGauge>
```

### Real-World Example

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

- **Package ID**: `Tail.Blazor.ArcGauge`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
