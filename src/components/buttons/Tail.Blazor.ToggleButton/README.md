# Tail.Blazor.ToggleButton

Independent NuGet package for the TailToggleButton component.

## Installation

```bash
dotnet add package Tail.Blazor.ToggleButton
```

## Features

- Toggle on/off states
- Visual feedback for toggled state
- 9 variants
- 5 sizes
- Disabled states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ToggleButton;
```

## Component Usage

```razor
<TailToggleButton></TailToggleButton>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **ToggledContent** | `RenderFragment?` | - | ToggledContent parameter |
| **Variant** | `ButtonVariant` | ButtonVariant.Primary | Visual variant style for the component |
| **Size** | `ButtonSize` | ButtonSize.Md | Size of the component |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **IsToggled** | `bool` | - | IsToggled parameter |
| **AriaLabel** | `string?` | - | Label text for the component |
| **Tooltip** | `string?` | - | Tooltip parameter |
| **Type** | `string` | "button" | Type parameter |
| **AutoFocus** | `bool` | false | AutoFocus parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **IsToggledChanged** | `EventCallback<bool>` | Raised when value changes |
| **OnClick** | `EventCallback<MouseEventArgs>` | Raised when component is clicked |

## Enums

### ButtonVariant

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

/// Button variant styles for toggle buttons.
///

### Tail.Blazor.ToggleButton;.ButtonVariant

```csharp
public enum Tail.Blazor.ToggleButton;.ButtonVariant
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

/// Button variant styles for toggle buttons.
///

### ButtonSize

```csharp
public enum ButtonSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Button size options for toggle buttons.
///

### Tail.Blazor.ToggleButton;.ButtonSize

```csharp
public enum Tail.Blazor.ToggleButton;.ButtonSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Button size options for toggle buttons.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ToggleButton

<TailToggleButton>
    Hello, World!
</TailToggleButton>
```

### Common Patterns

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailToggleButton Variant="ButtonVariant.Primary">
    Primary Action
</TailToggleButton>
```

**Medium Size**

```razor
<TailToggleButton Size="ButtonSize.Md">
    Medium Size
</TailToggleButton>
```

**With Click Handler**

```razor
<TailToggleButton IsToggledChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailToggleButton>
```

**Disabled State**

```razor
<TailToggleButton Disabled="true">
    Disabled
</TailToggleButton>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailToggleButton>Content</TailToggleButton>
```

### Variants

Different visual variants for various use cases:

```razor
<TailToggleButton Variant="ButtonVariant.Primary">Primary</TailToggleButton>
<TailToggleButton Variant="ButtonVariant.Success">Success</TailToggleButton>
<TailToggleButton Variant="ButtonVariant.Warning">Warning</TailToggleButton>
<TailToggleButton Variant="ButtonVariant.Danger">Danger</TailToggleButton>
<TailToggleButton Variant="ButtonVariant.Info">Info</TailToggleButton>
<TailToggleButton Variant="ButtonVariant.Outline">Outline</TailToggleButton>
<TailToggleButton Variant="ButtonVariant.Soft">Soft</TailToggleButton>
<TailToggleButton Variant="ButtonVariant.Ghost">Ghost</TailToggleButton>
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailToggleButton Size="ButtonSize.Xs">Xs</TailToggleButton>
<TailToggleButton Size="ButtonSize.Sm">Sm</TailToggleButton>
<TailToggleButton Size="ButtonSize.Md">Md</TailToggleButton>
<TailToggleButton Size="ButtonSize.Lg">Lg</TailToggleButton>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailToggleButton Disabled="true">Disabled</TailToggleButton>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailToggleButton IsToggledChanged="HandleIsToggledChanged">
    Click Me
</TailToggleButton>

@code {
    private void HandleIsToggledChanged(bool args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailToggleButton Variant="ButtonVariant.Primary" Size="ButtonSize.Sm">
    Combined Parameters
</TailToggleButton>
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailToggleButton Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailToggleButton>

<TailToggleButton OnClick="ToggleProcessing">
    Toggle State
</TailToggleButton>

@code {
    private void ToggleProcessing()
    {
        isProcessing = !isProcessing;
        isDisabled = isProcessing;
    }
}
```

#### With Tooltip

```razor
<TailToggleButton Tooltip="This is a helpful tooltip">
    Hover for Tooltip
</TailToggleButton>
```

#### Multiple Event Handlers

```razor
<TailToggleButton 
    IsToggledChanged="OnFirstEvent"
    OnClick="OnSecondEvent">
    Multiple Events
</TailToggleButton>

@code {
    private void OnFirstEvent()
    {
        Console.WriteLine("First event triggered");
    }
    
    private void OnSecondEvent()
    {
        Console.WriteLine("Second event triggered");
    }
}
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailToggleButton Type="submit">
        Submit Form
    </TailToggleButton>
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
<TailToggleButton Variant="Primary action button" Tooltip="Click to perform action">
    Accessible Button
</TailToggleButton>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailToggleButton Variant="ButtonVariant.Primary" Size="ButtonSize.Sm" IsToggledChanged="HandleAction">
        Action Button
    </TailToggleButton>
</div>

@code {
    private void HandleAction(bool args)
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

- **Package ID**: `Tail.Blazor.ToggleButton`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
