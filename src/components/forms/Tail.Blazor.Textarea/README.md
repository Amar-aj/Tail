# Tail.Blazor.Textarea

Independent NuGet package for the TailTextarea component.

## Installation

```bash
dotnet add package Tail.Blazor.Textarea
```

## Features

- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label and help text support
- Character count display
- Auto-resize option
- Validation error display
- Required field indicator
- Disabled and readonly states
- Customizable rows
- Max length support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Textarea;
```

## Component Usage

```razor
<TailTextarea></TailTextarea>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string?` | - | Current value of the component |
| **Size** | `TextareaSize` | TextareaSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **HelpText** | `string?` | - | HelpText parameter |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **ReadOnly** | `bool` | - | Whether the component is read-only |
| **Rows** | `int` | 3 | Rows parameter |
| **MaxLength** | `int?` | - | Maximum value constraint |
| **ShowCharacterCount** | `bool` | - | ShowCharacterCount parameter |
| **AutoResize** | `bool` | - | Size of the component |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |
| **OnFocus** | `EventCallback<FocusEventArgs>` | Raised when focus is gained |
| **OnBlur** | `EventCallback<FocusEventArgs>` | Raised when focus is lost |

## Enums

### TextareaSize

```csharp
public enum TextareaSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Textarea size options.
///

### Tail.Blazor.Textarea;.TextareaSize

```csharp
public enum Tail.Blazor.Textarea;.TextareaSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Textarea size options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Textarea

<TailTextarea />
```

### Common Patterns

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailTextarea Size="TextareaSize.Md">
    Medium Size
</TailTextarea>
```

**With Click Handler**

```razor
<TailTextarea ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailTextarea>
```

**Disabled State**

```razor
<TailTextarea Disabled="true">
    Disabled
</TailTextarea>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailTextarea />
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailTextarea Size="TextareaSize.Xs">Xs</TailTextarea>
<TailTextarea Size="TextareaSize.Sm">Sm</TailTextarea>
<TailTextarea Size="TextareaSize.Md">Md</TailTextarea>
<TailTextarea Size="TextareaSize.Lg">Lg</TailTextarea>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailTextarea Disabled="true">Disabled</TailTextarea>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailTextarea ValueChanged="HandleValueChanged">
    Click Me
</TailTextarea>

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
<TailTextarea Size="TextareaSize.Sm" Value="Sample Value" Label="Sample Label" Placeholder="Sample Placeholder" HelpText="Sample HelpText" />
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailTextarea Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailTextarea>

<TailTextarea OnClick="ToggleProcessing">
    Toggle State
</TailTextarea>

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

<TailTextarea @bind-Value="componentValue" ValueChanged="OnValueChanged">
    Bound Component
</TailTextarea>

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
<TailTextarea Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailTextarea>

@* Using Class parameter *@
<TailTextarea Class="my-custom-class shadow-lg">
    With Custom Class
</TailTextarea>
```

#### Multiple Event Handlers

```razor
<TailTextarea 
    ValueChanged="OnFirstEvent"
    OnFocus="OnSecondEvent">
    Multiple Events
</TailTextarea>

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
    
    <TailTextarea Type="submit">
        Submit Form
    </TailTextarea>
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
<TailTextarea Label="Primary action button">
    Accessible Button
</TailTextarea>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailTextarea Size="TextareaSize.Sm" ValueChanged="HandleAction" />
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

- **Package ID**: `Tail.Blazor.Textarea`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
