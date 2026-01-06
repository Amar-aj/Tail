# Tail.Blazor.Core.Theme



## Installation

```bash
dotnet add package Tail.Blazor.Core.Theme
```

## Features

- Rich Core.Theme component

## Namespace

```csharp
using Tail.Blazor.Core.Theme;
```

## Component Usage

```razor
<TailCore.Theme></TailCore.Theme>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ShowModeToggle** | `bool` | true | ShowModeToggle parameter |
| **ShowThemeSelector** | `bool` | true | ShowThemeSelector parameter |
| **ShowThemeName** | `bool` | false | ShowThemeName parameter |
| **Style** | `DisplayStyle` | DisplayStyle.Inline | Additional CSS styles |

## Events

No events exposed.

## Enums

### ThemeMode

```csharp
public enum ThemeMode
{
    Light,
    Dark,
}
```

ThemeMode enum

### Tail.Blazor.Core.Theme;.ThemeMode

```csharp
public enum Tail.Blazor.Core.Theme;.ThemeMode
{
    Light,
    Dark,
}
```

ThemeMode enum

### ThemePalette

```csharp
public enum ThemePalette
{
    Default,
    Blue,
    Green,
    Purple,
    Red,
}
```

ThemePalette enum

### Tail.Blazor.Core.Theme;.ThemePalette

```csharp
public enum Tail.Blazor.Core.Theme;.ThemePalette
{
    Default,
    Blue,
    Green,
    Purple,
    Red,
}
```

ThemePalette enum

### ThemeToggleStyle

```csharp
public enum ThemeToggleStyle
{
    Icon,
    Button,
}
```

/// Style options for the theme toggle button.
///

### Tail.Blazor.Core.Theme;.ThemeToggleStyle

```csharp
public enum Tail.Blazor.Core.Theme;.ThemeToggleStyle
{
    Icon,
    Button,
}
```

/// Style options for the theme toggle button.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Core.Theme

<TailCore.Theme />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailCore.Theme />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailCore.Theme ShowModeToggle="true" ShowThemeSelector="true" ShowThemeName="true" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailCore.Theme Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailCore.Theme>

@* Using Class parameter *@
<TailCore.Theme Class="my-custom-class shadow-lg">
    With Custom Class
</TailCore.Theme>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailCore.Theme  />
</div>

@code {
    // Component logic here
}
```

## Base Class

The component inherits from `Tail.Blazor.Core.TailComponentBase` (from `Tail.Blazor.Core.Base`), which provides:

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
- `Microsoft.Extensions.DependencyInjection.Abstractions`
- `Microsoft.Extensions.DependencyInjection.Abstractions`
- `Microsoft.Extensions.DependencyInjection.Abstractions`

## Target Frameworks

- .NET 8
- .NET 9
- .NET 10

## Package Information

- **Package ID**: `Tail.Blazor.Core.Theme`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
