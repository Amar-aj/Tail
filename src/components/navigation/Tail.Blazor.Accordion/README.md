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

## Namespace

```csharp
using Tail.Blazor.Accordion;
```

## Component Usage

```razor
<TailAccordion></TailAccordion>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Items** | `List<AccordionItem>` | new() | Data items collection |
| **AllowMultiple** | `bool` | - | AllowMultiple parameter |
| **Style** | `string?` | - | Additional CSS styles |

## Events

No events exposed.

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Accordion

<TailAccordion />
```

### Common Patterns

Frequently used patterns and combinations:

### Basic Usage

The simplest way to use the component:

```razor
<TailAccordion />
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailAccordion AllowMultiple="true" Style="Sample Style" />
```

### Advanced Examples

More complex usage scenarios:

#### Custom Styling

```razor
@* Using Style parameter *@
<TailAccordion Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailAccordion>

@* Using Class parameter *@
<TailAccordion Class="my-custom-class shadow-lg">
    With Custom Class
</TailAccordion>
```

### Real-World Example

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

## Package Information

- **Package ID**: `Tail.Blazor.Accordion`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
