# Tail.Blazor.Dialog

Independent NuGet package for the TailDialog component.

## Installation

```bash
dotnet add package Tail.Blazor.Dialog
```

## Usage

```razor
@using Tail.Blazor.Dialog

<TailDialog IsVisible="@showDialog" IsVisibleChanged="OnDialogChanged" Title="Confirm Action">
    <p>Are you sure you want to proceed?</p>
    <Footer>
        <button @onclick="Confirm">Confirm</button>
    </Footer>
</TailDialog>
```

## Features

- Modal dialog with backdrop
- 6 sizes (Sm, Md, Lg, Xl, Xxl, Full)
- Title and footer support
- Close button option
- Close on backdrop click
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~8 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

