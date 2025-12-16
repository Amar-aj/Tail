# Tail.Blazor.FileUpload

Independent NuGet package for the TailFileUpload component.

## Installation

```bash
dotnet add package Tail.Blazor.FileUpload
```

## Usage

```razor
@using Tail.Blazor.FileUpload

<TailFileUpload FilesChanged="HandleFiles" Multiple="true" Accept="image/*" Label="Upload Images" />
```

## Features

- File upload with drag & drop
- Multiple file selection
- File type filtering (accept attribute)
- File list display
- Remove file option
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Validation error display
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~5 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)
- Microsoft.AspNetCore.Components.Web (for IBrowserFile)

