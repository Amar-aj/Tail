---
title: TagInput
package: Tail.Blazor.TagInput
category: forms
namespace: Tail.Blazor.TagInput
route: /components/forms/taginput
is_generic: false
is_missing: false
---

# TagInput

Independent NuGet package for the TailTagInput component.

## Installation

```bash
dotnet add package Tail.Blazor.TagInput
```

## Features

- Tag input with add/remove functionality
- Enter to add tag
- Backspace to remove last tag
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Help text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.TagInput;
```

## Basic Usage

```razor
<TailTagInput />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.TagInput

<TailTagInput />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailTagInput Size="TagInputSize.Md">
    Medium Size
</TailTagInput>
```

**With Click Handler**

```razor
<TailTagInput TagsChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailTagInput>
```

**Disabled State**

```razor
<TailTagInput Disabled="true">
    Disabled
</TailTagInput>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailTagInput Size="TagInputSize.Xs">Xs</TailTagInput>
<TailTagInput Size="TagInputSize.Sm">Sm</TailTagInput>
<TailTagInput Size="TagInputSize.Md">Md</TailTagInput>
<TailTagInput Size="TagInputSize.Lg">Lg</TailTagInput>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailTagInput Disabled="true">Disabled</TailTagInput>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailTagInput TagsChanged="HandleTagsChanged">
    Click Me
</TailTagInput>

@code {
    private void HandleTagsChanged(Tail.Blazor.TagInput.List<string> args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailTagInput Size="TagInputSize.Sm" Tags="Sample Tags" Label="Sample Label" Placeholder="Sample Placeholder" HelpText="Sample HelpText" />
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
    <TailTagInput Size="TagInputSize.Sm" TagsChanged="HandleAction" />
</div>

@code {
    private void HandleAction(List<string> args)
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
| **Tags** | `List<string>` | new() | Tags parameter |
| **Size** | `TagInputSize` | TagInputSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **HelpText** | `string?` | - | HelpText parameter |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **TagsChanged** | `EventCallback<List<string>>` | Raised when value changes |

### Enums

#### TagInputSize

```csharp
public enum TagInputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// TagInput size options.
///

#### Tail.Blazor.TagInput;.TagInputSize

```csharp
public enum Tail.Blazor.TagInput;.TagInputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// TagInput size options.
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
