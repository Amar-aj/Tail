# Quick Start Guide

## Installation

### 1. Install Core Package

```bash
dotnet add package Tail.Blazor.Core
```

### 2. Install Component Packages (as needed)

```bash
# Buttons
dotnet add package Tail.Blazor.Buttons

# Forms
dotnet add package Tail.Blazor.Forms

# Layout
dotnet add package Tail.Blazor.Layout

# Navigation
dotnet add package Tail.Blazor.Navigation

# Feedback
dotnet add package Tail.Blazor.Feedback
```

## Configuration

### Program.cs

```csharp
using Tail.Blazor.Core;

var builder = WebApplication.CreateBuilder(args);

// Add Tail.Blazor
builder.Services.AddTailBlazor(config =>
{
    config.ThemeMode = ThemeMode.Light;
    config.ThemePalette = ThemePalette.Blue;
    config.UseGradients = true;
});

builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();

var app = builder.Build();
app.MapBlazorHub();
app.MapFallbackToPage("/_Host");
app.Run();
```

### Add Tailwind CSS

In `_Host.cshtml` or `index.html`:

```html
<script src="https://cdn.tailwindcss.com"></script>
```

## Your First Component

### _Imports.razor

```razor
@using Tail.Blazor.Buttons
@using Tail.Blazor.Core.Enums
```

### Example.razor

```razor
@page "/example"

<TailButton Variant="ButtonVariant.Primary" Size="ButtonSize.Md" OnClick="HandleClick">
    Click Me
</TailButton>

@code {
    private void HandleClick()
    {
        // Handle button click
    }
}
```

## Theme Customization

### Apply Theme

```razor
@using Tail.Blazor.Core.Theme
@inject ThemeEngine Theme

<ThemeProvider>
    @* Your app *@
</ThemeProvider>
```

### Custom Colors

```csharp
builder.Services.AddTailBlazor(config =>
{
    config.PrimaryColor = "#3b82f6";
    config.SecondaryColor = "#8b5cf6";
    config.UseGradients = true;
});
```

### Dynamic Theme

```csharp
Theme.ApplyGradientTheme(
    primaryStart: "#3b82f6",
    primaryEnd: "#1d4ed8"
);
```

## Next Steps

- Browse [Components](/components)
- Learn [Theming](/theming)
- View [Examples](/examples)
- Read [API Reference](/api)

