# Tail.Blazor.ScrollSpy

Independent NuGet package for the TailScrollSpy component.

## Installation

```bash
dotnet add package Tail.Blazor.ScrollSpy
```

## Features

- Scroll spy navigation
- Active section highlighting
- Left/right positioning
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Items | List<ScrollSpyItem> | new() | Data items collection |
| ActiveId | string? | - | ActiveId parameter |
| Position | ScrollSpyPosition | ScrollSpyPosition.Left | Position parameter |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| OnItemClick | ScrollSpyItem | Raised when component is clicked |

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| ScrollSpyItem | class | ScrollSpyItem property |
| Id | string | Id property |
| Label | string | Label property |
| Href | string? | Href property |
| ScrollSpyPosition | enum | ScrollSpyPosition property |

## Methods

No additional public methods.

## Examples

```razor
<TailScrollSpy></TailScrollSpy>
```