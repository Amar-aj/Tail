---
title: DatePicker
package: Tail.Blazor.DatePicker
category: forms
namespace: Tail.Blazor.DatePicker
route: /components/forms/datepicker
is_generic: false
is_missing: false
---

# DatePicker

Independent NuGet package for the TailDatePicker component.

## Installation

```bash
dotnet add package Tail.Blazor.DatePicker
```

## Features

- Date input with calendar picker
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Min/max date constraints
- Label and help text support
- Icon support
- Validation error display
- Required field indicator
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.DatePicker;
```

## Basic Usage

```razor
<TailDatePicker>Content</TailDatePicker>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.DatePicker

<TailDatePicker>
    Hello, World!
</TailDatePicker>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailDatePicker Size="DatePickerSize.Md">
    Medium Size
</TailDatePicker>
```

**With Click Handler**

```razor
<TailDatePicker ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailDatePicker>
```

**Disabled State**

```razor
<TailDatePicker Disabled="true">
    Disabled
</TailDatePicker>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailDatePicker Size="DatePickerSize.Xs">Xs</TailDatePicker>
<TailDatePicker Size="DatePickerSize.Sm">Sm</TailDatePicker>
<TailDatePicker Size="DatePickerSize.Md">Md</TailDatePicker>
<TailDatePicker Size="DatePickerSize.Lg">Lg</TailDatePicker>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailDatePicker Disabled="true">Disabled</TailDatePicker>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailDatePicker ValueChanged="HandleValueChanged">
    Click Me
</TailDatePicker>

@code {
    private void HandleValueChanged(DateTime? args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailDatePicker Size="DatePickerSize.Sm" Label="Sample Label" HelpText="Sample HelpText" ErrorMessage="Sample ErrorMessage">
    Combined Parameters
</TailDatePicker>
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
    <TailDatePicker Size="DatePickerSize.Sm" ValueChanged="HandleAction">
        Action Button
    </TailDatePicker>
</div>

@code {
    private void HandleAction(DateTime? args)
    {
        // Perform action
        Console.WriteLine("Action executed");
    }
}
```

## API Reference

### Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `DateTime?` | - | Current value of the component |
| **Size** | `DatePickerSize` | DatePickerSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **HelpText** | `string?` | - | HelpText parameter |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **MinDate** | `DateTime?` | - | Minimum value constraint |
| **MaxDate** | `DateTime?` | - | Maximum value constraint |
| **IconStart** | `RenderFragment?` | - | Icon to display |
| **Clearable** | `bool` | - | Clearable parameter |
| **ShowTodayButton** | `bool` | - | ShowTodayButton parameter |
| **Placeholder** | `string?` | - | Placeholder text |
| **AriaLabel** | `string?` | - | Label text for the component |
| **Tooltip** | `string?` | - | Tooltip parameter |
| **Format** | `string` | "dd-MM-yyyy" | Format parameter |
| **IsDateDisabled** | `Func<DateTime, bool>?` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |
| **ShowTime** | `bool` | - | ShowTime parameter |
| **ShowSeconds** | `bool` | - | ShowSeconds parameter |
| **TimeFormat** | `string` | "HH:mm" | TimeFormat parameter |
| **IsTimeOnly** | `bool` | - | IsTimeOnly parameter |
| **SpecialDates** | `List<DateTime>` | new() | SpecialDates parameter |
| **InitialViewDate** | `DateTime` | DateTime.Today | InitialViewDate parameter |
| **YearRange** | `int` | 10 | YearRange parameter |
| **ShowCalendar** | `bool` | true | ShowCalendar parameter |
| **ShowInput** | `bool` | true | ShowInput parameter |
| **FooterTemplate** | `RenderFragment<DateTime>?` | - | FooterTemplate parameter |
| **CustomParser** | `Func<string, DateTime?>?` | - | CustomParser parameter |
| **MultipleSelection** | `bool` | - | MultipleSelection parameter |
| **SelectedDates** | `List<DateTime>` | new() | SelectedDates parameter |
| **ShowYearMonthSelection** | `bool` | - | ShowYearMonthSelection parameter |
| **DateOnlyValue** | `DateOnly?` | - | Current value of the component |
| **TimeOnlyValue** | `TimeOnly?` | - | Current value of the component |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<DateTime?>` | Raised when value changes |
| **OnDateSelected** | `EventCallback<DateTime?>` | Raised with DateTime? value |
| **OnDateChanged** | `EventCallback<DateTime?>` | Raised when value changes |
| **SelectedDatesChanged** | `EventCallback<List<DateTime>>` | Raised when value changes |
| **TimeOnlyValueChanged** | `EventCallback<TimeOnly?>` | Raised when value changes |

### Enums

#### DatePickerSize

```csharp
public enum DatePickerSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// DatePicker size options.
///

#### Tail.Blazor.DatePicker;.DatePickerSize

```csharp
public enum Tail.Blazor.DatePicker;.DatePickerSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// DatePicker size options.
///

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
