# Tail.Blazor.Button

Independent NuGet package for the TailButton component.

## Installation

```bash
dotnet add package Tail.Blazor.Button
```

## Usage

```razor
@using Tail.Blazor.Button

<TailButton Variant="ButtonVariant.Primary" OnClick="HandleClick">
    Click Me
</TailButton>
```

## Features

- 9 variants (Primary, Success, Warning, Danger, Info, Outline, Soft, Ghost, Link)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Loading states
- Icon support (start/end)
- Disabled states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

