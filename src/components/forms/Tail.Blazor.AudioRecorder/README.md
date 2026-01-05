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

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Value | string? | - | Current value of the component |
| Size | AudioRecorderSize | AudioRecorderSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| Disabled | bool | - | Whether the component is disabled |
| MaxRecordingTime | int | 300 | Maximum value constraint |
| Quality | AudioQuality | AudioQuality.Medium | Quality parameter |
| AriaLabel | string? | - | Label text for the component |
| Tooltip | string? | - | Tooltip parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| ValueChanged | string? | Raised when value changes |
| OnRecordingStart | void | OnRecordingStart callback |
| OnRecordingStop | void | OnRecordingStop callback |
| OnRecordingClear | void | OnRecordingClear callback |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailAudioRecorder></TailAudioRecorder>
```