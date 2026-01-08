---
title: Alert
package: Tail.Blazor.Alert
category: feedback
namespace: Tail.Blazor.Alert
route: /components/feedback/alert
is_generic: false
is_missing: false
---

# Alert

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

## Basic Usage

```razor
<TailAlert>Content</TailAlert>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Alert

<TailAlert>
    Hello, World!
</TailAlert>
```

## Common Patterns

Frequently used patterns and combinations:

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

## Variants

Different visual variants for various use cases:

```razor
<TailAlert Variant="AlertVariant.Success">Success</TailAlert>
<TailAlert Variant="AlertVariant.Warning">Warning</TailAlert>
<TailAlert Variant="AlertVariant.Danger">Danger</TailAlert>
```

## Event Handling

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

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailAlert Variant="AlertVariant.Success" Title="Sample Title" Dismissible="true" ShowIcon="true">
    Combined Parameters
</TailAlert>
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

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Variant** | `AlertVariant` | AlertVariant.Info | Visual variant style for the component |
| **Title** | `string?` | - | Title parameter |
| **Dismissible** | `bool` | - | Dismissible parameter |
| **ShowIcon** | `bool` | true | Icon to display |
| **Icon** | `RenderFragment?` | - | Icon to display |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnDismiss** | `EventCallback` | OnDismiss callback |

### Enums

#### AlertVariant

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

#### Tail.Blazor.Alert;.AlertVariant

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
