---
title: TimePicker
package: Tail.Blazor.TimePicker
category: forms
namespace: Tail.Blazor.TimePicker
route: /components/forms/timepicker
is_generic: false
is_missing: false
---

# TimePicker

Independent NuGet package for the TailTimePicker component.

## Installation

```bash
dotnet add package Tail.Blazor.TimePicker
```

## Features

- Time input with picker
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Validation error display
- Required field indicator
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.TimePicker;
```

## Basic Usage

```razor
<TailTimePicker />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.TimePicker

<TailTimePicker />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailTimePicker Size="TimePickerSize.Md">
    Medium Size
</TailTimePicker>
```

**With Click Handler**

```razor
<TailTimePicker ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailTimePicker>
```

**Disabled State**

```razor
<TailTimePicker Disabled="true">
    Disabled
</TailTimePicker>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailTimePicker Size="TimePickerSize.Xs">Xs</TailTimePicker>
<TailTimePicker Size="TimePickerSize.Sm">Sm</TailTimePicker>
<TailTimePicker Size="TimePickerSize.Md">Md</TailTimePicker>
<TailTimePicker Size="TimePickerSize.Lg">Lg</TailTimePicker>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailTimePicker Disabled="true">Disabled</TailTimePicker>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailTimePicker ValueChanged="HandleValueChanged">
    Click Me
</TailTimePicker>

@code {
    private void HandleValueChanged(Tail.Blazor.TimePicker.TimeSpan? args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailTimePicker Size="TimePickerSize.Sm" Label="Sample Label" ErrorMessage="Sample ErrorMessage" Required="true" />
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
    <TailTimePicker Size="TimePickerSize.Sm" ValueChanged="HandleAction" />
</div>

@code {
    private void HandleAction(TimeSpan? args)
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
| **Value** | `TimeSpan?` | - | Current value of the component |
| **Size** | `TimePickerSize` | TimePickerSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<TimeSpan?>` | Raised when value changes |

### Enums

#### TimePickerSize

```csharp
public enum TimePickerSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// TimePicker size options.
///

#### Tail.Blazor.TimePicker;.TimePickerSize

```csharp
public enum Tail.Blazor.TimePicker;.TimePickerSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// TimePicker size options.
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
