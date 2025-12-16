# Tail.Blazor.Popconfirm

Independent NuGet package for the TailPopconfirm component.

## Installation

```bash
dotnet add package Tail.Blazor.Popconfirm
```

## Usage

```razor
@using Tail.Blazor.Popconfirm

<TailPopconfirm Title="Delete this item?" OnConfirm="HandleDelete" Trigger="PopconfirmTrigger.Click">
    <button>Delete</button>
</TailPopconfirm>
```

## Features

- Popconfirm dialog
- Click or hover trigger
- 4 placement options (Top, Bottom, Left, Right)
- Custom confirm/cancel text
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

