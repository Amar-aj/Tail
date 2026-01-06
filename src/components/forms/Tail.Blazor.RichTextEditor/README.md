# Tail.Blazor.RichTextEditor

Independent NuGet package for the TailRichTextEditor component.

## Installation

```bash
dotnet add package Tail.Blazor.RichTextEditor
```

## Features

- Rich text editor with formatting toolbar
- Bold, italic, underline formatting
- Content editable area
- Customizable min height
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.RichTextEditor;
```

## Component Usage

```razor
<TailRichTextEditor></TailRichTextEditor>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string?` | - | Current value of the component |
| **Size** | `RichTextEditorSize` | RichTextEditorSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **MinHeight** | `int` | 200 | Minimum value constraint |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **Style** | `string?` | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |

## Enums

### RichTextEditorSize

```csharp
public enum RichTextEditorSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// RichTextEditor size options.
///

### Tail.Blazor.RichTextEditor;.RichTextEditorSize

```csharp
public enum Tail.Blazor.RichTextEditor;.RichTextEditorSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// RichTextEditor size options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.RichTextEditor

<TailRichTextEditor />
```

### Common Patterns

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailRichTextEditor Size="RichTextEditorSize.Md">
    Medium Size
</TailRichTextEditor>
```

**With Click Handler**

```razor
<TailRichTextEditor ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailRichTextEditor>
```

**Disabled State**

```razor
<TailRichTextEditor Disabled="true">
    Disabled
</TailRichTextEditor>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailRichTextEditor />
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailRichTextEditor Size="RichTextEditorSize.Xs">Xs</TailRichTextEditor>
<TailRichTextEditor Size="RichTextEditorSize.Sm">Sm</TailRichTextEditor>
<TailRichTextEditor Size="RichTextEditorSize.Md">Md</TailRichTextEditor>
<TailRichTextEditor Size="RichTextEditorSize.Lg">Lg</TailRichTextEditor>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailRichTextEditor Disabled="true">Disabled</TailRichTextEditor>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailRichTextEditor ValueChanged="HandleValueChanged">
    Click Me
</TailRichTextEditor>

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
<TailRichTextEditor Size="RichTextEditorSize.Sm" Value="Sample Value" Label="Sample Label" MinHeight="10" />
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailRichTextEditor Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailRichTextEditor>

<TailRichTextEditor OnClick="ToggleProcessing">
    Toggle State
</TailRichTextEditor>

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

<TailRichTextEditor @bind-Value="componentValue" ValueChanged="OnValueChanged">
    Bound Component
</TailRichTextEditor>

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
<TailRichTextEditor Style="background-color: #3b82f6; color: white;">
    Custom Styled
</TailRichTextEditor>

@* Using Class parameter *@
<TailRichTextEditor Class="my-custom-class shadow-lg">
    With Custom Class
</TailRichTextEditor>
```

#### Form Integration

```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <TailRichTextEditor Type="submit">
        Submit Form
    </TailRichTextEditor>
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
<TailRichTextEditor Label="Primary action button">
    Accessible Button
</TailRichTextEditor>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailRichTextEditor Size="RichTextEditorSize.Sm" ValueChanged="HandleAction" />
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

- **Package ID**: `Tail.Blazor.RichTextEditor`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
