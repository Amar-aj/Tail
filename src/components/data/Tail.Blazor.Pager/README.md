# Tail.Blazor.Pager

Independent NuGet package for the TailPager component.

## Installation

```bash
dotnet add package Tail.Blazor.Pager
```

## Usage

```razor
@using Tail.Blazor.Pager

<TailPager CurrentPage="@currentPage" TotalPages="@totalPages" TotalItems="@totalItems" PageSize="10" />
```

## Features

- Page navigation
- Item count display
- Previous/Next buttons
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

