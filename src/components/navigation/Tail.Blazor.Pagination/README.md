# Tail.Blazor.Pagination

Independent NuGet package for the TailPagination component.

## Installation

```bash
dotnet add package Tail.Blazor.Pagination
```

## Usage

```razor
@using Tail.Blazor.Pagination

<TailPagination CurrentPage="@currentPage" TotalPages="@totalPages" CurrentPageChanged="OnPageChanged" />
```

## Features

- Page navigation
- Previous/Next buttons
- Page number buttons
- Ellipsis for large page counts
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~4 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

