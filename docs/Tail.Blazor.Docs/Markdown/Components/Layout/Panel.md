---
title: Panel
package: Tail.Blazor.Panel
category: layout
namespace: Tail.Blazor.Panel
route: /components/layout/panel
is_generic: false
is_missing: false
---

# Panel

Independent NuGet package for the TailPanel component.

## Installation

```bash
dotnet add package Tail.Blazor.Panel
```

## Features

- Panel with variants
- 5 variants (Default, Success, Warning, Danger, Info)
- Title support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Panel;
```

## Basic Usage

```razor
<TailPanel>Content</TailPanel>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Panel

<TailPanel>
    Hello, World!
</TailPanel>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailPanel Variant="PanelVariant.Default">
    Primary Action
</TailPanel>
```

## Variants

Different visual variants for various use cases:

```razor
<TailPanel Variant="PanelVariant.Default">Default</TailPanel>
<TailPanel Variant="PanelVariant.Success">Success</TailPanel>
<TailPanel Variant="PanelVariant.Warning">Warning</TailPanel>
<TailPanel Variant="PanelVariant.Danger">Danger</TailPanel>
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailPanel Variant="PanelVariant.Default" Title="Sample Title" Style="Sample Style">
    Combined Parameters
</TailPanel>
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
    <TailPanel Variant="PanelVariant.Default">
        Action Button
    </TailPanel>
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
| **Title** | `string?` | - | Title parameter |
| **Variant** | `PanelVariant` | PanelVariant.Default | Visual variant style for the component |
| **Style** | `string?` | - | Additional CSS styles |

### Enums

#### PanelVariant

```csharp
public enum PanelVariant
{
    Default,
    Success,
    Warning,
    Danger,
}
```

/// Panel variant styles.
///

#### Tail.Blazor.Panel;.PanelVariant

```csharp
public enum Tail.Blazor.Panel;.PanelVariant
{
    Default,
    Success,
    Warning,
    Danger,
}
```

/// Panel variant styles.
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
