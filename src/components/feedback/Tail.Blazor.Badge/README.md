# Tail.Blazor.Badge

Independent NuGet package for the TailBadge component.

## Installation

```bash
dotnet add package Tail.Blazor.Badge
```

## Features

- 6 variants (Primary, Success, Warning, Danger, Info, Gray)
- 3 sizes (Sm, Md, Lg)
- Dot indicator option
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
| Variant | BadgeVariant | BadgeVariant.Primary | Visual variant style for the component |
| Size | BadgeSize | BadgeSize.Md | Size of the component |
| ShowDot | bool | - | ShowDot parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailBadge></TailBadge>
```