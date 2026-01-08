---
title: OTPInput
package: Tail.Blazor.OTPInput
category: forms
namespace: Tail.Blazor.OTPInput
route: /components/forms/otpinput
is_generic: false
is_missing: false
---

# OTPInput

Independent NuGet package for the TailOTPInput component.

## Installation

```bash
dotnet add package Tail.Blazor.OTPInput
```

## Features

- One-time password input
- Multiple digit inputs
- Customizable length (default 6)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Help text
- Auto-focus next input
- Paste support
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.OTPInput;
```

## Basic Usage

```razor
<TailOTPInput />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.OTPInput

<TailOTPInput />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailOTPInput Size="OTPInputSize.Md">
    Medium Size
</TailOTPInput>
```

**With Click Handler**

```razor
<TailOTPInput ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailOTPInput>
```

**Disabled State**

```razor
<TailOTPInput Disabled="true">
    Disabled
</TailOTPInput>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailOTPInput Size="OTPInputSize.Xs">Xs</TailOTPInput>
<TailOTPInput Size="OTPInputSize.Sm">Sm</TailOTPInput>
<TailOTPInput Size="OTPInputSize.Md">Md</TailOTPInput>
<TailOTPInput Size="OTPInputSize.Lg">Lg</TailOTPInput>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailOTPInput Disabled="true">Disabled</TailOTPInput>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailOTPInput ValueChanged="HandleValueChanged">
    Click Me
</TailOTPInput>

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
<TailOTPInput Size="OTPInputSize.Sm" Value="Sample Value" Length="10" Label="Sample Label" HelpText="Sample HelpText" />
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
    <TailOTPInput Size="OTPInputSize.Sm" ValueChanged="HandleAction" />
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
| **Length** | `int` | 6 | Length parameter |
| **Size** | `OTPInputSize` | OTPInputSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **HelpText** | `string?` | - | HelpText parameter |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |

### Enums

#### OTPInputSize

```csharp
public enum OTPInputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// OTPInput size options.
///

#### Tail.Blazor.OTPInput;.OTPInputSize

```csharp
public enum Tail.Blazor.OTPInput;.OTPInputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// OTPInput size options.
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
