---
title: PasswordStrengthMeter
package: Tail.Blazor.PasswordStrengthMeter
category: forms
namespace: Tail.Blazor.PasswordStrengthMeter
route: /components/forms/passwordstrengthmeter
is_generic: false
is_missing: false
---

# PasswordStrengthMeter

Independent NuGet package for the TailPasswordStrengthMeter component.

## Installation

```bash
dotnet add package Tail.Blazor.PasswordStrengthMeter
```

## Features

- Password input with strength meter
- Show/hide password toggle
- Real-time strength calculation
- Visual strength indicator (5 levels)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Validation error display
- Required field indicator
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.PasswordStrengthMeter;
```

## Basic Usage

```razor
<TailPasswordStrengthMeter />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.PasswordStrengthMeter

<TailPasswordStrengthMeter />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailPasswordStrengthMeter Size="PasswordStrengthMeterSize.Md">
    Medium Size
</TailPasswordStrengthMeter>
```

**With Click Handler**

```razor
<TailPasswordStrengthMeter ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailPasswordStrengthMeter>
```

**Disabled State**

```razor
<TailPasswordStrengthMeter Disabled="true">
    Disabled
</TailPasswordStrengthMeter>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailPasswordStrengthMeter Size="PasswordStrengthMeterSize.Xs">Xs</TailPasswordStrengthMeter>
<TailPasswordStrengthMeter Size="PasswordStrengthMeterSize.Sm">Sm</TailPasswordStrengthMeter>
<TailPasswordStrengthMeter Size="PasswordStrengthMeterSize.Md">Md</TailPasswordStrengthMeter>
<TailPasswordStrengthMeter Size="PasswordStrengthMeterSize.Lg">Lg</TailPasswordStrengthMeter>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailPasswordStrengthMeter Disabled="true">Disabled</TailPasswordStrengthMeter>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailPasswordStrengthMeter ValueChanged="HandleValueChanged">
    Click Me
</TailPasswordStrengthMeter>

@code {
    private void HandleValueChanged(string? args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailPasswordStrengthMeter Size="PasswordStrengthMeterSize.Sm" Value="Sample Value" Label="Sample Label" Placeholder="Sample Placeholder" ErrorMessage="Sample ErrorMessage" />
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
    <TailPasswordStrengthMeter Size="PasswordStrengthMeterSize.Sm" ValueChanged="HandleAction" />
</div>

@code {
    private void HandleAction(string? args)
    {
        // Perform action
        Console.WriteLine("Action executed");
    }
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string?` | - | Current value of the component |
| **Size** | `PasswordStrengthMeterSize` | PasswordStrengthMeterSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **ShowStrengthMeter** | `bool` | true | ShowStrengthMeter parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |

### Enums

#### PasswordStrengthMeterSize

```csharp
public enum PasswordStrengthMeterSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// PasswordStrengthMeter size options.
///

#### Tail.Blazor.PasswordStrengthMeter;.PasswordStrengthMeterSize

```csharp
public enum Tail.Blazor.PasswordStrengthMeter;.PasswordStrengthMeterSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// PasswordStrengthMeter size options.
///

#### PasswordStrength

```csharp
public enum PasswordStrength
{
    VeryWeak,
    Weak,
    Fair,
    Good,
}
```

/// Password strength levels.
///

#### Tail.Blazor.PasswordStrengthMeter;.PasswordStrength

```csharp
public enum Tail.Blazor.PasswordStrengthMeter;.PasswordStrength
{
    VeryWeak,
    Weak,
    Fair,
    Good,
}
```

/// Password strength levels.
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
