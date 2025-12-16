# Tail.Blazor.CompareValidator

Independent NuGet package for the TailCompareValidator component.

## Installation

```bash
dotnet add package Tail.Blazor.CompareValidator
```

## Usage

```razor
@using Tail.Blazor.CompareValidator

<TailCompareValidator Value="@password" CompareTo="@confirmPassword" Operator="CompareOperator.Equal" />
```

## Features

- Value comparison validation
- 4 operators (Equal, NotEqual, GreaterThan, LessThan)
- Custom error message
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~2 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

