# Tail.Blazor.Input

Independent NuGet package for the TailInput component.

## Installation

```bash
dotnet add package Tail.Blazor.Input
```

## Features

- Multiple input types (Text, Password, Email, Number, Tel, Url, Search, Date, etc.)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label and help text support
- Icon support (start/end)
- Clear button
- Character count
- Validation error display
- Required field indicator
- Disabled and readonly states
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
| Type | InputType | InputType.Text | Type parameter |
| Size | InputSize | InputSize.Md | Size of the component |
| Variant | InputVariant | InputVariant.Standard | Visual variant style for the component |
| Label | string? | - | Label text for the component |
| Placeholder | string? | - | Placeholder text |
| HelpText | string? | - | HelpText parameter |
| ErrorMessage | string? | - | ErrorMessage parameter |
| Required | bool | - | Whether the component is required |
| Disabled | bool | - | Whether the component is disabled |
| ReadOnly | bool | - | Whether the component is read-only |
| MaxLength | int? | - | Maximum value constraint |
| ShowClearButton | bool | - | ShowClearButton parameter |
| ShowCharacterCount | bool | - | ShowCharacterCount parameter |
| FloatingLabel | bool | - | Label text for the component |
| IconStart | RenderFragment? | - | Icon to display |
| IconEnd | RenderFragment? | - | Icon to display |
| AdornmentStart | string? | - | AdornmentStart parameter |
| AdornmentEnd | string? | - | AdornmentEnd parameter |
| Style | string? | - | Additional CSS styles |
| Min | string? | - | Minimum value constraint |
| Max | string? | - | Maximum value constraint |
| Step | string? | - | Step value for numeric inputs |
| Pattern | string? | - | Validation pattern (regex) |
| AutoComplete | string? | - | AutoComplete parameter |
| AutoFocus | bool | false | AutoFocus parameter |
| AriaLabel | string? | - | Label text for the component |
| EnableAnimation | bool | true | EnableAnimation parameter |
| AnimationDuration | int | 200 | AnimationDuration parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| ValueChanged | string? | Raised when value changes |
| OnFocus | FocusEventArgs | Raised when focus is gained |
| OnBlur | FocusEventArgs | Raised when focus is lost |
| OnKeyDown | KeyboardEventArgs | Raised on key down |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailInput></TailInput>
```