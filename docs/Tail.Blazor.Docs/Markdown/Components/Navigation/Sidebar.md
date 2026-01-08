---
title: Sidebar
package: Tail.Blazor.Sidebar
category: navigation
namespace: Tail.Blazor.Sidebar
route: /components/navigation/sidebar
is_generic: false
is_missing: false
---

# Sidebar

Independent NuGet package for the TailSidebar component.

## Installation

```bash
dotnet add package Tail.Blazor.Sidebar
```

## Features

- Collapsible sidebar
- Left/right positioning
- Header and footer support
- Smooth collapse animation
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Sidebar;
```

## Basic Usage

```razor
<TailSidebar>Content</TailSidebar>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Sidebar

<TailSidebar>
    Hello, World!
</TailSidebar>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailSidebar IsCollapsed="true" IsCollapsible="true">
    Combined Parameters
</TailSidebar>
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
    <TailSidebar >
        Action Button
    </TailSidebar>
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
| **IsCollapsed** | `bool` | - | IsCollapsed parameter |
| **IsCollapsible** | `bool` | true | IsCollapsible parameter |
| **Position** | `SidebarPosition` | SidebarPosition.Left | Position parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Enums

#### SidebarPosition

```csharp
public enum SidebarPosition
{
    Left,
}
```

/// Sidebar position.
///

#### Tail.Blazor.Sidebar;.SidebarPosition

```csharp
public enum Tail.Blazor.Sidebar;.SidebarPosition
{
    Left,
}
```

/// Sidebar position.
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
