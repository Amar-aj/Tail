# Tail.Blazor.PhoneNumberInput

Independent NuGet package for the TailPhoneNumberInput component.

## Installation

```bash
dotnet add package Tail.Blazor.PhoneNumberInput
```

## Features

- Phone number input with country code selector
- Country code dropdown
- Phone number formatting
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.PhoneNumberInput;
```

## Component Usage

```razor
<TailPhoneNumberInput></TailPhoneNumberInput>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **PhoneNumber** | `string?` | - | PhoneNumber parameter |
| **SelectedCountryCode** | `string` | "+1" | SelectedCountryCode parameter |
| **Size** | `PhoneNumberInputSize` | PhoneNumberInputSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **PhoneNumberChanged** | `EventCallback<string?>` | Raised when value changes |
| **SelectedCountryCodeChanged** | `EventCallback<string>` | Raised when value changes |

## Enums

### PhoneNumberInputSize

```csharp
public enum PhoneNumberInputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// PhoneNumberInput size options.
///

### Tail.Blazor.PhoneNumberInput;.PhoneNumberInputSize

```csharp
public enum Tail.Blazor.PhoneNumberInput;.PhoneNumberInputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// PhoneNumberInput size options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.PhoneNumberInput

<TailPhoneNumberInput />
```

### Common Patterns

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailPhoneNumberInput Size="PhoneNumberInputSize.Md">
    Medium Size
</TailPhoneNumberInput>
```

**With Click Handler**

```razor
<TailPhoneNumberInput PhoneNumberChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailPhoneNumberInput>
```

**Disabled State**

```razor
<TailPhoneNumberInput Disabled="true">
    Disabled
</TailPhoneNumberInput>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailPhoneNumberInput />
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailPhoneNumberInput Size="PhoneNumberInputSize.Xs">Xs</TailPhoneNumberInput>
<TailPhoneNumberInput Size="PhoneNumberInputSize.Sm">Sm</TailPhoneNumberInput>
<TailPhoneNumberInput Size="PhoneNumberInputSize.Md">Md</TailPhoneNumberInput>
<TailPhoneNumberInput Size="PhoneNumberInputSize.Lg">Lg</TailPhoneNumberInput>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailPhoneNumberInput Disabled="true">Disabled</TailPhoneNumberInput>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailPhoneNumberInput PhoneNumberChanged="HandlePhoneNumberChanged">
    Click Me
</TailPhoneNumberInput>

@code {
    private void HandlePhoneNumberChanged(string? args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailPhoneNumberInput Size="PhoneNumberInputSize.Sm" PhoneNumber="Sample PhoneNumber" SelectedCountryCode="Sample SelectedCountryCode" Label="Sample Label" Placeholder="Sample Placeholder" />
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailPhoneNumberInput Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailPhoneNumberInput>

<TailPhoneNumberInput OnClick="ToggleProcessing">
    Toggle State
</TailPhoneNumberInput>

@code {
    private void ToggleProcessing()
    {
        isProcessing = !isProcessing;
        isDisabled = isProcessing;
    }
}
```

#### Custom Styling

```razor
@* Using Style parameter *@
<TailPhoneNumberInput Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailPhoneNumberInput>

@* Using Class parameter *@
<TailPhoneNumberInput Class="my-custom-class shadow-lg">
    With Custom Class
</TailPhoneNumberInput>
```

#### Multiple Event Handlers

```razor
<TailPhoneNumberInput 
    PhoneNumberChanged="OnFirstEvent"
    SelectedCountryCodeChanged="OnSecondEvent">
    Multiple Events
</TailPhoneNumberInput>

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
    
    <TailPhoneNumberInput Type="submit">
        Submit Form
    </TailPhoneNumberInput>
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
<TailPhoneNumberInput Label="Primary action button">
    Accessible Button
</TailPhoneNumberInput>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailPhoneNumberInput Size="PhoneNumberInputSize.Sm" PhoneNumberChanged="HandleAction" />
</div>

@code {
    private void HandleAction(string? args)
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

- **Package ID**: `Tail.Blazor.PhoneNumberInput`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
