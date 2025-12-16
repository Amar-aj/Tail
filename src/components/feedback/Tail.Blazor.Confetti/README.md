# Tail.Blazor.Confetti

Independent NuGet package for the TailConfetti component.

## Installation

```bash
dotnet add package Tail.Blazor.Confetti
```

## Usage

```razor
@using Tail.Blazor.Confetti

<TailConfetti IsActive="@showConfetti" ParticleCount="100" Shape="ConfettiShape.Mixed" Duration="3000" />
```

## Features

- Confetti animation
- 4 shape types (Circle, Rectangle, Star, Mixed)
- Customizable particle count
- Duration control
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~2 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

