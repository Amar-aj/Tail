---
title: Slider
package: Tail.Blazor.Slider
category: forms
namespace: Tail.Blazor.Slider
route: /components/forms/slider
is_generic: false
is_missing: false
---

# Slider

Independent NuGet package for the TailSlider component.

## Installation

```bash
dotnet add package Tail.Blazor.Slider
```

## Features

- Range input with min/max/step
- 3 sizes (Sm, Md, Lg)
- 4 variants (Primary, Success, Warning, Danger)
- Label support
- Value display
- Min/max labels
- Help text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Slider;
```

## Basic Usage

```razor
<TailSlider />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Slider

<TailSlider />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailSlider Variant="SliderVariant.Primary">
    Primary Action
</TailSlider>
```

**Medium Size**

```razor
<TailSlider Size="SliderSize.Sm">
    Medium Size
</TailSlider>
```

**With Click Handler**

```razor
<TailSlider ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailSlider>
```

**Disabled State**

```razor
<TailSlider Disabled="true">
    Disabled
</TailSlider>
```

## Variants

Different visual variants for various use cases:

```razor
<TailSlider Variant="SliderVariant.Primary">Primary</TailSlider>
<TailSlider Variant="SliderVariant.Success">Success</TailSlider>
<TailSlider Variant="SliderVariant.Warning">Warning</TailSlider>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailSlider Size="SliderSize.Sm">Sm</TailSlider>
<TailSlider Size="SliderSize.Md">Md</TailSlider>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailSlider Disabled="true">Disabled</TailSlider>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailSlider ValueChanged="HandleValueChanged">
    Click Me
</TailSlider>

@code {
    private void HandleValueChanged(double args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailSlider Variant="SliderVariant.Primary" Size="SliderSize.Md" Value="10" Min="10" Max="10" Step="10" />
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
    <TailSlider Variant="SliderVariant.Primary" Size="SliderSize.Md" ValueChanged="HandleAction" />
</div>

@code {
    private void HandleAction(double args)
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
| **Value** | `double` | - | Current value of the component |
| **Min** | `double` | 0 | Minimum value constraint |
| **Max** | `double` | 100 | Maximum value constraint |
| **Step** | `double` | 1 | Step value for numeric inputs |
| **Size** | `SliderSize` | SliderSize.Md | Size of the component |
| **Variant** | `SliderVariant` | SliderVariant.Primary | Visual variant style for the component |
| **Label** | `string?` | - | Label text for the component |
| **HelpText** | `string?` | - | HelpText parameter |
| **ShowValue** | `bool` | - | Current value of the component |
| **ShowLabels** | `bool` | - | Label text for the component |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<double>` | Raised when value changes |

### Enums

#### SliderSize

```csharp
public enum SliderSize
{
    Sm,
    Md,
}
```

/// Slider size options.
///

#### Tail.Blazor.Slider;.SliderSize

```csharp
public enum Tail.Blazor.Slider;.SliderSize
{
    Sm,
    Md,
}
```

/// Slider size options.
///

#### SliderVariant

```csharp
public enum SliderVariant
{
    Primary,
    Success,
    Warning,
}
```

/// Slider variant styles.
///

#### Tail.Blazor.Slider;.SliderVariant

```csharp
public enum Tail.Blazor.Slider;.SliderVariant
{
    Primary,
    Success,
    Warning,
}
```

/// Slider variant styles.
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
