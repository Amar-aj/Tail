---
title: SplitButton
package: Tail.Blazor.SplitButton
category: buttons
namespace: Tail.Blazor.SplitButton
route: /components/buttons/splitbutton
is_generic: false
is_missing: false
---

# SplitButton

Independent NuGet package for the TailSplitButton component.

## Installation

```bash
dotnet add package Tail.Blazor.SplitButton
```

## Features

- Primary action button
- Dropdown menu for secondary actions
- 9 variants
- 5 sizes
- Loading states
- Disabled states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.SplitButton;
```

## Basic Usage

```razor
<TailSplitButton>Content</TailSplitButton>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.SplitButton

<TailSplitButton>
    Hello, World!
</TailSplitButton>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailSplitButton Variant="ButtonVariant.Primary">
    Primary Action
</TailSplitButton>
```

**Medium Size**

```razor
<TailSplitButton Size="ButtonSize.Md">
    Medium Size
</TailSplitButton>
```

**With Click Handler**

```razor
<TailSplitButton OnPrimaryClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailSplitButton>
```

**Disabled State**

```razor
<TailSplitButton Disabled="true">
    Disabled
</TailSplitButton>
```

## Variants

Different visual variants for various use cases:

```razor
<TailSplitButton Variant="ButtonVariant.Primary">Primary</TailSplitButton>
<TailSplitButton Variant="ButtonVariant.Success">Success</TailSplitButton>
<TailSplitButton Variant="ButtonVariant.Warning">Warning</TailSplitButton>
<TailSplitButton Variant="ButtonVariant.Danger">Danger</TailSplitButton>
<TailSplitButton Variant="ButtonVariant.Info">Info</TailSplitButton>
<TailSplitButton Variant="ButtonVariant.Outline">Outline</TailSplitButton>
<TailSplitButton Variant="ButtonVariant.Soft">Soft</TailSplitButton>
<TailSplitButton Variant="ButtonVariant.Ghost">Ghost</TailSplitButton>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailSplitButton Size="ButtonSize.Xs">Xs</TailSplitButton>
<TailSplitButton Size="ButtonSize.Sm">Sm</TailSplitButton>
<TailSplitButton Size="ButtonSize.Md">Md</TailSplitButton>
<TailSplitButton Size="ButtonSize.Lg">Lg</TailSplitButton>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailSplitButton Disabled="true">Disabled</TailSplitButton>

@* Loading state *@
<TailSplitButton IsLoading="true">Loading...</TailSplitButton>

@* Both disabled and loading *@
<TailSplitButton Disabled="true" IsLoading="true">Processing</TailSplitButton>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailSplitButton OnPrimaryClick="HandleOnPrimaryClick">
    Click Me
</TailSplitButton>

@code {
    private void HandleOnPrimaryClick(MouseEventArgs args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailSplitButton Variant="ButtonVariant.Primary" Size="ButtonSize.Sm">
    Combined Parameters
</TailSplitButton>
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
    <TailSplitButton Variant="ButtonVariant.Primary" Size="ButtonSize.Sm" OnPrimaryClick="HandleAction">
        Action Button
    </TailSplitButton>
</div>

@code {
    private void HandleAction(MouseEventArgs args)
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
| **PrimaryContent** | `RenderFragment?` | - | PrimaryContent parameter |
| **DropdownContent** | `RenderFragment?` | - | DropdownContent parameter |
| **DropdownIcon** | `RenderFragment?` | - | Icon to display |
| **Variant** | `ButtonVariant` | ButtonVariant.Primary | Visual variant style for the component |
| **Size** | `ButtonSize` | ButtonSize.Md | Size of the component |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **IsLoading** | `bool` | - | Whether the component is in loading state |
| **Type** | `string` | "button" | Type parameter |
| **AriaLabel** | `string?` | - | Label text for the component |
| **Tooltip** | `string?` | - | Tooltip parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnPrimaryClick** | `EventCallback<MouseEventArgs>` | Raised when component is clicked |
| **OnDropdownToggle** | `EventCallback` | OnDropdownToggle callback |

### Enums

#### ButtonVariant

```csharp
public enum ButtonVariant
{
    Primary,
    Success,
    Warning,
    Danger,
    Info,
    Outline,
    Soft,
    Ghost,
}
```

/// Button variant styles for split buttons.
///

#### Tail.Blazor.SplitButton;.ButtonVariant

```csharp
public enum Tail.Blazor.SplitButton;.ButtonVariant
{
    Primary,
    Success,
    Warning,
    Danger,
    Info,
    Outline,
    Soft,
    Ghost,
}
```

/// Button variant styles for split buttons.
///

#### ButtonSize

```csharp
public enum ButtonSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Button size options for split buttons.
///

#### Tail.Blazor.SplitButton;.ButtonSize

```csharp
public enum Tail.Blazor.SplitButton;.ButtonSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Button size options for split buttons.
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
