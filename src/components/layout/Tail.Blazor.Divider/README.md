# Tail.Blazor.Divider

Independent NuGet package for the TailDivider component.

## Installation

```bash
dotnet add package Tail.Blazor.Divider
```

## Features

- Divider with optional text
- Horizontal/vertical orientation
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Divider;
```

## Component Usage

```razor
<TailDivider></TailDivider>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Text** | `string?` | - | Text parameter |
| **Orientation** | `DividerOrientation` | DividerOrientation.Horizontal | Orientation parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Enums

### DividerOrientation

```csharp
public enum DividerOrientation
{
    Horizontal,
}
```

/// Divider orientation.
///

### Tail.Blazor.Divider;.DividerOrientation

```csharp
public enum Tail.Blazor.Divider;.DividerOrientation
{
    Horizontal,
}
```

/// Divider orientation.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Divider

<TailDivider />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailDivider />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailDivider Text="Sample Text" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailDivider Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailDivider>

@* Using Class parameter *@
<TailDivider Class="my-custom-class shadow-lg">
    With Custom Class
</TailDivider>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailDivider  />
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

- **Package ID**: `Tail.Blazor.Divider`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
