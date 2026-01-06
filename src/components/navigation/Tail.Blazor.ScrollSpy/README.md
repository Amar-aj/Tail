# Tail.Blazor.ScrollSpy

Independent NuGet package for the TailScrollSpy component.

## Installation

```bash
dotnet add package Tail.Blazor.ScrollSpy
```

## Features

- Scroll spy navigation
- Active section highlighting
- Left/right positioning
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ScrollSpy;
```

## Component Usage

```razor
<TailScrollSpy></TailScrollSpy>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Items** | `List<ScrollSpyItem>` | new() | Data items collection |
| **ActiveId** | `string?` | - | ActiveId parameter |
| **Position** | `ScrollSpyPosition` | ScrollSpyPosition.Left | Position parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **OnItemClick** | `EventCallback<ScrollSpyItem>` | Raised when component is clicked |

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ScrollSpy

<TailScrollSpy />
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailScrollSpy OnItemClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailScrollSpy>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailScrollSpy />
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailScrollSpy OnItemClick="HandleOnItemClick">
    Click Me
</TailScrollSpy>

@code {
    private void HandleOnItemClick(Tail.Blazor.ScrollSpy.ScrollSpyItem args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailScrollSpy ActiveId="Sample ActiveId" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailScrollSpy Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailScrollSpy>

@* Using Class parameter *@
<TailScrollSpy Class="my-custom-class shadow-lg">
    With Custom Class
</TailScrollSpy>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailScrollSpy Type="submit">
        Submit Form
    </TailScrollSpy>
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
    <TailScrollSpy OnItemClick="HandleAction" />
</div>

@code {
    private void HandleAction(ScrollSpyItem args)
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

- **Package ID**: `Tail.Blazor.ScrollSpy`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
