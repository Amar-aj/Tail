---
title: Timeline
package: Tail.Blazor.Timeline
category: visualization
namespace: Tail.Blazor.Timeline
route: /components/visualization/timeline
is_generic: false
is_missing: false
---

# Timeline

Independent NuGet package for the TailTimeline component.

## Installation

```bash
dotnet add package Tail.Blazor.Timeline
```

## Features

- Timeline visualization
- Title and description
- Timestamp display
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Timeline;
```

## Basic Usage

```razor
<TailTimeline />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Timeline

<TailTimeline />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailTimeline Style="Sample Style" />
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
    <TailTimeline  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Items** | `List<TimelineItem>` | new() | Data items collection |
| **Style** | `string?` | - | Additional CSS styles |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `TimelineItem` | `class` | TimelineItem property |
| `Title` | `string` | Title property |
| `Description` | `string?` | Description property |
| `Timestamp` | `DateTime?` | Timestamp property |

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
