---
title: PhoneNumberInput
package: Tail.Blazor.PhoneNumberInput
category: forms
namespace: Tail.Blazor.PhoneNumberInput
route: /components/forms/phonenumberinput
is_generic: false
is_missing: false
---

# PhoneNumberInput

Independent NuGet package for the TailPhoneNumberInput component.

## Installation

```bash
dotnet add package Tail.Blazor.PhoneNumberInput
```

## Features

- Phone number input with country code selector
- Country code dropdown
- Phone number formatting
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.PhoneNumberInput;
```

## Basic Usage

```razor
<TailPhoneNumberInput />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.PhoneNumberInput

<TailPhoneNumberInput />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailPhoneNumberInput Size="PhoneNumberInputSize.Md">
    Medium Size
</TailPhoneNumberInput>
```

**With Click Handler**

```razor
<TailPhoneNumberInput PhoneNumberChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailPhoneNumberInput>
```

**Disabled State**

```razor
<TailPhoneNumberInput Disabled="true">
    Disabled
</TailPhoneNumberInput>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailPhoneNumberInput Size="PhoneNumberInputSize.Xs">Xs</TailPhoneNumberInput>
<TailPhoneNumberInput Size="PhoneNumberInputSize.Sm">Sm</TailPhoneNumberInput>
<TailPhoneNumberInput Size="PhoneNumberInputSize.Md">Md</TailPhoneNumberInput>
<TailPhoneNumberInput Size="PhoneNumberInputSize.Lg">Lg</TailPhoneNumberInput>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailPhoneNumberInput Disabled="true">Disabled</TailPhoneNumberInput>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailPhoneNumberInput PhoneNumberChanged="HandlePhoneNumberChanged">
    Click Me
</TailPhoneNumberInput>

@code {
    private void HandlePhoneNumberChanged(string? args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailPhoneNumberInput Size="PhoneNumberInputSize.Sm" PhoneNumber="Sample PhoneNumber" SelectedCountryCode="Sample SelectedCountryCode" Label="Sample Label" Placeholder="Sample Placeholder" />
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
    <TailPhoneNumberInput Size="PhoneNumberInputSize.Sm" PhoneNumberChanged="HandleAction" />
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
| **PhoneNumber** | `string?` | - | PhoneNumber parameter |
| **SelectedCountryCode** | `string` | "+1" | SelectedCountryCode parameter |
| **Size** | `PhoneNumberInputSize` | PhoneNumberInputSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **PhoneNumberChanged** | `EventCallback<string?>` | Raised when value changes |
| **SelectedCountryCodeChanged** | `EventCallback<string>` | Raised when value changes |

### Enums

#### PhoneNumberInputSize

```csharp
public enum PhoneNumberInputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// PhoneNumberInput size options.
///

#### Tail.Blazor.PhoneNumberInput;.PhoneNumberInputSize

```csharp
public enum Tail.Blazor.PhoneNumberInput;.PhoneNumberInputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// PhoneNumberInput size options.
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
