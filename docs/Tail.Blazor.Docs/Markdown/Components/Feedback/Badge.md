---
title: Badge
package: Tail.Blazor.Badge
category: feedback
namespace: Tail.Blazor.Badge
route: /components/feedback/badge
is_generic: false
is_missing: false
---

# Badge

Independent NuGet package for the TailBadge component.

## Installation

```bash
dotnet add package Tail.Blazor.Badge
```

## Features

- 6 variants (Primary, Success, Warning, Danger, Info, Gray)
- 3 sizes (Sm, Md, Lg)
- Dot indicator option
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Badge;
```

## Basic Usage

```razor
<TailBadge>Content</TailBadge>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Badge

<TailBadge>
    Hello, World!
</TailBadge>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailBadge Variant="BadgeVariant.Primary">
    Primary Action
</TailBadge>
```

**Medium Size**

```razor
<TailBadge Size="BadgeSize.Sm">
    Medium Size
</TailBadge>
```

## Variants

Different visual variants for various use cases:

```razor
<TailBadge Variant="BadgeVariant.Primary">Primary</TailBadge>
<TailBadge Variant="BadgeVariant.Success">Success</TailBadge>
<TailBadge Variant="BadgeVariant.Warning">Warning</TailBadge>
<TailBadge Variant="BadgeVariant.Danger">Danger</TailBadge>
<TailBadge Variant="BadgeVariant.Info">Info</TailBadge>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailBadge Size="BadgeSize.Sm">Sm</TailBadge>
<TailBadge Size="BadgeSize.Md">Md</TailBadge>
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailBadge Variant="BadgeVariant.Primary" Size="BadgeSize.Md" ShowDot="true" Style="Sample Style">
    Combined Parameters
</TailBadge>
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
    <TailBadge Variant="BadgeVariant.Primary" Size="BadgeSize.Md">
        Action Button
    </TailBadge>
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
| **Variant** | `BadgeVariant` | BadgeVariant.Primary | Visual variant style for the component |
| **Size** | `BadgeSize` | BadgeSize.Md | Size of the component |
| **ShowDot** | `bool` | - | ShowDot parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Enums

#### BadgeVariant

```csharp
public enum BadgeVariant
{
    Primary,
    Success,
    Warning,
    Danger,
    Info,
}
```

/// Badge variant styles.
///

#### Tail.Blazor.Badge;.BadgeVariant

```csharp
public enum Tail.Blazor.Badge;.BadgeVariant
{
    Primary,
    Success,
    Warning,
    Danger,
    Info,
}
```

/// Badge variant styles.
///

#### BadgeSize

```csharp
public enum BadgeSize
{
    Sm,
    Md,
}
```

/// Badge size options.
///

#### Tail.Blazor.Badge;.BadgeSize

```csharp
public enum Tail.Blazor.Badge;.BadgeSize
{
    Sm,
    Md,
}
```

/// Badge size options.
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
