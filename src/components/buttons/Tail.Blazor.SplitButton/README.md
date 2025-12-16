# Tail.Blazor.SplitButton

Independent NuGet package for the TailSplitButton component.

## Installation

```bash
dotnet add package Tail.Blazor.SplitButton
```

## Usage

```razor
@using Tail.Blazor.SplitButton

<TailSplitButton PrimaryContent="@(() => "Save")" OnPrimaryClick="HandleSave">
    <DropdownContent>
        <button @onclick="HandleSaveAs">Save As...</button>
        <button @onclick="HandleExport">Export</button>
    </DropdownContent>
</TailSplitButton>
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

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

