# Tail.Blazor.CollapsibleMenu

Independent NuGet package for the TailCollapsibleMenu component.

## Installation

```bash
dotnet add package Tail.Blazor.CollapsibleMenu
```

## Features

- Collapsible menu
- Expand/collapse animation
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.CollapsibleMenu;
```

## Component Usage

```razor
<TailCollapsibleMenu></TailCollapsibleMenu>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Title** | `string` | string.Empty | Title parameter |
| **IsExpanded** | `bool` | - | IsExpanded parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **IsExpandedChanged** | `EventCallback<bool>` | Raised when value changes |

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.CollapsibleMenu

<TailCollapsibleMenu>
    Hello, World!
</TailCollapsibleMenu>
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailCollapsibleMenu IsExpandedChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailCollapsibleMenu>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailCollapsibleMenu>Content</TailCollapsibleMenu>
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailCollapsibleMenu IsExpandedChanged="HandleIsExpandedChanged">
    Click Me
</TailCollapsibleMenu>

@code {
    private void HandleIsExpandedChanged(bool args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailCollapsibleMenu Title="Sample Title" IsExpanded="true" Style="Sample Style">
    Combined Parameters
</TailCollapsibleMenu>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailCollapsibleMenu Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailCollapsibleMenu>

@* Using Class parameter *@
<TailCollapsibleMenu Class="my-custom-class shadow-lg">
    With Custom Class
</TailCollapsibleMenu>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailCollapsibleMenu Type="submit">
        Submit Form
    </TailCollapsibleMenu>
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
    <TailCollapsibleMenu IsExpandedChanged="HandleAction">
        Action Button
    </TailCollapsibleMenu>
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

- **Package ID**: `Tail.Blazor.CollapsibleMenu`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
