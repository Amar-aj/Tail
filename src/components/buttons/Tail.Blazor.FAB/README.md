# Tail.Blazor.FAB

Independent NuGet package for the TailFAB (Floating Action Button) component.

## Installation

```bash
dotnet add package Tail.Blazor.FAB
```

## Features

- 4 positions (TopLeft, TopRight, BottomLeft, BottomRight)
- Fixed positioning
- Circular design
- Loading states
- Disabled states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.FAB;
```

## Component Usage

```razor
<TailFAB></TailFAB>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Position** | `FABPosition` | FABPosition.BottomRight | Position parameter |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **IsLoading** | `bool` | - | Whether the component is in loading state |
| **Type** | `string` | "button" | Type parameter |
| **Style** | `string?` | - | Additional CSS styles |
| **AutoFocus** | `bool` | false | AutoFocus parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **OnClick** | `EventCallback<MouseEventArgs>` | Raised when component is clicked |

## Enums

### FABPosition

```csharp
public enum FABPosition
{
    TopLeft,
    TopRight,
    BottomLeft,
}
```

/// Floating Action Button position options.
///

### Tail.Blazor.FAB;.FABPosition

```csharp
public enum Tail.Blazor.FAB;.FABPosition
{
    TopLeft,
    TopRight,
    BottomLeft,
}
```

/// Floating Action Button position options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.FAB

<TailFAB>
    Hello, World!
</TailFAB>
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailFAB OnClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailFAB>
```

**Disabled State**

```razor
<TailFAB Disabled="true">
    Disabled
</TailFAB>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailFAB>Content</TailFAB>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailFAB Disabled="true">Disabled</TailFAB>

@* Loading state *@
<TailFAB IsLoading="true">Loading...</TailFAB>

@* Both disabled and loading *@
<TailFAB Disabled="true" IsLoading="true">Processing</TailFAB>
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailFAB OnClick="HandleOnClick">
    Click Me
</TailFAB>

@code {
    private void HandleOnClick(MouseEventArgs args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailFAB Type="Sample Type">
    Combined Parameters
</TailFAB>
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailFAB Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailFAB>

<TailFAB OnClick="ToggleProcessing">
    Toggle State
</TailFAB>

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
<TailFAB Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailFAB>

@* Using Class parameter *@
<TailFAB Class="my-custom-class shadow-lg">
    With Custom Class
</TailFAB>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailFAB Type="submit">
        Submit Form
    </TailFAB>
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

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailFAB OnClick="HandleAction">
        Action Button
    </TailFAB>
</div>

@code {
    private void HandleAction(MouseEventArgs args)
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

- **Package ID**: `Tail.Blazor.FAB`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
