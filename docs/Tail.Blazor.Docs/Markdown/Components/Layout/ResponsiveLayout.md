---
title: ResponsiveLayout
package: Tail.Blazor.ResponsiveLayout
category: layout
namespace: Tail.Blazor.ResponsiveLayout
route: /components/layout/responsivelayout
is_generic: false
is_missing: false
---

# ResponsiveLayout

Independent NuGet package for the TailResponsiveLayout component.

## Installation

```bash
dotnet add package Tail.Blazor.ResponsiveLayout
```

## Features

- Responsive layout container
- Breakpoint-based sizing
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ResponsiveLayout;
```

## Basic Usage

```razor
<TailResponsiveLayout>Content</TailResponsiveLayout>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ResponsiveLayout

<TailResponsiveLayout>
    Hello, World!
</TailResponsiveLayout>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailResponsiveLayout AppName="Sample AppName">
    Combined Parameters
</TailResponsiveLayout>
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
    <TailResponsiveLayout >
        Action Button
    </TailResponsiveLayout>
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
| **LogoTemplate** | `RenderFragment?` | - | LogoTemplate parameter |
| **SidebarContent** | `RenderFragment?` | - | SidebarContent parameter |
| **AvatarContent** | `RenderFragment?` | - | AvatarContent parameter |
| **AppName** | `string?` | - | AppName parameter |
| **ShowMenuToggle** | `bool` | true | ShowMenuToggle parameter |
| **ShowThemeToggle** | `bool` | true | ShowThemeToggle parameter |
| **ShowAvatar** | `bool` | false | ShowAvatar parameter |
| **ShowSidebar** | `bool` | true | ShowSidebar parameter |
| **ShowHeader** | `bool` | true | ShowHeader parameter |
| **StickyHeader** | `bool` | true | StickyHeader parameter |
| **HeaderShadow** | `bool` | true | HeaderShadow parameter |
| **MenuOpenByDefault** | `bool` | true | MenuOpenByDefault parameter |
| **MenuOpenOnMobileByDefault** | `bool` | false | MenuOpenOnMobileByDefault parameter |
| **AutoHideOnMobileAfterNavigation** | `bool` | true | AutoHideOnMobileAfterNavigation parameter |
| **LayoutMode** | `LayoutMode` | LayoutMode.DrawerLeft | LayoutMode parameter |
| **Density** | `DensityMode` | DensityMode.Normal | Density parameter |
| **MobileMenuTitle** | `string?` | - | MobileMenuTitle parameter |
| **Style** | `string?` | - | Additional CSS styles |
| **HideScrollbars** | `bool` | true | HideScrollbars parameter |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `Dispose` | `void` | Dispose property |

### Enums

#### LayoutMode

```csharp
public enum LayoutMode
{
    DrawerLeft,
    DrawerRight,
    FixedLeft,
    FixedRight,
    sidebar,
}
```

/// Layout mode for responsive layout component.
///

#### Tail.Blazor.ResponsiveLayout;.LayoutMode

```csharp
public enum Tail.Blazor.ResponsiveLayout;.LayoutMode
{
    DrawerLeft,
    DrawerRight,
    FixedLeft,
    FixedRight,
    sidebar,
}
```

/// Layout mode for responsive layout component.
///

#### DensityMode

```csharp
public enum DensityMode
{
    Compact,
    Normal,
}
```

/// Density mode for responsive layout component.
///

#### Tail.Blazor.ResponsiveLayout;.DensityMode

```csharp
public enum Tail.Blazor.ResponsiveLayout;.DensityMode
{
    Compact,
    Normal,
}
```

/// Density mode for responsive layout component.
///

#### ResponsiveLayoutBreakpoint

```csharp
public enum ResponsiveLayoutBreakpoint
{
    Sm,
    Md,
    Lg,
}
```

/// Responsive layout breakpoint.
///

#### Tail.Blazor.ResponsiveLayout;.ResponsiveLayoutBreakpoint

```csharp
public enum Tail.Blazor.ResponsiveLayout;.ResponsiveLayoutBreakpoint
{
    Sm,
    Md,
    Lg,
}
```

/// Responsive layout breakpoint.
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
- `Tail.Blazor.Button`
- `Tail.Blazor.Core.Theme`

## Target Frameworks

- .NET 8
- .NET 9
- .NET 10
