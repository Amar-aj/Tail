# Tail.Blazor.Pager

Independent NuGet package for the TailPager component.

## Installation

```bash
dotnet add package Tail.Blazor.Pager
```

## Features

- Page navigation
- Item count display
- Previous/Next buttons
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
| TotalItems | int | - | Data items collection |
| PageSize | int | 10 | Size of the component |
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
<TailPager></TailPager>
```