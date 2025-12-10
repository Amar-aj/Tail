# ?? Custom Theme System - Tail.Blazor

## Overview

Tail.Blazor now includes a powerful theme system with **5 predefined themes** (each with light & dark mode) plus **custom theme support**, all persisted in **localStorage**.

---

## ? Features

### 5 Predefined Themes

1. **?? Ocean** - Cool blue ocean vibes
2. **?? Forest** - Natural green forest theme
3. **?? Sunset** - Warm sunset colors
4. **?? Purple Haze** - Rich purple gradient theme
5. **?? Midnight** - Deep blue midnight theme

### Each Theme Includes:
- ? **Light Mode** - Optimized colors for light backgrounds
- ? **Dark Mode** - Optimized colors for dark backgrounds
- ? **Smooth Transitions** - Animated color changes
- ? **localStorage Persistence** - Your choice is remembered
- ? **Instant Apply** - No page reload required

### Custom Themes
- ?? **Custom Color Picker** - Choose any colors you want
- ?? **Save Custom Themes** - Stored in localStorage
- ?? **Switch Anytime** - Easy to switch between preset and custom

---

## ?? Components Created

### 1. ThemePresets.cs
**Location:** `src/packages/Tail.Blazor.Core/Theme/ThemePresets.cs`

Defines 5 predefined themes with light and dark color schemes:

```csharp
public class ThemePreset
{
    public string Name { get; set; }
    public string Description { get; set; }
    public ThemeColors Light { get; set; }
    public ThemeColors Dark { get; set; }
}

public class ThemeColors
{
    public string Primary { get; set; }
    public string Secondary { get; set; }
    public string Accent { get; set; }
    public string Success { get; set; }
    public string Warning { get; set; }
    public string Danger { get; set; }
    public string Info { get; set; }
    public string Background { get; set; }
    public string Surface { get; set; }
    public string TextPrimary { get; set; }
    public string TextSecondary { get; set; }
    public string Border { get; set; }
}
```

**Available Themes:**
- `ThemePresets.Ocean`
- `ThemePresets.Forest`
- `ThemePresets.Sunset`
- `ThemePresets.Purple`
- `ThemePresets.Midnight`

### 2. ThemeService.cs
**Location:** `src/packages/Tail.Blazor.Core/Theme/ThemeService.cs`

Manages theme settings with localStorage persistence:

```csharp
public class ThemeService
{
    // Load theme from localStorage
    Task<ThemeSettings> LoadThemeAsync();
    
    // Save theme to localStorage
    Task SaveThemeAsync();
    
    // Apply a predefined theme
    Task ApplyPresetAsync(string presetName, string mode = "Light");
    
    // Apply custom theme colors
    Task ApplyCustomThemeAsync(ThemeColors colors, string mode = "Light");
    
    // Toggle between light and dark mode
    Task ToggleModeAsync();
    
    // Initialize theme on app startup
    Task InitializeAsync();
    
    // Get all available presets
    List<ThemePreset> GetPresets();
    
    // Event triggered when theme changes
    event Action? OnThemeChanged;
}
```

### 3. TailThemeSelector.razor
**Location:** `src/packages/Tail.Blazor.Core/Theme/TailThemeSelector.razor`

Interactive UI component for selecting and customizing themes:

**Features:**
- Preview current theme with color swatches
- Grid of preset theme buttons
- Custom color pickers for all theme colors
- Light/Dark mode toggle
- Real-time preview

**Usage:**
```razor
<TailThemeSelector ShowPreview="true" />
```

**Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| ShowPreview | bool | true | Show current theme preview |
| CssClass | string? | null | Additional CSS classes |

### 4. ServiceCollectionExtensions.cs
**Location:** `src/packages/Tail.Blazor.Core/Extensions/ServiceCollectionExtensions.cs`

Extension method for registering theme services:

```csharp
public static IServiceCollection AddTailBlazorTheme(this IServiceCollection services)
{
    services.AddScoped<ThemeService>();
    return services;
}
```

