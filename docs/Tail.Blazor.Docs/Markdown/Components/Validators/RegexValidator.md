---
title: RegexValidator
package: Tail.Blazor.RegexValidator
category: validators
namespace: Tail.Blazor.RegexValidator
route: /components/validators/regexvalidator
is_generic: false
is_missing: false
---

# RegexValidator

Independent NuGet package for the TailRegexValidator component.

## Installation

```bash
dotnet add package Tail.Blazor.RegexValidator
```

## Features

- Regex pattern validation
- Custom error message
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.RegexValidator;
```

## Basic Usage

```razor
<TailRegexValidator />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.RegexValidator

<TailRegexValidator />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailRegexValidator Value="Sample Value" Pattern="Sample Pattern" ErrorMessage="Sample ErrorMessage" Style="Sample Style" />
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
    <TailRegexValidator  />
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
| **Pattern** | `string` | string.Empty | Validation pattern (regex) |
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
