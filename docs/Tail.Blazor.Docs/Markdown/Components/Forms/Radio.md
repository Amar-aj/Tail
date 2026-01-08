---
title: Radio
package: Tail.Blazor.Radio
category: forms
namespace: Tail.Blazor.Radio
route: /components/forms/radio
is_generic: false
is_missing: false
---

# Radio

Independent NuGet package for the TailRadio component.

## Installation

```bash
dotnet add package Tail.Blazor.Radio
```

## Features

- Radio button input
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Group name support
- Label support
- Custom content support
- Validation error display
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Radio;
```

## Basic Usage

```razor
<TailRadio>Content</TailRadio>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Radio

<TailRadio>
    Hello, World!
</TailRadio>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailRadio Size="RadioSize.Md">
    Medium Size
</TailRadio>
```

**With Click Handler**

```razor
<TailRadio IsCheckedChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailRadio>
```

**Disabled State**

```razor
<TailRadio Disabled="true">
    Disabled
</TailRadio>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailRadio Size="RadioSize.Xs">Xs</TailRadio>
<TailRadio Size="RadioSize.Sm">Sm</TailRadio>
<TailRadio Size="RadioSize.Md">Md</TailRadio>
<TailRadio Size="RadioSize.Lg">Lg</TailRadio>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailRadio Disabled="true">Disabled</TailRadio>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailRadio IsCheckedChanged="HandleIsCheckedChanged">
    Click Me
</TailRadio>

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
<TailRadio Size="RadioSize.Sm" Value="Sample Value" GroupName="Sample GroupName" IsChecked="true" Label="Sample Label">
    Combined Parameters
</TailRadio>
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
    <TailRadio Size="RadioSize.Sm" IsCheckedChanged="HandleAction">
        Action Button
    </TailRadio>
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
| **Value** | `string?` | - | Current value of the component |
| **GroupName** | `string?` | - | GroupName parameter |
| **IsChecked** | `bool` | - | IsChecked parameter |
| **Size** | `RadioSize` | RadioSize.Md | Size of the component |
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

#### RadioSize

```csharp
public enum RadioSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Radio size options.
///

#### Tail.Blazor.Radio;.RadioSize

```csharp
public enum Tail.Blazor.Radio;.RadioSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Radio size options.
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
