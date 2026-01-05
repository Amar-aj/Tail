# Tail.Blazor.Skeleton

Independent NuGet package for the TailSkeleton component.

## Installation

```bash
dotnet add package Tail.Blazor.Skeleton
```

## Features

- 4 types (Text, Circle, Rectangle, Custom)
- Customizable width and height
- Animation option
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| ChildContent | RenderFragment? | - | ChildContent parameter |
| Type | SkeletonType | SkeletonType.Text | Type parameter |
| Width | int? | - | Width parameter |
| Height | int? | - | Height parameter |
| Animated | bool | true | Animated parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailSkeleton></TailSkeleton>
```