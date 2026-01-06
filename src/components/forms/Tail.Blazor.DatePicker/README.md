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

## Namespace

```csharp
using Tail.Blazor.DatePicker;
```

## Component Usage

```razor
<TailDatePicker></TailDatePicker>
```

## Parameters

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

## Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<DateTime?>` | Raised when value changes |
| **OnDateSelected** | `EventCallback<DateTime?>` | Raised with DateTime? value |
| **OnDateChanged** | `EventCallback<DateTime?>` | Raised when value changes |
| **SelectedDatesChanged** | `EventCallback<List<DateTime>>` | Raised when value changes |
| **TimeOnlyValueChanged** | `EventCallback<TimeOnly?>` | Raised when value changes |

## Enums

### DatePickerSize

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

### Tail.Blazor.DatePicker;.DatePickerSize

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

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.DatePicker

<TailDatePicker>
    Hello, World!
</TailDatePicker>
```

### Common Patterns

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

### Basic Usage

The simplest way to use the component:

```razor
<TailDatePicker>Content</TailDatePicker>
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailDatePicker Size="DatePickerSize.Xs">Xs</TailDatePicker>
<TailDatePicker Size="DatePickerSize.Sm">Sm</TailDatePicker>
<TailDatePicker Size="DatePickerSize.Md">Md</TailDatePicker>
<TailDatePicker Size="DatePickerSize.Lg">Lg</TailDatePicker>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailDatePicker Disabled="true">Disabled</TailDatePicker>

```

### Event Handling

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

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailDatePicker Size="DatePickerSize.Sm" Label="Sample Label" HelpText="Sample HelpText" ErrorMessage="Sample ErrorMessage">
    Combined Parameters
</TailDatePicker>
```

### Advanced Examples

More complex usage scenarios:

#### With Icons

```razor
<TailDatePicker>
    <IconStart>
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
    </IconStart>
    Button Text
    <IconEnd>
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
        </svg>
    </IconEnd>
</TailDatePicker>
```

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailDatePicker Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailDatePicker>

<TailDatePicker OnClick="ToggleProcessing">
    Toggle State
</TailDatePicker>

@code {
    private void ToggleProcessing()
    {
        isProcessing = !isProcessing;
        isDisabled = isProcessing;
    }
}
```

#### Data Binding

```razor
@code {
    private string componentValue = "";
}

<TailDatePicker @bind-Value="componentValue" ValueChanged="OnValueChanged">
    Bound Component
</TailDatePicker>

<p>Current Value: @componentValue</p>

@code {
    private void OnValueChanged()
    {
        Console.WriteLine($"Value changed to: {componentValue}");
    }
}
```

#### Custom Styling

```razor
@* Using Style parameter *@
<TailDatePicker Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailDatePicker>

@* Using Class parameter *@
<TailDatePicker Class="my-custom-class shadow-lg">
    With Custom Class
</TailDatePicker>
```

#### With Tooltip

```razor
<TailDatePicker Tooltip="This is a helpful tooltip">
    Hover for Tooltip
</TailDatePicker>
```

#### Multiple Event Handlers

```razor
<TailDatePicker 
    ValueChanged="OnFirstEvent"
    OnDateSelected="OnSecondEvent">
    Multiple Events
</TailDatePicker>

@code {
    private void OnFirstEvent()
    {
        Console.WriteLine("First event triggered");
    }
    
    private void OnSecondEvent()
    {
        Console.WriteLine("Second event triggered");
    }
}
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailDatePicker Type="submit">
        Submit Form
    </TailDatePicker>
</EditForm>

@code {
    private MyModel model = new();
    
    private void HandleSubmit()
    {
        // Process form submission
        Console.WriteLine("Form submitted successfully");
    }
}
```

#### Accessibility

```razor
@* Accessible component with ARIA label and tooltip *@
<TailDatePicker Label="Primary action button" Tooltip="Click to perform action">
    Accessible Button
</TailDatePicker>
```

### Real-World Example

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

## Package Information

- **Package ID**: `Tail.Blazor.DatePicker`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
