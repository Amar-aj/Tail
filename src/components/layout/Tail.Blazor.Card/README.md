# Tail.Blazor.Card

Independent NuGet package for the TailCard component.

## Installation

```bash
dotnet add package Tail.Blazor.Card
```

## Features

- Card with header/footer
- Hoverable option
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Card;
```

## Component Usage

```razor
<TailCard></TailCard>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Header** | `RenderFragment?` | - | Header parameter |
| **Footer** | `RenderFragment?` | - | Footer parameter |
| **Hoverable** | `bool` | - | Hoverable parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Card

<TailCard>
    Hello, World!
</TailCard>
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailCard>Content</TailCard>
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailCard Hoverable="true" Style="Sample Style">
    Combined Parameters
</TailCard>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailCard Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailCard>

@* Using Class parameter *@
<TailCard Class="my-custom-class shadow-lg">
    With Custom Class
</TailCard>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailCard >
        Action Button
    </TailCard>
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

- **Package ID**: `Tail.Blazor.Card`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
