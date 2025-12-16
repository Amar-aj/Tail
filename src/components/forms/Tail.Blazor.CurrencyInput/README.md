# Tail.Blazor.CurrencyInput

Independent NuGet package for the TailCurrencyInput component.

## Installation

```bash
dotnet add package Tail.Blazor.CurrencyInput
```

## Usage

```razor
@using Tail.Blazor.CurrencyInput

<TailCurrencyInput @bind-Value="amount" CurrencySymbol="$" SymbolPosition="CurrencySymbolPosition.Left" Label="Amount" />
```

## Features

- Currency input with symbol
- Left or right symbol position
- Custom currency symbol
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~4 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

