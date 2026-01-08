---
title: Icon
package: Tail.Blazor.Icon
category: icons
namespace: Tail.Blazor.Icon
route: /components/icons/icon
is_generic: false
is_missing: false
---

# Icon

Independent NuGet package for the TailIcon component.

## Installation

```bash
dotnet add package Tail.Blazor.Icon
```

## Features

- Icon component
- Built-in icons
- Custom SVG support
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Icon;
```

## Basic Usage

```razor
<TailIcon>Content</TailIcon>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Icon

<TailIcon>
    Hello, World!
</TailIcon>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailIcon Size="IconSize.Md">
    Medium Size
</TailIcon>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailIcon Size="IconSize.Xs">Xs</TailIcon>
<TailIcon Size="IconSize.Sm">Sm</TailIcon>
<TailIcon Size="IconSize.Md">Md</TailIcon>
<TailIcon Size="IconSize.Lg">Lg</TailIcon>
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailIcon Size="IconSize.Sm" Style="Sample Style">
    Combined Parameters
</TailIcon>
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
    <TailIcon Size="IconSize.Sm">
        Action Button
    </TailIcon>
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **CustomSvg** | `RenderFragment?` | - | CustomSvg parameter |
| **Name** | `IconName` | IconName.None | Name parameter |
| **Size** | `IconSize` | IconSize.Md | Size of the component |
| **Style** | `string?` | - | Additional CSS styles |

### Enums

#### IconName

```csharp
public enum IconName
{
    None,
    Home,
    User,
}
```

/// Icon name options.
///

#### Tail.Blazor.Icon;.IconName

```csharp
public enum Tail.Blazor.Icon;.IconName
{
    None,
    Home,
    User,
}
```

/// Icon name options.
///

#### IconSize

```csharp
public enum IconSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Icon size options.
///

#### Tail.Blazor.Icon;.IconSize

```csharp
public enum Tail.Blazor.Icon;.IconSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Icon size options.
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
