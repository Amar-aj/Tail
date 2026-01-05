# Tail.Blazor.Alert

Independent NuGet package for the TailAlert component.

## Installation

```bash
dotnet add package Tail.Blazor.Alert
```

## Features

- 4 variants (Success, Warning, Danger, Info)
- Optional title
- Dismissible alerts
- Icon support
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
| Variant | AlertVariant | AlertVariant.Info | Visual variant style for the component |
| Title | string? | - | Title parameter |
| Dismissible | bool | - | Dismissible parameter |
| ShowIcon | bool | true | Icon to display |
| Icon | RenderFragment? | - | Icon to display |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| OnDismiss | void | OnDismiss callback |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailAlert></TailAlert>
```