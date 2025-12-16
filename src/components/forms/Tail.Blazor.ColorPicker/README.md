# Tail.Blazor.ColorPicker

Independent NuGet package for the TailColorPicker component.

## Installation

```bash
dotnet add package Tail.Blazor.ColorPicker
```

## Usage

```razor
@using Tail.Blazor.ColorPicker

<TailColorPicker @bind-Value="selectedColor" Label="Choose Color" ShowPreview="true" />
```

## Features

- Color picker with visual selector
- Hex color input
- Color preview
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Help text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~4 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

