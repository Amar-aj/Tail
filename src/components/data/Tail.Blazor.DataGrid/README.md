# Tail.Blazor.DataGrid

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

## Class

Component class generated from the Razor file.

## Type Parameters

| Name | Description |
| --- | --- |
| T | Generic type parameter for typed data |

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Data | List<T> | new() | Data parameter |
| Columns | List<DataGridColumn<T>> | new() | Columns parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| DataGridColumn | class | DataGridColumn property |
| Header | string | Header property |
| Render | RenderFragment<T>? | Render property |

## Methods

No additional public methods.

## Examples

```razor
<TailDataGrid></TailDataGrid>
```