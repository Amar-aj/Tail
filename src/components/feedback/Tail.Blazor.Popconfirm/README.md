# Tail.Blazor.Popconfirm

Independent NuGet package for the TailPopconfirm component.

## Installation

```bash
dotnet add package Tail.Blazor.Popconfirm
```

## Features

- Popconfirm dialog
- Click or hover trigger
- 4 placement options (Top, Bottom, Left, Right)
- Custom confirm/cancel text
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Popconfirm;
```

## Component Usage

```razor
<TailPopconfirm></TailPopconfirm>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Title** | `string` | "Are you sure?" | Title parameter |
| **ConfirmText** | `string` | "Confirm" | ConfirmText parameter |
| **CancelText** | `string` | "Cancel" | CancelText parameter |
| **Trigger** | `PopconfirmTrigger` | PopconfirmTrigger.Click | Trigger parameter |
| **Placement** | `PopconfirmPlacement` | PopconfirmPlacement.Top | Placement parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **OnConfirm** | `EventCallback` | OnConfirm callback |
| **OnCancel** | `EventCallback` | OnCancel callback |

## Enums

### PopconfirmTrigger

```csharp
public enum PopconfirmTrigger
{
    Click,
}
```

/// Popconfirm trigger type.
///

### Tail.Blazor.Popconfirm;.PopconfirmTrigger

```csharp
public enum Tail.Blazor.Popconfirm;.PopconfirmTrigger
{
    Click,
}
```

/// Popconfirm trigger type.
///

### PopconfirmPlacement

```csharp
public enum PopconfirmPlacement
{
    Top,
    Bottom,
    Left,
}
```

/// Popconfirm placement.
///

### Tail.Blazor.Popconfirm;.PopconfirmPlacement

```csharp
public enum Tail.Blazor.Popconfirm;.PopconfirmPlacement
{
    Top,
    Bottom,
    Left,
}
```

/// Popconfirm placement.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Popconfirm

<TailPopconfirm>
    Hello, World!
</TailPopconfirm>
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailPopconfirm OnConfirm="() => Console.WriteLine("Clicked")">
    Click Me
</TailPopconfirm>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailPopconfirm>Content</TailPopconfirm>
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailPopconfirm OnConfirm="HandleOnConfirm">
    Click Me
</TailPopconfirm>

@code {
    private void HandleOnConfirm()
    {
        // Handle the event
        Console.WriteLine("Event triggered");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailPopconfirm Title="Sample Title" ConfirmText="Sample ConfirmText" CancelText="Sample CancelText">
    Combined Parameters
</TailPopconfirm>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailPopconfirm Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailPopconfirm>

@* Using Class parameter *@
<TailPopconfirm Class="my-custom-class shadow-lg">
    With Custom Class
</TailPopconfirm>
```

#### Multiple Event Handlers

```razor
<TailPopconfirm 
    OnConfirm="OnFirstEvent"
    OnCancel="OnSecondEvent">
    Multiple Events
</TailPopconfirm>

@code {
    private void OnFirstEvent()
    {
        Console.WriteLine("First event triggered");
    }
    
    private void OnSecondEvent()
    {
        Console.WriteLine("Second event triggered");
    }
}
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailPopconfirm Type="submit">
        Submit Form
    </TailPopconfirm>
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
    <TailPopconfirm OnConfirm="HandleAction">
        Action Button
    </TailPopconfirm>
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

- **Package ID**: `Tail.Blazor.Popconfirm`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
