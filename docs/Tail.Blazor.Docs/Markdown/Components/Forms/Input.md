---
title: Input
package: Tail.Blazor.Input
category: forms
namespace: Tail.Blazor.Input
route: /components/forms/input
is_generic: false
is_missing: false
---

# Input

Independent NuGet package for the TailInput component.

## Installation

```bash
dotnet add package Tail.Blazor.Input
```

## Features

- Multiple input types (Text, Password, Email, Number, Tel, Url, Search, Date, etc.)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label and help text support
- Icon support (start/end)
- Clear button
- Character count
- Validation error display
- Required field indicator
- Disabled and readonly states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Input;
```

## Basic Usage

```razor
<TailInput>Content</TailInput>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Input

<TailInput>
    Hello, World!
</TailInput>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailInput Variant="InputVariant.Standard">
    Primary Action
</TailInput>
```

**Medium Size**

```razor
<TailInput Size="InputSize.Md">
    Medium Size
</TailInput>
```

**With Click Handler**

```razor
<TailInput ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailInput>
```

**Disabled State**

```razor
<TailInput Disabled="true">
    Disabled
</TailInput>
```

## Variants

Different visual variants for various use cases:

```razor
<TailInput Variant="InputVariant.Standard">Standard</TailInput>
<TailInput Variant="InputVariant.Outlined">Outlined</TailInput>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailInput Size="InputSize.Xs">Xs</TailInput>
<TailInput Size="InputSize.Sm">Sm</TailInput>
<TailInput Size="InputSize.Md">Md</TailInput>
<TailInput Size="InputSize.Lg">Lg</TailInput>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailInput Disabled="true">Disabled</TailInput>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailInput ValueChanged="HandleValueChanged">
    Click Me
</TailInput>

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
<TailInput Variant="InputVariant.Standard" Size="InputSize.Sm" Value="Sample Value" Label="Sample Label">
    Combined Parameters
</TailInput>
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
    <TailInput Variant="InputVariant.Standard" Size="InputSize.Sm" ValueChanged="HandleAction">
        Action Button
    </TailInput>
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
| **Type** | `InputType` | InputType.Text | Type parameter |
| **Size** | `InputSize` | InputSize.Md | Size of the component |
| **Variant** | `InputVariant` | InputVariant.Standard | Visual variant style for the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **HelpText** | `string?` | - | HelpText parameter |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **ReadOnly** | `bool` | - | Whether the component is read-only |
| **MaxLength** | `int?` | - | Maximum value constraint |
| **ShowClearButton** | `bool` | - | ShowClearButton parameter |
| **ShowCharacterCount** | `bool` | - | ShowCharacterCount parameter |
| **FloatingLabel** | `bool` | - | Label text for the component |
| **IconStart** | `RenderFragment?` | - | Icon to display |
| **IconEnd** | `RenderFragment?` | - | Icon to display |
| **AdornmentStart** | `string?` | - | AdornmentStart parameter |
| **AdornmentEnd** | `string?` | - | AdornmentEnd parameter |
| **Style** | `string?` | - | Additional CSS styles |
| **Min** | `string?` | - | Minimum value constraint |
| **Max** | `string?` | - | Maximum value constraint |
| **Step** | `string?` | - | Step value for numeric inputs |
| **Pattern** | `string?` | - | Validation pattern (regex) |
| **AutoComplete** | `string?` | - | AutoComplete parameter |
| **AutoFocus** | `bool` | false | AutoFocus parameter |
| **AriaLabel** | `string?` | - | Label text for the component |
| **EnableAnimation** | `bool` | true | EnableAnimation parameter |
| **AnimationDuration** | `int` | 200 | AnimationDuration parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |
| **OnFocus** | `EventCallback<FocusEventArgs>` | Raised when focus is gained |
| **OnBlur** | `EventCallback<FocusEventArgs>` | Raised when focus is lost |
| **OnKeyDown** | `EventCallback<KeyboardEventArgs>` | Raised on key down |

### Enums

#### InputType

```csharp
public enum InputType
{
    Text,
    Password,
    Email,
    Number,
    Tel,
    Url,
    Search,
    Date,
    DateTimeLocal,
    Time,
    Month,
}
```

/// Input type options.
///

#### Tail.Blazor.Input;.InputType

```csharp
public enum Tail.Blazor.Input;.InputType
{
    Text,
    Password,
    Email,
    Number,
    Tel,
    Url,
    Search,
    Date,
    DateTimeLocal,
    Time,
    Month,
}
```

/// Input type options.
///

#### InputSize

```csharp
public enum InputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Input size options.
///

#### Tail.Blazor.Input;.InputSize

```csharp
public enum Tail.Blazor.Input;.InputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Input size options.
///

#### InputVariant

```csharp
public enum InputVariant
{
    Standard,
    Outlined,
}
```

/// Input variant options (visual style).
///

#### Tail.Blazor.Input;.InputVariant

```csharp
public enum Tail.Blazor.Input;.InputVariant
{
    Standard,
    Outlined,
}
```

/// Input variant options (visual style).
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
