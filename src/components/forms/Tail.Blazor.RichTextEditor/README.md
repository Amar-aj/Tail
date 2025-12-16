# Tail.Blazor.RichTextEditor

Independent NuGet package for the TailRichTextEditor component.

## Installation

```bash
dotnet add package Tail.Blazor.RichTextEditor
```

## Usage

```razor
@using Tail.Blazor.RichTextEditor

<TailRichTextEditor @bind-Value="htmlContent" Label="Content" MinHeight="300" />
```

## Features

- Rich text editor with formatting toolbar
- Bold, italic, underline formatting
- Content editable area
- Customizable min height
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~8 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

