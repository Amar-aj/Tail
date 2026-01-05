# Tail.Blazor.SplitButton

Independent NuGet package for the TailSplitButton component.

## Installation

```bash
dotnet add package Tail.Blazor.SplitButton
```

## Features

- Primary action button
- Dropdown menu for secondary actions
- 9 variants
- 5 sizes
- Loading states
- Disabled states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| PrimaryContent | RenderFragment? | - | PrimaryContent parameter |
| DropdownContent | RenderFragment? | - | DropdownContent parameter |
| DropdownIcon | RenderFragment? | - | Icon to display |
| Variant | ButtonVariant | ButtonVariant.Primary | Visual variant style for the component |
| Size | ButtonSize | ButtonSize.Md | Size of the component |
| Disabled | bool | - | Whether the component is disabled |
| IsLoading | bool | - | Whether the component is in loading state |
| Type | string | "button" | Type parameter |
| AriaLabel | string? | - | Label text for the component |
| Tooltip | string? | - | Tooltip parameter |

## Events

| Event | Type | Description |
| --- | --- | --- |
| OnPrimaryClick | MouseEventArgs | Raised when component is clicked |
| OnDropdownToggle | void | OnDropdownToggle callback |

## Public Properties

No additional public properties.

## Methods

No additional public methods.

## Examples

```razor
<TailSplitButton></TailSplitButton>
```