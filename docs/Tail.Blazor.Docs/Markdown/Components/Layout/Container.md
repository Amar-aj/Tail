---
title: Container
package: Tail.Blazor.Container
category: layout
namespace: Tail.Blazor.Container
route: /components/layout/container
is_generic: false
is_missing: false
---

# Container

Independent NuGet package for the TailContainer component.

## Installation

```bash
dotnet add package Tail.Blazor.Container
```

## Features

- Container with sizes
- 6 sizes (Sm, Md, Lg, Xl, Xxl, Full)
- Responsive design
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Container;
```

## Basic Usage

```razor
<TailContainer>Content</TailContainer>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Container

<TailContainer>
    Hello, World!
</TailContainer>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailContainer Size="ContainerSize.Lg">
    Medium Size
</TailContainer>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailContainer Size="ContainerSize.Sm">Sm</TailContainer>
<TailContainer Size="ContainerSize.Md">Md</TailContainer>
<TailContainer Size="ContainerSize.Lg">Lg</TailContainer>
<TailContainer Size="ContainerSize.Xl">Xl</TailContainer>
<TailContainer Size="ContainerSize.Xxl">Xxl</TailContainer>
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailContainer Size="ContainerSize.Md" Style="Sample Style" HideScrollbars="true">
    Combined Parameters
</TailContainer>
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
    <TailContainer Size="ContainerSize.Md">
        Action Button
    </TailContainer>
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
| **Size** | `ContainerSize` | ContainerSize.Md | Size of the component |
| **Style** | `string?` | - | Additional CSS styles |
| **HideScrollbars** | `bool` | true | HideScrollbars parameter |

### Enums

#### ContainerSize

```csharp
public enum ContainerSize
{
    Sm,
    Md,
    Lg,
    Xl,
    Xxl,
}
```

/// Container size options.
///

#### Tail.Blazor.Container;.ContainerSize

```csharp
public enum Tail.Blazor.Container;.ContainerSize
{
    Sm,
    Md,
    Lg,
    Xl,
    Xxl,
}
```

/// Container size options.
///

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
