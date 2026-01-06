# Tail.Blazor.EmptyState

Independent NuGet package for the TailEmptyState component.

## Installation

```bash
dotnet add package Tail.Blazor.EmptyState
```

## Features

- Empty state display
- 3 sizes (Sm, Md, Lg)
- 3 variants (Default, Minimal, Detailed)
- Custom icon support
- Title and description
- Action button support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.EmptyState;
```

## Component Usage

```razor
<TailEmptyState></TailEmptyState>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **Icon** | `RenderFragment?` | - | Icon to display |
| **Action** | `RenderFragment?` | - | Action parameter |
| **Title** | `string?` | - | Title parameter |
| **Description** | `string?` | - | Description parameter |
| **Size** | `EmptyStateSize` | EmptyStateSize.Md | Size of the component |
| **Variant** | `EmptyStateVariant` | EmptyStateVariant.Default | Visual variant style for the component |
| **ShowDefaultIcon** | `bool` | true | Icon to display |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Enums

### EmptyStateSize

```csharp
public enum EmptyStateSize
{
    Sm,
    Md,
}
```

/// Empty state size.
///

### Tail.Blazor.EmptyState;.EmptyStateSize

```csharp
public enum Tail.Blazor.EmptyState;.EmptyStateSize
{
    Sm,
    Md,
}
```

/// Empty state size.
///

### EmptyStateVariant

```csharp
public enum EmptyStateVariant
{
    Default,
    Minimal,
}
```

/// Empty state variant.
///

### Tail.Blazor.EmptyState;.EmptyStateVariant

```csharp
public enum Tail.Blazor.EmptyState;.EmptyStateVariant
{
    Default,
    Minimal,
}
```

/// Empty state variant.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.EmptyState

<TailEmptyState>
    Hello, World!
</TailEmptyState>
```

### Common Patterns

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailEmptyState Variant="EmptyStateVariant.Default">
    Primary Action
</TailEmptyState>
```

**Medium Size**

```razor
<TailEmptyState Size="EmptyStateSize.Sm">
    Medium Size
</TailEmptyState>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailEmptyState>Content</TailEmptyState>
```

### Variants

Different visual variants for various use cases:

```razor
<TailEmptyState Variant="EmptyStateVariant.Default">Default</TailEmptyState>
<TailEmptyState Variant="EmptyStateVariant.Minimal">Minimal</TailEmptyState>
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailEmptyState Size="EmptyStateSize.Sm">Sm</TailEmptyState>
<TailEmptyState Size="EmptyStateSize.Md">Md</TailEmptyState>
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailEmptyState Variant="EmptyStateVariant.Default" Size="EmptyStateSize.Md" Title="Sample Title" Description="Sample Description">
    Combined Parameters
</TailEmptyState>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailEmptyState Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailEmptyState>

@* Using Class parameter *@
<TailEmptyState Class="my-custom-class shadow-lg">
    With Custom Class
</TailEmptyState>
```

#### Accessibility

```razor
@* Accessible component with ARIA label and tooltip *@
<TailEmptyState Variant="Primary action button">
    Accessible Button
</TailEmptyState>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailEmptyState Variant="EmptyStateVariant.Default" Size="EmptyStateSize.Md">
        Action Button
    </TailEmptyState>
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

- **Package ID**: `Tail.Blazor.EmptyState`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
