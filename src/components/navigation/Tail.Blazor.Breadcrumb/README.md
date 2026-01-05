# Tail.Blazor.Breadcrumb

Independent NuGet package for the TailBreadcrumb component.

## Installation

```bash
dotnet add package Tail.Blazor.Breadcrumb
```

## Features

- Breadcrumb navigation
- Separator icons
- Link support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Items | List<BreadcrumbItem> | new() | Data items collection |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| BreadcrumbItem | class | BreadcrumbItem property |
| Text | string | Text property |
| Href | string? | Href property |

## Methods

No additional public methods.

## Examples

```razor
<TailBreadcrumb></TailBreadcrumb>
```