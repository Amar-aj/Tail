---
title: Scheduler
package: Tail.Blazor.Scheduler
category: data
namespace: Tail.Blazor.Scheduler
route: /components/data/scheduler
is_generic: false
is_missing: false
---

# Scheduler

Independent NuGet package for the TailScheduler component.

## Installation

```bash
dotnet add package Tail.Blazor.Scheduler
```

## Features

- Calendar scheduler
- Event display
- Month view
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Scheduler;
```

## Basic Usage

```razor
<TailScheduler />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Scheduler

<TailScheduler />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailScheduler Style="Sample Style" />
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
    <TailScheduler  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **CurrentDate** | `DateTime` | DateTime.Now | CurrentDate parameter |
| **Events** | `List<SchedulerEvent>` | new() | Events parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `CalendarDay` | `class` | CalendarDay property |
| `Date` | `DateTime` | Date property |
| `Day` | `int` | Day property |
| `Events` | `List<SchedulerEvent>` | Events property |
| `SchedulerEvent` | `class` | SchedulerEvent property |
| `Date` | `DateTime` | Date property |
| `Title` | `string` | Title property |

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
