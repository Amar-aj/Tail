# Tail.Blazor.CommandPalette

Independent NuGet package for the TailCommandPalette component.

## Installation

```bash
dotnet add package Tail.Blazor.CommandPalette
```

## Features

- Command palette (Cmd+K style)
- Search/filter commands
- Keyboard navigation
- Shortcut display
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| IsVisible | bool | - | Whether the component is visible |
| Commands | List<CommandItem> | new() | Commands parameter |
| Placeholder | string | "Type a command or search..." | Placeholder text |
| Style | string? | - | Additional CSS styles |

## Events

| Event | Type | Description |
| --- | --- | --- |
| IsVisibleChanged | bool | Raised when value changes |

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| CommandItem | class | CommandItem property |
| Label | string | Label property |
| Description | string? | Description property |
| Shortcut | string? | Shortcut property |
| OnExecute | EventCallback | OnExecute property |

## Methods

No additional public methods.

## Examples

```razor
<TailCommandPalette></TailCommandPalette>
```