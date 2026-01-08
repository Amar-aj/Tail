---
title: CurrencyInput
package: Tail.Blazor.CurrencyInput
category: forms
namespace: Tail.Blazor.CurrencyInput
route: /components/forms/currencyinput
is_generic: false
is_missing: false
---

# CurrencyInput

Independent NuGet package for the TailCurrencyInput component.

## Installation

```bash
dotnet add package Tail.Blazor.CurrencyInput
```

## Features

- Currency input with symbol
- Left or right symbol position
- Custom currency symbol
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.CurrencyInput;
```

## Basic Usage

```razor
<TailCurrencyInput />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.CurrencyInput

<TailCurrencyInput />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailCurrencyInput Size="CurrencyInputSize.Md">
    Medium Size
</TailCurrencyInput>
```

**With Click Handler**

```razor
<TailCurrencyInput ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailCurrencyInput>
```

**Disabled State**

```razor
<TailCurrencyInput Disabled="true">
    Disabled
</TailCurrencyInput>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailCurrencyInput Size="CurrencyInputSize.Xs">Xs</TailCurrencyInput>
<TailCurrencyInput Size="CurrencyInputSize.Sm">Sm</TailCurrencyInput>
<TailCurrencyInput Size="CurrencyInputSize.Md">Md</TailCurrencyInput>
<TailCurrencyInput Size="CurrencyInputSize.Lg">Lg</TailCurrencyInput>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailCurrencyInput Disabled="true">Disabled</TailCurrencyInput>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailCurrencyInput ValueChanged="HandleValueChanged">
    Click Me
</TailCurrencyInput>

@code {
    private void HandleValueChanged(decimal? args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailCurrencyInput Size="CurrencyInputSize.Sm" CurrencySymbol="Sample CurrencySymbol" Label="Sample Label" />
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
    <TailCurrencyInput Size="CurrencyInputSize.Sm" ValueChanged="HandleAction" />
</div>

@code {
    private void HandleAction(decimal? args)
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
| **Value** | `decimal?` | - | Current value of the component |
| **CurrencySymbol** | `string` | "$" | CurrencySymbol parameter |
| **SymbolPosition** | `CurrencySymbolPosition` | CurrencySymbolPosition.Left | SymbolPosition parameter |
| **Size** | `CurrencyInputSize` | CurrencyInputSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<decimal?>` | Raised when value changes |

### Enums

#### CurrencyInputSize

```csharp
public enum CurrencyInputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// CurrencyInput size options.
///

#### Tail.Blazor.CurrencyInput;.CurrencyInputSize

```csharp
public enum Tail.Blazor.CurrencyInput;.CurrencyInputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// CurrencyInput size options.
///

#### CurrencySymbolPosition

```csharp
public enum CurrencySymbolPosition
{
    Left,
}
```

/// Currency symbol position.
///

#### Tail.Blazor.CurrencyInput;.CurrencySymbolPosition

```csharp
public enum Tail.Blazor.CurrencyInput;.CurrencySymbolPosition
{
    Left,
}
```

/// Currency symbol position.
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
