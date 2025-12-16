# Tail.Blazor.DateRangePicker

Independent NuGet package for the TailDateRangePicker component.

## Installation

```bash
dotnet add package Tail.Blazor.DateRangePicker
```

## Usage

```razor
@using Tail.Blazor.DateRangePicker

<TailDateRangePicker @bind-StartDate="startDate" @bind-EndDate="endDate" Label="Date Range" />
```

## Features

- Date range selection (start and end dates)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Min/max date constraints
- Label support
- Validation error display
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~10 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

