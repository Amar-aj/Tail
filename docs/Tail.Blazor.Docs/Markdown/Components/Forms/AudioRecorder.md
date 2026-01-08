---
title: AudioRecorder
package: Tail.Blazor.AudioRecorder
category: forms
namespace: Tail.Blazor.AudioRecorder
route: /components/forms/audiorecorder
is_generic: false
is_missing: false
---

# AudioRecorder

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

## Basic Usage

```razor
<TailAudioRecorder />
```

## Quick Start

Get up and running in seconds:

```razor
@page "/quickstart"
@using Tail.Blazor.AudioRecorder

<TailAudioRecorder />
```

## Common Patterns

Frequently used patterns and combinations:

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

## Sizes

Size options to fit different layouts and contexts:

```razor
<TailAudioRecorder Size="AudioRecorderSize.Xs">Xs</TailAudioRecorder>
<TailAudioRecorder Size="AudioRecorderSize.Sm">Sm</TailAudioRecorder>
<TailAudioRecorder Size="AudioRecorderSize.Md">Md</TailAudioRecorder>
<TailAudioRecorder Size="AudioRecorderSize.Lg">Lg</TailAudioRecorder>
```

## States

Component states for different interaction scenarios:

```razor
@* Disabled state *@
<TailAudioRecorder Disabled="true">Disabled</TailAudioRecorder>
```

## Event Handling

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

## Parameter Combinations

Combine multiple parameters for advanced usage:

```razor
<TailAudioRecorder Size="AudioRecorderSize.Sm" Value="Sample Value" Label="Sample Label" MaxRecordingTime="10" />
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

## API Reference

### Parameters

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

### Events

| Event | Type | Description |
| --- | --- | --- |
| **ValueChanged** | `EventCallback<string?>` | Raised when value changes |
| **OnRecordingStart** | `EventCallback` | OnRecordingStart callback |
| **OnRecordingStop** | `EventCallback` | OnRecordingStop callback |
| **OnRecordingClear** | `EventCallback` | OnRecordingClear callback |

### Enums

#### AudioRecorderSize

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

#### Tail.Blazor.AudioRecorder;.AudioRecorderSize

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

#### AudioQuality

```csharp
public enum AudioQuality
{
    Low,
    Medium,
}
```

/// Audio recording quality options.
///

#### Tail.Blazor.AudioRecorder;.AudioQuality

```csharp
public enum Tail.Blazor.AudioRecorder;.AudioQuality
{
    Low,
    Medium,
}
```

/// Audio recording quality options.
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
