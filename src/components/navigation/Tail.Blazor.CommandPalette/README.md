# Tail.Blazor.CommandPalette

Independent NuGet package for the TailCommandPalette component.

## Installation

```bash
dotnet add package Tail.Blazor.CommandPalette
```

## Features

- Command palette (Cmd+K style)
- Search/filter commands
- Keyboard navigation
- Shortcut display
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.CommandPalette;
```

## Component Usage

```razor
<TailCommandPalette></TailCommandPalette>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **IsVisible** | `bool` | - | Whether the component is visible |
| **Commands** | `List<CommandItem>` | new() | Commands parameter |
| **Placeholder** | `string` | "Type a command or search..." | Placeholder text |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **IsVisibleChanged** | `EventCallback<bool>` | Raised when value changes |

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.CommandPalette

<TailCommandPalette />
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailCommandPalette IsVisibleChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailCommandPalette>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailCommandPalette />
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailCommandPalette IsVisibleChanged="HandleIsVisibleChanged">
    Click Me
</TailCommandPalette>

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
<TailCommandPalette IsVisible="true" Placeholder="Sample Placeholder" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailCommandPalette Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailCommandPalette>

@* Using Class parameter *@
<TailCommandPalette Class="my-custom-class shadow-lg">
    With Custom Class
</TailCommandPalette>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailCommandPalette Type="submit">
        Submit Form
    </TailCommandPalette>
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
    <TailCommandPalette IsVisibleChanged="HandleAction" />
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

- **Package ID**: `Tail.Blazor.CommandPalette`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
