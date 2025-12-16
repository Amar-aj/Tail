# Tail.Blazor.Chart

Independent NuGet package for the TailChart component.

## Installation

```bash
dotnet add package Tail.Blazor.Chart
```

## Usage

```razor
@using Tail.Blazor.Chart

<TailChart Data="@chartData" ChartType="ChartType.Line" Width="400" Height="200" />
```

## Features

- Multiple chart types (Line, Bar, Area, Pie)
- SVG-based rendering
- Customizable size
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~5 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

