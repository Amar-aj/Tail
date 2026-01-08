---
title: Progress
package: Tail.Blazor.Progress
category: feedback
namespace: Tail.Blazor.Progress
route: /components/feedback/progress
is_generic: false
is_missing: false
---

# Progress

Independent NuGet package for the TailProgress component.

## Installation

```bash
dotnet add package Tail.Blazor.Progress
```

## Features

- Progress bar with percentage
- 5 variants (Primary, Success, Warning, Danger, Info)
- 4 sizes (Sm, Md, Lg, Xl)
- Label support (inside/outside)
- Animation option
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Progress;
```

## Basic Usage

```razor
<TailProgress />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Progress

<TailProgress />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailProgress Variant="ProgressVariant.Primary">
    Primary Action
</TailProgress>
```

**Medium Size**

```razor
<TailProgress Size="ProgressSize.Md">
    Medium Size
</TailProgress>
```

## Variants

Different visual variants for various use cases:

```razor
<TailProgress Variant="ProgressVariant.Primary">Primary</TailProgress>
<TailProgress Variant="ProgressVariant.Success">Success</TailProgress>
<TailProgress Variant="ProgressVariant.Warning">Warning</TailProgress>
<TailProgress Variant="ProgressVariant.Danger">Danger</TailProgress>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailProgress Size="ProgressSize.Sm">Sm</TailProgress>
<TailProgress Size="ProgressSize.Md">Md</TailProgress>
<TailProgress Size="ProgressSize.Lg">Lg</TailProgress>
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailProgress Variant="ProgressVariant.Primary" Size="ProgressSize.Md" Value="10" ShowLabel="true" />
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
    <TailProgress Variant="ProgressVariant.Primary" Size="ProgressSize.Md" />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `int` | - | Current value of the component |
| **Variant** | `ProgressVariant` | ProgressVariant.Primary | Visual variant style for the component |
| **Size** | `ProgressSize` | ProgressSize.Md | Size of the component |
| **ShowLabel** | `bool` | - | Label text for the component |
| **LabelPosition** | `ProgressLabelPosition` | ProgressLabelPosition.Outside | Label text for the component |
| **Label** | `string?` | - | Label text for the component |
| **Animated** | `bool` | - | Animated parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Enums

#### ProgressVariant

```csharp
public enum ProgressVariant
{
    Primary,
    Success,
    Warning,
    Danger,
}
```

/// Progress variant styles.
///

#### Tail.Blazor.Progress;.ProgressVariant

```csharp
public enum Tail.Blazor.Progress;.ProgressVariant
{
    Primary,
    Success,
    Warning,
    Danger,
}
```

/// Progress variant styles.
///

#### ProgressSize

```csharp
public enum ProgressSize
{
    Sm,
    Md,
    Lg,
}
```

/// Progress size options.
///

#### Tail.Blazor.Progress;.ProgressSize

```csharp
public enum Tail.Blazor.Progress;.ProgressSize
{
    Sm,
    Md,
    Lg,
}
```

/// Progress size options.
///

#### ProgressLabelPosition

```csharp
public enum ProgressLabelPosition
{
    Inside,
}
```

/// Progress label position.
///

#### Tail.Blazor.Progress;.ProgressLabelPosition

```csharp
public enum Tail.Blazor.Progress;.ProgressLabelPosition
{
    Inside,
}
```

/// Progress label position.
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
