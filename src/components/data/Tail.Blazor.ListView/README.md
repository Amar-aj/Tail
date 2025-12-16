# Tail.Blazor.ListView

Independent NuGet package for the TailListView component.

## Installation

```bash
dotnet add package Tail.Blazor.ListView
```

## Usage

```razor
@using Tail.Blazor.ListView

<TailListView Items="@items">
    <ItemTemplate>
        <div>@context.Name</div>
    </ItemTemplate>
</TailListView>
```

## Features

- List view with items
- Custom item template
- Hover effects
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

