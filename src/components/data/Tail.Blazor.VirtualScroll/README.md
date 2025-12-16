# Tail.Blazor.VirtualScroll

Independent NuGet package for the TailVirtualScroll component.

## Installation

```bash
dotnet add package Tail.Blazor.VirtualScroll
```

## Usage

```razor
@using Tail.Blazor.VirtualScroll

<TailVirtualScroll Items="@items" ItemHeight="50" VisibleCount="10">
    <ItemTemplate>
        <div>@context.Name</div>
    </ItemTemplate>
</TailVirtualScroll>
```

## Features

- Virtual scrolling for large lists
- Performance optimization
- Customizable item height
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~4 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

