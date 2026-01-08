---
title: ProgressBarCircular
package: Tail.Blazor.ProgressBarCircular
category: feedback
namespace: Tail.Blazor.ProgressBarCircular
route: /components/feedback/progressbarcircular
is_generic: false
is_missing: false
---

# ProgressBarCircular

Independent NuGet package for the TailProgressBarCircular component.

## Installation

```bash
dotnet add package Tail.Blazor.ProgressBarCircular
```

## Features

- Circular progress indicator
- Customizable size
- 5 variants (Primary, Success, Warning, Danger, Info)
- Label support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ProgressBarCircular;
```

## Basic Usage

```razor
<TailProgressBarCircular />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ProgressBarCircular

<TailProgressBarCircular />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailProgressBarCircular Variant="ProgressBarCircularVariant.Primary">
    Primary Action
</TailProgressBarCircular>
```

## Variants

Different visual variants for various use cases:

```razor
<TailProgressBarCircular Variant="ProgressBarCircularVariant.Primary">Primary</TailProgressBarCircular>
<TailProgressBarCircular Variant="ProgressBarCircularVariant.Success">Success</TailProgressBarCircular>
<TailProgressBarCircular Variant="ProgressBarCircularVariant.Warning">Warning</TailProgressBarCircular>
<TailProgressBarCircular Variant="ProgressBarCircularVariant.Danger">Danger</TailProgressBarCircular>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailProgressBarCircular Size="12">Small</TailProgressBarCircular>
<TailProgressBarCircular Size="16">Medium</TailProgressBarCircular>
<TailProgressBarCircular Size="24">Large</TailProgressBarCircular>
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailProgressBarCircular Variant="ProgressBarCircularVariant.Primary" Value="10" StrokeWidth="10" ShowLabel="true" />
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
    <TailProgressBarCircular Variant="ProgressBarCircularVariant.Primary" />
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
| **Size** | `int` | 100 | Size of the component |
| **StrokeWidth** | `int` | 8 | StrokeWidth parameter |
| **Variant** | `ProgressBarCircularVariant` | ProgressBarCircularVariant.Primary | Visual variant style for the component |
| **ShowLabel** | `bool` | true | Label text for the component |
| **Style** | `string?` | - | Additional CSS styles |

### Enums

#### ProgressBarCircularVariant

```csharp
public enum ProgressBarCircularVariant
{
    Primary,
    Success,
    Warning,
    Danger,
}
```

/// ProgressBarCircular variant styles.
///

#### Tail.Blazor.ProgressBarCircular;.ProgressBarCircularVariant

```csharp
public enum Tail.Blazor.ProgressBarCircular;.ProgressBarCircularVariant
{
    Primary,
    Success,
    Warning,
    Danger,
}
```

/// ProgressBarCircular variant styles.
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
