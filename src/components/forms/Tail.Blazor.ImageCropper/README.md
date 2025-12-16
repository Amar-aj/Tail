# Tail.Blazor.ImageCropper

Independent NuGet package for the TailImageCropper component.

## Installation

```bash
dotnet add package Tail.Blazor.ImageCropper
```

## Usage

```razor
@using Tail.Blazor.ImageCropper

<TailImageCropper @bind-Value="croppedImage" Label="Profile Picture" AspectRatioWidth="1" AspectRatioHeight="1" />
```

## Features

- Image upload and cropping
- Aspect ratio control
- Image preview
- Crop functionality
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~6 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)
- Microsoft.AspNetCore.Components.Web (for IBrowserFile)

