# Tail.Blazor.PivotDataGrid

Independent NuGet package for the TailPivotDataGrid component.

## Installation

```bash
dotnet add package Tail.Blazor.PivotDataGrid
```

## Features

- Pivot table
- Row and column headers
- Data aggregation
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| RowHeader | string | "Row" | RowHeader parameter |
| Columns | List<string> | new() | Columns parameter |
| Rows | List<PivotRow> | new() | Rows parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| PivotRow | class | PivotRow property |
| Key | string | Key property |
| string | Dictionary<string, | string property |

## Methods

No additional public methods.

## Examples

```razor
<TailPivotDataGrid></TailPivotDataGrid>
```