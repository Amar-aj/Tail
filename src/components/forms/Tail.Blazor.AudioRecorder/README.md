# Tail.Blazor.AudioRecorder

Independent NuGet package for the TailAudioRecorder component.

## Installation

```bash
dotnet add package Tail.Blazor.AudioRecorder
```

## Usage

```razor
@using Tail.Blazor.AudioRecorder

<TailAudioRecorder @bind-Value="audioData" Label="Record Audio" />
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

## Package Size

~5 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

