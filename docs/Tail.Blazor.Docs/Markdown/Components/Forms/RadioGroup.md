---
title: RadioGroup
package: Tail.Blazor.RadioGroup
category: forms
namespace: Tail.Blazor.RadioGroup
route: /components/forms/radiogroup
is_generic: false
is_missing: false
---

# RadioGroup

Independent NuGet package for the TailRadioGroup component.

## Installation

```bash
dotnet add package Tail.Blazor.RadioGroup
```

## Features

- Radio button grouping
- Vertical and horizontal orientations
- Label support
- Help text support
- Validation error display
- Required field indicator
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.RadioGroup;
```

## Basic Usage

```razor
<TailRadioGroup>Content</TailRadioGroup>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.RadioGroup

<TailRadioGroup>
    Hello, World!
</TailRadioGroup>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailRadioGroup Label="Sample Label" HelpText="Sample HelpText" ErrorMessage="Sample ErrorMessage" Required="true">
    Combined Parameters
</TailRadioGroup>
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
    <TailRadioGroup >
        Action Button
    </TailRadioGroup>
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Label** | `string?` | - | Label text for the component |
| **HelpText** | `string?` | - | HelpText parameter |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Orientation** | `RadioGroupOrientation` | RadioGroupOrientation.Vertical | Orientation parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Enums

#### RadioGroupOrientation

```csharp
public enum RadioGroupOrientation
{
    Vertical,
}
```

/// Radio group orientation options.
///

#### Tail.Blazor.RadioGroup;.RadioGroupOrientation

```csharp
public enum Tail.Blazor.RadioGroup;.RadioGroupOrientation
{
    Vertical,
}
```

/// Radio group orientation options.
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
