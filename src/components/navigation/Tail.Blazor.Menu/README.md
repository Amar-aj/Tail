# Tail.Blazor.Menu

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

## Component Usage

```razor
<TailMenu></TailMenu>
```

## Parameters

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

## Events

No events exposed.

## Enums

### MenuVariant

```csharp
public enum MenuVariant
{
    Default,
    Vertical,
}
```

/// Menu variant styles.
///

### Tail.Blazor.Menu;.MenuVariant

```csharp
public enum Tail.Blazor.Menu;.MenuVariant
{
    Default,
    Vertical,
}
```

/// Menu variant styles.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Menu

<TailMenu>
    Hello, World!
</TailMenu>
```

### Common Patterns

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailMenu Variant="MenuVariant.Default">
    Primary Action
</TailMenu>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailMenu>Content</TailMenu>
```

### Variants

Different visual variants for various use cases:

```razor
<TailMenu Variant="MenuVariant.Default">Default</TailMenu>
<TailMenu Variant="MenuVariant.Vertical">Vertical</TailMenu>
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailMenu Variant="MenuVariant.Default">
    Combined Parameters
</TailMenu>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailMenu Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailMenu>

@* Using Class parameter *@
<TailMenu Class="my-custom-class shadow-lg">
    With Custom Class
</TailMenu>
```

#### Accessibility

```razor
@* Accessible component with ARIA label and tooltip *@
<TailMenu Variant="Primary action button">
    Accessible Button
</TailMenu>
```

### Real-World Example

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

## Package Information

- **Package ID**: `Tail.Blazor.Menu`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
