---
title: InfiniteScroll
package: Tail.Blazor.InfiniteScroll
category: data
namespace: Tail.Blazor.InfiniteScroll
route: /components/data/infinitescroll
is_generic: false
is_missing: true
---

# InfiniteScroll



## Installation

```bash
dotnet add package Tail.Blazor.InfiniteScroll
```

## Namespace

```csharp
using Tail.Blazor.InfiniteScroll;
```

## Basic Usage

🚧 **Coming Soon** - This component is planned but not yet implemented.

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **IsLoading** | `bool` | - | Whether the component is in loading state |
| **ThresholdPixels** | `int` | 200 | ThresholdPixels parameter |
| **AdditionalAttributes** | `Dictionary<string, object>?` | - | AdditionalAttributes parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnLoadMore** | `EventCallback` | OnLoadMore callback |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `ChildContent` | `RenderFragment?` | ChildContent property |
| `IsLoading` | `bool` | IsLoading property |
| `OnLoadMore` | `EventCallback` | OnLoadMore property |
| `ThresholdPixels` | `int` | ThresholdPixels property |
| `object` | `Dictionary<string,` | object property |

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
