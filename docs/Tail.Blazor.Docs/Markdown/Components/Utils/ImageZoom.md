---
title: ImageZoom
package: Tail.Blazor.ImageZoom
category: utils
namespace: Tail.Blazor.ImageZoom
route: /components/utils/imagezoom
is_generic: false
is_missing: false
---

# ImageZoom

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

## Basic Usage

```razor
<TailImageZoom />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ImageZoom

<TailImageZoom />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailImageZoom ImageSrc="Sample ImageSrc" Alt="Sample Alt" ZoomLevel="10" Style="Sample Style" />
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
    <TailImageZoom  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ImageSrc** | `string` | string.Empty | ImageSrc parameter |
| **Alt** | `string?` | - | Alt parameter |
| **ZoomLevel** | `double` | 2.0 | ZoomLevel parameter |
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
