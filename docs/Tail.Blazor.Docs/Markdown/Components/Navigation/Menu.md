---
title: Menu
package: Tail.Blazor.Menu
category: navigation
namespace: Tail.Blazor.Menu
route: /components/navigation/menu
is_generic: false
is_missing: false
---

# Menu

Independent NuGet package for the TailMenu component.

## Installation

```bash
dotnet add package Tail.Blazor.Menu
```

## Features

- Menu container
- 3 variants (Default, Vertical, Horizontal)
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Menu;
```

## Basic Usage

```razor
<TailMenu>Content</TailMenu>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Menu

<TailMenu>
    Hello, World!
</TailMenu>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailMenu Variant="MenuVariant.Default">
    Primary Action
</TailMenu>
```

## Variants

Different visual variants for various use cases:

```razor
<TailMenu Variant="MenuVariant.Default">Default</TailMenu>
<TailMenu Variant="MenuVariant.Vertical">Vertical</TailMenu>
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailMenu Variant="MenuVariant.Default">
    Combined Parameters
</TailMenu>
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
    <TailMenu Variant="MenuVariant.Default">
        Action Button
    </TailMenu>
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
| **HeaderTemplate** | `RenderFragment?` | - | HeaderTemplate parameter |
| **FooterTemplate** | `RenderFragment?` | - | FooterTemplate parameter |
| **Variant** | `MenuVariant` | MenuVariant.Default | Visual variant style for the component |
| **Orientation** | `MenuOrientation` | MenuOrientation.Vertical | Orientation parameter |
| **Align** | `MenuAlign` | MenuAlign.Start | Align parameter |
| **Dense** | `bool` | false | Dense parameter |
| **HoverBackground** | `string?` | "var(--color-surface-hover)" | HoverBackground parameter |
| **HoverTextColor** | `string?` | "var(--color-text-primary)" | Color scheme for the component |
| **ActiveBackground** | `string?` | "var(--color-primary)" | ActiveBackground parameter |
| **ActiveTextColor** | `string?` | "var(--color-text-on-primary, #ffffff)" | Color scheme for the component |
| **AriaLabel** | `string?` | "Main menu" | Label text for the component |
| **Style** | `string?` | - | Additional CSS styles |
| **ItemClass** | `string?` | - | Additional CSS classes |
| **AnimationDuration** | `int` | 200 | AnimationDuration parameter |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `MenuOrientation` | `enum` | MenuOrientation property |
| `MenuAlign` | `enum` | MenuAlign property |

### Enums

#### MenuVariant

```csharp
public enum MenuVariant
{
    Default,
    Vertical,
}
```

/// Menu variant styles.
///

#### Tail.Blazor.Menu;.MenuVariant

```csharp
public enum Tail.Blazor.Menu;.MenuVariant
{
    Default,
    Vertical,
}
```

/// Menu variant styles.
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
