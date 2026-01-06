# Tail.Blazor.Steps

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

## Component Usage

```razor
<TailSteps></TailSteps>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Steps** | `List<StepItem>` | new() | Step value for numeric inputs |
| **CurrentStep** | `int` | 1 | Step value for numeric inputs |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Steps

<TailSteps />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailSteps />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailSteps CurrentStep="10" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailSteps Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailSteps>

@* Using Class parameter *@
<TailSteps Class="my-custom-class shadow-lg">
    With Custom Class
</TailSteps>
```

### Real-World Example

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

- **Package ID**: `Tail.Blazor.Steps`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
