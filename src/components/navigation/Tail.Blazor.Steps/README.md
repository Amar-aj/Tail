# Tail.Blazor.Steps

Independent NuGet package for the TailSteps component.

## Installation

```bash
dotnet add package Tail.Blazor.Steps
```

## Features

- Step indicator
- Active step highlighting
- Completed step checkmarks
- Connector lines
- Title and description support
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Steps | List<StepItem> | new() | Step value for numeric inputs |
| CurrentStep | int | 1 | Step value for numeric inputs |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| StepItem | class | StepItem property |
| Title | string | Title property |
| Description | string? | Description property |

## Methods

No additional public methods.

## Examples

```razor
<TailSteps></TailSteps>
```