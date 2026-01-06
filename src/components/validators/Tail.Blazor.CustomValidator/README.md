# Tail.Blazor.CustomValidator

Independent NuGet package for the TailCustomValidator component.

## Installation

```bash
dotnet add package Tail.Blazor.CustomValidator
```

## Features

- Custom validation logic
- Manual validation control
- Custom error message
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.CustomValidator;
```

## Component Usage

```razor
<TailCustomValidator></TailCustomValidator>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **IsValid** | `bool` | true | IsValid parameter |
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
@using Tail.Blazor.CustomValidator

<TailCustomValidator />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailCustomValidator />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailCustomValidator IsValid="true" ErrorMessage="Sample ErrorMessage" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailCustomValidator Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailCustomValidator>

@* Using Class parameter *@
<TailCustomValidator Class="my-custom-class shadow-lg">
    With Custom Class
</TailCustomValidator>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailCustomValidator  />
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

- **Package ID**: `Tail.Blazor.CustomValidator`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
