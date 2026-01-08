---
title: CompareValidator
package: Tail.Blazor.CompareValidator
category: validators
namespace: Tail.Blazor.CompareValidator
route: /components/validators/comparevalidator
is_generic: false
is_missing: false
---

# CompareValidator

Independent NuGet package for the TailCompareValidator component.

## Installation

```bash
dotnet add package Tail.Blazor.CompareValidator
```

## Features

- Value comparison validation
- 4 operators (Equal, NotEqual, GreaterThan, LessThan)
- Custom error message
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.CompareValidator;
```

## Basic Usage

```razor
<TailCompareValidator />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.CompareValidator

<TailCompareValidator />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailCompareValidator Value="Sample Value" CompareTo="Sample CompareTo" ErrorMessage="Sample ErrorMessage" Style="Sample Style" />
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
    <TailCompareValidator  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string?` | - | Current value of the component |
| **CompareTo** | `string?` | - | CompareTo parameter |
| **Operator** | `CompareOperator` | CompareOperator.Equal | Operator parameter |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Enums

#### CompareOperator

```csharp
public enum CompareOperator
{
    Equal,
    NotEqual,
    GreaterThan,
}
```

/// Compare operator options.
///

#### Tail.Blazor.CompareValidator;.CompareOperator

```csharp
public enum Tail.Blazor.CompareValidator;.CompareOperator
{
    Equal,
    NotEqual,
    GreaterThan,
}
```

/// Compare operator options.
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
