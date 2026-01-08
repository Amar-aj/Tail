---
title: FileUpload
package: Tail.Blazor.FileUpload
category: forms
namespace: Tail.Blazor.FileUpload
route: /components/forms/fileupload
is_generic: false
is_missing: false
---

# FileUpload

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

## Namespace

```csharp
using Tail.Blazor.FileUpload;
```

## Basic Usage

```razor
<TailFileUpload />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.FileUpload

<TailFileUpload />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailFileUpload Size="FileUploadSize.Md">
    Medium Size
</TailFileUpload>
```

**With Click Handler**

```razor
<TailFileUpload FilesChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailFileUpload>
```

**Disabled State**

```razor
<TailFileUpload Disabled="true">
    Disabled
</TailFileUpload>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailFileUpload Size="FileUploadSize.Xs">Xs</TailFileUpload>
<TailFileUpload Size="FileUploadSize.Sm">Sm</TailFileUpload>
<TailFileUpload Size="FileUploadSize.Md">Md</TailFileUpload>
<TailFileUpload Size="FileUploadSize.Lg">Lg</TailFileUpload>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailFileUpload Disabled="true">Disabled</TailFileUpload>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailFileUpload FilesChanged="HandleFilesChanged">
    Click Me
</TailFileUpload>

@code {
    private void HandleFilesChanged(Tail.Blazor.FileUpload.IBrowserFile[] args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailFileUpload Size="FileUploadSize.Sm" Label="Sample Label" Accept="Sample Accept" Multiple="true" ErrorMessage="Sample ErrorMessage" />
```

## Advanced Examples

More complex usage scenarios:

More complex usage scenarios:

##

## Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailFileUpload Size="FileUploadSize.Sm" FilesChanged="HandleAction" />
</div>

@code {
    private void HandleAction(IBrowserFile[] args)
    {
        // Perform action
        Console.WriteLine("Action executed");
    }
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Size** | `FileUploadSize` | FileUploadSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Accept** | `string?` | - | Accept parameter |
| **Multiple** | `bool` | - | Multiple parameter |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |
| **MaxFiles** | `int` | 5 | Maximum value constraint |
| **MaxFileSize** | `long` | 10 * 1024 * 1024 | Size of the component |
| **ShowPreview** | `bool` | true | ShowPreview parameter |
| **AutoUpload** | `bool` | false | AutoUpload parameter |
| **UploadHandler** | `Func<IBrowserFile, Task<bool>>?` | - | UploadHandler parameter |
| **ShowUploadButton** | `bool` | true | ShowUploadButton parameter |
| **ShowRemoveButton** | `bool` | true | ShowRemoveButton parameter |
| **ShowRemoveAll** | `bool` | true | ShowRemoveAll parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **FilesChanged** | `EventCallback<IBrowserFile[]>` | Raised when value changes |
| **FilesSelected** | `EventCallback<IBrowserFile[]>` | Raised with IBrowserFile[] value |
| **UploadRequested** | `EventCallback<IBrowserFile[]>` | Raised with IBrowserFile[] value |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `File` | `IBrowserFile` | File property |
| `PreviewUrl` | `string?` | PreviewUrl property |
| `Progress` | `int` | Progress property |
| `Uploading` | `bool` | Uploading property |
| `Uploaded` | `bool` | Uploaded property |
| `Error` | `string?` | Error property |
| `ValueTask` | `async` | ValueTask property |

### Enums

#### FileUploadSize

```csharp
public enum FileUploadSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// FileUpload size options.
///

#### Tail.Blazor.FileUpload;.FileUploadSize

```csharp
public enum Tail.Blazor.FileUpload;.FileUploadSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// FileUpload size options.
///

## Base Class

The component inherits from `TailComponentBase` (from `Tail.Blazor.Core.Base`), which provides:

- `Class` parameter for additional CSS classes
- `AdditionalAttributes` parameter for additional HTML attributes

## Dependencies

- `Tail.Blazor.Core.Base` (required)
- `Microsoft.AspNetCore.Components`
- `Microsoft.AspNetCore.Components.Web`
- `Microsoft.AspNetCore.Components`
- `Microsoft.AspNetCore.Components.Web`
- `Microsoft.AspNetCore.Components`
- `Microsoft.AspNetCore.Components.Web`

## Target Frameworks

- .NET 8
- .NET 9
- .NET 10
