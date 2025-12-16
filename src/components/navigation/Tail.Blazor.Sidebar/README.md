# Tail.Blazor.Sidebar

Independent NuGet package for the TailSidebar component.

## Installation

```bash
dotnet add package Tail.Blazor.Sidebar
```

## Usage

```razor
@using Tail.Blazor.Sidebar

<TailSidebar IsCollapsible="true" Position="SidebarPosition.Left">
    <Header>Navigation</Header>
    <nav>...</nav>
</TailSidebar>
```

## Features

- Collapsible sidebar
- Left/right positioning
- Header and footer support
- Smooth collapse animation
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~6 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

