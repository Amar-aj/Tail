---
title: MegaMenu
package: Tail.Blazor.MegaMenu
category: navigation
namespace: Tail.Blazor.MegaMenu
route: /components/navigation/megamenu
is_generic: false
is_missing: false
---

# MegaMenu

Independent NuGet package for the TailMegaMenu component.

## Installation

```bash
dotnet add package Tail.Blazor.MegaMenu
```

## Features

- Mega menu with multiple columns
- Hover activation
- Section organization
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.MegaMenu;
```

## Basic Usage

```razor
<TailMegaMenu>Content</TailMegaMenu>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.MegaMenu

<TailMegaMenu>
    Hello, World!
</TailMegaMenu>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailMegaMenu Columns="10" Style="Sample Style">
    Combined Parameters
</TailMegaMenu>
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
    <TailMegaMenu >
        Action Button
    </TailMegaMenu>
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Trigger** | `RenderFragment?` | - | Trigger parameter |
| **Sections** | `List<MegaMenuSection>` | new() | Sections parameter |
| **Columns** | `int` | 3 | Columns parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `MegaMenuSection` | `class` | MegaMenuSection property |
| `Title` | `string?` | Title property |
| `Items` | `List<MegaMenuItem>` | Items property |
| `MegaMenuItem` | `class` | MegaMenuItem property |
| `Label` | `string` | Label property |
| `Href` | `string?` | Href property |

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
