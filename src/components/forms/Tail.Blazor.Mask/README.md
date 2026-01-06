# Tail.Blazor.Mask

Independent NuGet package for the TailMask component.

## Installation

```bash
dotnet add package Tail.Blazor.Mask
```

## Features

- Input masking (phone, credit card, etc.)
- Custom mask patterns
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Validation error display
- Required field indicator
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Mask;
```

## Component Usage

```razor
<TailMask></TailMask>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string?` | - | Current value of the component |
| **Mask** | `string` | "(###) ###-####" | Mask parameter |
| **Size** | `MaskSize` | MaskSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |

## Enums

### MaskSize

```csharp
public enum MaskSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Mask size options.
///

### Tail.Blazor.Mask;.MaskSize

```csharp
public enum Tail.Blazor.Mask;.MaskSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Mask size options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Mask

<TailMask />
```

### Common Patterns

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailMask Size="MaskSize.Md">
    Medium Size
</TailMask>
```

**With Click Handler**

```razor
<TailMask ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailMask>
```

**Disabled State**

```razor
<TailMask Disabled="true">
    Disabled
</TailMask>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailMask />
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailMask Size="MaskSize.Xs">Xs</TailMask>
<TailMask Size="MaskSize.Sm">Sm</TailMask>
<TailMask Size="MaskSize.Md">Md</TailMask>
<TailMask Size="MaskSize.Lg">Lg</TailMask>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailMask Disabled="true">Disabled</TailMask>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailMask ValueChanged="HandleValueChanged">
    Click Me
</TailMask>

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
<TailMask Size="MaskSize.Sm" Value="Sample Value" Mask="Sample Mask" Label="Sample Label" Placeholder="Sample Placeholder" />
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailMask Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailMask>

<TailMask OnClick="ToggleProcessing">
    Toggle State
</TailMask>

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

<TailMask @bind-Value="componentValue" ValueChanged="OnValueChanged">
    Bound Component
</TailMask>

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
<TailMask Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailMask>

@* Using Class parameter *@
<TailMask Class="my-custom-class shadow-lg">
    With Custom Class
</TailMask>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailMask Type="submit">
        Submit Form
    </TailMask>
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
<TailMask Label="Primary action button">
    Accessible Button
</TailMask>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailMask Size="MaskSize.Sm" ValueChanged="HandleAction" />
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

- **Package ID**: `Tail.Blazor.Mask`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
