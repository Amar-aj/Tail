# Tail.Blazor.ImageCropper

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

## Component Usage

```razor
<TailImageCropper></TailImageCropper>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string?` | - | Current value of the component |
| **Size** | `ImageCropperSize` | ImageCropperSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **AspectRatioWidth** | `int` | 1 | AspectRatioWidth parameter |
| **AspectRatioHeight** | `int` | 1 | AspectRatioHeight parameter |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |

## Enums

### ImageCropperSize

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

### Tail.Blazor.ImageCropper;.ImageCropperSize

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

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ImageCropper

<TailImageCropper />
```

### Common Patterns

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

### Basic Usage

The simplest way to use the component:

```razor
<TailImageCropper />
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailImageCropper Size="ImageCropperSize.Xs">Xs</TailImageCropper>
<TailImageCropper Size="ImageCropperSize.Sm">Sm</TailImageCropper>
<TailImageCropper Size="ImageCropperSize.Md">Md</TailImageCropper>
<TailImageCropper Size="ImageCropperSize.Lg">Lg</TailImageCropper>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailImageCropper Disabled="true">Disabled</TailImageCropper>

```

### Event Handling

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

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailImageCropper Size="ImageCropperSize.Sm" Value="Sample Value" Label="Sample Label" AspectRatioWidth="10" AspectRatioHeight="10" />
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailImageCropper Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailImageCropper>

<TailImageCropper OnClick="ToggleProcessing">
    Toggle State
</TailImageCropper>

@code {
    private void ToggleProcessing()
    {
        isProcessing = !isProcessing;
        isDisabled = isProcessing;
    }
}
```

#### Data Binding

```razor
@code {
    private string componentValue = "";
}

<TailImageCropper @bind-Value="componentValue" ValueChanged="OnValueChanged">
    Bound Component
</TailImageCropper>

<p>Current Value: @componentValue</p>

@code {
    private void OnValueChanged()
    {
        Console.WriteLine($"Value changed to: {componentValue}");
    }
}
```

#### Custom Styling

```razor
@* Using Style parameter *@
<TailImageCropper Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailImageCropper>

@* Using Class parameter *@
<TailImageCropper Class="my-custom-class shadow-lg">
    With Custom Class
</TailImageCropper>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailImageCropper Type="submit">
        Submit Form
    </TailImageCropper>
</EditForm>

@code {
    private MyModel model = new();
    
    private void HandleSubmit()
    {
        // Process form submission
        Console.WriteLine("Form submitted successfully");
    }
}
```

#### Accessibility

```razor
@* Accessible component with ARIA label and tooltip *@
<TailImageCropper Label="Primary action button">
    Accessible Button
</TailImageCropper>
```

### Real-World Example

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

## Package Information

- **Package ID**: `Tail.Blazor.ImageCropper`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
