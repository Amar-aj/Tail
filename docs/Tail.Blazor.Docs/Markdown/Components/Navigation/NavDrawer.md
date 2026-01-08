---
title: NavDrawer
package: Tail.Blazor.NavDrawer
category: navigation
namespace: Tail.Blazor.NavDrawer
route: /components/navigation/navdrawer
is_generic: false
is_missing: true
---

# NavDrawer



## Installation

```bash
dotnet add package Tail.Blazor.NavDrawer
```

## Namespace

```csharp
using Tail.Blazor.NavDrawer;
```

## Basic Usage

🚧 **Coming Soon** - This component is planned but not yet implemented.

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **ChildContent** | `RenderFragment?` | - | ChildContent parameter |
| **IsOpen** | `bool` | - | IsOpen parameter |
| **ShowCloseButton** | `bool` | true | ShowCloseButton parameter |
| **AdditionalAttributes** | `Dictionary<string, object>?` | - | AdditionalAttributes parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **IsOpenChanged** | `EventCallback<bool>` | Raised when value changes |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `ChildContent` | `RenderFragment?` | ChildContent property |
| `IsOpen` | `bool` | IsOpen property |
| `IsOpenChanged` | `EventCallback<bool>` | IsOpenChanged property |
| `ShowCloseButton` | `bool` | ShowCloseButton property |
| `object` | `Dictionary<string,` | object property |
| `Task` | `async` | Task property |
| `Task` | `async` | Task property |

### Public Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `Toggle()` | `None` | Invokes Toggle method |
| `Close()` | `None` | Invokes Close method |

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
