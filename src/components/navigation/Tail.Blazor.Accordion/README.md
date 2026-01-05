# Tail.Blazor.Accordion

Independent NuGet package for the TailAccordion component.

## Installation

```bash
dotnet add package Tail.Blazor.Accordion
```

## Features

- Accordion with expandable sections
- Single or multiple expansion
- Animated expand/collapse
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Items | List<AccordionItem> | new() | Data items collection |
| AllowMultiple | bool | - | AllowMultiple parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| AccordionItem | class | AccordionItem property |
| Id | string | Id property |
| Title | string | Title property |
| Content | RenderFragment? | Content property |
| IsExpanded | bool | IsExpanded property |

## Methods

No additional public methods.

## Examples

```razor
<TailAccordion></TailAccordion>
```