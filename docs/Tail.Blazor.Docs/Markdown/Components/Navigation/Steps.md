---
title: Steps
package: Tail.Blazor.Steps
category: navigation
namespace: Tail.Blazor.Steps
route: /components/navigation/steps
is_generic: false
is_missing: false
---

# Steps

Independent NuGet package for the TailSteps component.

## Installation

```bash
dotnet add package Tail.Blazor.Steps
```

## Features

- Step indicator
- Active step highlighting
- Completed step checkmarks
- Connector lines
- Title and description support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Steps;
```

## Basic Usage

```razor
<TailSteps />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Steps

<TailSteps />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailSteps CurrentStep="10" Style="Sample Style" />
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
    <TailSteps  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Steps** | `List<StepItem>` | new() | Step value for numeric inputs |
| **CurrentStep** | `int` | 1 | Step value for numeric inputs |
| **Style** | `string?` | - | Additional CSS styles |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `StepItem` | `class` | StepItem property |
| `Title` | `string` | Title property |
| `Description` | `string?` | Description property |

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
