---
title: Accordion
package: Tail.Blazor.Accordion
category: navigation
namespace: Tail.Blazor.Accordion
route: /components/navigation/accordion
is_generic: false
is_missing: false
---

# Accordion

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

## Namespace

```csharp
using Tail.Blazor.Accordion;
```

## Basic Usage

```razor
<TailAccordion />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Accordion

<TailAccordion />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailAccordion AllowMultiple="true" Style="Sample Style" />
```

## Advanced Examples

More complex usage scenarios:

More complex usage scenarios:

##

## Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailAccordion  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Items** | `List<AccordionItem>` | new() | Data items collection |
| **AllowMultiple** | `bool` | - | AllowMultiple parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `AccordionItem` | `class` | AccordionItem property |
| `Id` | `string` | Id property |
| `Title` | `string` | Title property |
| `Content` | `RenderFragment?` | Content property |
| `IsExpanded` | `bool` | IsExpanded property |

## Base Class

The component inherits from `TailComponentBase` (from `Tail.Blazor.Core.Base`), which provides:

- `Class` parameter for additional CSS classes
- `AdditionalAttributes` parameter for additional HTML attributes

## Dependencies

- `Tail.Blazor.Core.Base` (required)
- `Microsoft.AspNetCore.Components`
- `Microsoft.AspNetCore.Components.Web`
- `Microsoft.AspNetCore.Components`
- `Microsoft.AspNetCore.Components.Web`
- `Microsoft.AspNetCore.Components`
- `Microsoft.AspNetCore.Components.Web`

## Target Frameworks

- .NET 8
- .NET 9
- .NET 10
