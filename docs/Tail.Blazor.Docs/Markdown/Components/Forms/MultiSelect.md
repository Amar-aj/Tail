---
title: MultiSelect
package: Tail.Blazor.MultiSelect
category: forms
namespace: Tail.Blazor.MultiSelect
route: /components/forms/multiselect
is_generic: false
is_missing: false
---

# MultiSelect

Independent NuGet package for the TailMultiSelect component.

## Installation

```bash
dotnet add package Tail.Blazor.MultiSelect
```

## Features

- Multi-selection dropdown
- Tag display for selected items
- Search functionality (can be added)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Validation error display
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.MultiSelect;
```

## Basic Usage

```razor
<TailMultiSelect />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.MultiSelect

<TailMultiSelect />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailMultiSelect Size="MultiSelectSize.Md">
    Medium Size
</TailMultiSelect>
```

**With Click Handler**

```razor
<TailMultiSelect SelectedValuesChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailMultiSelect>
```

**Disabled State**

```razor
<TailMultiSelect Disabled="true">
    Disabled
</TailMultiSelect>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailMultiSelect Size="MultiSelectSize.Xs">Xs</TailMultiSelect>
<TailMultiSelect Size="MultiSelectSize.Sm">Sm</TailMultiSelect>
<TailMultiSelect Size="MultiSelectSize.Md">Md</TailMultiSelect>
<TailMultiSelect Size="MultiSelectSize.Lg">Lg</TailMultiSelect>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailMultiSelect Disabled="true">Disabled</TailMultiSelect>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailMultiSelect SelectedValuesChanged="HandleSelectedValuesChanged">
    Click Me
</TailMultiSelect>

@code {
    private void HandleSelectedValuesChanged(Tail.Blazor.MultiSelect.List<string> args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailMultiSelect Size="MultiSelectSize.Sm" SelectedValues="Sample SelectedValues" Label="Sample Label" Placeholder="Sample Placeholder" />
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
    <TailMultiSelect Size="MultiSelectSize.Sm" SelectedValuesChanged="HandleAction" />
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
| **SelectedValues** | `List<string>?` | - | Current value of the component |
| **Items** | `List<MultiSelectItem>?` | - | Data items collection |
| **Size** | `MultiSelectSize` | MultiSelectSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **SelectedValuesChanged** | `EventCallback<List<string>>` | Raised when value changes |

### Enums

#### MultiSelectSize

```csharp
public enum MultiSelectSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// MultiSelect size options.
///

#### Tail.Blazor.MultiSelect;.MultiSelectSize

```csharp
public enum Tail.Blazor.MultiSelect;.MultiSelectSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// MultiSelect size options.
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
