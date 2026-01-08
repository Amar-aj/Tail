---
title: LengthValidator
package: Tail.Blazor.LengthValidator
category: validators
namespace: Tail.Blazor.LengthValidator
route: /components/validators/lengthvalidator
is_generic: false
is_missing: false
---

# LengthValidator

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

## Basic Usage

```razor
<TailLengthValidator />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.LengthValidator

<TailLengthValidator />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailLengthValidator Value="Sample Value" MinLength="10" MaxLength="10" ErrorMessage="Sample ErrorMessage" Style="Sample Style" />
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
    <TailLengthValidator  />
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
| **MinLength** | `int?` | - | Minimum value constraint |
| **MaxLength** | `int?` | - | Maximum value constraint |
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