---

## ?? Usage Guide

### 1. Register the Service

In your `Program.cs`:

```csharp
using Tail.Blazor.Core.Extensions;

builder.Services.AddTailBlazorTheme();
```

### 2. Use in Components

```razor
@page "/my-page"
@using Tail.Blazor.Core.Theme
@inject ThemeService ThemeService

<TailThemeSelector ShowPreview="true" />

@code {
    protected override async Task OnInitializedAsync()
    {
        // Initialize theme on page load
        await ThemeService.InitializeAsync();
    }
}
```

### 3. Programmatic Theme Control

```csharp
@inject ThemeService ThemeService

// Apply a preset theme
await ThemeService.ApplyPresetAsync("Ocean", "Dark");

// Toggle light/dark mode
await ThemeService.ToggleModeAsync();

// Apply custom colors
var customColors = new ThemeColors
{
    Primary = "#ff6b6b",
    Secondary = "#4ecdc4",
    Accent = "#ffe66d"
};
await ThemeService.ApplyCustomThemeAsync(customColors, "Light");

// Listen to theme changes
ThemeService.OnThemeChanged += OnThemeChanged;

private void OnThemeChanged()
{
    StateHasChanged();
}
```

---

## ?? Theme Color Scheme

Each theme defines these colors:

| Color | Purpose | Example |
|-------|---------|---------|
| **Primary** | Main brand color | Buttons, links, primary actions |
| **Secondary** | Supporting color | Secondary buttons, badges |
| **Accent** | Highlight color | Call-to-actions, highlights |
| **Success** | Success states | Success messages, confirmations |
| **Warning** | Warning states | Warning messages, cautions |
| **Danger** | Error states | Error messages, destructive actions |
| **Info** | Informational | Info messages, tips |
| **Background** | Main background | Page background |
| **Surface** | Component surfaces | Cards, panels, modals |
| **TextPrimary** | Primary text | Headings, body text |
| **TextSecondary** | Secondary text | Labels, descriptions |
| **Border** | Borders | Card borders, dividers |

---

## ?? Preset Theme Colors

### ?? Ocean Theme

**Light Mode:**
- Primary: `#0ea5e9` (Sky Blue)
- Secondary: `#06b6d4` (Cyan)
- Accent: `#8b5cf6` (Purple)

**Dark Mode:**
- Primary: `#38bdf8` (Light Sky Blue)
- Secondary: `#22d3ee` (Light Cyan)
- Accent: `#a78bfa` (Light Purple)

### ?? Forest Theme

**Light Mode:**
- Primary: `#10b981` (Emerald)
- Secondary: `#059669` (Green)
- Accent: `#f59e0b` (Amber)

**Dark Mode:**
- Primary: `#34d399` (Light Emerald)
- Secondary: `#10b981` (Emerald)
- Accent: `#fbbf24` (Yellow)

### ?? Sunset Theme

**Light Mode:**
- Primary: `#f97316` (Orange)
- Secondary: `#f59e0b` (Amber)
- Accent: `#ec4899` (Pink)

**Dark Mode:**
- Primary: `#fb923c` (Light Orange)
- Secondary: `#fbbf24` (Yellow)
- Accent: `#f472b6` (Light Pink)

### ?? Purple Haze Theme

**Light Mode:**
- Primary: `#8b5cf6` (Violet)
- Secondary: `#a78bfa` (Light Violet)
- Accent: `#ec4899` (Pink)

**Dark Mode:**
- Primary: `#a78bfa` (Light Violet)
- Secondary: `#c4b5fd` (Very Light Violet)
- Accent: `#f472b6` (Light Pink)

### ?? Midnight Theme

**Light Mode:**
- Primary: `#3b82f6` (Blue)
- Secondary: `#6366f1` (Indigo)
- Accent: `#06b6d4` (Cyan)

**Dark Mode:**
- Primary: `#60a5fa` (Light Blue)
- Secondary: `#818cf8` (Light Indigo)
- Accent: `#22d3ee` (Light Cyan)

