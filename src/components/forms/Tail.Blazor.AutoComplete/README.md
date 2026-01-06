# Tail.Blazor.AutoComplete

Independent NuGet package for the TailAutoComplete component.

## Installation

```bash
dotnet add package Tail.Blazor.AutoComplete
```

## Features

- Autocomplete with suggestions dropdown
- Real-time filtering
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.AutoComplete;
```

## Component Usage

```razor
<TailAutoComplete></TailAutoComplete>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string?` | - | Current value of the component |
| **Items** | `List<string>?` | - | Data items collection |
| **Size** | `AutoCompleteSize` | AutoCompleteSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **MinChars** | `int` | 1 | Minimum value constraint |
| **MaxItems** | `int` | 10 | Maximum value constraint |
| **IsLoading** | `bool` | - | Whether the component is in loading state |
| **ItemTemplate** | `RenderFragment<string>?` | - | ItemTemplate parameter |
| **AriaLabel** | `string?` | - | Label text for the component |
| **Tooltip** | `string?` | - | Tooltip parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |
| **OnItemSelected** | `EventCallback<string>` | Raised with string value |
| **OnSearch** | `EventCallback<string>` | Raised with string value |

## Enums

### AutoCompleteSize

```csharp
public enum AutoCompleteSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// AutoComplete size options.
///

### Tail.Blazor.AutoComplete;.AutoCompleteSize

```csharp
public enum Tail.Blazor.AutoComplete;.AutoCompleteSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// AutoComplete size options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.AutoComplete

<TailAutoComplete>
    Hello, World!
</TailAutoComplete>
```

### Common Patterns

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailAutoComplete Size="AutoCompleteSize.Md">
    Medium Size
</TailAutoComplete>
```

**With Click Handler**

```razor
<TailAutoComplete ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailAutoComplete>
```

**Disabled State**

```razor
<TailAutoComplete Disabled="true">
    Disabled
</TailAutoComplete>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailAutoComplete>Content</TailAutoComplete>
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailAutoComplete Size="AutoCompleteSize.Xs">Xs</TailAutoComplete>
<TailAutoComplete Size="AutoCompleteSize.Sm">Sm</TailAutoComplete>
<TailAutoComplete Size="AutoCompleteSize.Md">Md</TailAutoComplete>
<TailAutoComplete Size="AutoCompleteSize.Lg">Lg</TailAutoComplete>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailAutoComplete Disabled="true">Disabled</TailAutoComplete>

@* Loading state *@
<TailAutoComplete IsLoading="true">Loading...</TailAutoComplete>

@* Both disabled and loading *@
<TailAutoComplete Disabled="true" IsLoading="true">Processing</TailAutoComplete>
```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailAutoComplete ValueChanged="HandleValueChanged">
    Click Me
</TailAutoComplete>

@code {
    private void HandleValueChanged(string? args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailAutoComplete Size="AutoCompleteSize.Sm" Value="Sample Value" Items="Sample Items" Label="Sample Label" Placeholder="Sample Placeholder">
    Combined Parameters
</TailAutoComplete>
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailAutoComplete Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailAutoComplete>

<TailAutoComplete OnClick="ToggleProcessing">
    Toggle State
</TailAutoComplete>

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

<TailAutoComplete @bind-Value="componentValue" ValueChanged="OnValueChanged">
    Bound Component
</TailAutoComplete>

<p>Current Value: @componentValue</p>

@code {
    private void OnValueChanged()
    {
        Console.WriteLine($"Value changed to: {componentValue}");
    }
}
```

#### With Tooltip

```razor
<TailAutoComplete Tooltip="This is a helpful tooltip">
    Hover for Tooltip
</TailAutoComplete>
```

#### Multiple Event Handlers

```razor
<TailAutoComplete 
    ValueChanged="OnFirstEvent"
    OnItemSelected="OnSecondEvent">
    Multiple Events
</TailAutoComplete>

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
    
    <TailAutoComplete Type="submit">
        Submit Form
    </TailAutoComplete>
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
<TailAutoComplete Label="Primary action button" Tooltip="Click to perform action">
    Accessible Button
</TailAutoComplete>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailAutoComplete Size="AutoCompleteSize.Sm" ValueChanged="HandleAction">
        Action Button
    </TailAutoComplete>
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

- **Package ID**: `Tail.Blazor.AutoComplete`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
