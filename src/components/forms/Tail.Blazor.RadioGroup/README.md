# Tail.Blazor.RadioGroup

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

## Component Usage

```razor
<TailRadioGroup></TailRadioGroup>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Label** | `string?` | - | Label text for the component |
| **HelpText** | `string?` | - | HelpText parameter |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Orientation** | `RadioGroupOrientation` | RadioGroupOrientation.Vertical | Orientation parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Enums

### RadioGroupOrientation

```csharp
public enum RadioGroupOrientation
{
    Vertical,
}
```

/// Radio group orientation options.
///

### Tail.Blazor.RadioGroup;.RadioGroupOrientation

```csharp
public enum Tail.Blazor.RadioGroup;.RadioGroupOrientation
{
    Vertical,
}
```

/// Radio group orientation options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.RadioGroup

<TailRadioGroup>
    Hello, World!
</TailRadioGroup>
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailRadioGroup>Content</TailRadioGroup>
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailRadioGroup Label="Sample Label" HelpText="Sample HelpText" ErrorMessage="Sample ErrorMessage" Required="true">
    Combined Parameters
</TailRadioGroup>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailRadioGroup Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailRadioGroup>

@* Using Class parameter *@
<TailRadioGroup Class="my-custom-class shadow-lg">
    With Custom Class
</TailRadioGroup>
```

#### Accessibility

```razor
@* Accessible component with ARIA label and tooltip *@
<TailRadioGroup Label="Primary action button">
    Accessible Button
</TailRadioGroup>
```

### Real-World Example

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

- **Package ID**: `Tail.Blazor.RadioGroup`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
