---
title: Popover
package: Tail.Blazor.Popover
category: feedback
namespace: Tail.Blazor.Popover
route: /components/feedback/popover
is_generic: false
is_missing: true
---

# Popover



## Installation

```bash
dotnet add package Tail.Blazor.Popover
```

## Namespace

```csharp
using Tail.Blazor.Popover;
```

## Basic Usage

🚧 **Coming Soon** - This component is planned but not yet implemented.

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **TriggerContent** | `RenderFragment?` | - | TriggerContent parameter |
| **Position** | `string` | "top" | Position parameter |
| **Trigger** | `PopoverTrigger` | PopoverTrigger.Click | Trigger parameter |
| **IsOpen** | `bool` | - | IsOpen parameter |
| **AdditionalAttributes** | `Dictionary<string, object>?` | - | AdditionalAttributes parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **IsOpenChanged** | `EventCallback<bool>` | Raised when value changes |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `ChildContent` | `RenderFragment?` | ChildContent property |
| `TriggerContent` | `RenderFragment?` | TriggerContent property |
| `Position` | `string` | Position property |
| `Trigger` | `PopoverTrigger` | Trigger property |
| `IsOpen` | `bool` | IsOpen property |
| `IsOpenChanged` | `EventCallback<bool>` | IsOpenChanged property |
| `object` | `Dictionary<string,` | object property |
| `PopoverTrigger` | `enum` | PopoverTrigger property |

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