---

## ?? localStorage Structure

Theme settings are stored in `tail-blazor-theme-settings`:

```json
{
  "PresetName": "Ocean",
  "Mode": "Dark",
  "IsCustom": false,
  "Colors": {
    "Primary": "#38bdf8",
    "Secondary": "#22d3ee",
    "Accent": "#a78bfa",
    "Success": "#10b981",
    "Warning": "#f59e0b",
    "Danger": "#ef4444",
    "Info": "#3b82f6",
    "Background": "#0c1821",
    "Surface": "#1e293b",
    "TextPrimary": "#f0f9ff",
    "TextSecondary": "#cbd5e1",
    "Border": "#334155"
  }
}
```

---

## ?? CSS Variables

The theme system applies CSS custom properties to `document.documentElement`:

```css
--color-primary: #38bdf8;
--color-secondary: #22d3ee;
--color-accent: #a78bfa;
--color-success: #10b981;
--color-warning: #f59e0b;
--color-danger: #ef4444;
--color-info: #3b82f6;
--color-background: #0c1821;
--color-surface: #1e293b;
--color-text-primary: #f0f9ff;
--color-text-secondary: #cbd5e1;
--color-border: #334155;
```

**Use in your CSS:**
```css
.my-component {
    background-color: var(--color-surface);
    color: var(--color-text-primary);
    border: 1px solid var(--color-border);
}

.my-button {
    background-color: var(--color-primary);
    color: white;
}
```

---

## ?? API Reference

### ThemeService Methods

#### LoadThemeAsync()
```csharp
Task<ThemeSettings> LoadThemeAsync()
```
Loads theme settings from localStorage. Returns default Ocean/Light if no settings found.

#### SaveThemeAsync()
```csharp
Task SaveThemeAsync()
```
Saves current theme settings to localStorage and triggers `OnThemeChanged` event.

#### ApplyPresetAsync()
```csharp
Task ApplyPresetAsync(string presetName, string mode = "Light")
```
Applies a predefined theme preset.

**Parameters:**
- `presetName`: "Ocean", "Forest", "Sunset", "Purple", or "Midnight"
- `mode`: "Light" or "Dark"

#### ApplyCustomThemeAsync()
```csharp
Task ApplyCustomThemeAsync(ThemeColors colors, string mode = "Light")
```
Applies custom theme colors.

#### ToggleModeAsync()
```csharp
Task ToggleModeAsync()
```
Toggles between Light and Dark mode while preserving the current theme.

#### InitializeAsync()
```csharp
Task InitializeAsync()
```
Initializes the theme on app startup. Call this in `OnInitializedAsync` of your root component.

#### GetPresets()
```csharp
List<ThemePreset> GetPresets()
```
Returns list of all available theme presets.

---

## ?? Demo Page

Visit `/theme-selector-demo` to see the theme selector in action with:

- Interactive theme selection
- Live preview of components
- Custom color picker
- Real-time theme switching

---

## ? Features Checklist

- [x] 5 predefined themes
- [x] Light & Dark mode for each theme
- [x] Custom theme support
- [x] localStorage persistence
- [x] Instant theme application
- [x] CSS variables for easy theming
- [x] Theme change events
- [x] Interactive UI component
- [x] Documentation
- [x] Demo page

---

## ?? Summary

The Tail.Blazor theme system provides:

1. **5 Beautiful Presets** - Ocean, Forest, Sunset, Purple Haze, Midnight
2. **Light & Dark Modes** - 10 total theme variations
3. **Custom Themes** - Create unlimited custom color schemes
4. **localStorage** - Your preferences persist across sessions
5. **Easy Integration** - Simple API and components
6. **Modern CSS** - CSS custom properties for flexibility
7. **Real-time Updates** - Instant theme changes without reload

Visit `/theme-selector-demo` to try it out!

---

**Status:** ? Complete  
**Version:** 1.0.0  
**Date:** December 2024
