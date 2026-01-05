# Tail.Blazor.TagInput

Independent NuGet package for the TailTagInput component.

## Installation

```bash
dotnet add package Tail.Blazor.TagInput
```

## Features

- Tag input with add/remove functionality
- Enter to add tag
- Backspace to remove last tag
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Help text
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
| Tags | List<string> | new() | Tags parameter |
| Size | TagInputSize | TagInputSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| Placeholder | string? | - | Placeholder text |
| HelpText | string? | - | HelpText parameter |
| Disabled | bool | - | Whether the component is disabled |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| TagsChanged | List<string> | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailTagInput></TailTagInput>
```