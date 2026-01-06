# Tail.Blazor.IconButton

Independent NuGet package for the TailIconButton component.

## Installation

```bash
dotnet add package Tail.Blazor.IconButton
```

## Features

- Icon-only button design
- 9 variants (Primary, Success, Warning, Danger, Info, Outline, Soft, Ghost, Link)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Loading states
- Disabled states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.IconButton;
```

## Component Usage

```razor
<TailIconButton></TailIconButton>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Variant** | `ButtonVariant` | ButtonVariant.Primary | Visual variant style for the component |
| **Size** | `ButtonSize` | ButtonSize.Md | Size of the component |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **IsLoading** | `bool` | - | Whether the component is in loading state |
| **Type** | `string` | "button" | Type parameter |
| **StopPropagation** | `bool` | - | StopPropagation parameter |
| **Style** | `string?` | - | Additional CSS styles |
| **AriaLabel** | `string?` | - | Label text for the component |
| **Tooltip** | `string?` | - | Tooltip parameter |
| **Shape** | `ButtonShape` | ButtonShape.Square | Shape parameter |
| **AutoFocus** | `bool` | false | AutoFocus parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **OnClick** | `EventCallback<MouseEventArgs>` | Raised when component is clicked |

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.IconButton

<TailIconButton>
    Hello, World!
</TailIconButton>
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailIconButton OnClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailIconButton>
```

**Disabled State**

```razor
<TailIconButton Disabled="true">
    Disabled
</TailIconButton>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailIconButton>Content</TailIconButton>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailIconButton Disabled="true">Disabled</TailIconButton>

@* Loading state *@
<TailIconButton IsLoading="true">Loading...</TailIconButton>

@* Both disabled and loading *@
<TailIconButton Disabled="true" IsLoading="true">Processing</TailIconButton>
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailIconButton OnClick="HandleOnClick">
    Click Me
</TailIconButton>

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
<TailIconButton>
    Content
</TailIconButton>
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailIconButton Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailIconButton>

<TailIconButton OnClick="ToggleProcessing">
    Toggle State
</TailIconButton>

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
<TailIconButton Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailIconButton>

@* Using Class parameter *@
<TailIconButton Class="my-custom-class shadow-lg">
    With Custom Class
</TailIconButton>
```

#### With Tooltip

```razor
<TailIconButton Tooltip="This is a helpful tooltip">
    Hover for Tooltip
</TailIconButton>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailIconButton Type="submit">
        Submit Form
    </TailIconButton>
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
<TailIconButton Variant="Primary action button" Tooltip="Click to perform action">
    Accessible Button
</TailIconButton>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailIconButton OnClick="HandleAction">
        Action Button
    </TailIconButton>
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
- `Tail.Blazor.Button`

## Target Frameworks

- .NET 8
- .NET 9
- .NET 10

## Package Information

- **Package ID**: `Tail.Blazor.IconButton`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
