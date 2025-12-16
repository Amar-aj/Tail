# Tail.Blazor.Rating

Independent NuGet package for the TailRating component.

## Installation

```bash
dotnet add package Tail.Blazor.Rating
```

## Usage

```razor
@using Tail.Blazor.Rating

<TailRating @bind-Value="rating" MaxRating="5" ShowValue="true" />

<TailRating @bind-Value="rating" Size="RatingSize.Lg" Color="RatingColor.Orange" />
```

## Features

- Star rating system
- Customizable max rating (default 5)
- 4 sizes (Sm, Md, Lg, Xl)
- 5 colors (Yellow, Orange, Red, Pink, Purple)
- Hover effects
- Value display
- Disabled and readonly states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~2 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

