# Tail.Blazor.DockingLayout

Independent NuGet package for the TailDockingLayout component.

## Installation

```bash
dotnet add package Tail.Blazor.DockingLayout
```

## Features

- Docking layout with 5 zones
- Top, Left, Center, Right, Bottom panels
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.DockingLayout;
```

## Component Usage

```razor
<TailDockingLayout></TailDockingLayout>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Top** | `RenderFragment?` | - | Top parameter |
| **Left** | `RenderFragment?` | - | Left parameter |
| **Center** | `RenderFragment?` | - | Center parameter |
| **Right** | `RenderFragment?` | - | Right parameter |
| **Bottom** | `RenderFragment?` | - | Bottom parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.DockingLayout

<TailDockingLayout>
    Hello, World!
</TailDockingLayout>
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailDockingLayout>Content</TailDockingLayout>
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailDockingLayout>
    Content
</TailDockingLayout>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailDockingLayout Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailDockingLayout>

@* Using Class parameter *@
<TailDockingLayout Class="my-custom-class shadow-lg">
    With Custom Class
</TailDockingLayout>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailDockingLayout >
        Action Button
    </TailDockingLayout>
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

- **Package ID**: `Tail.Blazor.DockingLayout`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
