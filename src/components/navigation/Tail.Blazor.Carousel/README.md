# Tail.Blazor.Carousel

Independent NuGet package for the TailCarousel component.

## Installation

```bash
dotnet add package Tail.Blazor.Carousel
```

## Features

- Image/content carousel
- Previous/Next controls
- Indicator dots
- Auto-play option
- Smooth transitions
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Carousel;
```

## Component Usage

```razor
<TailCarousel></TailCarousel>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Items** | `List<RenderFragment>` | new() | Data items collection |
| **CurrentIndex** | `int` | - | CurrentIndex parameter |
| **ShowControls** | `bool` | true | ShowControls parameter |
| **ShowIndicators** | `bool` | true | ShowIndicators parameter |
| **AutoPlay** | `bool` | - | AutoPlay parameter |
| **AutoPlayInterval** | `int` | 3000 | AutoPlayInterval parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Carousel

<TailCarousel>
    Hello, World!
</TailCarousel>
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailCarousel>Content</TailCarousel>
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailCarousel CurrentIndex="10" ShowControls="true" ShowIndicators="true" AutoPlay="true">
    Combined Parameters
</TailCarousel>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailCarousel Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailCarousel>

@* Using Class parameter *@
<TailCarousel Class="my-custom-class shadow-lg">
    With Custom Class
</TailCarousel>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailCarousel >
        Action Button
    </TailCarousel>
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

- **Package ID**: `Tail.Blazor.Carousel`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
