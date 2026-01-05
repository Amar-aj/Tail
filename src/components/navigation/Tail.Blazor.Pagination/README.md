# Tail.Blazor.Pagination

Independent NuGet package for the TailPagination component.

## Installation

```bash
dotnet add package Tail.Blazor.Pagination
```

## Features

- Page navigation
- Previous/Next buttons
- Page number buttons
- Ellipsis for large page counts
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| CurrentPage | int | 1 | CurrentPage parameter |
| TotalPages | int | 1 | TotalPages parameter |
| VisiblePages | int | 5 | Whether the component is visible |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| CurrentPageChanged | int | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailPagination></TailPagination>
```