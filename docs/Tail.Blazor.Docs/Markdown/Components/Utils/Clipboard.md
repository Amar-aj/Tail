---
title: Clipboard
package: Tail.Blazor.Clipboard
category: utils
namespace: Tail.Blazor.Clipboard
route: /components/utils/clipboard
is_generic: false
is_missing: false
---

# Clipboard

Independent NuGet package for the TailClipboard component.

## Installation

```bash
dotnet add package Tail.Blazor.Clipboard
```

## Features

- Copy to clipboard
- Success feedback
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Clipboard;
```

## Basic Usage

```razor
<TailClipboard>Content</TailClipboard>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Clipboard

<TailClipboard>
    Hello, World!
</TailClipboard>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**With Click Handler**

```razor
<TailClipboard OnCopied="() => Console.WriteLine("Clicked")">
    Click Me
</TailClipboard>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailClipboard OnCopied="HandleOnCopied">
    Click Me
</TailClipboard>

@code {
    private void HandleOnCopied()
    {
        // Handle the event
        Console.WriteLine("Event triggered");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailClipboard Text="Sample Text" Style="Sample Style">
    Combined Parameters
</TailClipboard>
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
    <TailClipboard OnCopied="HandleAction">
        Action Button
    </TailClipboard>
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
| **Text** | `string?` | - | Text parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnCopied** | `EventCallback` | OnCopied callback |

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
