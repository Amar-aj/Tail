# Tail.Blazor.Tabs

Independent NuGet package for the TailTabs component.

## Installation

```bash
dotnet add package Tail.Blazor.Tabs
```

## Features

- Tab navigation
- 3 variants (Default, Pills, Underline)
- Active tab highlighting
- Disabled tab support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Tabs;
```

## Component Usage

```razor
<TailTabs></TailTabs>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Parent** | `private TailTabs?` | - | Parent parameter |
| **Title** | `string?` | - | Title parameter |
| **Label** | `string?` | - | Label text for the component |
| **Icon** | `RenderFragment?` | - | Icon to display |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Badge** | `string?` | - | Badge parameter |
| **Count** | `int?` | - | Count parameter |

## Events

No events exposed.

## Enums

### TabsVariant

```csharp
public enum TabsVariant
{
    Default,
    Pills,
    Underline,
    Enclosed,
}
```

/// Tabs variant styles.
///

### Tail.Blazor.Tabs;.TabsVariant

```csharp
public enum Tail.Blazor.Tabs;.TabsVariant
{
    Default,
    Pills,
    Underline,
    Enclosed,
}
```

/// Tabs variant styles.
///

### TabsPosition

```csharp
public enum TabsPosition
{
    Top,
    Bottom,
    Left,
}
```

/// Tabs position.
///

### Tail.Blazor.Tabs;.TabsPosition

```csharp
public enum Tail.Blazor.Tabs;.TabsPosition
{
    Top,
    Bottom,
    Left,
}
```

/// Tabs position.
///

### TabsSize

```csharp
public enum TabsSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Tabs size.
///

### Tail.Blazor.Tabs;.TabsSize

```csharp
public enum Tail.Blazor.Tabs;.TabsSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Tabs size.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Tabs

<TailTabs>
    Hello, World!
</TailTabs>
```

### Common Patterns

Frequently used patterns and combinations:

**Disabled State**

```razor
<TailTabs Disabled="true">
    Disabled
</TailTabs>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailTabs>Content</TailTabs>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailTabs Disabled="true">Disabled</TailTabs>

```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailTabs Title="Sample Title" Label="Sample Label">
    Combined Parameters
</TailTabs>
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailTabs Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailTabs>

@code {
    private void ToggleProcessing()
    {
        isProcessing = !isProcessing;
        isDisabled = isProcessing;
    }
}
```

#### Accessibility

```razor
@* Accessible component with ARIA label and tooltip *@
<TailTabs Label="Primary action button">
    Accessible Button
</TailTabs>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailTabs >
        Action Button
    </TailTabs>
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

- **Package ID**: `Tail.Blazor.Tabs`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
