# Tail.Blazor.Tabs

Independent NuGet package for the TailTabs component.

## Installation

```bash
dotnet add package Tail.Blazor.Tabs
```

## Usage

```razor
@using Tail.Blazor.Tabs

<TailTabs Tabs="@tabItems" ActiveTab="@activeTab" ActiveTabChanged="OnTabChanged" />
```

## Features

- Tab navigation
- 3 variants (Default, Pills, Underline)
- Active tab highlighting
- Disabled tab support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~5 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

