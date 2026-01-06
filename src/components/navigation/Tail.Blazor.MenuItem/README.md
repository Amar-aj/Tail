# Tail.Blazor.MenuItem

Independent NuGet package for the TailMenuItem component.

## Installation

```bash
dotnet add package Tail.Blazor.MenuItem
```

## Features

- Menu item with link
- Icon support
- Badge support
- Active state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.MenuItem;
```

## Component Usage

```razor
<TailMenuItem></TailMenuItem>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Icon** | `RenderFragment?` | - | Icon to display |
| **Badge** | `RenderFragment?` | - | Badge parameter |
| **Href** | `string?` | "#" | Href parameter |
| **IsActive** | `bool` | - | IsActive parameter |
| **Target** | `string?` | - | Target parameter |
| **Disabled** | `bool` | false | Whether the component is disabled |
| **PreventDefault** | `bool` | true | PreventDefault parameter |
| **Style** | `string?` | - | Additional CSS styles |
| **ItemClass** | `string?` | - | Additional CSS classes |
| **Bordered** | `bool` | false | Bordered parameter |
| **Shadow** | `ShadowLevel` | ShadowLevel.None | Shadow parameter |
| **Underline** | `bool` | false | Underline parameter |
| **BorderColor** | `string?` | - | Color scheme for the component |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **OnClick** | `EventCallback<MenuItemClickArgs>` | Raised when component is clicked |

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.MenuItem

<TailMenuItem>
    Hello, World!
</TailMenuItem>
```

### Common Patterns

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailMenuItem OnClick="() => Console.WriteLine("Clicked")">
    Click Me
</TailMenuItem>
```

**Disabled State**

```razor
<TailMenuItem Disabled="true">
    Disabled
</TailMenuItem>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailMenuItem>Content</TailMenuItem>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailMenuItem Disabled="true">Disabled</TailMenuItem>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailMenuItem OnClick="HandleOnClick">
    Click Me
</TailMenuItem>

@code {
    private void HandleOnClick(Tail.Blazor.MenuItem.MenuItemClickArgs args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailMenuItem Href="Sample Href" IsActive="true">
    Combined Parameters
</TailMenuItem>
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailMenuItem Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailMenuItem>

<TailMenuItem OnClick="ToggleProcessing">
    Toggle State
</TailMenuItem>

@code {
    private void ToggleProcessing()
    {
        isProcessing = !isProcessing;
        isDisabled = isProcessing;
    }
}
```

#### Custom Styling

```razor
@* Using Style parameter *@
<TailMenuItem Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailMenuItem>

@* Using Class parameter *@
<TailMenuItem Class="my-custom-class shadow-lg">
    With Custom Class
</TailMenuItem>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailMenuItem Type="submit">
        Submit Form
    </TailMenuItem>
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
    <TailMenuItem OnClick="HandleAction">
        Action Button
    </TailMenuItem>
</div>

@code {
    private void HandleAction(MenuItemClickArgs args)
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

- **Package ID**: `Tail.Blazor.MenuItem`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
