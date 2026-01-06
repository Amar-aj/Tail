# Tail.Blazor.Switch

Independent NuGet package for the TailSwitch component.

## Installation

```bash
dotnet add package Tail.Blazor.Switch
```

## Features

- Toggle switch design
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Custom content support
- Validation error display
- Disabled state
- Smooth animations
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Switch;
```

## Component Usage

```razor
<TailSwitch></TailSwitch>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **IsChecked** | `bool` | - | IsChecked parameter |
| **Size** | `SwitchSize` | SwitchSize.Md | Size of the component |
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

### SwitchSize

```csharp
public enum SwitchSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Switch size options.
///

### Tail.Blazor.Switch;.SwitchSize

```csharp
public enum Tail.Blazor.Switch;.SwitchSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Switch size options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Switch

<TailSwitch>
    Hello, World!
</TailSwitch>
```

### Common Patterns

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailSwitch Size="SwitchSize.Md">
    Medium Size
</TailSwitch>
```

**With Click Handler**

```razor
<TailSwitch IsCheckedChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailSwitch>
```

**Disabled State**

```razor
<TailSwitch Disabled="true">
    Disabled
</TailSwitch>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailSwitch>Content</TailSwitch>
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailSwitch Size="SwitchSize.Xs">Xs</TailSwitch>
<TailSwitch Size="SwitchSize.Sm">Sm</TailSwitch>
<TailSwitch Size="SwitchSize.Md">Md</TailSwitch>
<TailSwitch Size="SwitchSize.Lg">Lg</TailSwitch>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailSwitch Disabled="true">Disabled</TailSwitch>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailSwitch IsCheckedChanged="HandleIsCheckedChanged">
    Click Me
</TailSwitch>

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
<TailSwitch Size="SwitchSize.Sm" IsChecked="true" Label="Sample Label" ErrorMessage="Sample ErrorMessage">
    Combined Parameters
</TailSwitch>
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailSwitch Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailSwitch>

<TailSwitch OnClick="ToggleProcessing">
    Toggle State
</TailSwitch>

@code {
    private void ToggleProcessing()
    {
        isProcessing = !isProcessing;
        isDisabled = isProcessing;
    }
}
```

#### Custom Styling

```razor
@* Using Style parameter *@
<TailSwitch Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailSwitch>

@* Using Class parameter *@
<TailSwitch Class="my-custom-class shadow-lg">
    With Custom Class
</TailSwitch>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailSwitch Type="submit">
        Submit Form
    </TailSwitch>
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
<TailSwitch Label="Primary action button">
    Accessible Button
</TailSwitch>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailSwitch Size="SwitchSize.Sm" IsCheckedChanged="HandleAction">
        Action Button
    </TailSwitch>
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

- **Package ID**: `Tail.Blazor.Switch`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
