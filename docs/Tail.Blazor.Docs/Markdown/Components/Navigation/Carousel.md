---
title: Carousel
package: Tail.Blazor.Carousel
category: navigation
namespace: Tail.Blazor.Carousel
route: /components/navigation/carousel
is_generic: false
is_missing: false
---

# Carousel

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

## Basic Usage

```razor
<TailCarousel>Content</TailCarousel>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Carousel

<TailCarousel>
    Hello, World!
</TailCarousel>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailCarousel CurrentIndex="10" ShowControls="true" ShowIndicators="true" AutoPlay="true">
    Combined Parameters
</TailCarousel>
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
    <TailCarousel >
        Action Button
    </TailCarousel>
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Items** | `List<RenderFragment>` | new() | Data items collection |
| **CurrentIndex** | `int` | - | CurrentIndex parameter |
| **ShowControls** | `bool` | true | ShowControls parameter |
| **ShowIndicators** | `bool` | true | ShowIndicators parameter |
| **AutoPlay** | `bool` | - | AutoPlay parameter |
| **AutoPlayInterval** | `int` | 3000 | AutoPlayInterval parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `Dispose` | `void` | Dispose property |

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
