# Tail.Blazor.DatePicker

Independent NuGet package for the TailDatePicker component.

## Installation

```bash
dotnet add package Tail.Blazor.DatePicker
```

## Usage

```razor
@using Tail.Blazor.DatePicker

<TailDatePicker @bind-Value="selectedDate" Label="Select Date" MinDate="@DateTime.Today" />
```

## Features

- Date input with calendar picker
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Min/max date constraints
- Label and help text support
- Icon support
- Validation error display
- Required field indicator
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~8 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

