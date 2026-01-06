# Tail.Blazor.ImageZoom

Independent NuGet package for the TailImageZoom component.

## Installation

```bash
dotnet add package Tail.Blazor.ImageZoom
```

## Features

- Image zoom on hover
- Customizable zoom level
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ImageZoom;
```

## Component Usage

```razor
<TailImageZoom></TailImageZoom>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ImageSrc** | `string` | string.Empty | ImageSrc parameter |
| **Alt** | `string?` | - | Alt parameter |
| **ZoomLevel** | `double` | 2.0 | ZoomLevel parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ImageZoom

<TailImageZoom />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailImageZoom />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailImageZoom ImageSrc="Sample ImageSrc" Alt="Sample Alt" ZoomLevel="10" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailImageZoom Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailImageZoom>

@* Using Class parameter *@
<TailImageZoom Class="my-custom-class shadow-lg">
    With Custom Class
</TailImageZoom>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailImageZoom  />
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

- **Package ID**: `Tail.Blazor.ImageZoom`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
