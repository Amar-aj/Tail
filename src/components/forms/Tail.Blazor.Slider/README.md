# Tail.Blazor.Slider

Independent NuGet package for the TailSlider component.

## Installation

```bash
dotnet add package Tail.Blazor.Slider
```

## Usage

```razor
@using Tail.Blazor.Slider

<TailSlider @bind-Value="value" Min="0" Max="100" Step="1" Label="Volume" ShowValue="true" />
```

## Features

- Range input with min/max/step
- 3 sizes (Sm, Md, Lg)
- 4 variants (Primary, Success, Warning, Danger)
- Label support
- Value display
- Min/max labels
- Help text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

