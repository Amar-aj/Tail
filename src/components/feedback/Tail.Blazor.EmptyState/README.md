# Tail.Blazor.EmptyState

Independent NuGet package for the TailEmptyState component.

## Installation

```bash
dotnet add package Tail.Blazor.EmptyState
```

## Usage

```razor
@using Tail.Blazor.EmptyState

<TailEmptyState Title="No items found" Description="Get started by creating your first item.">
    <Action>
        <button>Create Item</button>
    </Action>
</TailEmptyState>
```

## Features

- Empty state display
- 3 sizes (Sm, Md, Lg)
- 3 variants (Default, Minimal, Detailed)
- Custom icon support
- Title and description
- Action button support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~2 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

