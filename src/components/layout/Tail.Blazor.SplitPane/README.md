# Tail.Blazor.SplitPane

Independent NuGet package for the TailSplitPane component.

## Installation

```bash
dotnet add package Tail.Blazor.SplitPane
```

## Features

- Split pane layout
- Resizable panes
- Customizable split percentage
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.SplitPane;
```

## Component Usage

```razor
<TailSplitPane></TailSplitPane>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Pane1** | `RenderFragment?` | - | Pane1 parameter |
| **Pane2** | `RenderFragment?` | - | Pane2 parameter |
| **SplitPercentage** | `int` | 50 | SplitPercentage parameter |
| **Resizable** | `bool` | true | Resizable parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.SplitPane

<TailSplitPane>
    Hello, World!
</TailSplitPane>
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailSplitPane>Content</TailSplitPane>
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailSplitPane SplitPercentage="10" Resizable="true" Style="Sample Style">
    Combined Parameters
</TailSplitPane>
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailSplitPane Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailSplitPane>

@* Using Class parameter *@
<TailSplitPane Class="my-custom-class shadow-lg">
    With Custom Class
</TailSplitPane>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailSplitPane >
        Action Button
    </TailSplitPane>
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

- **Package ID**: `Tail.Blazor.SplitPane`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
