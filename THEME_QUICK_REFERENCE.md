# ?? Theme System - Quick Reference

## ?? Quick Start

### 1. Register Service
```csharp
// Program.cs
builder.Services.AddTailBlazorTheme();
```

### 2. Add Component
```razor
@using Tail.Blazor.Core.Theme

<TailThemeSelector ShowPreview="true" />
```

### 3. Use Programmatically
```csharp
@inject ThemeService ThemeService

// Apply preset
await ThemeService.ApplyPresetAsync("Ocean", "Dark");

// Toggle mode
await ThemeService.ToggleModeAsync();

// Custom theme
await ThemeService.ApplyCustomThemeAsync(new ThemeColors { ... }, "Light");
```

---

## ?? 5 Preset Themes

| Theme | Icon | Description | Primary (Light) | Primary (Dark) |
|-------|------|-------------|-----------------|----------------|
| **Ocean** | ?? | Cool blue vibes | `#0ea5e9` | `#38bdf8` |
| **Forest** | ?? | Natural green | `#10b981` | `#34d399` |
| **Sunset** | ?? | Warm colors | `#f97316` | `#fb923c` |
| **Purple Haze** | ?? | Rich purple | `#8b5cf6` | `#a78bfa` |
| **Midnight** | ?? | Deep blue | `#3b82f6` | `#60a5fa` |

---

## ?? localStorage Key

**Key:** `tail-blazor-theme-settings`

**Structure:**
```json
{
  "PresetName": "Ocean",
  "Mode": "Dark",
  "IsCustom": false,
  "Colors": { /* 12 color properties */ }
}
```

---

## ?? CSS Variables

```css
--color-primary
--color-secondary
--color-accent
--color-success
--color-warning
--color-danger
--color-info
--color-background
--color-surface
--color-text-primary
--color-text-secondary
--color-border
```

**Usage:**
```css
.my-class {
    background: var(--color-surface);
    color: var(--color-text-primary);
}
```

---

## ?? ThemeService API

| Method | Parameters | Description |
|--------|-----------|-------------|
| `LoadThemeAsync()` | - | Load from localStorage |
| `SaveThemeAsync()` | - | Save to localStorage |
| `ApplyPresetAsync()` | name, mode | Apply preset theme |
| `ApplyCustomThemeAsync()` | colors, mode | Apply custom colors |
| `ToggleModeAsync()` | - | Toggle light/dark |
| `InitializeAsync()` | - | Initialize on startup |
| `GetPresets()` | - | Get all presets |

---

## ?? Demo Page

Visit: `/theme-selector-demo`

---

## ? Checklist

- [x] 5 preset themes
- [x] Light & dark modes (10 variations)
- [x] Custom theme support
- [x] localStorage persistence
- [x] CSS variables
- [x] Interactive UI
- [x] Event system
- [x] Demo page
- [x] Documentation

---

**Ready to use!** ??
