# Tail.Blazor.MultiSelect

Independent NuGet package for the TailMultiSelect component.

## Installation

```bash
dotnet add package Tail.Blazor.MultiSelect
```

## Features

- Multi-selection dropdown
- Tag display for selected items
- Search functionality (can be added)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Placeholder text
- Validation error display
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.MultiSelect;
```

## Component Usage

```razor
<TailMultiSelect></TailMultiSelect>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **SelectedValues** | `List<string>?` | - | Current value of the component |
| **Items** | `List<MultiSelectItem>?` | - | Data items collection |
| **Size** | `MultiSelectSize` | MultiSelectSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **SelectedValuesChanged** | `EventCallback<List<string>>` | Raised when value changes |

## Enums

### MultiSelectSize

```csharp
public enum MultiSelectSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// MultiSelect size options.
///

### Tail.Blazor.MultiSelect;.MultiSelectSize

```csharp
public enum Tail.Blazor.MultiSelect;.MultiSelectSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// MultiSelect size options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.MultiSelect

<TailMultiSelect />
```

### Common Patterns

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailMultiSelect Size="MultiSelectSize.Md">
    Medium Size
</TailMultiSelect>
```

**With Click Handler**

```razor
<TailMultiSelect SelectedValuesChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailMultiSelect>
```

**Disabled State**

```razor
<TailMultiSelect Disabled="true">
    Disabled
</TailMultiSelect>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailMultiSelect />
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailMultiSelect Size="MultiSelectSize.Xs">Xs</TailMultiSelect>
<TailMultiSelect Size="MultiSelectSize.Sm">Sm</TailMultiSelect>
<TailMultiSelect Size="MultiSelectSize.Md">Md</TailMultiSelect>
<TailMultiSelect Size="MultiSelectSize.Lg">Lg</TailMultiSelect>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailMultiSelect Disabled="true">Disabled</TailMultiSelect>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailMultiSelect SelectedValuesChanged="HandleSelectedValuesChanged">
    Click Me
</TailMultiSelect>

@code {
    private void HandleSelectedValuesChanged(Tail.Blazor.MultiSelect.List<string> args)
    {
        // Handle the event
        Console.WriteLine($"Event triggered: {args}");
    }
}
```

### Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailMultiSelect Size="MultiSelectSize.Sm" SelectedValues="Sample SelectedValues" Label="Sample Label" Placeholder="Sample Placeholder" />
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailMultiSelect Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailMultiSelect>

<TailMultiSelect OnClick="ToggleProcessing">
    Toggle State
</TailMultiSelect>

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

<TailMultiSelect @bind-Value="componentValue" SelectedValuesChanged="OnValueChanged">
    Bound Component
</TailMultiSelect>

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
<TailMultiSelect Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailMultiSelect>

@* Using Class parameter *@
<TailMultiSelect Class="my-custom-class shadow-lg">
    With Custom Class
</TailMultiSelect>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailMultiSelect Type="submit">
        Submit Form
    </TailMultiSelect>
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
<TailMultiSelect Label="Primary action button">
    Accessible Button
</TailMultiSelect>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailMultiSelect Size="MultiSelectSize.Sm" SelectedValuesChanged="HandleAction" />
</div>

@code {
    private void HandleAction(List<string> args)
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

- **Package ID**: `Tail.Blazor.MultiSelect`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
