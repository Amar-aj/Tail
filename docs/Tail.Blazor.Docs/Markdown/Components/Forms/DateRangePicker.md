---
title: DateRangePicker
package: Tail.Blazor.DateRangePicker
category: forms
namespace: Tail.Blazor.DateRangePicker
route: /components/forms/daterangepicker
is_generic: false
is_missing: false
---

# DateRangePicker

Independent NuGet package for the TailDateRangePicker component.

## Installation

```bash
dotnet add package Tail.Blazor.DateRangePicker
```

## Features

- Date range selection (start and end dates)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Min/max date constraints
- Label support
- Validation error display
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.DateRangePicker;
```

## Basic Usage

```razor
<TailDateRangePicker>Content</TailDateRangePicker>
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.DateRangePicker

<TailDateRangePicker>
    Hello, World!
</TailDateRangePicker>
```

## Common Patterns

Frequently used patterns and combinations:

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailDateRangePicker Size="DateRangePickerSize.Md">
    Medium Size
</TailDateRangePicker>
```

**With Click Handler**

```razor
<TailDateRangePicker StartDateChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailDateRangePicker>
```

**Disabled State**

```razor
<TailDateRangePicker Disabled="true">
    Disabled
</TailDateRangePicker>
```

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailDateRangePicker Size="DateRangePickerSize.Xs">Xs</TailDateRangePicker>
<TailDateRangePicker Size="DateRangePickerSize.Sm">Sm</TailDateRangePicker>
<TailDateRangePicker Size="DateRangePickerSize.Md">Md</TailDateRangePicker>
<TailDateRangePicker Size="DateRangePickerSize.Lg">Lg</TailDateRangePicker>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailDateRangePicker Disabled="true">Disabled</TailDateRangePicker>
```

## Event Handling

Handle user interactions with event callbacks:

```razor
<TailDateRangePicker StartDateChanged="HandleStartDateChanged">
    Click Me
</TailDateRangePicker>

