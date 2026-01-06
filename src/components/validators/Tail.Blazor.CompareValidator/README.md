# Tail.Blazor.CompareValidator

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

## Component Usage

```razor
<TailCompareValidator></TailCompareValidator>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string?` | - | Current value of the component |
| **CompareTo** | `string?` | - | CompareTo parameter |
| **Operator** | `CompareOperator` | CompareOperator.Equal | Operator parameter |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Enums

### CompareOperator

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

### Tail.Blazor.CompareValidator;.CompareOperator

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

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.CompareValidator

<TailCompareValidator />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailCompareValidator />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailCompareValidator Value="Sample Value" CompareTo="Sample CompareTo" ErrorMessage="Sample ErrorMessage" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailCompareValidator Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailCompareValidator>

@* Using Class parameter *@
<TailCompareValidator Class="my-custom-class shadow-lg">
    With Custom Class
</TailCompareValidator>
```

### Real-World Example

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

- **Package ID**: `Tail.Blazor.CompareValidator`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
