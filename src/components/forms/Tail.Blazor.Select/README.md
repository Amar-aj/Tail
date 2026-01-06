# Tail.Blazor.Select

Independent NuGet package for the TailSelect component.

## Installation

```bash
dotnet add package Tail.Blazor.Select
```

## Features

- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label and help text support
- Placeholder option
- Items list support
- Custom option content
- Validation error display
- Required field indicator
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Select;
```

## Component Usage

```razor
<TailSelect></TailSelect>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string?` | - | Current value of the component |
| **Size** | `SelectSize` | SelectSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **HelpText** | `string?` | - | HelpText parameter |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Items** | `List<SelectItem>?` | - | Data items collection |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |

## Enums

### SelectSize

```csharp
public enum SelectSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Select size options.
///

### Tail.Blazor.Select;.SelectSize

```csharp
public enum Tail.Blazor.Select;.SelectSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Select size options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Select

<TailSelect>
    Hello, World!
</TailSelect>
```

### Common Patterns

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailSelect Size="SelectSize.Md">
    Medium Size
</TailSelect>
```

**With Click Handler**

```razor
<TailSelect ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailSelect>
```

**Disabled State**

```razor
<TailSelect Disabled="true">
    Disabled
</TailSelect>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailSelect>Content</TailSelect>
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailSelect Size="SelectSize.Xs">Xs</TailSelect>
<TailSelect Size="SelectSize.Sm">Sm</TailSelect>
<TailSelect Size="SelectSize.Md">Md</TailSelect>
<TailSelect Size="SelectSize.Lg">Lg</TailSelect>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailSelect Disabled="true">Disabled</TailSelect>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailSelect ValueChanged="HandleValueChanged">
    Click Me
</TailSelect>

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
<TailSelect Size="SelectSize.Sm" Value="Sample Value" Label="Sample Label" Placeholder="Sample Placeholder" HelpText="Sample HelpText">
    Combined Parameters
</TailSelect>
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailSelect Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailSelect>

<TailSelect OnClick="ToggleProcessing">
    Toggle State
</TailSelect>

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

<TailSelect @bind-Value="componentValue" ValueChanged="OnValueChanged">
    Bound Component
</TailSelect>

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
<TailSelect Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailSelect>

@* Using Class parameter *@
<TailSelect Class="my-custom-class shadow-lg">
    With Custom Class
</TailSelect>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailSelect Type="submit">
        Submit Form
    </TailSelect>
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
<TailSelect Label="Primary action button">
    Accessible Button
</TailSelect>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailSelect Size="SelectSize.Sm" ValueChanged="HandleAction">
        Action Button
    </TailSelect>
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

- **Package ID**: `Tail.Blazor.Select`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
