# Tail.Blazor.NumericRangeValidator

Independent NuGet package for the TailNumericRangeValidator component.

## Installation

```bash
dotnet add package Tail.Blazor.NumericRangeValidator
```

## Features

- Numeric range validation
- Integer min/max constraints
- Custom error message
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.NumericRangeValidator;
```

## Component Usage

```razor
<TailNumericRangeValidator></TailNumericRangeValidator>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `int?` | - | Current value of the component |
| **Min** | `int` | - | Minimum value constraint |
| **Max** | `int` | - | Maximum value constraint |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.NumericRangeValidator

<TailNumericRangeValidator />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailNumericRangeValidator />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailNumericRangeValidator Value="10" Min="10" Max="10" ErrorMessage="Sample ErrorMessage" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailNumericRangeValidator Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailNumericRangeValidator>

@* Using Class parameter *@
<TailNumericRangeValidator Class="my-custom-class shadow-lg">
    With Custom Class
</TailNumericRangeValidator>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailNumericRangeValidator  />
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

- **Package ID**: `Tail.Blazor.NumericRangeValidator`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
