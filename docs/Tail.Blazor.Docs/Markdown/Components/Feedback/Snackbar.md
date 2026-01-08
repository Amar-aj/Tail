---
title: Snackbar
package: Tail.Blazor.Snackbar
category: feedback
namespace: Tail.Blazor.Snackbar
route: /components/feedback/snackbar
is_generic: false
is_missing: true
---

# Snackbar



## Installation

```bash
dotnet add package Tail.Blazor.Snackbar
```

## Namespace

```csharp
using Tail.Blazor.Snackbar;
```

## Basic Usage

🚧 **Coming Soon** - This component is planned but not yet implemented.

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Message** | `string` | - | Message parameter |
| **ActionText** | `string?` | - | ActionText parameter |
| **ShowClose** | `bool` | true | ShowClose parameter |
| **Position** | `string` | "bottom" | Position parameter |
| **AdditionalAttributes** | `Dictionary<string, object>?` | - | AdditionalAttributes parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnAction** | `EventCallback` | OnAction callback |
| **OnClose** | `EventCallback` | OnClose callback |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `Message` | `string` | Message property |
| `ActionText` | `string?` | ActionText property |
| `OnAction` | `EventCallback` | OnAction property |
| `OnClose` | `EventCallback` | OnClose property |
| `ShowClose` | `bool` | ShowClose property |
| `Position` | `string` | Position property |
| `object` | `Dictionary<string,` | object property |

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
