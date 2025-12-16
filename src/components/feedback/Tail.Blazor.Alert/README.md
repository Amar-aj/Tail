# Tail.Blazor.Alert

Independent NuGet package for the TailAlert component.

## Installation

```bash
dotnet add package Tail.Blazor.Alert
```

## Usage

```razor
@using Tail.Blazor.Alert

<TailAlert Variant="AlertVariant.Success" Title="Success!" Dismissible="true">
    Operation completed successfully.
</TailAlert>
```

## Features

- 4 variants (Success, Warning, Danger, Info)
- Optional title
- Dismissible alerts
- Icon support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)
