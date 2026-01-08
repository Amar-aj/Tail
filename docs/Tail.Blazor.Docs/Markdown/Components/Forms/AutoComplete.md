---
title: AutoComplete
package: Tail.Blazor.AutoComplete
category: forms
namespace: Tail.Blazor.AutoComplete
route: /components/forms/autocomplete
is_generic: false
is_missing: false
---

# AutoComplete

Independent NuGet package for the TailAutoComplete component.

## Installation

```bash
dotnet add package Tail.Blazor.AutoComplete
```

## Features

- Autocomplete with suggestions dropdown
- Real-time filtering
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.AutoComplete;
```

## Basic Usage

```razor
<TailAutoComplete>Content</TailAutoComplete>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.AutoComplete

<TailAutoComplete>
    Hello, World!
</TailAutoComplete>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailAutoComplete Size="AutoCompleteSize.Md">
    Medium Size
</TailAutoComplete>
```

**With Click Handler**

```razor
<TailAutoComplete ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailAutoComplete>
```

**Disabled State**

```razor
<TailAutoComplete Disabled="true">
    Disabled
</TailAutoComplete>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailAutoComplete Size="AutoCompleteSize.Xs">Xs</TailAutoComplete>
<TailAutoComplete Size="AutoCompleteSize.Sm">Sm</TailAutoComplete>
<TailAutoComplete Size="AutoCompleteSize.Md">Md</TailAutoComplete>
<TailAutoComplete Size="AutoCompleteSize.Lg">Lg</TailAutoComplete>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailAutoComplete Disabled="true">Disabled</TailAutoComplete>

@* Loading state *@
<TailAutoComplete IsLoading="true">Loading...</TailAutoComplete>

@* Both disabled and loading *@
<TailAutoComplete Disabled="true" IsLoading="true">Processing</TailAutoComplete>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailAutoComplete ValueChanged="HandleValueChanged">
    Click Me
</TailAutoComplete>

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
<TailAutoComplete Size="AutoCompleteSize.Sm" Value="Sample Value" Items="Sample Items" Label="Sample Label" Placeholder="Sample Placeholder">
    Combined Parameters
</TailAutoComplete>
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
    <TailAutoComplete Size="AutoCompleteSize.Sm" ValueChanged="HandleAction">
        Action Button
    </TailAutoComplete>
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
| **Items** | `List<string>?` | - | Data items collection |
| **Size** | `AutoCompleteSize` | AutoCompleteSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **MinChars** | `int` | 1 | Minimum value constraint |
| **MaxItems** | `int` | 10 | Maximum value constraint |
| **IsLoading** | `bool` | - | Whether the component is in loading state |
| **ItemTemplate** | `RenderFragment<string>?` | - | ItemTemplate parameter |
| **AriaLabel** | `string?` | - | Label text for the component |
| **Tooltip** | `string?` | - | Tooltip parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |
| **OnItemSelected** | `EventCallback<string>` | Raised with string value |
| **OnSearch** | `EventCallback<string>` | Raised with string value |

### Enums

#### AutoCompleteSize

```csharp
public enum AutoCompleteSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// AutoComplete size options.
///

#### Tail.Blazor.AutoComplete;.AutoCompleteSize

```csharp
public enum Tail.Blazor.AutoComplete;.AutoCompleteSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// AutoComplete size options.
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
