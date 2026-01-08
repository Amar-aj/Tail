---
title: RequiredValidator
package: Tail.Blazor.RequiredValidator
category: validators
namespace: Tail.Blazor.RequiredValidator
route: /components/validators/requiredvalidator
is_generic: false
is_missing: false
---

# RequiredValidator

Independent NuGet package for the TailRequiredValidator component.

## Installation

```bash
dotnet add package Tail.Blazor.RequiredValidator
```

## Features

- Required field validation
- Custom error message
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.RequiredValidator;
```

## Basic Usage

```razor
<TailRequiredValidator />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.RequiredValidator

<TailRequiredValidator />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailRequiredValidator Value="Sample Value" ErrorMessage="Sample ErrorMessage" Style="Sample Style" />
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
    <TailRequiredValidator  />
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
