# Tail.Blazor.DatePicker

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

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Value | DateTime? | - | Current value of the component |
| Size | DatePickerSize | DatePickerSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| HelpText | string? | - | HelpText parameter |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Required | bool | - | Whether the component is required |
| Disabled | bool | - | Whether the component is disabled |
| MinDate | DateTime? | - | Minimum value constraint |
| MaxDate | DateTime? | - | Maximum value constraint |
| IconStart | RenderFragment? | - | Icon to display |
| Clearable | bool | - | Clearable parameter |
| ShowTodayButton | bool | - | ShowTodayButton parameter |
| Placeholder | string? | - | Placeholder text |
| AriaLabel | string? | - | Label text for the component |
| Tooltip | string? | - | Tooltip parameter |
| Format | string | "dd-MM-yyyy" | Format parameter |
| IsDateDisabled | Func<DateTime, bool>? | - | Whether the component is disabled |
| Style | string? | - | Additional CSS styles |
| ShowTime | bool | - | ShowTime parameter |
| ShowSeconds | bool | - | ShowSeconds parameter |
| TimeFormat | string | "HH:mm" | TimeFormat parameter |
| IsTimeOnly | bool | - | IsTimeOnly parameter |
| SpecialDates | List<DateTime> | new() | SpecialDates parameter |
| InitialViewDate | DateTime | DateTime.Today | InitialViewDate parameter |
| YearRange | int | 10 | YearRange parameter |
| ShowCalendar | bool | true | ShowCalendar parameter |
| ShowInput | bool | true | ShowInput parameter |
| FooterTemplate | RenderFragment<DateTime>? | - | FooterTemplate parameter |
| CustomParser | Func<string, DateTime?>? | - | CustomParser parameter |
| MultipleSelection | bool | - | MultipleSelection parameter |
| SelectedDates | List<DateTime> | new() | SelectedDates parameter |
| ShowYearMonthSelection | bool | - | ShowYearMonthSelection parameter |
| DateOnlyValue | DateOnly? | - | Current value of the component |
| TimeOnlyValue | TimeOnly? | - | Current value of the component |

## Events

| Event | Type | Description |
| --- | --- | --- |
| ValueChanged | DateTime? | Raised when value changes |
| OnDateSelected | DateTime? | Raised with DateTime? value |
| OnDateChanged | DateTime? | Raised when value changes |
| SelectedDatesChanged | List<DateTime> | Raised when value changes |
| TimeOnlyValueChanged | TimeOnly? | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailDatePicker></TailDatePicker>
```