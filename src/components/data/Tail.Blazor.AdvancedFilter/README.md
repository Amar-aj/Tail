# Tail.Blazor.AdvancedFilter

Independent NuGet package for the TailAdvancedFilter component.

## Installation

```bash
dotnet add package Tail.Blazor.AdvancedFilter
```

## Features

- Advanced filtering
- Field selection
- Operator selection
- Filter value input
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.AdvancedFilter;
```

## Component Usage

```razor
<TailAdvancedFilter></TailAdvancedFilter>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Fields** | `List<string>` | new() | Fields parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **OnFilterApplied** | `EventCallback<FilterCriteria>` | Raised with FilterCriteria value |

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.AdvancedFilter

<TailAdvancedFilter />
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailAdvancedFilter OnFilterApplied="() => Console.WriteLine("Clicked")">
    Click Me
</TailAdvancedFilter>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailAdvancedFilter />
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailAdvancedFilter OnFilterApplied="HandleOnFilterApplied">
    Click Me
</TailAdvancedFilter>

@code {
    private void HandleOnFilterApplied(Tail.Blazor.AdvancedFilter.FilterCriteria args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailAdvancedFilter Fields="Sample Fields" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailAdvancedFilter Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailAdvancedFilter>

@* Using Class parameter *@
<TailAdvancedFilter Class="my-custom-class shadow-lg">
    With Custom Class
</TailAdvancedFilter>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailAdvancedFilter Type="submit">
        Submit Form
    </TailAdvancedFilter>
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
    <TailAdvancedFilter OnFilterApplied="HandleAction" />
</div>

@code {
    private void HandleAction(FilterCriteria args)
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

- **Package ID**: `Tail.Blazor.AdvancedFilter`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
