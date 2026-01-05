# Tail.Blazor.ImageCropper

Independent NuGet package for the TailImageCropper component.

## Installation

```bash
dotnet add package Tail.Blazor.ImageCropper
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

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Value | string? | - | Current value of the component |
| Size | ImageCropperSize | ImageCropperSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| AspectRatioWidth | int | 1 | AspectRatioWidth parameter |
| AspectRatioHeight | int | 1 | AspectRatioHeight parameter |
| Disabled | bool | - | Whether the component is disabled |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| ValueChanged | string? | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailImageCropper></TailImageCropper>
```