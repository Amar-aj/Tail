# Tail.Blazor.FAB

Independent NuGet package for the TailFAB (Floating Action Button) component.

## Installation

```bash
dotnet add package Tail.Blazor.FAB
```

## Usage

```razor
@using Tail.Blazor.FAB

<TailFAB Position="FABPosition.BottomRight" OnClick="HandleClick">
    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
    </svg>
</TailFAB>
```

## Features

- 4 positions (TopLeft, TopRight, BottomLeft, BottomRight)
- Fixed positioning
- Circular design
- Loading states
- Disabled states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

