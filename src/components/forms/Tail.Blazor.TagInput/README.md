# Tail.Blazor.TagInput

Independent NuGet package for the TailTagInput component.

## Installation

```bash
dotnet add package Tail.Blazor.TagInput
```

## Usage

```razor
@using Tail.Blazor.TagInput

<TailTagInput @bind-Tags="tags" Placeholder="Add tags..." />
```

## Features

- Tag input with add/remove functionality
- Enter to add tag
- Backspace to remove last tag
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Help text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~4 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

