# Tail.Blazor.Textarea

Independent NuGet package for the TailTextarea component.

## Installation

```bash
dotnet add package Tail.Blazor.Textarea
```

## Features

- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label and help text support
- Character count display
- Auto-resize option
- Validation error display
- Required field indicator
- Disabled and readonly states
- Customizable rows
- Max length support
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
| Size | TextareaSize | TextareaSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| Placeholder | string? | - | Placeholder text |
| HelpText | string? | - | HelpText parameter |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Required | bool | - | Whether the component is required |
| Disabled | bool | - | Whether the component is disabled |
| ReadOnly | bool | - | Whether the component is read-only |
| Rows | int | 3 | Rows parameter |
| MaxLength | int? | - | Maximum value constraint |
| ShowCharacterCount | bool | - | ShowCharacterCount parameter |
| AutoResize | bool | - | Size of the component |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| ValueChanged | string? | Raised when value changes |
| OnFocus | FocusEventArgs | Raised when focus is gained |
| OnBlur | FocusEventArgs | Raised when focus is lost |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailTextarea></TailTextarea>
```