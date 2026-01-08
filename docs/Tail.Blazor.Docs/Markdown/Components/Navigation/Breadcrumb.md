---
title: Breadcrumb
package: Tail.Blazor.Breadcrumb
category: navigation
namespace: Tail.Blazor.Breadcrumb
route: /components/navigation/breadcrumb
is_generic: false
is_missing: false
---

# Breadcrumb

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

## Namespace

```csharp
using Tail.Blazor.Breadcrumb;
```

## Basic Usage

```razor
<TailBreadcrumb />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Breadcrumb

<TailBreadcrumb />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailBreadcrumb Style="Sample Style" />
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
    <TailBreadcrumb  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Items** | `List<BreadcrumbItem>` | new() | Data items collection |
| **Style** | `string?` | - | Additional CSS styles |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `BreadcrumbItem` | `class` | BreadcrumbItem property |
| `Text` | `string` | Text property |
| `Href` | `string?` | Href property |

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
