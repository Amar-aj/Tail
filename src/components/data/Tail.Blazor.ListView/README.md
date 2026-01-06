# Tail.Blazor.ListView

Independent NuGet package for the TailListView component.

## Installation

```bash
dotnet add package Tail.Blazor.ListView
```

## Features

- List view with items
- Custom item template
- Hover effects
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ListView;
```

## Component Usage

```razor
<TailListView></TailListView>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Items** | `List<T>` | new() | Data items collection |
| **ItemTemplate** | `RenderFragment<T>` | default! | ItemTemplate parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.ListView

<TailListView>
    Hello, World!
</TailListView>
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailListView T="YourModel">Content</TailListView>
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailListView Style="Sample Style">
    Combined Parameters
</TailListView>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailListView Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailListView>

@* Using Class parameter *@
<TailListView Class="my-custom-class shadow-lg">
    With Custom Class
</TailListView>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailListView >
        Action Button
    </TailListView>
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

- **Package ID**: `Tail.Blazor.ListView`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
