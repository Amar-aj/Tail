---
title: ListView
package: Tail.Blazor.ListView
category: data
namespace: Tail.Blazor.ListView
route: /components/data/listview
is_generic: true
is_missing: false
---

# ListView

Independent NuGet package for the TailListView component.

## Installation

```bash
dotnet add package Tail.Blazor.ListView
```

## Features

- List view with items
- Custom item template
- Hover effects
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.ListView;
```

## Basic Usage

⚠️ **Generic Component** - This component requires a type parameter.

```razor
<TailListView T="YourModel">Content</TailListView>
```

## API Reference

### Type Parameters

| Name | Description |
| --- | --- |
| `T` | Generic type parameter for typed data |

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Items** | `List<T>` | new() | Data items collection |
| **ItemTemplate** | `RenderFragment<T>` | default! | ItemTemplate parameter |
| **Style** | `string?` | - | Additional CSS styles |

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
