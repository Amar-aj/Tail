# Tail.Blazor.RegexValidator

Independent NuGet package for the TailRegexValidator component.

## Installation

```bash
dotnet add package Tail.Blazor.RegexValidator
```

## Usage

```razor
@using Tail.Blazor.RegexValidator

<TailRegexValidator Value="@phoneValue" Pattern="^[0-9]{10}$" ErrorMessage="Invalid phone number" />
```

## Features

- Regex pattern validation
- Custom error message
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~1 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

