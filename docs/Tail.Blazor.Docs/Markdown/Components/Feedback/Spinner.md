---
title: Spinner
package: Tail.Blazor.Spinner
category: feedback
namespace: Tail.Blazor.Spinner
route: /components/feedback/spinner
is_generic: false
is_missing: false
---

# Spinner

Independent NuGet package for the TailSpinner component.

## Installation

```bash
dotnet add package Tail.Blazor.Spinner
```

## Features

- 4 sizes (Sm, Md, Lg, Xl)
- 6 color options (Primary, Success, Warning, Danger, White, Gray)
- Animated spinner
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Spinner;
```

## Basic Usage

```razor
<TailSpinner />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Spinner

<TailSpinner />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailSpinner Size="SpinnerSize.Md">
    Medium Size
</TailSpinner>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailSpinner Size="SpinnerSize.Sm">Sm</TailSpinner>
<TailSpinner Size="SpinnerSize.Md">Md</TailSpinner>
<TailSpinner Size="SpinnerSize.Lg">Lg</TailSpinner>
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailSpinner Size="SpinnerSize.Md" Style="Sample Style" />
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
    <TailSpinner Size="SpinnerSize.Md" />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Size** | `SpinnerSize` | SpinnerSize.Md | Size of the component |
| **Color** | `SpinnerColor` | SpinnerColor.Primary | Color scheme for the component |
| **Style** | `string?` | - | Additional CSS styles |

### Enums

#### SpinnerSize

```csharp
public enum SpinnerSize
{
    Sm,
    Md,
    Lg,
}
```

/// Spinner size options.
///

#### Tail.Blazor.Spinner;.SpinnerSize

```csharp
public enum Tail.Blazor.Spinner;.SpinnerSize
{
    Sm,
    Md,
    Lg,
}
```

/// Spinner size options.
///

#### SpinnerColor

```csharp
public enum SpinnerColor
{
    Primary,
    Success,
    Warning,
    Danger,
    White,
}
```

/// Spinner color options.
///

#### Tail.Blazor.Spinner;.SpinnerColor

```csharp
public enum Tail.Blazor.Spinner;.SpinnerColor
{
    Primary,
    Success,
    Warning,
    Danger,
    White,
}
```

/// Spinner color options.
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
