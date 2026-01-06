# Tail.Blazor.Pagination

Independent NuGet package for the TailPagination component.

## Installation

```bash
dotnet add package Tail.Blazor.Pagination
```

## Features

- Page navigation
- Previous/Next buttons
- Page number buttons
- Ellipsis for large page counts
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Pagination;
```

## Component Usage

```razor
<TailPagination></TailPagination>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **CurrentPage** | `int` | 1 | CurrentPage parameter |
| **TotalPages** | `int` | 1 | TotalPages parameter |
| **VisiblePages** | `int` | 5 | Whether the component is visible |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **CurrentPageChanged** | `EventCallback<int>` | Raised when value changes |

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Pagination

<TailPagination />
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailPagination CurrentPageChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailPagination>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailPagination />
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailPagination CurrentPageChanged="HandleCurrentPageChanged">
    Click Me
</TailPagination>

@code {
    private void HandleCurrentPageChanged(int args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailPagination CurrentPage="10" TotalPages="10" VisiblePages="10" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailPagination Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailPagination>

@* Using Class parameter *@
<TailPagination Class="my-custom-class shadow-lg">
    With Custom Class
</TailPagination>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailPagination Type="submit">
        Submit Form
    </TailPagination>
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
    <TailPagination CurrentPageChanged="HandleAction" />
</div>

@code {
    private void HandleAction(int args)
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

- **Package ID**: `Tail.Blazor.Pagination`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
