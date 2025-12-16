# Tail.Blazor.PhoneNumberInput

Independent NuGet package for the TailPhoneNumberInput component.

## Installation

```bash
dotnet add package Tail.Blazor.PhoneNumberInput
```

## Usage

```razor
@using Tail.Blazor.PhoneNumberInput

<TailPhoneNumberInput @bind-PhoneNumber="phone" @bind-SelectedCountryCode="countryCode" Label="Phone Number" />
```

## Features

- Phone number input with country code selector
- Country code dropdown
- Phone number formatting
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~5 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

