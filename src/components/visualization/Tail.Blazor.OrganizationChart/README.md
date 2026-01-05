# Tail.Blazor.OrganizationChart

Independent NuGet package for the TailOrganizationChart component.

## Installation

```bash
dotnet add package Tail.Blazor.OrganizationChart
```

## Features

- Organization chart
- Hierarchical structure
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| RootNode | OrganizationNode | default! | RootNode parameter |
| Style | string? | - | Additional CSS styles |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| OrganizationNode | class | OrganizationNode property |
| Name | string | Name property |
| Children | List<OrganizationNode> | Children property |

## Methods

No additional public methods.

## Examples

```razor
<TailOrganizationChart></TailOrganizationChart>
```