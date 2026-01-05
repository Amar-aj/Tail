# Tail.Blazor.AdvancedFilter

Independent NuGet package for the TailAdvancedFilter component.

## Installation

```bash
dotnet add package Tail.Blazor.AdvancedFilter
```

## Features

- Advanced filtering
- Field selection
- Operator selection
- Filter value input
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Fields | List<string> | new() | Fields parameter |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| OnFilterApplied | FilterCriteria | Raised with FilterCriteria value |

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| FilterCriteria | class | FilterCriteria property |
| Field | string | Field property |
| Operator | string | Operator property |
| Value | string | Value property |

## Methods

No additional public methods.

## Examples

```razor
<TailAdvancedFilter></TailAdvancedFilter>
```