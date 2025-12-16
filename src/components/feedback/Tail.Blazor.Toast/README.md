# Tail.Blazor.Toast

Independent NuGet package for the TailToast component.

## Installation

```bash
dotnet add package Tail.Blazor.Toast
```

## Usage

```razor
@using Tail.Blazor.Toast

<TailToast Message="Operation completed!" Variant="ToastVariant.Success" AutoDismissAfter="3000" />
```

## Features

- Toast notification
- 4 variants (Success, Warning, Error, Info)
- Auto-dismiss option
- Title and message support
- Icon support
- Dismissible
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~4 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

