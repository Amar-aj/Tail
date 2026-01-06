# Tail.Blazor.Clipboard

Independent NuGet package for the TailClipboard component.

## Installation

```bash
dotnet add package Tail.Blazor.Clipboard
```

## Features

- Copy to clipboard
- Success feedback
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Clipboard;
```

## Component Usage

```razor
<TailClipboard></TailClipboard>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Text** | `string?` | - | Text parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **OnCopied** | `EventCallback` | OnCopied callback |

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Clipboard

<TailClipboard>
    Hello, World!
</TailClipboard>
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailClipboard OnCopied="() => Console.WriteLine("Clicked")">
    Click Me
</TailClipboard>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailClipboard>Content</TailClipboard>
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailClipboard OnCopied="HandleOnCopied">
    Click Me
</TailClipboard>

@code {
    private void HandleOnCopied()
    {
        // Handle the event
        Console.WriteLine("Event triggered");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailClipboard Text="Sample Text" Style="Sample Style">
    Combined Parameters
</TailClipboard>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailClipboard Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailClipboard>

@* Using Class parameter *@
<TailClipboard Class="my-custom-class shadow-lg">
    With Custom Class
</TailClipboard>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailClipboard Type="submit">
        Submit Form
    </TailClipboard>
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
    <TailClipboard OnCopied="HandleAction">
        Action Button
    </TailClipboard>
</div>

@code {
    private void HandleAction()
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

- **Package ID**: `Tail.Blazor.Clipboard`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
