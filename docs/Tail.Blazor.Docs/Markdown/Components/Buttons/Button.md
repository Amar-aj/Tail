---
title: Button
package: Tail.Blazor.Button
category: buttons
namespace: Tail.Blazor.Button
route: /components/buttons/button
is_generic: false
is_missing: false
---

# Button

Independent NuGet package for the TailButton component - a lightweight, high-performance button component for Blazor applications.

## Installation

```bash
dotnet add package Tail.Blazor.Button
```

## Features

- **9 Variants**: Primary, Success, Warning, Danger, Info, Outline, Soft, Ghost, Link
- **5 Sizes**: Xs, Sm, Md, Lg, Xl
- **Loading States**: Built-in spinner with customizable loading text
- **Icon Support**: Start and end icon slots via RenderFragment
- **Disabled States**: Full disabled state support
- **Full Theme Support**: CSS variable-based theming for easy customization
- **Accessibility**: ARIA label support, tooltip support, autofocus capability
- **Event Handling**: Click event with optional stop propagation
- **MAUI Blazor Hybrid Compatible**: Works seamlessly in hybrid applications

## Namespace

```csharp
using Tail.Blazor.Button;
```

## Basic Usage

```razor
<TailButton>Content</TailButton>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Button

<TailButton>
    Hello, World!
</TailButton>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailButton Variant="ButtonVariant.Primary">
    Primary Action
</TailButton>
```

**Medium Size**

```razor
<TailButton Size="ButtonSize.Md">
    Medium Size
</TailButton>
```

**With Click Handler**

```razor
<TailButton OnClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailButton>
```

**Disabled State**

```razor
<TailButton Disabled="true">
    Disabled
</TailButton>
```

## Variants

Different visual variants for various use cases:

```razor
<TailButton Variant="ButtonVariant.Primary">Primary</TailButton>
<TailButton Variant="ButtonVariant.Success">Success</TailButton>
<TailButton Variant="ButtonVariant.Warning">Warning</TailButton>
<TailButton Variant="ButtonVariant.Danger">Danger</TailButton>
<TailButton Variant="ButtonVariant.Info">Info</TailButton>
<TailButton Variant="ButtonVariant.Outline">Outline</TailButton>
<TailButton Variant="ButtonVariant.Soft">Soft</TailButton>
<TailButton Variant="ButtonVariant.Ghost">Ghost</TailButton>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailButton Size="ButtonSize.Xs">Xs</TailButton>
<TailButton Size="ButtonSize.Sm">Sm</TailButton>
<TailButton Size="ButtonSize.Md">Md</TailButton>
<TailButton Size="ButtonSize.Lg">Lg</TailButton>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailButton Disabled="true">Disabled</TailButton>

@* Loading state *@
<TailButton IsLoading="true">Loading...</TailButton>

@* Both disabled and loading *@
<TailButton Disabled="true" IsLoading="true">Processing</TailButton>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailButton OnClick="HandleOnClick">
    Click Me
</TailButton>

@code {
    private void HandleOnClick(MouseEventArgs args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailButton Variant="ButtonVariant.Primary" Size="ButtonSize.Sm">
    Combined Parameters
</TailButton>
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
    <TailButton Variant="ButtonVariant.Primary" Size="ButtonSize.Sm" OnClick="HandleAction">
        Action Button
    </TailButton>
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
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Variant** | `ButtonVariant` | ButtonVariant.Primary | Visual variant style for the component |
| **Size** | `ButtonSize` | ButtonSize.Md | Size of the component |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **IsLoading** | `bool` | - | Whether the component is in loading state |
| **LoadingText** | `string?` | - | Whether the component is in loading state |
| **ShowDefaultLoadingText** | `bool` | false | Whether the component is in loading state |
| **DefaultLoadingText** | `string` | "Loading..." | Whether the component is in loading state |
| **Type** | `string` | "button" | Type parameter |
| **StopPropagation** | `bool` | - | StopPropagation parameter |
| **IconStart** | `RenderFragment?` | - | Icon to display |
| **IconEnd** | `RenderFragment?` | - | Icon to display |
| **Style** | `string?` | - | Additional CSS styles |
| **Tooltip** | `string?` | - | Tooltip parameter |
| **EnableRipple** | `bool` | true | EnableRipple parameter |
| **FullWidth** | `bool` | false | FullWidth parameter |
| **AnimationDuration** | `string` | "duration-200" | AnimationDuration parameter |
| **AriaLabel** | `string?` | - | Label text for the component |
| **AutoFocus** | `bool` | false | AutoFocus parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnClick** | `EventCallback<MouseEventArgs>` | Raised when component is clicked |

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

/// Button variant styles.
///

#### Tail.Blazor.Button;.ButtonVariant

```csharp
public enum Tail.Blazor.Button;.ButtonVariant
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

/// Button variant styles.
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

/// Button size options.
///

#### Tail.Blazor.Button;.ButtonSize

```csharp
public enum Tail.Blazor.Button;.ButtonSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Button size options.
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
