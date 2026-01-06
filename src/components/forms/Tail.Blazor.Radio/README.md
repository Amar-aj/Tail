# Tail.Blazor.Radio

Independent NuGet package for the TailRadio component.

## Installation

```bash
dotnet add package Tail.Blazor.Radio
```

## Features

- Radio button input
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Group name support
- Label support
- Custom content support
- Validation error display
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Radio;
```

## Component Usage

```razor
<TailRadio></TailRadio>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string?` | - | Current value of the component |
| **GroupName** | `string?` | - | GroupName parameter |
| **IsChecked** | `bool` | - | IsChecked parameter |
| **Size** | `RadioSize` | RadioSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **IsCheckedChanged** | `EventCallback<bool>` | Raised when value changes |

## Enums

### RadioSize

```csharp
public enum RadioSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Radio size options.
///

### Tail.Blazor.Radio;.RadioSize

```csharp
public enum Tail.Blazor.Radio;.RadioSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Radio size options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Radio

<TailRadio>
    Hello, World!
</TailRadio>
```

### Common Patterns

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailRadio Size="RadioSize.Md">
    Medium Size
</TailRadio>
```

**With Click Handler**

```razor
<TailRadio IsCheckedChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailRadio>
```

**Disabled State**

```razor
<TailRadio Disabled="true">
    Disabled
</TailRadio>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailRadio>Content</TailRadio>
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailRadio Size="RadioSize.Xs">Xs</TailRadio>
<TailRadio Size="RadioSize.Sm">Sm</TailRadio>
<TailRadio Size="RadioSize.Md">Md</TailRadio>
<TailRadio Size="RadioSize.Lg">Lg</TailRadio>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailRadio Disabled="true">Disabled</TailRadio>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailRadio IsCheckedChanged="HandleIsCheckedChanged">
    Click Me
</TailRadio>

@code {
    private void HandleIsCheckedChanged(bool args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailRadio Size="RadioSize.Sm" Value="Sample Value" GroupName="Sample GroupName" IsChecked="true" Label="Sample Label">
    Combined Parameters
</TailRadio>
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailRadio Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailRadio>

<TailRadio OnClick="ToggleProcessing">
    Toggle State
</TailRadio>

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

<TailRadio @bind-Value="componentValue" IsCheckedChanged="OnValueChanged">
    Bound Component
</TailRadio>

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
<TailRadio Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailRadio>

@* Using Class parameter *@
<TailRadio Class="my-custom-class shadow-lg">
    With Custom Class
</TailRadio>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailRadio Type="submit">
        Submit Form
    </TailRadio>
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
<TailRadio Label="Primary action button">
    Accessible Button
</TailRadio>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailRadio Size="RadioSize.Sm" IsCheckedChanged="HandleAction">
        Action Button
    </TailRadio>
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

- **Package ID**: `Tail.Blazor.Radio`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
