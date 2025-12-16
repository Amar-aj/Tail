# Tail.Blazor.Mask

Independent NuGet package for the TailMask component.

## Installation

```bash
dotnet add package Tail.Blazor.Mask
```

## Usage

```razor
@using Tail.Blazor.Mask

<TailMask @bind-Value="phoneNumber" Mask="(###) ###-####" Label="Phone Number" />
```

## Features

- Input masking (phone, credit card, etc.)
- Custom mask patterns
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Validation error display
- Required field indicator
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

