---
title: ButtonGroup
package: Tail.Blazor.ButtonGroup
category: buttons
namespace: Tail.Blazor.ButtonGroup
route: /components/buttons/buttongroup
is_generic: false
is_missing: false
---

# ButtonGroup

Independent NuGet package for the TailButtonGroup component.

## Installation

```bash
dotnet add package Tail.Blazor.ButtonGroup
```

## Features

- Horizontal and vertical layouts
- Seamless button grouping
- Rounded corners
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ButtonGroup;
```

## Basic Usage

```razor
<TailButtonGroup>Content</TailButtonGroup>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ButtonGroup

<TailButtonGroup>
    Hello, World!
</TailButtonGroup>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailButtonGroup Size="ButtonGroupSize.Md">
    Medium Size
</TailButtonGroup>
```

**Disabled State**

```razor
<TailButtonGroup Disabled="true">
    Disabled
</TailButtonGroup>
```

## Variants

Different visual variants for various use cases:

```razor
<TailButtonGroup Variant="string?.Primary">Primary</TailButtonGroup>
<TailButtonGroup Variant="string?.Success">Success</TailButtonGroup>
<TailButtonGroup Variant="string?.Warning">Warning</TailButtonGroup>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailButtonGroup Size="ButtonGroupSize.Xs">Xs</TailButtonGroup>
<TailButtonGroup Size="ButtonGroupSize.Sm">Sm</TailButtonGroup>
<TailButtonGroup Size="ButtonGroupSize.Md">Md</TailButtonGroup>
<TailButtonGroup Size="ButtonGroupSize.Lg">Lg</TailButtonGroup>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailButtonGroup Disabled="true">Disabled</TailButtonGroup>
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailButtonGroup Size="ButtonGroupSize.Sm" Vertical="true">
    Combined Parameters
</TailButtonGroup>
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
    <TailButtonGroup Size="ButtonGroupSize.Sm">
        Action Button
    </TailButtonGroup>
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
| **Vertical** | `bool` | - | Vertical parameter |
| **Spacing** | `ButtonGroupSpacing` | ButtonGroupSpacing.None | Spacing parameter |
| **Size** | `ButtonGroupSize` | ButtonGroupSize.Md | Size of the component |
| **BorderRadius** | `ButtonGroupBorderRadius` | ButtonGroupBorderRadius.Md | BorderRadius parameter |
| **Attached** | `bool` | true | Attached parameter |
| **ShowBorder** | `bool` | true | ShowBorder parameter |
| **ShowShadow** | `bool` | false | ShowShadow parameter |
| **Style** | `string?` | - | Additional CSS styles |
| **Disabled** | `bool` | false | Whether the component is disabled |
| **AriaLabel** | `string?` | - | Label text for the component |
| **AnimationDuration** | `string` | "duration-200" | AnimationDuration parameter |
| **ResponsiveVertical** | `bool` | false | ResponsiveVertical parameter |
| **Variant** | `string?` | - | Visual variant style for the component |

### Enums

#### ButtonGroupSpacing

```csharp
public enum ButtonGroupSpacing
{
    None,
    Sm,
    Md,
}
```

/// Button group spacing options.
///

#### Tail.Blazor.ButtonGroup;.ButtonGroupSpacing

```csharp
public enum Tail.Blazor.ButtonGroup;.ButtonGroupSpacing
{
    None,
    Sm,
    Md,
}
```

/// Button group spacing options.
///

#### ButtonGroupSize

```csharp
public enum ButtonGroupSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Button group size options.
///

#### Tail.Blazor.ButtonGroup;.ButtonGroupSize

```csharp
public enum Tail.Blazor.ButtonGroup;.ButtonGroupSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Button group size options.
///

#### ButtonGroupBorderRadius

```csharp
public enum ButtonGroupBorderRadius
{
    None,
    Sm,
    Md,
    Lg,
}
```

/// Button group border radius options.
///

#### Tail.Blazor.ButtonGroup;.ButtonGroupBorderRadius

```csharp
public enum Tail.Blazor.ButtonGroup;.ButtonGroupBorderRadius
{
    None,
    Sm,
    Md,
    Lg,
}
```

/// Button group border radius options.
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
