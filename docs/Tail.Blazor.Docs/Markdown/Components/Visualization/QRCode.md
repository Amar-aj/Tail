---
title: QRCode
package: Tail.Blazor.QRCode
category: visualization
namespace: Tail.Blazor.QRCode
route: /components/visualization/qrcode
is_generic: false
is_missing: false
---

# QRCode

Independent NuGet package for the TailQRCode component.

## Installation

```bash
dotnet add package Tail.Blazor.QRCode
```

## Features

- QR code generation
- Customizable size
- SVG-based rendering
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.QRCode;
```

## Basic Usage

```razor
<TailQRCode />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.QRCode

<TailQRCode />
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailQRCode Size="12">Small</TailQRCode>
<TailQRCode Size="16">Medium</TailQRCode>
<TailQRCode Size="24">Large</TailQRCode>
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailQRCode Value="Sample Value" Style="Sample Style" />
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
    <TailQRCode  />
</div>

@code {
    // Component logic here
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string` | string.Empty | Current value of the component |
| **Size** | `int` | 200 | Size of the component |
| **Style** | `string?` | - | Additional CSS styles |

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
