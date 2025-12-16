# Tail.Blazor.Textarea

Independent NuGet package for the TailTextarea component.

## Installation

```bash
dotnet add package Tail.Blazor.Textarea
```

## Usage

```razor
@using Tail.Blazor.Textarea

<TailTextarea @bind-Value="description" Label="Description" Rows="5" MaxLength="500" ShowCharacterCount="true" />
```

## Features

- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label and help text support
- Character count display
- Auto-resize option
- Validation error display
- Required field indicator
- Disabled and readonly states
- Customizable rows
- Max length support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

