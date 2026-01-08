---
title: ImageCropper
package: Tail.Blazor.ImageCropper
category: forms
namespace: Tail.Blazor.ImageCropper
route: /components/forms/imagecropper
is_generic: false
is_missing: false
---

# ImageCropper

Independent NuGet package for the TailImageCropper component.

## Installation

```bash
dotnet add package Tail.Blazor.ImageCropper
```

## Features

- Image upload and cropping
- Aspect ratio control
- Image preview
- Crop functionality
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ImageCropper;
```

## Basic Usage

```razor
<TailImageCropper />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ImageCropper

<TailImageCropper />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailImageCropper Size="ImageCropperSize.Md">
    Medium Size
</TailImageCropper>
```

**With Click Handler**

```razor
<TailImageCropper ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailImageCropper>
```

**Disabled State**

```razor
<TailImageCropper Disabled="true">
    Disabled
</TailImageCropper>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailImageCropper Size="ImageCropperSize.Xs">Xs</TailImageCropper>
<TailImageCropper Size="ImageCropperSize.Sm">Sm</TailImageCropper>
<TailImageCropper Size="ImageCropperSize.Md">Md</TailImageCropper>
<TailImageCropper Size="ImageCropperSize.Lg">Lg</TailImageCropper>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailImageCropper Disabled="true">Disabled</TailImageCropper>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailImageCropper ValueChanged="HandleValueChanged">
    Click Me
</TailImageCropper>

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
<TailImageCropper Size="ImageCropperSize.Sm" Value="Sample Value" Label="Sample Label" AspectRatioWidth="10" AspectRatioHeight="10" />
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
    <TailImageCropper Size="ImageCropperSize.Sm" ValueChanged="HandleAction" />
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
| **Size** | `ImageCropperSize` | ImageCropperSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **AspectRatioWidth** | `int` | 1 | AspectRatioWidth parameter |
| **AspectRatioHeight** | `int` | 1 | AspectRatioHeight parameter |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |

### Enums

#### ImageCropperSize

```csharp
public enum ImageCropperSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// ImageCropper size options.
///

#### Tail.Blazor.ImageCropper;.ImageCropperSize

```csharp
public enum Tail.Blazor.ImageCropper;.ImageCropperSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// ImageCropper size options.
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
