---
title: IconButton
package: Tail.Blazor.IconButton
category: buttons
namespace: Tail.Blazor.IconButton
route: /components/buttons/iconbutton
is_generic: false
is_missing: false
---

# IconButton

Independent NuGet package for the TailIconButton component.

## Installation

```bash
dotnet add package Tail.Blazor.IconButton
```

## Features

- Icon-only button design
- 9 variants (Primary, Success, Warning, Danger, Info, Outline, Soft, Ghost, Link)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Loading states
- Disabled states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.IconButton;
```

## Basic Usage

```razor
<TailIconButton>Content</TailIconButton>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.IconButton

<TailIconButton>
    Hello, World!
</TailIconButton>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailIconButton OnClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailIconButton>
```

**Disabled State**

```razor
<TailIconButton Disabled="true">
    Disabled
</TailIconButton>
```

## Variants

Different visual variants for various use cases:

```razor
<TailIconButton Variant="ButtonVariant.Primary">Primary</TailIconButton>
<TailIconButton Variant="ButtonVariant.Success">Success</TailIconButton>
<TailIconButton Variant="ButtonVariant.Warning">Warning</TailIconButton>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailIconButton Size="ButtonSize.Sm">Small</TailIconButton>
<TailIconButton Size="ButtonSize.Md">Medium</TailIconButton>
<TailIconButton Size="ButtonSize.Lg">Large</TailIconButton>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailIconButton Disabled="true">Disabled</TailIconButton>

@* Loading state *@
<TailIconButton IsLoading="true">Loading...</TailIconButton>

@* Both disabled and loading *@
<TailIconButton Disabled="true" IsLoading="true">Processing</TailIconButton>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailIconButton OnClick="HandleOnClick">
    Click Me
</TailIconButton>

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
<TailIconButton>
    Content
</TailIconButton>
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
    <TailIconButton OnClick="HandleAction">
        Action Button
    </TailIconButton>
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
| **Type** | `string` | "button" | Type parameter |
| **StopPropagation** | `bool` | - | StopPropagation parameter |
| **Style** | `string?` | - | Additional CSS styles |
| **AriaLabel** | `string?` | - | Label text for the component |
| **Tooltip** | `string?` | - | Tooltip parameter |
| **Shape** | `ButtonShape` | ButtonShape.Square | Shape parameter |
| **AutoFocus** | `bool` | false | AutoFocus parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnClick** | `EventCallback<MouseEventArgs>` | Raised when component is clicked |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `ButtonShape` | `enum` | ButtonShape property |

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
- `Tail.Blazor.Button`

## Target Frameworks

- .NET 8
- .NET 9
- .NET 10
