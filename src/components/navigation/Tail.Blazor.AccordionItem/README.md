# Tail.Blazor.AccordionItem

Independent NuGet package for the TailAccordionItem component.

## Installation

```bash
dotnet add package Tail.Blazor.AccordionItem
```

## Features

- Individual accordion item
- Expand/collapse animation
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
| Title | string | string.Empty | Title parameter |
| IsExpanded | bool | - | IsExpanded parameter |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| IsExpandedChanged | bool | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailAccordionItem></TailAccordionItem>
```