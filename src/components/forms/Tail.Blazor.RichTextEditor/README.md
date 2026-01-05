# Tail.Blazor.RichTextEditor

Independent NuGet package for the TailRichTextEditor component.

## Installation

```bash
dotnet add package Tail.Blazor.RichTextEditor
```

## Features

- Rich text editor with formatting toolbar
- Bold, italic, underline formatting
- Content editable area
- Customizable min height
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
| Size | RichTextEditorSize | RichTextEditorSize.Md | Size of the component |
| Label | string? | - | Label text for the component |
| MinHeight | int | 200 | Minimum value constraint |
| Disabled | bool | - | Whether the component is disabled |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| ValueChanged | string? | Raised when value changes |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailRichTextEditor></TailRichTextEditor>
```