# Tail.Blazor.AccordionItem

Independent NuGet package for the TailAccordionItem component.

## Installation

```bash
dotnet add package Tail.Blazor.AccordionItem
```

## Features

- Individual accordion item
- Expand/collapse animation
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.AccordionItem;
```

## Component Usage

```razor
<TailAccordionItem></TailAccordionItem>
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
@using Tail.Blazor.AccordionItem

<TailAccordionItem>
    Hello, World!
</TailAccordionItem>
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailAccordionItem IsExpandedChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailAccordionItem>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailAccordionItem>Content</TailAccordionItem>
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailAccordionItem IsExpandedChanged="HandleIsExpandedChanged">
    Click Me
</TailAccordionItem>

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
<TailAccordionItem Title="Sample Title" IsExpanded="true" Style="Sample Style">
    Combined Parameters
</TailAccordionItem>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailAccordionItem Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailAccordionItem>

@* Using Class parameter *@
<TailAccordionItem Class="my-custom-class shadow-lg">
    With Custom Class
</TailAccordionItem>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailAccordionItem Type="submit">
        Submit Form
    </TailAccordionItem>
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
    <TailAccordionItem IsExpandedChanged="HandleAction">
        Action Button
    </TailAccordionItem>
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

- **Package ID**: `Tail.Blazor.AccordionItem`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
