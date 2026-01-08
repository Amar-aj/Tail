---
title: ColorPicker
package: Tail.Blazor.ColorPicker
category: forms
namespace: Tail.Blazor.ColorPicker
route: /components/forms/colorpicker
is_generic: false
is_missing: false
---

# ColorPicker

Independent NuGet package for the TailColorPicker component.

## Installation

```bash
dotnet add package Tail.Blazor.ColorPicker
```

## Features

- Color picker with visual selector
- Hex color input
- Color preview
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Help text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ColorPicker;
```

## Basic Usage

```razor
<TailColorPicker />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ColorPicker

<TailColorPicker />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailColorPicker Size="ColorPickerSize.Md">
    Medium Size
</TailColorPicker>
```

**With Click Handler**

```razor
<TailColorPicker ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailColorPicker>
```

**Disabled State**

```razor
<TailColorPicker Disabled="true">
    Disabled
</TailColorPicker>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailColorPicker Size="ColorPickerSize.Xs">Xs</TailColorPicker>
<TailColorPicker Size="ColorPickerSize.Sm">Sm</TailColorPicker>
<TailColorPicker Size="ColorPickerSize.Md">Md</TailColorPicker>
<TailColorPicker Size="ColorPickerSize.Lg">Lg</TailColorPicker>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailColorPicker Disabled="true">Disabled</TailColorPicker>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailColorPicker ValueChanged="HandleValueChanged">
    Click Me
</TailColorPicker>

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
<TailColorPicker Size="ColorPickerSize.Sm" Value="Sample Value" Label="Sample Label" HelpText="Sample HelpText" ShowPreview="true" />
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
    <TailColorPicker Size="ColorPickerSize.Sm" ValueChanged="HandleAction" />
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
| **Size** | `ColorPickerSize` | ColorPickerSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **HelpText** | `string?` | - | HelpText parameter |
| **ShowPreview** | `bool` | true | ShowPreview parameter |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |

### Enums

#### ColorPickerSize

```csharp
public enum ColorPickerSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// ColorPicker size options.
///

#### Tail.Blazor.ColorPicker;.ColorPickerSize

```csharp
public enum Tail.Blazor.ColorPicker;.ColorPickerSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// ColorPicker size options.
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
