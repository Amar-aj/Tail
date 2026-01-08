---
title: BottomSheet
package: Tail.Blazor.BottomSheet
category: layout
namespace: Tail.Blazor.BottomSheet
route: /components/layout/bottomsheet
is_generic: false
is_missing: false
---

# BottomSheet

Independent NuGet package for the TailBottomSheet component.

## Installation

```bash
dotnet add package Tail.Blazor.BottomSheet
```

## Features

- Bottom sheet modal
- 4 sizes (Sm, Md, Lg, Full)
- Backdrop click to close
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.BottomSheet;
```

## Basic Usage

```razor
<TailBottomSheet>Content</TailBottomSheet>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.BottomSheet

<TailBottomSheet>
    Hello, World!
</TailBottomSheet>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailBottomSheet Size="BottomSheetSize.Md">
    Medium Size
</TailBottomSheet>
```

**With Click Handler**

```razor
<TailBottomSheet IsVisibleChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailBottomSheet>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailBottomSheet Size="BottomSheetSize.Sm">Sm</TailBottomSheet>
<TailBottomSheet Size="BottomSheetSize.Md">Md</TailBottomSheet>
<TailBottomSheet Size="BottomSheetSize.Lg">Lg</TailBottomSheet>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailBottomSheet IsVisibleChanged="HandleIsVisibleChanged">
    Click Me
</TailBottomSheet>

@code {
    private void HandleIsVisibleChanged(bool args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailBottomSheet Size="BottomSheetSize.Md" IsVisible="true" CloseOnBackdropClick="true" Style="Sample Style">
    Combined Parameters
</TailBottomSheet>
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
    <TailBottomSheet Size="BottomSheetSize.Md" IsVisibleChanged="HandleAction">
        Action Button
    </TailBottomSheet>
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
| **IsVisible** | `bool` | - | Whether the component is visible |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Size** | `BottomSheetSize` | BottomSheetSize.Md | Size of the component |
| **CloseOnBackdropClick** | `bool` | true | Event callback raised when clicked |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **IsVisibleChanged** | `EventCallback<bool>` | Raised when value changes |

### Enums

#### BottomSheetSize

```csharp
public enum BottomSheetSize
{
    Sm,
    Md,
    Lg,
}
```

/// Bottom sheet size options.
///

#### Tail.Blazor.BottomSheet;.BottomSheetSize

```csharp
public enum Tail.Blazor.BottomSheet;.BottomSheetSize
{
    Sm,
    Md,
    Lg,
}
```

/// Bottom sheet size options.
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
