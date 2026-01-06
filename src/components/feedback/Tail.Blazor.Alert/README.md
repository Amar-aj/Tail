# Tail.Blazor.Alert

Independent NuGet package for the TailAlert component.

## Installation

```bash
dotnet add package Tail.Blazor.Alert
```

## Features

- 4 variants (Success, Warning, Danger, Info)
- Optional title
- Dismissible alerts
- Icon support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Alert;
```

## Component Usage

```razor
<TailAlert></TailAlert>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Variant** | `AlertVariant` | AlertVariant.Info | Visual variant style for the component |
| **Title** | `string?` | - | Title parameter |
| **Dismissible** | `bool` | - | Dismissible parameter |
| **ShowIcon** | `bool` | true | Icon to display |
| **Icon** | `RenderFragment?` | - | Icon to display |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **OnDismiss** | `EventCallback` | OnDismiss callback |

## Enums

### AlertVariant

```csharp
public enum AlertVariant
{
    Success,
    Warning,
    Danger,
}
```

/// Alert variant styles.
///

### Tail.Blazor.Alert;.AlertVariant

```csharp
public enum Tail.Blazor.Alert;.AlertVariant
{
    Success,
    Warning,
    Danger,
}
```

/// Alert variant styles.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Alert

<TailAlert>
    Hello, World!
</TailAlert>
```

### Common Patterns

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailAlert Variant="AlertVariant.Success">
    Primary Action
</TailAlert>
```

**With Click Handler**

```razor
<TailAlert OnDismiss="() => Console.WriteLine("Clicked")">
    Click Me
</TailAlert>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailAlert>Content</TailAlert>
```

### Variants

Different visual variants for various use cases:

```razor
<TailAlert Variant="AlertVariant.Success">Success</TailAlert>
<TailAlert Variant="AlertVariant.Warning">Warning</TailAlert>
<TailAlert Variant="AlertVariant.Danger">Danger</TailAlert>
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailAlert OnDismiss="HandleOnDismiss">
    Click Me
</TailAlert>

@code {
    private void HandleOnDismiss()
    {
        // Handle the event
        Console.WriteLine("Event triggered");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailAlert Variant="AlertVariant.Success" Title="Sample Title" Dismissible="true" ShowIcon="true">
    Combined Parameters
</TailAlert>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailAlert Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailAlert>

@* Using Class parameter *@
<TailAlert Class="my-custom-class shadow-lg">
    With Custom Class
</TailAlert>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailAlert Type="submit">
        Submit Form
    </TailAlert>
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

#### Accessibility

```razor
@* Accessible component with ARIA label and tooltip *@
<TailAlert Variant="Primary action button">
    Accessible Button
</TailAlert>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailAlert Variant="AlertVariant.Success" OnDismiss="HandleAction">
        Action Button
    </TailAlert>
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

- **Package ID**: `Tail.Blazor.Alert`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
