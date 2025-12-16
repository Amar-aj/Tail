# Tail.Blazor.Tour

Independent NuGet package for the TailTour component.

## Installation

```bash
dotnet add package Tail.Blazor.Tour
```

## Usage

```razor
@using Tail.Blazor.Tour

<TailTour Steps="@tourSteps" IsActive="@showTour" OnTourComplete="HandleTourComplete" />
```

## Features

- Interactive tour/walkthrough
- Step-by-step navigation
- Spotlight overlay
- Custom tooltip placement
- Previous/Next navigation
- Finish tour callback
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~5 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