@code {
    private void HandleStartDateChanged(DateTime? args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailDateRangePicker Size="DateRangePickerSize.Sm">
    Combined Parameters
</TailDateRangePicker>
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
    <TailDateRangePicker Size="DateRangePickerSize.Sm" StartDateChanged="HandleAction">
        Action Button
    </TailDateRangePicker>
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
| **StartDate** | `DateTime?` | - | StartDate parameter |
| **EndDate** | `DateTime?` | - | EndDate parameter |
| **StartDateOnly** | `DateOnly?` | - | StartDateOnly parameter |
| **EndDateOnly** | `DateOnly?` | - | EndDateOnly parameter |
| **StartTimeOnly** | `TimeOnly?` | - | StartTimeOnly parameter |
| **EndTimeOnly** | `TimeOnly?` | - | EndTimeOnly parameter |
| **ShowTime** | `bool` | false | ShowTime parameter |
| **TimeOnlyMode** | `bool` | false | TimeOnlyMode parameter |
| **HourFormat** | `HourFormat` | HourFormat.TwentyFourHour | HourFormat parameter |
| **Size** | `DateRangePickerSize` | DateRangePickerSize.Md | Size of the component |
| **DisplayMode** | `DatePickerDisplayMode` | DatePickerDisplayMode.InputAndPopup | DisplayMode parameter |
| **ShowCalendarButton** | `bool` | true | ShowCalendarButton parameter |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | "Select date range" | Placeholder text |
| **StartPlaceholder** | `string?` | - | Placeholder text |
| **EndPlaceholder** | `string?` | - | Placeholder text |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **InitialViewDate** | `DateTime?` | - | InitialViewDate parameter |
| **YearRangeStart** | `int?` | - | YearRangeStart parameter |
| **YearRangeEnd** | `int?` | - | YearRangeEnd parameter |
| **InitialViewMode** | `DatePickerViewMode` | DatePickerViewMode.Days | InitialViewMode parameter |
| **SelectionMode** | `DateSelectionMode` | DateSelectionMode.SingleRange | SelectionMode parameter |
| **Animation** | `CalendarAnimation` | CalendarAnimation.Fade | Animation parameter |
| **AnimationDuration** | `int` | 200 | AnimationDuration parameter |
| **MinDate** | `DateTime?` | - | Minimum value constraint |
| **MaxDate** | `DateTime?` | - | Maximum value constraint |
| **MinDateOnly** | `DateOnly?` | - | Minimum value constraint |
| **MaxDateOnly** | `DateOnly?` | - | Maximum value constraint |
| **DisabledDates** | `List<DateTime>` | new() | Whether the component is disabled |
| **DisabledDateOnly** | `List<DateOnly>` | new() | Whether the component is disabled |
| **IsDateDisabled** | `Func<DateTime, bool>?` | - | Whether the component is disabled |
| **SpecialDates** | `List<DateTime>` | new() | SpecialDates parameter |
| **SpecialDateOnly** | `List<DateOnly>` | new() | SpecialDateOnly parameter |
| **GetDateClass** | `Func<DateTime, string?>?` | - | Additional CSS classes |
| **GetDateTooltip** | `Func<DateTime, string?>?` | - | GetDateTooltip parameter |
| **DateTemplate** | `RenderFragment<DateTime>?` | - | DateTemplate parameter |
| **FooterTemplate** | `RenderFragment?` | - | FooterTemplate parameter |
| **HeaderTemplate** | `RenderFragment?` | - | HeaderTemplate parameter |
| **CustomDateParser** | `Func<string, DateTime?>?` | - | CustomDateParser parameter |
| **CustomDateFormatter** | `Func<DateTime, string>?` | - | CustomDateFormatter parameter |
| **Style** | `string?` | - | Additional CSS styles |

### Events

| Event | Type | Description |
| --- | --- | --- |
| **StartDateChanged** | `EventCallback<DateTime?>` | Raised when value changes |
| **EndDateChanged** | `EventCallback<DateTime?>` | Raised when value changes |
| **StartDateOnlyChanged** | `EventCallback<DateOnly?>` | Raised when value changes |
| **EndDateOnlyChanged** | `EventCallback<DateOnly?>` | Raised when value changes |
| **StartTimeOnlyChanged** | `EventCallback<TimeOnly?>` | Raised when value changes |
| **EndTimeOnlyChanged** | `EventCallback<TimeOnly?>` | Raised when value changes |

### Enums

#### DateRangePickerSize

```csharp
public enum DateRangePickerSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// DateRangePicker size options.
///

#### Tail.Blazor.DateRangePicker;.DateRangePickerSize

```csharp
public enum Tail.Blazor.DateRangePicker;.DateRangePickerSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// DateRangePicker size options.
///

#### HourFormat

```csharp
public enum HourFormat
{
    TwelveHour,
}
```

/// Hour format options for time selection.
///

#### Tail.Blazor.DateRangePicker;.HourFormat

```csharp
public enum Tail.Blazor.DateRangePicker;.HourFormat
{
    TwelveHour,
}
```

/// Hour format options for time selection.
///

#### DatePickerViewMode

```csharp
public enum DatePickerViewMode
{
    Days,
    Months,
}
```

/// View mode for the date picker calendar.
///

#### Tail.Blazor.DateRangePicker;.DatePickerViewMode

```csharp
public enum Tail.Blazor.DateRangePicker;.DatePickerViewMode
{
    Days,
    Months,
}
```

/// View mode for the date picker calendar.
///

#### DateSelectionMode

```csharp
public enum DateSelectionMode
{
    SingleRange,
}
```

/// Selection mode for date picking.
///

#### Tail.Blazor.DateRangePicker;.DateSelectionMode

```csharp
public enum Tail.Blazor.DateRangePicker;.DateSelectionMode
{
    SingleRange,
}
```

/// Selection mode for date picking.
///

#### DatePickerDisplayMode

```csharp
public enum DatePickerDisplayMode
{
    InputAndPopup,
    InputOnly,
}
```

/// Display mode for the date picker.
///

#### Tail.Blazor.DateRangePicker;.DatePickerDisplayMode

```csharp
public enum Tail.Blazor.DateRangePicker;.DatePickerDisplayMode
{
    InputAndPopup,
    InputOnly,
}
```

/// Display mode for the date picker.
///

#### CalendarAnimation

```csharp
public enum CalendarAnimation
{
    None,
    Fade,
    SlideDown,
}
```

/// Animation type for calendar popup.
///

#### Tail.Blazor.DateRangePicker;.CalendarAnimation

```csharp
public enum Tail.Blazor.DateRangePicker;.CalendarAnimation
{
    None,
    Fade,
    SlideDown,
}
```

/// Animation type for calendar popup.
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
