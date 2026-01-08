---
title: RichTextEditor
package: Tail.Blazor.RichTextEditor
category: forms
namespace: Tail.Blazor.RichTextEditor
route: /components/forms/richtexteditor
is_generic: false
is_missing: false
---

# RichTextEditor

Independent NuGet package for the TailRichTextEditor component.

## Installation

```bash
dotnet add package Tail.Blazor.RichTextEditor
```

## Features

- Rich text editor with formatting toolbar
- Bold, italic, underline formatting
- Content editable area
- Customizable min height
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.RichTextEditor;
```

## Basic Usage

```razor
<TailRichTextEditor />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.RichTextEditor

<TailRichTextEditor />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailRichTextEditor Size="RichTextEditorSize.Md">
    Medium Size
</TailRichTextEditor>
```

**With Click Handler**

```razor
<TailRichTextEditor ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailRichTextEditor>
```

**Disabled State**

```razor
<TailRichTextEditor Disabled="true">
    Disabled
</TailRichTextEditor>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailRichTextEditor Size="RichTextEditorSize.Xs">Xs</TailRichTextEditor>
<TailRichTextEditor Size="RichTextEditorSize.Sm">Sm</TailRichTextEditor>
<TailRichTextEditor Size="RichTextEditorSize.Md">Md</TailRichTextEditor>
<TailRichTextEditor Size="RichTextEditorSize.Lg">Lg</TailRichTextEditor>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailRichTextEditor Disabled="true">Disabled</TailRichTextEditor>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailRichTextEditor ValueChanged="HandleValueChanged">
    Click Me
</TailRichTextEditor>

@code {
    private void HandleValueChanged(string? args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailRichTextEditor Size="RichTextEditorSize.Sm" Value="Sample Value" Label="Sample Label" MinHeight="10" />
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
    <TailRichTextEditor Size="RichTextEditorSize.Sm" ValueChanged="HandleAction" />
</div>

@code {
    private void HandleAction(string? args)
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
| **Value** | `string?` | - | Current value of the component |
| **Size** | `RichTextEditorSize` | RichTextEditorSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **MinHeight** | `int` | 200 | Minimum value constraint |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |

### Enums

#### RichTextEditorSize

```csharp
public enum RichTextEditorSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// RichTextEditor size options.
///

#### Tail.Blazor.RichTextEditor;.RichTextEditorSize

```csharp
public enum Tail.Blazor.RichTextEditor;.RichTextEditorSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// RichTextEditor size options.
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
