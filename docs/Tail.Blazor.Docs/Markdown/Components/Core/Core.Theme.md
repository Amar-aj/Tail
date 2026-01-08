---
title: Core.Theme
package: Tail.Blazor.Core.Theme
category: core
namespace: Tail.Blazor.Core.Theme
route: /components/core/core.theme
is_generic: false
is_missing: false
---

# Core.Theme



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

## Basic Usage

```razor
<TailCore.Theme />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Core.Theme

<TailCore.Theme />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailCore.Theme ShowModeToggle="true" ShowThemeSelector="true" ShowThemeName="true" />
```

## Advanced Examples

More complex usage scenarios:

More complex usage scenarios:

##

## Real-World Example

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

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ShowModeToggle** | `bool` | true | ShowModeToggle parameter |
| **ShowThemeSelector** | `bool` | true | ShowThemeSelector parameter |
| **ShowThemeName** | `bool` | false | ShowThemeName parameter |
| **Style** | `DisplayStyle` | DisplayStyle.Inline | Additional CSS styles |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `Dispose` | `void` | Dispose property |
| `DisplayStyle` | `enum` | DisplayStyle property |

### Enums

#### ThemeMode

```csharp
public enum ThemeMode
{
    Light,
    Dark,
}
```

ThemeMode enum

#### Tail.Blazor.Core.Theme;.ThemeMode

```csharp
public enum Tail.Blazor.Core.Theme;.ThemeMode
{
    Light,
    Dark,
}
```

ThemeMode enum

#### ThemePalette

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

#### Tail.Blazor.Core.Theme;.ThemePalette

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

#### ThemeToggleStyle

```csharp
public enum ThemeToggleStyle
{
    Icon,
    Button,
}
```

/// Style options for the theme toggle button.
///

#### Tail.Blazor.Core.Theme;.ThemeToggleStyle

```csharp
public enum Tail.Blazor.Core.Theme;.ThemeToggleStyle
{
    Icon,
    Button,
}
```

/// Style options for the theme toggle button.
///

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
