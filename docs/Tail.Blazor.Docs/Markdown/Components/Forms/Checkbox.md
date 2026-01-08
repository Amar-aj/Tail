---
title: Checkbox
package: Tail.Blazor.Checkbox
category: forms
namespace: Tail.Blazor.Checkbox
route: /components/forms/checkbox
is_generic: false
is_missing: false
---

# Checkbox

Independent NuGet package for the TailCheckbox component.

## Installation

```bash
dotnet add package Tail.Blazor.Checkbox
```

## Features

- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Custom content support
- Validation error display
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Checkbox;
```

## Basic Usage

```razor
<TailCheckbox>Content</TailCheckbox>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Checkbox

<TailCheckbox>
    Hello, World!
</TailCheckbox>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailCheckbox Size="CheckboxSize.Md">
    Medium Size
</TailCheckbox>
```

**With Click Handler**

```razor
<TailCheckbox IsCheckedChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailCheckbox>
```

**Disabled State**

```razor
<TailCheckbox Disabled="true">
    Disabled
</TailCheckbox>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailCheckbox Size="CheckboxSize.Xs">Xs</TailCheckbox>
<TailCheckbox Size="CheckboxSize.Sm">Sm</TailCheckbox>
<TailCheckbox Size="CheckboxSize.Md">Md</TailCheckbox>
<TailCheckbox Size="CheckboxSize.Lg">Lg</TailCheckbox>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailCheckbox Disabled="true">Disabled</TailCheckbox>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailCheckbox IsCheckedChanged="HandleIsCheckedChanged">
    Click Me
</TailCheckbox>

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
<TailCheckbox Size="CheckboxSize.Sm" IsChecked="true" Label="Sample Label" ErrorMessage="Sample ErrorMessage">
    Combined Parameters
</TailCheckbox>
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
    <TailCheckbox Size="CheckboxSize.Sm" IsCheckedChanged="HandleAction">
        Action Button
    </TailCheckbox>
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
| **Size** | `CheckboxSize` | CheckboxSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **IsIndeterminate** | `bool` | - | Minimum value constraint |
| **CustomCheckIcon** | `RenderFragment?` | - | Icon to display |
| **AriaLabel** | `string?` | - | Label text for the component |
| **Tooltip** | `string?` | - | Tooltip parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **IsCheckedChanged** | `EventCallback<bool>` | Raised when value changes |
| **OnCheckedChanged** | `EventCallback<bool>` | Raised when value changes |

### Enums

#### CheckboxSize

```csharp
public enum CheckboxSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Checkbox size options.
///

#### Tail.Blazor.Checkbox;.CheckboxSize

```csharp
public enum Tail.Blazor.Checkbox;.CheckboxSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Checkbox size options.
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
