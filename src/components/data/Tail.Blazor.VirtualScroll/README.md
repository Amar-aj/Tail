# Tail.Blazor.VirtualScroll

Independent NuGet package for the TailVirtualScroll component.

## Installation

```bash
dotnet add package Tail.Blazor.VirtualScroll
```

## Features

- Virtual scrolling for large lists
- Performance optimization
- Customizable item height
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.VirtualScroll;
```

## Component Usage

```razor
<TailVirtualScroll></TailVirtualScroll>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Items** | `List<T>` | new() | Data items collection |
| **ItemTemplate** | `RenderFragment<T>` | default! | ItemTemplate parameter |
| **ItemHeight** | `int` | 50 | ItemHeight parameter |
| **VisibleCount** | `int` | 10 | Whether the component is visible |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.VirtualScroll

<TailVirtualScroll>
    Hello, World!
</TailVirtualScroll>
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailVirtualScroll T="YourModel">Content</TailVirtualScroll>
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailVirtualScroll ItemHeight="10" VisibleCount="10" Style="Sample Style">
    Combined Parameters
</TailVirtualScroll>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailVirtualScroll Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailVirtualScroll>

@* Using Class parameter *@
<TailVirtualScroll Class="my-custom-class shadow-lg">
    With Custom Class
</TailVirtualScroll>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailVirtualScroll >
        Action Button
    </TailVirtualScroll>
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

- **Package ID**: `Tail.Blazor.VirtualScroll`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
