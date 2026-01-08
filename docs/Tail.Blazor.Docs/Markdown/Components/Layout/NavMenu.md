---
title: NavMenu
package: Tail.Blazor.NavMenu
category: layout
namespace: Tail.Blazor.NavMenu
route: /components/layout/navmenu
is_generic: false
is_missing: false
---

# NavMenu

Independent NuGet package for the TailNavMenu component.

## Installation

```bash
dotnet add package Tail.Blazor.NavMenu
```

## Features

- Navigation menu
- Horizontal/vertical orientation
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.NavMenu;
```

## Basic Usage

```razor
<TailNavMenu>Content</TailNavMenu>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.NavMenu

<TailNavMenu>
    Hello, World!
</TailNavMenu>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailNavMenu Style="Sample Style">
    Combined Parameters
</TailNavMenu>
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
    <TailNavMenu >
        Action Button
    </TailNavMenu>
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
| **Orientation** | `NavMenuOrientation` | NavMenuOrientation.Horizontal | Orientation parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Enums

#### NavMenuOrientation

```csharp
public enum NavMenuOrientation
{
    Horizontal,
}
```

/// Nav menu orientation.
///

#### Tail.Blazor.NavMenu;.NavMenuOrientation

```csharp
public enum Tail.Blazor.NavMenu;.NavMenuOrientation
{
    Horizontal,
}
```

/// Nav menu orientation.
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
