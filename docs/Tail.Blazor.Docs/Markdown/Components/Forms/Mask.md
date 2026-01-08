---
title: Mask
package: Tail.Blazor.Mask
category: forms
namespace: Tail.Blazor.Mask
route: /components/forms/mask
is_generic: false
is_missing: false
---

# Mask

Independent NuGet package for the TailMask component.

## Installation

```bash
dotnet add package Tail.Blazor.Mask
```

## Features

- Input masking (phone, credit card, etc.)
- Custom mask patterns
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Validation error display
- Required field indicator
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Mask;
```

## Basic Usage

```razor
<TailMask />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Mask

<TailMask />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailMask Size="MaskSize.Md">
    Medium Size
</TailMask>
```

**With Click Handler**

```razor
<TailMask ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailMask>
```

**Disabled State**

```razor
<TailMask Disabled="true">
    Disabled
</TailMask>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailMask Size="MaskSize.Xs">Xs</TailMask>
<TailMask Size="MaskSize.Sm">Sm</TailMask>
<TailMask Size="MaskSize.Md">Md</TailMask>
<TailMask Size="MaskSize.Lg">Lg</TailMask>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailMask Disabled="true">Disabled</TailMask>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailMask ValueChanged="HandleValueChanged">
    Click Me
</TailMask>

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
<TailMask Size="MaskSize.Sm" Value="Sample Value" Mask="Sample Mask" Label="Sample Label" Placeholder="Sample Placeholder" />
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
    <TailMask Size="MaskSize.Sm" ValueChanged="HandleAction" />
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
| **Mask** | `string` | "(###) ###-####" | Mask parameter |
| **Size** | `MaskSize` | MaskSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |

### Enums

#### MaskSize

```csharp
public enum MaskSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Mask size options.
///

#### Tail.Blazor.Mask;.MaskSize

```csharp
public enum Tail.Blazor.Mask;.MaskSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Mask size options.
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
