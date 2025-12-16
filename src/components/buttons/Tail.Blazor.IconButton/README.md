# Tail.Blazor.IconButton

Independent NuGet package for the TailIconButton component.

## Installation

```bash
dotnet add package Tail.Blazor.IconButton
```

## Usage

```razor
@using Tail.Blazor.IconButton

<TailIconButton Variant="ButtonVariant.Primary" OnClick="HandleClick">
    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
    </svg>
</TailIconButton>
```

## Features

- Icon-only button design
- 9 variants (Primary, Success, Warning, Danger, Info, Outline, Soft, Ghost, Link)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Loading states
- Disabled states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~2 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

