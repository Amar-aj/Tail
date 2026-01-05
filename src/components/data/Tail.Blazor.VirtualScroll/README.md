# Tail.Blazor.VirtualScroll

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

## Class

Component class generated from the Razor file.

## Type Parameters

| Name | Description |
| --- | --- |
| T | Generic type parameter for typed data |

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Items | List<T> | new() | Data items collection |
| ItemTemplate | RenderFragment<T> | default! | ItemTemplate parameter |
| ItemHeight | int | 50 | ItemHeight parameter |
| VisibleCount | int | 10 | Whether the component is visible |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailVirtualScroll></TailVirtualScroll>
```