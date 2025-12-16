# Tail.Blazor.Numeric

Independent NuGet package for the TailNumeric component.

## Installation

```bash
dotnet add package Tail.Blazor.Numeric
```

## Usage

```razor
@using Tail.Blazor.Numeric

<TailNumeric @bind-Value="quantity" Min="0" Max="100" Step="1" Label="Quantity" />
```

## Features

- Numeric input with increment/decrement buttons
- Min/max constraints
- Custom step value
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

