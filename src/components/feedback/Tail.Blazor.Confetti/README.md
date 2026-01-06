# Tail.Blazor.Confetti

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

## Component Usage

```razor
<TailConfetti></TailConfetti>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **IsActive** | `bool` | - | IsActive parameter |
| **ParticleCount** | `int` | 50 | ParticleCount parameter |
| **Shape** | `ConfettiShape` | ConfettiShape.Mixed | Shape parameter |
| **Duration** | `int` | 3000 | Duration parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Enums

### ConfettiShape

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

### Tail.Blazor.Confetti;.ConfettiShape

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

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Confetti

<TailConfetti />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailConfetti />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailConfetti IsActive="true" ParticleCount="10" Duration="10" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailConfetti Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailConfetti>

@* Using Class parameter *@
<TailConfetti Class="my-custom-class shadow-lg">
    With Custom Class
</TailConfetti>
```

### Real-World Example

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

- **Package ID**: `Tail.Blazor.Confetti`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
