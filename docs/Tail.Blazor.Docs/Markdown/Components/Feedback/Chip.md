---
title: Chip
package: Tail.Blazor.Chip
category: feedback
namespace: Tail.Blazor.Chip
route: /components/feedback/chip
is_generic: false
is_missing: true
---

# Chip



## Installation

```bash
dotnet add package Tail.Blazor.Chip
```

## Namespace

```csharp
using Tail.Blazor.Chip;
```

## Basic Usage

🚧 **Coming Soon** - This component is planned but not yet implemented.

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Label** | `string` | - | Label text for the component |
| **Icon** | `string?` | - | Icon to display |
| **Removable** | `bool` | - | Removable parameter |
| **Variant** | `string` | "default" | Visual variant style for the component |
| **AdditionalAttributes** | `Dictionary<string, object>?` | - | AdditionalAttributes parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnRemove** | `EventCallback` | OnRemove callback |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `Label` | `string` | Label property |
| `Icon` | `string?` | Icon property |
| `Removable` | `bool` | Removable property |
| `OnRemove` | `EventCallback` | OnRemove property |
| `Variant` | `string` | Variant property |
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
