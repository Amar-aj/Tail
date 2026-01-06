# Tail.Blazor.Input

Independent NuGet package for the TailInput component.

## Installation

```bash
dotnet add package Tail.Blazor.Input
```

## Features

- Multiple input types (Text, Password, Email, Number, Tel, Url, Search, Date, etc.)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label and help text support
- Icon support (start/end)
- Clear button
- Character count
- Validation error display
- Required field indicator
- Disabled and readonly states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.Input;
```

## Component Usage

```razor
<TailInput></TailInput>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string?` | - | Current value of the component |
| **Type** | `InputType` | InputType.Text | Type parameter |
| **Size** | `InputSize` | InputSize.Md | Size of the component |
| **Variant** | `InputVariant` | InputVariant.Standard | Visual variant style for the component |
| **Label** | `string?` | - | Label text for the component |
| **Placeholder** | `string?` | - | Placeholder text |
| **HelpText** | `string?` | - | HelpText parameter |
| **ErrorMessage** | `string?` | - | ErrorMessage parameter |
| **Required** | `bool` | - | Whether the component is required |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **ReadOnly** | `bool` | - | Whether the component is read-only |
| **MaxLength** | `int?` | - | Maximum value constraint |
| **ShowClearButton** | `bool` | - | ShowClearButton parameter |
| **ShowCharacterCount** | `bool` | - | ShowCharacterCount parameter |
| **FloatingLabel** | `bool` | - | Label text for the component |
| **IconStart** | `RenderFragment?` | - | Icon to display |
| **IconEnd** | `RenderFragment?` | - | Icon to display |
| **AdornmentStart** | `string?` | - | AdornmentStart parameter |
| **AdornmentEnd** | `string?` | - | AdornmentEnd parameter |
| **Style** | `string?` | - | Additional CSS styles |
| **Min** | `string?` | - | Minimum value constraint |
| **Max** | `string?` | - | Maximum value constraint |
| **Step** | `string?` | - | Step value for numeric inputs |
| **Pattern** | `string?` | - | Validation pattern (regex) |
| **AutoComplete** | `string?` | - | AutoComplete parameter |
| **AutoFocus** | `bool` | false | AutoFocus parameter |
| **AriaLabel** | `string?` | - | Label text for the component |
| **EnableAnimation** | `bool` | true | EnableAnimation parameter |
| **AnimationDuration** | `int` | 200 | AnimationDuration parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |
| **OnFocus** | `EventCallback<FocusEventArgs>` | Raised when focus is gained |
| **OnBlur** | `EventCallback<FocusEventArgs>` | Raised when focus is lost |
| **OnKeyDown** | `EventCallback<KeyboardEventArgs>` | Raised on key down |

## Enums

### InputType

```csharp
public enum InputType
{
    Text,
    Password,
    Email,
    Number,
    Tel,
    Url,
    Search,
    Date,
    DateTimeLocal,
    Time,
    Month,
}
```

/// Input type options.
///

### Tail.Blazor.Input;.InputType

```csharp
public enum Tail.Blazor.Input;.InputType
{
    Text,
    Password,
    Email,
    Number,
    Tel,
    Url,
    Search,
    Date,
    DateTimeLocal,
    Time,
    Month,
}
```

/// Input type options.
///

### InputSize

```csharp
public enum InputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Input size options.
///

### Tail.Blazor.Input;.InputSize

```csharp
public enum Tail.Blazor.Input;.InputSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// Input size options.
///

### InputVariant

```csharp
public enum InputVariant
{
    Standard,
    Outlined,
}
```

/// Input variant options (visual style).
///

### Tail.Blazor.Input;.InputVariant

```csharp
public enum Tail.Blazor.Input;.InputVariant
{
    Standard,
    Outlined,
}
```

/// Input variant options (visual style).
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.Input

<TailInput>
    Hello, World!
</TailInput>
```

### Common Patterns

Frequently used patterns and combinations:

**Primary Action**

```razor
<TailInput Variant="InputVariant.Standard">
    Primary Action
</TailInput>
```

**Medium Size**

```razor
<TailInput Size="InputSize.Md">
    Medium Size
</TailInput>
```

**With Click Handler**

```razor
<TailInput ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailInput>
```

**Disabled State**

```razor
<TailInput Disabled="true">
    Disabled
</TailInput>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailInput>Content</TailInput>
```

### Variants

Different visual variants for various use cases:

```razor
<TailInput Variant="InputVariant.Standard">Standard</TailInput>
<TailInput Variant="InputVariant.Outlined">Outlined</TailInput>
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailInput Size="InputSize.Xs">Xs</TailInput>
<TailInput Size="InputSize.Sm">Sm</TailInput>
<TailInput Size="InputSize.Md">Md</TailInput>
<TailInput Size="InputSize.Lg">Lg</TailInput>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailInput Disabled="true">Disabled</TailInput>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailInput ValueChanged="HandleValueChanged">
    Click Me
</TailInput>

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
<TailInput Variant="InputVariant.Standard" Size="InputSize.Sm" Value="Sample Value" Label="Sample Label">
    Combined Parameters
</TailInput>
```

### Advanced Examples

More complex usage scenarios:

#### With Icons

```razor
<TailInput>
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
</TailInput>
```

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailInput Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailInput>

<TailInput OnClick="ToggleProcessing">
    Toggle State
</TailInput>

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

<TailInput @bind-Value="componentValue" ValueChanged="OnValueChanged">
    Bound Component
</TailInput>

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
<TailInput Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailInput>

@* Using Class parameter *@
<TailInput Class="my-custom-class shadow-lg">
    With Custom Class
</TailInput>
```

#### Multiple Event Handlers

```razor
<TailInput 
    ValueChanged="OnFirstEvent"
    OnFocus="OnSecondEvent">
    Multiple Events
</TailInput>

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
    
    <TailInput Type="submit">
        Submit Form
    </TailInput>
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
<TailInput Variant="Primary action button">
    Accessible Button
</TailInput>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailInput Variant="InputVariant.Standard" Size="InputSize.Sm" ValueChanged="HandleAction">
        Action Button
    </TailInput>
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

- **Package ID**: `Tail.Blazor.Input`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
