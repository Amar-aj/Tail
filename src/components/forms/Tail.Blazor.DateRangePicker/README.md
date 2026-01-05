# Tail.Blazor.DateRangePicker

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

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| StartDate | DateTime? | - | StartDate parameter |
| EndDate | DateTime? | - | EndDate parameter |
| StartDateOnly | DateOnly? | - | StartDateOnly parameter |
| EndDateOnly | DateOnly? | - | EndDateOnly parameter |
| StartTimeOnly | TimeOnly? | - | StartTimeOnly parameter |
| EndTimeOnly | TimeOnly? | - | EndTimeOnly parameter |
| ShowTime | bool | false | ShowTime parameter |
| TimeOnlyMode | bool | false | TimeOnlyMode parameter |
| HourFormat | HourFormat | HourFormat.TwentyFourHour | HourFormat parameter |
| Size | DateRangePickerSize | DateRangePickerSize.Md | Size of the component |
| DisplayMode | DatePickerDisplayMode | DatePickerDisplayMode.InputAndPopup | DisplayMode parameter |
| ShowCalendarButton | bool | true | ShowCalendarButton parameter |
| Label | string? | - | Label text for the component |
| Placeholder | string? | "Select date range" | Placeholder text |
| StartPlaceholder | string? | - | Placeholder text |
| EndPlaceholder | string? | - | Placeholder text |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Required | bool | - | Whether the component is required |
| Disabled | bool | - | Whether the component is disabled |
| InitialViewDate | DateTime? | - | InitialViewDate parameter |
| YearRangeStart | int? | - | YearRangeStart parameter |
| YearRangeEnd | int? | - | YearRangeEnd parameter |
| InitialViewMode | DatePickerViewMode | DatePickerViewMode.Days | InitialViewMode parameter |
| SelectionMode | DateSelectionMode | DateSelectionMode.SingleRange | SelectionMode parameter |
| Animation | CalendarAnimation | CalendarAnimation.Fade | Animation parameter |
| AnimationDuration | int | 200 | AnimationDuration parameter |
| MinDate | DateTime? | - | Minimum value constraint |
| MaxDate | DateTime? | - | Maximum value constraint |
| MinDateOnly | DateOnly? | - | Minimum value constraint |
| MaxDateOnly | DateOnly? | - | Maximum value constraint |
| DisabledDates | List<DateTime> | new() | Whether the component is disabled |
| DisabledDateOnly | List<DateOnly> | new() | Whether the component is disabled |
| IsDateDisabled | Func<DateTime, bool>? | - | Whether the component is disabled |
| SpecialDates | List<DateTime> | new() | SpecialDates parameter |
| SpecialDateOnly | List<DateOnly> | new() | SpecialDateOnly parameter |
| GetDateClass | Func<DateTime, string?>? | - | Additional CSS classes |
| GetDateTooltip | Func<DateTime, string?>? | - | GetDateTooltip parameter |
| DateTemplate | RenderFragment<DateTime>? | - | DateTemplate parameter |
| FooterTemplate | RenderFragment? | - | FooterTemplate parameter |
| HeaderTemplate | RenderFragment? | - | HeaderTemplate parameter |
| CustomDateParser | Func<string, DateTime?>? | - | CustomDateParser parameter |
| CustomDateFormatter | Func<DateTime, string>? | - | CustomDateFormatter parameter |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| StartDateChanged | DateTime? | Raised when value changes |
| EndDateChanged | DateTime? | Raised when value changes |
| StartDateOnlyChanged | DateOnly? | Raised when value changes |
| EndDateOnlyChanged | DateOnly? | Raised when value changes |
| StartTimeOnlyChanged | TimeOnly? | Raised when value changes |
| EndTimeOnlyChanged | TimeOnly? | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailDateRangePicker></TailDateRangePicker>
```