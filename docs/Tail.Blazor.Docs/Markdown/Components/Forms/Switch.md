---
title: Switch
package: Tail.Blazor.Switch
category: forms
namespace: Tail.Blazor.Switch
route: /components/forms/switch
is_generic: false
is_missing: false
---

# Switch

Independent NuGet package for the TailSwitch component.

## Installation

```bash
dotnet add package Tail.Blazor.Switch
```

## Features

- Toggle switch design
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Custom content support
- Validation error display
- Disabled state
- Smooth animations
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Switch;
```

## Basic Usage

```razor
<TailSwitch>Content</TailSwitch>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Switch

<TailSwitch>
    Hello, World!
</TailSwitch>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailSwitch Size="SwitchSize.Md">
    Medium Size
</TailSwitch>
```

**With Click Handler**

```razor
<TailSwitch IsCheckedChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailSwitch>
```

**Disabled State**

```razor
<TailSwitch Disabled="true">
    Disabled
</TailSwitch>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailSwitch Size="SwitchSize.Xs">Xs</TailSwitch>
<TailSwitch Size="SwitchSize.Sm">Sm</TailSwitch>
<TailSwitch Size="SwitchSize.Md">Md</TailSwitch>
<TailSwitch Size="SwitchSize.Lg">Lg</TailSwitch>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailSwitch Disabled="true">Disabled</TailSwitch>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailSwitch IsCheckedChanged="HandleIsCheckedChanged">
    Click Me
</TailSwitch>

@code {
    private void HandleIsCheckedChanged(bool args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailSwitch Size="SwitchSize.Sm" IsChecked="true" Label="Sample Label" ErrorMessage="Sample ErrorMessage">
    Combined Parameters
</TailSwitch>
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
    <TailSwitch Size="SwitchSize.Sm" IsCheckedChanged="HandleAction">
        Action Button
    </TailSwitch>
</div>

@code {
    private void HandleAction(bool args)
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
| **IsChecked** | `bool` | - | IsChecked parameter |
| **Size** | `SwitchSize` | SwitchSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **IsCheckedChanged** | `EventCallback<bool>` | Raised when value changes |

### Enums

#### SwitchSize

```csharp
public enum SwitchSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Switch size options.
///

#### Tail.Blazor.Switch;.SwitchSize

```csharp
public enum Tail.Blazor.Switch;.SwitchSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Switch size options.
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
