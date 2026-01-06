# Tail.Blazor.Dialog

Independent NuGet package for the TailDialog component.

## Installation

```bash
dotnet add package Tail.Blazor.Dialog
```

## Features

- Modal dialog with backdrop
- 6 sizes (Sm, Md, Lg, Xl, Xxl, Full)
- Title and footer support
- Close button option
- Close on backdrop click
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Dialog;
```

## Component Usage

```razor
<TailDialog></TailDialog>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **IsVisible** | `bool` | - | Whether the component is visible |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Footer** | `RenderFragment?` | - | Footer parameter |
| **Title** | `string?` | - | Title parameter |
| **Size** | `DialogSize` | DialogSize.Md | Size of the component |
| **ShowCloseButton** | `bool` | true | ShowCloseButton parameter |
| **CloseOnBackdropClick** | `bool` | true | Event callback raised when clicked |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **IsVisibleChanged** | `EventCallback<bool>` | Raised when value changes |

## Enums

### DialogSize

```csharp
public enum DialogSize
{
    Sm,
    Md,
    Lg,
    Xl,
    Xxl,
}
```

/// Dialog size options.
///

### Tail.Blazor.Dialog;.DialogSize

```csharp
public enum Tail.Blazor.Dialog;.DialogSize
{
    Sm,
    Md,
    Lg,
    Xl,
    Xxl,
}
```

/// Dialog size options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Dialog

<TailDialog>
    Hello, World!
</TailDialog>
```

### Common Patterns

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailDialog Size="DialogSize.Lg">
    Medium Size
</TailDialog>
```

**With Click Handler**

```razor
<TailDialog IsVisibleChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailDialog>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailDialog>Content</TailDialog>
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailDialog Size="DialogSize.Sm">Sm</TailDialog>
<TailDialog Size="DialogSize.Md">Md</TailDialog>
<TailDialog Size="DialogSize.Lg">Lg</TailDialog>
<TailDialog Size="DialogSize.Xl">Xl</TailDialog>
<TailDialog Size="DialogSize.Xxl">Xxl</TailDialog>
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailDialog IsVisibleChanged="HandleIsVisibleChanged">
    Click Me
</TailDialog>

@code {
    private void HandleIsVisibleChanged(bool args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailDialog Size="DialogSize.Md" IsVisible="true" Title="Sample Title">
    Combined Parameters
</TailDialog>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailDialog Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailDialog>

@* Using Class parameter *@
<TailDialog Class="my-custom-class shadow-lg">
    With Custom Class
</TailDialog>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailDialog Type="submit">
        Submit Form
    </TailDialog>
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
    <TailDialog Size="DialogSize.Md" IsVisibleChanged="HandleAction">
        Action Button
    </TailDialog>
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

- **Package ID**: `Tail.Blazor.Dialog`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
