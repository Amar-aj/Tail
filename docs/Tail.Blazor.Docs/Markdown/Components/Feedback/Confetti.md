---
title: Confetti
package: Tail.Blazor.Confetti
category: feedback
namespace: Tail.Blazor.Confetti
route: /components/feedback/confetti
is_generic: false
is_missing: false
---

# Confetti

Independent NuGet package for the TailConfetti component.

## Installation

```bash
dotnet add package Tail.Blazor.Confetti
```

## Features

- Confetti animation
- 4 shape types (Circle, Rectangle, Star, Mixed)
- Customizable particle count
- Duration control
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Confetti;
```

## Basic Usage

```razor
<TailConfetti />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Confetti

<TailConfetti />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailConfetti IsActive="true" ParticleCount="10" Duration="10" Style="Sample Style" />
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
    <TailConfetti  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **IsActive** | `bool` | - | IsActive parameter |
| **ParticleCount** | `int` | 50 | ParticleCount parameter |
| **Shape** | `ConfettiShape` | ConfettiShape.Mixed | Shape parameter |
| **Duration** | `int` | 3000 | Duration parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Enums

#### ConfettiShape

```csharp
public enum ConfettiShape
{
    Circle,
    Rectangle,
    Star,
}
```

/// Confetti shape type.
///

#### Tail.Blazor.Confetti;.ConfettiShape

```csharp
public enum Tail.Blazor.Confetti;.ConfettiShape
{
    Circle,
    Rectangle,
    Star,
}
```

/// Confetti shape type.
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
