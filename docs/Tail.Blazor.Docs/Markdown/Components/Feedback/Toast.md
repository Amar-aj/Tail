---
title: Toast
package: Tail.Blazor.Toast
category: feedback
namespace: Tail.Blazor.Toast
route: /components/feedback/toast
is_generic: false
is_missing: false
---

# Toast

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

## Basic Usage

```razor
<TailToast>Content</TailToast>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Toast

<TailToast>
    Hello, World!
</TailToast>
```

## Common Patterns

Frequently used patterns and combinations:

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

## Variants

Different visual variants for various use cases:

```razor
<TailToast Variant="ToastVariant.Success">Success</TailToast>
<TailToast Variant="ToastVariant.Warning">Warning</TailToast>
<TailToast Variant="ToastVariant.Error">Error</TailToast>
```

## Event Handling

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

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailToast Variant="ToastVariant.Success" Message="Sample Message" Title="Sample Title" Dismissible="true" ShowIcon="true">
    Combined Parameters
</TailToast>
```

## Advanced Examples

More complex usage scenarios:

More complex usage scenarios:

##

## Real-World Example

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

## API Reference

### Parameters

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

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnDismiss** | `EventCallback` | OnDismiss callback |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `Dispose` | `void` | Dispose property |

### Enums

#### ToastVariant

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

#### Tail.Blazor.Toast;.ToastVariant

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
