# Tail.Blazor.ContextMenu

Independent NuGet package for the TailContextMenu component.

## Installation

```bash
dotnet add package Tail.Blazor.ContextMenu
```

## Features

- Right-click context menu
- Menu items with actions
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ContextMenu;
```

## Component Usage

```razor
<TailContextMenu></TailContextMenu>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Items** | `List<ContextMenuItem>` | new() | Data items collection |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **OnItemClick** | `EventCallback<ContextMenuItem>` | Raised when component is clicked |

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ContextMenu

<TailContextMenu>
    Hello, World!
</TailContextMenu>
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailContextMenu OnItemClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailContextMenu>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailContextMenu>Content</TailContextMenu>
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailContextMenu OnItemClick="HandleOnItemClick">
    Click Me
</TailContextMenu>

@code {
    private void HandleOnItemClick(Tail.Blazor.ContextMenu.ContextMenuItem args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailContextMenu Style="Sample Style">
    Combined Parameters
</TailContextMenu>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailContextMenu Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailContextMenu>

@* Using Class parameter *@
<TailContextMenu Class="my-custom-class shadow-lg">
    With Custom Class
</TailContextMenu>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailContextMenu Type="submit">
        Submit Form
    </TailContextMenu>
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
    <TailContextMenu OnItemClick="HandleAction">
        Action Button
    </TailContextMenu>
</div>

@code {
    private void HandleAction(ContextMenuItem args)
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

- **Package ID**: `Tail.Blazor.ContextMenu`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
