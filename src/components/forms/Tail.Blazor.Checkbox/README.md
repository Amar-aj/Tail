# Tail.Blazor.Checkbox

Independent NuGet package for the TailCheckbox component.

## Installation

```bash
dotnet add package Tail.Blazor.Checkbox
```

## Usage

```razor
@using Tail.Blazor.Checkbox

<TailCheckbox @bind-IsChecked="isChecked" Label="I agree to the terms" />

<TailCheckbox @bind-IsChecked="isChecked" Size="CheckboxSize.Lg">
    Custom content here
</TailCheckbox>
```

## Features

- 5 sizes (Xs, Sm, Md, Lg, Xl)
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

