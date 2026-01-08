---
title: NumericRangeValidator
package: Tail.Blazor.NumericRangeValidator
category: validators
namespace: Tail.Blazor.NumericRangeValidator
route: /components/validators/numericrangevalidator
is_generic: false
is_missing: false
---

# NumericRangeValidator

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

## Basic Usage

```razor
<TailNumericRangeValidator />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.NumericRangeValidator

<TailNumericRangeValidator />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailNumericRangeValidator Value="10" Min="10" Max="10" ErrorMessage="Sample ErrorMessage" Style="Sample Style" />
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
    <TailNumericRangeValidator  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `int?` | - | Current value of the component |
| **Min** | `int` | - | Minimum value constraint |
| **Max** | `int` | - | Maximum value constraint |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Style** | `string?` | - | Additional CSS styles |

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
