# Tail.Blazor.AutoComplete

Independent NuGet package for the TailAutoComplete component.

## Installation

```bash
dotnet add package Tail.Blazor.AutoComplete
```

## Usage

```razor
@using Tail.Blazor.AutoComplete

<TailAutoComplete @bind-Value="searchTerm" Items="@suggestions" Label="Search" Placeholder="Type to search..." />
```

## Features

- Autocomplete with suggestions dropdown
- Real-time filtering
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~5 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

