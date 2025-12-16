# Tail.Blazor.ToastContainer

Independent NuGet package for the TailToastContainer component.

## Installation

```bash
dotnet add package Tail.Blazor.ToastContainer
```

## Usage

```razor
@using Tail.Blazor.ToastContainer

<TailToastContainer @ref="toastContainer" Position="ToastPosition.TopRight" />
```

## Features

- Toast container with positioning
- 6 positions (TopLeft, TopRight, TopCenter, BottomLeft, BottomRight, BottomCenter)
- Max toasts limit
- Programmatic toast display
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

