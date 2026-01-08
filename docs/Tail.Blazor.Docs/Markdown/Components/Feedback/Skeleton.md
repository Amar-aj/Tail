---
title: Skeleton
package: Tail.Blazor.Skeleton
category: feedback
namespace: Tail.Blazor.Skeleton
route: /components/feedback/skeleton
is_generic: false
is_missing: false
---

# Skeleton

Independent NuGet package for the TailSkeleton component.

## Installation

```bash
dotnet add package Tail.Blazor.Skeleton
```

## Features

- 4 types (Text, Circle, Rectangle, Custom)
- Customizable width and height
- Animation option
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Skeleton;
```

## Basic Usage

```razor
<TailSkeleton>Content</TailSkeleton>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Skeleton

<TailSkeleton>
    Hello, World!
</TailSkeleton>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailSkeleton Width="10" Height="10" Animated="true">
    Combined Parameters
</TailSkeleton>
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
    <TailSkeleton >
        Action Button
    </TailSkeleton>
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
| **Type** | `SkeletonType` | SkeletonType.Text | Type parameter |
| **Width** | `int?` | - | Width parameter |
| **Height** | `int?` | - | Height parameter |
| **Animated** | `bool` | true | Animated parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Enums

#### SkeletonType

```csharp
public enum SkeletonType
{
    Text,
    Circle,
    Rectangle,
}
```

/// Skeleton type options.
///

#### Tail.Blazor.Skeleton;.SkeletonType

```csharp
public enum Tail.Blazor.Skeleton;.SkeletonType
{
    Text,
    Circle,
    Rectangle,
}
```

/// Skeleton type options.
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
