# Tail.Blazor.Toast

Independent NuGet package for the TailToast component.

## Installation

```bash
dotnet add package Tail.Blazor.Toast
```

## Features

- Toast notification
- 4 variants (Success, Warning, Error, Info)
- Auto-dismiss option
- Title and message support
- Icon support
- Dismissible
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Toast;
```

## Component Usage

```razor
<TailToast></TailToast>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Message** | `string?` | - | Message parameter |
| **Title** | `string?` | - | Title parameter |
| **Variant** | `ToastVariant` | ToastVariant.Info | Visual variant style for the component |
| **Dismissible** | `bool` | true | Dismissible parameter |
| **ShowIcon** | `bool` | true | Icon to display |
| **Icon** | `RenderFragment?` | - | Icon to display |
| **AutoDismissAfter** | `int?` | 5000 | AutoDismissAfter parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **OnDismiss** | `EventCallback` | OnDismiss callback |

## Enums

### ToastVariant

```csharp
public enum ToastVariant
{
    Success,
    Warning,
    Error,
}
```

/// Toast variant styles.
///

### Tail.Blazor.Toast;.ToastVariant

```csharp
public enum Tail.Blazor.Toast;.ToastVariant
{
    Success,
    Warning,
    Error,
}
```

/// Toast variant styles.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Toast

<TailToast>
    Hello, World!
</TailToast>
```

### Common Patterns

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailToast Variant="ToastVariant.Success">
    Primary Action
</TailToast>
```

**With Click Handler**

```razor
<TailToast OnDismiss="() => Console.WriteLine("Clicked")">
    Click Me
</TailToast>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailToast>Content</TailToast>
```

### Variants

Different visual variants for various use cases:

```razor
<TailToast Variant="ToastVariant.Success">Success</TailToast>
<TailToast Variant="ToastVariant.Warning">Warning</TailToast>
<TailToast Variant="ToastVariant.Error">Error</TailToast>
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailToast OnDismiss="HandleOnDismiss">
    Click Me
</TailToast>

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
<TailToast Variant="ToastVariant.Success" Message="Sample Message" Title="Sample Title" Dismissible="true" ShowIcon="true">
    Combined Parameters
</TailToast>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailToast Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailToast>

@* Using Class parameter *@
<TailToast Class="my-custom-class shadow-lg">
    With Custom Class
</TailToast>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailToast Type="submit">
        Submit Form
    </TailToast>
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
<TailToast Variant="Primary action button">
    Accessible Button
</TailToast>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailToast Variant="ToastVariant.Success" OnDismiss="HandleAction">
        Action Button
    </TailToast>
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

- **Package ID**: `Tail.Blazor.Toast`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
