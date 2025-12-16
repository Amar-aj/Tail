# Tail.Blazor.TimePicker

Independent NuGet package for the TailTimePicker component.

## Installation

```bash
dotnet add package Tail.Blazor.TimePicker
```

## Usage

```razor
@using Tail.Blazor.TimePicker

<TailTimePicker @bind-Value="selectedTime" Label="Select Time" />
```

## Features

- Time input with picker
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Validation error display
- Required field indicator
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~6 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

