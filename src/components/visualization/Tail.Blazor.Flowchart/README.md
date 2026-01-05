# Tail.Blazor.Flowchart

Independent NuGet package for the TailFlowchart component.

## Installation

```bash
dotnet add package Tail.Blazor.Flowchart
```

## Features

- Flowchart visualization
- Nodes and connections
- SVG-based rendering
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| Nodes | List<FlowchartNode> | new() | Nodes parameter |
| Connections | List<FlowchartConnection> | new() | Connections parameter |
| Width | int | 800 | Width parameter |
| Height | int | 600 | Height parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| FlowchartNode | class | FlowchartNode property |
| Id | string | Id property |
| Label | string | Label property |
| X | double | X property |
| Y | double | Y property |
| FlowchartConnection | class | FlowchartConnection property |
| FromId | string | FromId property |
| ToId | string | ToId property |
| FromX | double | FromX property |
| FromY | double | FromY property |
| ToX | double | ToX property |
| ToY | double | ToY property |

## Methods

No additional public methods.

## Examples

```razor
<TailFlowchart></TailFlowchart>
```