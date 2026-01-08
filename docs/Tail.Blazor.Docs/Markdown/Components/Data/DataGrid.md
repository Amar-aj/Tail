---
title: DataGrid
package: Tail.Blazor.DataGrid
category: data
namespace: Tail.Blazor.DataGrid
route: /components/data/datagrid
is_generic: true
is_missing: false
---

# DataGrid

Independent NuGet package for the TailDataGrid component.

## Installation

```bash
dotnet add package Tail.Blazor.DataGrid
```

## Features

- Data grid with columns
- Custom column rendering
- Hover effects
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.DataGrid;
```

## Basic Usage

⚠️ **Generic Component** - This component requires a type parameter.

```razor
<TailDataGrid T="YourModel">Content</TailDataGrid>
```

## API Reference

### Type Parameters

| Name | Description |
| --- | --- |
| `T` | Generic type parameter for typed data |

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Data** | `List<T>` | new() | Data parameter |
| **Columns** | `List<DataGridColumn<T>>` | new() | Columns parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `DataGridColumn` | `class` | DataGridColumn property |
| `Header` | `string` | Header property |
| `Render` | `RenderFragment<T>?` | Render property |

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
