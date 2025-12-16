# Tail.Blazor.ContextMenu

Independent NuGet package for the TailContextMenu component.

## Installation

```bash
dotnet add package Tail.Blazor.ContextMenu
```

## Usage

```razor
@using Tail.Blazor.ContextMenu

<TailContextMenu Items="@contextMenuItems" OnItemClick="HandleItemClick">
    <div>Right-click me</div>
</TailContextMenu>
```

## Features

- Right-click context menu
- Menu items with actions
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

