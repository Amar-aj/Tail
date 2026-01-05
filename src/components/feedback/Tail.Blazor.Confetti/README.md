# Tail.Blazor.Confetti

Independent NuGet package for the TailConfetti component.

## Installation

```bash
dotnet add package Tail.Blazor.Confetti
```

## Features

- Confetti animation
- 4 shape types (Circle, Rectangle, Star, Mixed)
- Customizable particle count
- Duration control
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| IsActive | bool | - | IsActive parameter |
| ParticleCount | int | 50 | ParticleCount parameter |
| Shape | ConfettiShape | ConfettiShape.Mixed | Shape parameter |
| Duration | int | 3000 | Duration parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailConfetti></TailConfetti>
```