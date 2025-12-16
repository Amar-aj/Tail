# Tail.Blazor.Radio

Independent NuGet package for the TailRadio component.

## Installation

```bash
dotnet add package Tail.Blazor.Radio
```

## Usage

```razor
@using Tail.Blazor.Radio

<TailRadio GroupName="options" Value="option1" @bind-IsChecked="isOption1" Label="Option 1" />
<TailRadio GroupName="options" Value="option2" @bind-IsChecked="isOption2" Label="Option 2" />
```

## Features

- Radio button input
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Group name support
- Label support
- Custom content support
- Validation error display
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~2 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

