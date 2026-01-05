# Tail.Blazor.Toast

Independent NuGet package for the TailToast component.

## Installation

```bash
dotnet add package Tail.Blazor.Toast
```

## Features

- Toast notification
- 4 variants (Success, Warning, Error, Info)
- Auto-dismiss option
- Title and message support
- Icon support
- Dismissible
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Message | string? | - | Message parameter |
| Title | string? | - | Title parameter |
| Variant | ToastVariant | ToastVariant.Info | Visual variant style for the component |
| Dismissible | bool | true | Dismissible parameter |
| ShowIcon | bool | true | Icon to display |
| Icon | RenderFragment? | - | Icon to display |
| AutoDismissAfter | int? | 5000 | AutoDismissAfter parameter |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| OnDismiss | void | OnDismiss callback |

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| Dispose | void | Dispose property |

## Methods

No additional public methods.

## Examples

```razor
<TailToast></TailToast>
```