# Tail.Blazor.MultiSelect

Independent NuGet package for the TailMultiSelect component.

## Installation

```bash
dotnet add package Tail.Blazor.MultiSelect
```

## Usage

```razor
@using Tail.Blazor.MultiSelect

<TailMultiSelect @bind-SelectedValues="selectedValues" Items="@items" Label="Select multiple options" />
```

## Features

- Multi-selection dropdown
- Tag display for selected items
- Search functionality (can be added)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Validation error display
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~6 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

