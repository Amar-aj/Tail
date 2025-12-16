# Tail.Blazor.Clipboard

Independent NuGet package for the TailClipboard component.

## Installation

```bash
dotnet add package Tail.Blazor.Clipboard
```

## Usage

```razor
@using Tail.Blazor.Clipboard

<TailClipboard Text="@textToCopy" OnCopied="HandleCopied">
    Copy
</TailClipboard>
```

## Features

- Copy to clipboard
- Success feedback
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~2 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

