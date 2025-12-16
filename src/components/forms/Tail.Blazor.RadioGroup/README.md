# Tail.Blazor.RadioGroup

Independent NuGet package for the TailRadioGroup component.

## Installation

```bash
dotnet add package Tail.Blazor.RadioGroup
```

## Usage

```razor
@using Tail.Blazor.RadioGroup

<TailRadioGroup Label="Choose an option" Orientation="RadioGroupOrientation.Vertical">
    <TailRadio GroupName="options" Value="option1" Label="Option 1" />
    <TailRadio GroupName="options" Value="option2" Label="Option 2" />
    <TailRadio GroupName="options" Value="option3" Label="Option 3" />
</TailRadioGroup>
```

## Features

- Radio button grouping
- Vertical and horizontal orientations
- Label support
- Help text support
- Validation error display
- Required field indicator
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

