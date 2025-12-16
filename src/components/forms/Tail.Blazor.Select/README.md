# Tail.Blazor.Select

Independent NuGet package for the TailSelect component.

## Installation

```bash
dotnet add package Tail.Blazor.Select
```

## Usage

```razor
@using Tail.Blazor.Select

<TailSelect @bind-Value="selectedValue" Label="Choose an option" Items="@items" />

<TailSelect @bind-Value="selectedValue" Label="Country">
    <option value="us">United States</option>
    <option value="uk">United Kingdom</option>
    <option value="ca">Canada</option>
</TailSelect>
```

## Features

- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label and help text support
- Placeholder option
- Items list support
- Custom option content
- Validation error display
- Required field indicator
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~5 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

