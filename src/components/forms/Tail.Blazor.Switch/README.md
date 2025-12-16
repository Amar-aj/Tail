# Tail.Blazor.Switch

Independent NuGet package for the TailSwitch component.

## Installation

```bash
dotnet add package Tail.Blazor.Switch
```

## Usage

```razor
@using Tail.Blazor.Switch

<TailSwitch @bind-IsChecked="isEnabled" Label="Enable notifications" />

<TailSwitch @bind-IsChecked="isEnabled" Size="SwitchSize.Lg">
    Large switch
</TailSwitch>
```

## Features

- Toggle switch design
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Custom content support
- Validation error display
- Disabled state
- Smooth animations
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~2 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

