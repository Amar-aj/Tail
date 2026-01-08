---
title: BottomNavigation
package: Tail.Blazor.BottomNavigation
category: navigation
namespace: Tail.Blazor.BottomNavigation
route: /components/navigation/bottomnavigation
is_generic: false
is_missing: true
---

# BottomNavigation



## Installation

```bash
dotnet add package Tail.Blazor.BottomNavigation
```

## Namespace

```csharp
using Tail.Blazor.BottomNavigation;
```

## Basic Usage

🚧 **Coming Soon** - This component is planned but not yet implemented.

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Items** | `List<NavItem>` | new() | Data items collection |
| **ActiveItemId** | `string?` | - | ActiveItemId parameter |
| **AdditionalAttributes** | `Dictionary<string, object>?` | - | AdditionalAttributes parameter |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **OnItemSelected** | `EventCallback<NavItem>` | Raised with NavItem value |

### Public Properties

| Property | Type | Description |
| --- | --- | --- |
| `Items` | `List<NavItem>` | Items property |
| `ActiveItemId` | `string?` | ActiveItemId property |
| `OnItemSelected` | `EventCallback<NavItem>` | OnItemSelected property |
| `object` | `Dictionary<string,` | object property |
| `NavItem` | `class` | NavItem property |
| `Id` | `string` | Id property |
| `Label` | `string?` | Label property |
| `Icon` | `string?` | Icon property |
| `Target` | `string?` | Target property |

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
