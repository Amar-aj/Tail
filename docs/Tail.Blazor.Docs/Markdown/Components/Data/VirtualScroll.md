---
title: VirtualScroll
package: Tail.Blazor.VirtualScroll
category: data
namespace: Tail.Blazor.VirtualScroll
route: /components/data/virtualscroll
is_generic: true
is_missing: false
---

# VirtualScroll

Independent NuGet package for the TailVirtualScroll component.

## Installation

```bash
dotnet add package Tail.Blazor.VirtualScroll
```

## Features

- Virtual scrolling for large lists
- Performance optimization
- Customizable item height
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.VirtualScroll;
```

## Basic Usage

⚠️ **Generic Component** - This component requires a type parameter.

```razor
<TailVirtualScroll T="YourModel">Content</TailVirtualScroll>
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
| **ItemHeight** | `int` | 50 | ItemHeight parameter |
| **VisibleCount** | `int` | 10 | Whether the component is visible |
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
