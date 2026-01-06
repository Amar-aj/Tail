# Tail.Blazor.AudioRecorder

Independent NuGet package for the TailAudioRecorder component.

## Installation

```bash
dotnet add package Tail.Blazor.AudioRecorder
```

## Features

- Audio recording functionality
- Start/stop recording
- Recording time display
- Audio playback
- Clear recording
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Namespace

```csharp
using Tail.Blazor.AudioRecorder;
```

## Component Usage

```razor
<TailAudioRecorder></TailAudioRecorder>
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **Value** | `string?` | - | Current value of the component |
| **Size** | `AudioRecorderSize` | AudioRecorderSize.Md | Size of the component |
| **Label** | `string?` | - | Label text for the component |
| **Disabled** | `bool` | - | Whether the component is disabled |
| **MaxRecordingTime** | `int` | 300 | Maximum value constraint |
| **Quality** | `AudioQuality` | AudioQuality.Medium | Quality parameter |
| **AriaLabel** | `string?` | - | Label text for the component |
| **Tooltip** | `string?` | - | Tooltip parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |
| **OnRecordingStart** | `EventCallback` | OnRecordingStart callback |
| **OnRecordingStop** | `EventCallback` | OnRecordingStop callback |
| **OnRecordingClear** | `EventCallback` | OnRecordingClear callback |

## Enums

### AudioRecorderSize

```csharp
public enum AudioRecorderSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// AudioRecorder size options.
///

### Tail.Blazor.AudioRecorder;.AudioRecorderSize

```csharp
public enum Tail.Blazor.AudioRecorder;.AudioRecorderSize
{
    Xs,
    Sm,
    Md,
    Lg,
}
```

/// AudioRecorder size options.
///

### AudioQuality

```csharp
public enum AudioQuality
{
    Low,
    Medium,
}
```

/// Audio recording quality options.
///

### Tail.Blazor.AudioRecorder;.AudioQuality

```csharp
public enum Tail.Blazor.AudioRecorder;.AudioQuality
{
    Low,
    Medium,
}
```

/// Audio recording quality options.
///

## Examples

This section provides comprehensive examples to help you get started with the component.

### Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.AudioRecorder

<TailAudioRecorder />
```

### Common Patterns

Frequently used patterns and combinations:

**Medium Size**

```razor
<TailAudioRecorder Size="AudioRecorderSize.Md">
    Medium Size
</TailAudioRecorder>
```

**With Click Handler**

```razor
<TailAudioRecorder ValueChanged="() => Console.WriteLine("Clicked")">
    Click Me
</TailAudioRecorder>
```

**Disabled State**

```razor
<TailAudioRecorder Disabled="true">
    Disabled
</TailAudioRecorder>
```

### Basic Usage

The simplest way to use the component:

```razor
<TailAudioRecorder />
```

### Sizes

Size options to fit different layouts and contexts:

```razor
<TailAudioRecorder Size="AudioRecorderSize.Xs">Xs</TailAudioRecorder>
<TailAudioRecorder Size="AudioRecorderSize.Sm">Sm</TailAudioRecorder>
<TailAudioRecorder Size="AudioRecorderSize.Md">Md</TailAudioRecorder>
<TailAudioRecorder Size="AudioRecorderSize.Lg">Lg</TailAudioRecorder>
```

### States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailAudioRecorder Disabled="true">Disabled</TailAudioRecorder>

```

### Event Handling

Handle user interactions with event callbacks:

```razor
<TailAudioRecorder ValueChanged="HandleValueChanged">
    Click Me
</TailAudioRecorder>

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
<TailAudioRecorder Size="AudioRecorderSize.Sm" Value="Sample Value" Label="Sample Label" MaxRecordingTime="10" />
```

### Advanced Examples

More complex usage scenarios:

#### Conditional Rendering

```razor
@code {
    private bool isProcessing = false;
    private bool isDisabled = false;
}

<TailAudioRecorder Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {
        <text>Processing...</text>
    }
    else
    {
        <text>Submit</text>
    }
</TailAudioRecorder>

<TailAudioRecorder OnClick="ToggleProcessing">
    Toggle State
</TailAudioRecorder>

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

<TailAudioRecorder @bind-Value="componentValue" ValueChanged="OnValueChanged">
    Bound Component
</TailAudioRecorder>

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
<TailAudioRecorder Tooltip="This is a helpful tooltip">
    Hover for Tooltip
</TailAudioRecorder>
```

#### Multiple Event Handlers

```razor
<TailAudioRecorder 
    ValueChanged="OnFirstEvent"
    OnRecordingStart="OnSecondEvent">
    Multiple Events
</TailAudioRecorder>

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
    
    <TailAudioRecorder Type="submit">
        Submit Form
    </TailAudioRecorder>
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
<TailAudioRecorder Label="Primary action button" Tooltip="Click to perform action">
    Accessible Button
</TailAudioRecorder>
```

### Real-World Example

A complete example showing practical usage:

```razor
@page "/example"

<h3>Component Demo</h3>

<div class="space-y-4">
    <TailAudioRecorder Size="AudioRecorderSize.Sm" ValueChanged="HandleAction" />
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

- **Package ID**: `Tail.Blazor.AudioRecorder`
- **Version**: 1.0.0
- **License**: MIT
- **Authors**: Tail.Blazor Core Team
- **Repository**: https://github.com/tailblazor/tailblazor
