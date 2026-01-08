---
title: Card
package: Tail.Blazor.Card
category: layout
namespace: Tail.Blazor.Card
route: /components/layout/card
is_generic: false
is_missing: false
---

# Card

Independent NuGet package for the TailCard component.

## Installation

```bash
dotnet add package Tail.Blazor.Card
```

## Features

- Card with header/footer
- Hoverable option
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Card;
```

## Basic Usage

```razor
<TailCard>Content</TailCard>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Card

<TailCard>
    Hello, World!
</TailCard>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailCard Hoverable="true" Style="Sample Style">
    Combined Parameters
</TailCard>
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
    <TailCard >
        Action Button
    </TailCard>
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Header** | `RenderFragment?` | - | Header parameter |
| **Footer** | `RenderFragment?` | - | Footer parameter |
| **Hoverable** | `bool` | - | Hoverable parameter |
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
