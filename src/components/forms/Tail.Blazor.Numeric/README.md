# Tail.Blazor.Numeric

Independent NuGet package for the TailNumeric component.

## Installation

```bash
dotnet add package Tail.Blazor.Numeric
```

## Features

- Numeric input with increment/decrement buttons
- Min/max constraints
- Custom step value
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Numeric;
```

## Component Usage

```razor
<TailNumeric></TailNumeric>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `decimal` | - | Current value of the component |
| **Min** | `decimal` | decimal.MinValue | Minimum value constraint |
| **Max** | `decimal` | decimal.MaxValue | Maximum value constraint |
| **Step** | `decimal` | 1 | Step value for numeric inputs |
| **Size** | `NumericSize` | NumericSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<decimal>` | Raised when value changes |

## Enums

### NumericSize

```csharp
public enum NumericSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Numeric size options.
///

### Tail.Blazor.Numeric;.NumericSize

```csharp
public enum Tail.Blazor.Numeric;.NumericSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Numeric size options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Numeric

<TailNumeric />
```

### Common Patterns

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailNumeric Size="NumericSize.Md">
    Medium Size
</TailNumeric>
```

**With Click Handler**

```razor
<TailNumeric ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailNumeric>
```

**Disabled State**

```razor
<TailNumeric Disabled="true">
    Disabled
</TailNumeric>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailNumeric />
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailNumeric Size="NumericSize.Xs">Xs</TailNumeric>
<TailNumeric Size="NumericSize.Sm">Sm</TailNumeric>
<TailNumeric Size="NumericSize.Md">Md</TailNumeric>
<TailNumeric Size="NumericSize.Lg">Lg</TailNumeric>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailNumeric Disabled="true">Disabled</TailNumeric>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailNumeric ValueChanged="HandleValueChanged">
    Click Me
</TailNumeric>

@code {
    private void HandleValueChanged(decimal args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailNumeric Size="NumericSize.Sm" />
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailNumeric Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailNumeric>

<TailNumeric OnClick="ToggleProcessing">
    Toggle State
</TailNumeric>

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

<TailNumeric @bind-Value="componentValue" ValueChanged="OnValueChanged">
    Bound Component
</TailNumeric>

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
<TailNumeric Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailNumeric>

@* Using Class parameter *@
<TailNumeric Class="my-custom-class shadow-lg">
    With Custom Class
</TailNumeric>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailNumeric Type="submit">
        Submit Form
    </TailNumeric>
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
<TailNumeric Label="Primary action button">
    Accessible Button
</TailNumeric>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailNumeric Size="NumericSize.Sm" ValueChanged="HandleAction" />
</div>

@code {
    private void HandleAction(decimal args)
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

- **Package ID**: `Tail.Blazor.Numeric`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
