# Tail.Blazor.Tour

Independent NuGet package for the TailTour component.

## Installation

```bash
dotnet add package Tail.Blazor.Tour
```

## Features

- Interactive tour/walkthrough
- Step-by-step navigation
- Spotlight overlay
- Custom tooltip placement
- Previous/Next navigation
- Finish tour callback
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Tour;
```

## Component Usage

```razor
<TailTour></TailTour>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Steps** | `List<TourStep>` | new() | Step value for numeric inputs |
| **IsActive** | `bool` | - | IsActive parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **OnTourComplete** | `EventCallback` | OnTourComplete callback |

## Enums

### TourTooltipPlacement

```csharp
public enum TourTooltipPlacement
{
    Auto,
    Top,
    Bottom,
    Left,
}
```

/// Tour tooltip placement.
///

### Tail.Blazor.Tour;.TourTooltipPlacement

```csharp
public enum Tail.Blazor.Tour;.TourTooltipPlacement
{
    Auto,
    Top,
    Bottom,
    Left,
}
```

/// Tour tooltip placement.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Tour

<TailTour />
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailTour OnTourComplete="() => Console.WriteLine("Clicked")">
    Click Me
</TailTour>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailTour />
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailTour OnTourComplete="HandleOnTourComplete">
    Click Me
</TailTour>

@code {
    private void HandleOnTourComplete()
    {
        // Handle the event
        Console.WriteLine("Event triggered");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailTour IsActive="true" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailTour Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailTour>

@* Using Class parameter *@
<TailTour Class="my-custom-class shadow-lg">
    With Custom Class
</TailTour>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailTour Type="submit">
        Submit Form
    </TailTour>
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
    <TailTour OnTourComplete="HandleAction" />
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

- **Package ID**: `Tail.Blazor.Tour`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
