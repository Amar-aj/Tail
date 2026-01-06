# Tail.Blazor.ToastContainer

Independent NuGet package for the TailToastContainer component.

## Installation

```bash
dotnet add package Tail.Blazor.ToastContainer
```

## Features

- Toast container with positioning
- 6 positions (TopLeft, TopRight, TopCenter, BottomLeft, BottomRight, BottomCenter)
- Max toasts limit
- Programmatic toast display
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ToastContainer;
```

## Component Usage

```razor
<TailToastContainer></TailToastContainer>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Position** | `ToastPosition` | ToastPosition.TopRight | Position parameter |
| **MaxToasts** | `int` | 5 | Maximum value constraint |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Enums

### ToastPosition

```csharp
public enum ToastPosition
{
    TopLeft,
    TopRight,
    TopCenter,
    BottomLeft,
    BottomRight,
}
```

/// Toast position options.
///

### Tail.Blazor.ToastContainer;.ToastPosition

```csharp
public enum Tail.Blazor.ToastContainer;.ToastPosition
{
    TopLeft,
    TopRight,
    TopCenter,
    BottomLeft,
    BottomRight,
}
```

/// Toast position options.
///

### ToastVariant

```csharp
public enum ToastVariant
{
    Success,
    Warning,
    Error,
}
```

/// Toast variant styles.
///

### Tail.Blazor.ToastContainer;.ToastVariant

```csharp
public enum Tail.Blazor.ToastContainer;.ToastVariant
{
    Success,
    Warning,
    Error,
}
```

/// Toast variant styles.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ToastContainer

<TailToastContainer />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailToastContainer />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailToastContainer MaxToasts="10" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailToastContainer Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailToastContainer>

@* Using Class parameter *@
<TailToastContainer Class="my-custom-class shadow-lg">
    With Custom Class
</TailToastContainer>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailToastContainer  />
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

- **Package ID**: `Tail.Blazor.ToastContainer`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
