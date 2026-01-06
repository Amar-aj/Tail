# Tail.Blazor.CurrencyInput

Independent NuGet package for the TailCurrencyInput component.

## Installation

```bash
dotnet add package Tail.Blazor.CurrencyInput
```

## Features

- Currency input with symbol
- Left or right symbol position
- Custom currency symbol
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.CurrencyInput;
```

## Component Usage

```razor
<TailCurrencyInput></TailCurrencyInput>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `decimal?` | - | Current value of the component |
| **CurrencySymbol** | `string` | "$" | CurrencySymbol parameter |
| **SymbolPosition** | `CurrencySymbolPosition` | CurrencySymbolPosition.Left | SymbolPosition parameter |
| **Size** | `CurrencyInputSize` | CurrencyInputSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<decimal?>` | Raised when value changes |

## Enums

### CurrencyInputSize

```csharp
public enum CurrencyInputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// CurrencyInput size options.
///

### Tail.Blazor.CurrencyInput;.CurrencyInputSize

```csharp
public enum Tail.Blazor.CurrencyInput;.CurrencyInputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// CurrencyInput size options.
///

### CurrencySymbolPosition

```csharp
public enum CurrencySymbolPosition
{
    Left,
}
```

/// Currency symbol position.
///

### Tail.Blazor.CurrencyInput;.CurrencySymbolPosition

```csharp
public enum Tail.Blazor.CurrencyInput;.CurrencySymbolPosition
{
    Left,
}
```

/// Currency symbol position.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.CurrencyInput

<TailCurrencyInput />
```

### Common Patterns

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailCurrencyInput Size="CurrencyInputSize.Md">
    Medium Size
</TailCurrencyInput>
```

**With Click Handler**

```razor
<TailCurrencyInput ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailCurrencyInput>
```

**Disabled State**

```razor
<TailCurrencyInput Disabled="true">
    Disabled
</TailCurrencyInput>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailCurrencyInput />
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailCurrencyInput Size="CurrencyInputSize.Xs">Xs</TailCurrencyInput>
<TailCurrencyInput Size="CurrencyInputSize.Sm">Sm</TailCurrencyInput>
<TailCurrencyInput Size="CurrencyInputSize.Md">Md</TailCurrencyInput>
<TailCurrencyInput Size="CurrencyInputSize.Lg">Lg</TailCurrencyInput>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailCurrencyInput Disabled="true">Disabled</TailCurrencyInput>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailCurrencyInput ValueChanged="HandleValueChanged">
    Click Me
</TailCurrencyInput>

@code {
    private void HandleValueChanged(decimal? args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailCurrencyInput Size="CurrencyInputSize.Sm" CurrencySymbol="Sample CurrencySymbol" Label="Sample Label" />
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailCurrencyInput Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailCurrencyInput>

<TailCurrencyInput OnClick="ToggleProcessing">
    Toggle State
</TailCurrencyInput>

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

<TailCurrencyInput @bind-Value="componentValue" ValueChanged="OnValueChanged">
    Bound Component
</TailCurrencyInput>

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
<TailCurrencyInput Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailCurrencyInput>

@* Using Class parameter *@
<TailCurrencyInput Class="my-custom-class shadow-lg">
    With Custom Class
</TailCurrencyInput>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailCurrencyInput Type="submit">
        Submit Form
    </TailCurrencyInput>
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
<TailCurrencyInput Label="Primary action button">
    Accessible Button
</TailCurrencyInput>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailCurrencyInput Size="CurrencyInputSize.Sm" ValueChanged="HandleAction" />
</div>

@code {
    private void HandleAction(decimal? args)
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

- **Package ID**: `Tail.Blazor.CurrencyInput`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
