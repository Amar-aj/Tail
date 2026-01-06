# Tail.Blazor.LengthValidator

Independent NuGet package for the TailLengthValidator component.

## Installation

```bash
dotnet add package Tail.Blazor.LengthValidator
```

## Features

- Length validation
- Min/max length constraints
- Custom error message
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.LengthValidator;
```

## Component Usage

```razor
<TailLengthValidator></TailLengthValidator>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string?` | - | Current value of the component |
| **MinLength** | `int?` | - | Minimum value constraint |
| **MaxLength** | `int?` | - | Maximum value constraint |
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
@using Tail.Blazor.LengthValidator

<TailLengthValidator />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailLengthValidator />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailLengthValidator Value="Sample Value" MinLength="10" MaxLength="10" ErrorMessage="Sample ErrorMessage" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailLengthValidator Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailLengthValidator>

@* Using Class parameter *@
<TailLengthValidator Class="my-custom-class shadow-lg">
    With Custom Class
</TailLengthValidator>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailLengthValidator  />
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

- **Package ID**: `Tail.Blazor.LengthValidator`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
