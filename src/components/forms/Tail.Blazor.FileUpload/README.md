# Tail.Blazor.FileUpload

Independent NuGet package for the TailFileUpload component.

## Installation

```bash
dotnet add package Tail.Blazor.FileUpload
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

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Size | FileUploadSize | FileUploadSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| Accept | string? | - | Accept parameter |
| Multiple | bool | - | Multiple parameter |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Required | bool | - | Whether the component is required |
| Disabled | bool | - | Whether the component is disabled |
| Style | string? | - | Additional CSS styles |
| MaxFiles | int | 5 | Maximum value constraint |
| MaxFileSize | long | 10 * 1024 * 1024 | Size of the component |
| ShowPreview | bool | true | ShowPreview parameter |
| AutoUpload | bool | false | AutoUpload parameter |
| UploadHandler | Func<IBrowserFile, Task<bool>>? | - | UploadHandler parameter |
| ShowUploadButton | bool | true | ShowUploadButton parameter |
| ShowRemoveButton | bool | true | ShowRemoveButton parameter |
| ShowRemoveAll | bool | true | ShowRemoveAll parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| FilesChanged | IBrowserFile[] | Raised when value changes |
| FilesSelected | IBrowserFile[] | Raised with IBrowserFile[] value |
| UploadRequested | IBrowserFile[] | Raised with IBrowserFile[] value |

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| File | IBrowserFile | File property |
| PreviewUrl | string? | PreviewUrl property |
| Progress | int | Progress property |
| Uploading | bool | Uploading property |
| Uploaded | bool | Uploaded property |
| Error | string? | Error property |
| ValueTask | async | ValueTask property |

## Methods

No additional public methods.

## Examples

```razor
<TailFileUpload></TailFileUpload>
```