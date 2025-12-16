# Tail.Blazor.PasswordStrengthMeter

Independent NuGet package for the TailPasswordStrengthMeter component.

## Installation

```bash
dotnet add package Tail.Blazor.PasswordStrengthMeter
```

## Usage

```razor
@using Tail.Blazor.PasswordStrengthMeter

<TailPasswordStrengthMeter @bind-Value="password" Label="Password" ShowStrengthMeter="true" />
```

## Features

- Password input with strength meter
- Show/hide password toggle
- Real-time strength calculation
- Visual strength indicator (5 levels)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Validation error display
- Required field indicator
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~6 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

