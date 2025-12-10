# ?? Global Theme System - Implementation Guide

## ? Complete - Theme System Now Works Globally!

The Tail.Blazor theme system is now configured to work **globally** across **all packages** and the **docs project**. All custom variables, themes, and modes are applied automatically.

---

## ?? What Was Updated

### 1. **MainLayout.razor** - Global Theme Initialization
**File:** `docs/Tail.Blazor.Docs/Shared/MainLayout.razor`

**Changes:**
- ? Injected `ThemeService`
- ? Initializes theme on app startup (`OnInitializedAsync`)
- ? Subscribes to theme changes for reactive updates
- ? Applies root styles using CSS variables
- ? Handles cleanup on dispose

**Result:** Theme loads automatically from localStorage when app starts and applies to all pages.

### 2. **tail-theme.css** - Global CSS Variables
**File:** `src/packages/Tail.Blazor.Core/wwwroot/tail-theme.css`

**Provides:**
- ? All 23 CSS variables defined globally
- ? Light mode defaults (Ocean theme)
- ? Dark mode overrides (`.dark` class)
- ? Utility classes (`.theme-surface`, `.theme-button`, etc.)
- ? Smooth transitions for theme changes
- ? Focus styles for accessibility
- ? Scrollbar styling
- ? Selection colors

**Result:** CSS variables available in **all components** across **all packages**.

### 3. **_Layout.cshtml** - CSS Includes
**File:** `docs/Tail.Blazor.Docs/Pages/_Layout.cshtml`

**Added:**
```html
<link href="_content/Tail.Blazor.Core/tail-theme.css" rel="stylesheet" />
```

**Result:** Global theme CSS loaded on every page.

---

## ?? How It Works

### Startup Sequence

1. **App Starts** ? `MainLayout.OnInitializedAsync()` called
2. **ThemeService.InitializeAsync()** ? Loads from localStorage
3. **Theme Applied** ? JavaScript injects CSS variables to `:root`
4. **All Components Update** ? Using CSS variables instantly

### Theme Change Sequence

1. **User Changes Theme** ? Via Theme Manager or ThemeControl
2. **ThemeService** ? Updates CurrentSettings
3. **Saves to localStorage** ? Persists for next visit
4. **JavaScript** ? Updates CSS variables on `:root`
5. **OnThemeChanged Event** ? Triggers component re-renders
6. **UI Updates** ? Smooth transitions across all components

---

## ?? Global CSS Variables (23 Total)

### Available Everywhere

All components in all packages can now use these variables:

#### **Primary Colors (3)**
```css
var(--color-primary)      /* Main brand color */
var(--color-secondary)    /* Supporting color */
var(--color-accent)       /* Highlight color */
```

#### **State Colors (4)**
```css
var(--color-success)      /* Green - success states */
var(--color-warning)      /* Yellow - warnings */
var(--color-danger)       /* Red - errors/danger */
var(--color-info)         /* Blue - information */
```

#### **Background & Surfaces (4)**
```css
var(--color-background)   /* Page background */
var(--color-surface)      /* Component surface (level 1) */
var(--color-surface-2)    /* Elevated surface (level 2) */
var(--color-surface-3)    /* Raised surface (level 3) */
```

#### **Text Colors (3)**
```css
var(--color-text-primary)     /* Main text */
var(--color-text-secondary)   /* Labels, descriptions */
var(--color-text-muted)       /* Placeholders, hints */
```

#### **Borders & Dividers (2)**
```css
var(--color-border)       /* Component borders */
var(--color-divider)      /* Horizontal rules, separators */
```

#### **Shadows (3)**
```css
var(--shadow-sm)          /* Subtle elevation */
var(--shadow-md)          /* Medium elevation */
var(--shadow-lg)          /* High elevation */
```

#### **Border Radius (3)**
```css
var(--radius-sm)          /* 4px - small elements */
var(--radius-md)          /* 6px - medium elements */
var(--radius-lg)          /* 8px - large elements */
```

#### **Transitions (2)**
```css
var(--transition-fast)    /* 150ms - interactions */
var(--transition-normal)  /* 200ms - state changes */
```

---

## ?? Usage in Components

### In Any Package Component

```razor
<!-- Your component in ANY package -->
<div style="background-color: var(--color-surface); 
            color: var(--color-text-primary);
            border: 1px solid var(--color-border);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
            transition: box-shadow var(--transition-fast);">
    
    <h3 style="color: var(--color-text-primary)">Hello</h3>
    <p style="color: var(--color-text-secondary)">Description</p>
    
    <button style="background-color: var(--color-primary); color: white;">
        Action
    </button>
</div>
```

### Using Utility Classes

```razor
<!-- Use predefined classes from tail-theme.css -->
<div class="theme-card">
    <h3 class="theme-text-primary">Title</h3>
    <p class="theme-text-secondary">Description</p>
    <button class="theme-button">Click Me</button>
</div>

<div class="theme-surface p-4">
    <input class="theme-input" placeholder="Enter text..." />
</div>
```

---

## ?? For New Package Development

### 1. CSS Variables Are Already Available

No setup needed! Just use the variables:

```css
.my-new-component {
    background: var(--color-surface);
    color: var(--color-text-primary);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-sm);
}
```

### 2. Access ThemeService (Optional)

If you need programmatic theme control:

```razor
@inject ThemeService ThemeService

<button @onclick="ToggleTheme">
    Switch to @(ThemeService.CurrentSettings.Mode == "Light" ? "Dark" : "Light")
</button>

@code {
    private async Task ToggleTheme()
    {
        await ThemeService.ToggleModeAsync();
    }
}
```

### 3. React to Theme Changes (Optional)

```razor
@inject ThemeService ThemeService
@implements IDisposable

@code {
    protected override void OnInitialized()
    {
        ThemeService.OnThemeChanged += HandleThemeChanged;
    }

    private void HandleThemeChanged()
    {
        InvokeAsync(StateHasChanged);
    }

    public void Dispose()
    {
        ThemeService.OnThemeChanged -= HandleThemeChanged;
    }
}
```

---

## ?? Testing the Global System

### 1. Build All Packages

```bash
cd D:\Users\AMAR\source\repos\Tail
dotnet build
```

### 2. Run Docs App

```bash
cd docs/Tail.Blazor.Docs
dotnet run
```

### 3. Test Theme Persistence

1. **Visit** `http://localhost:5000/theme-manager`
2. **Select a theme** (e.g., Forest Dark)
3. **Navigate** to any other page
4. **Verify** theme persists (all components use selected theme)
5. **Refresh page** ? Theme still applied (from localStorage)
6. **Open in new tab** ? Same theme (shared localStorage)

### 4. Test Component Updates

1. **Open** `/components/buttons`
2. **Change theme** ? Buttons update colors
3. **Toggle mode** ? Buttons adapt to dark/light
4. **Try custom colors** ? See immediate changes

---

## ?? Benefits

### ? **Truly Global**
- Works in ALL packages (Core, Buttons, Forms, Layout, Navigation, Feedback, Data)
- No per-component setup required
- Consistent across entire application

### ? **Persistent**
- Saved to localStorage
- Survives page reloads
- Shared across tabs
- No server calls needed

### ? **Reactive**
- Instant updates when theme changes
- Smooth transitions (150ms/200ms)
- No page reload required
- Components update automatically

### ? **Flexible**
- 5 preset themes × 2 modes = 10 variations
- Unlimited custom themes
- Easy to extend with new presets
- CSS variables for maximum flexibility

### ? **Professional**
- 4 surface levels for depth
- 3 shadow elevations
- 3 border radius sizes
- Smooth transition speeds
- Accessibility-friendly

---

## ?? Theme Manager Features

The unified Theme Manager (`/theme-manager`) provides:

- **Preset Selection** - Choose from 5 beautiful themes
- **Custom Colors** - Create your own palette
- **Live Preview** - See changes instantly
- **CSS Inspector** - View all 23 variables
- **Component Demos** - Test with real components
- **Export/Import** - Share themes as JSON
- **Dark/Light Toggle** - Switch modes easily

---

## ?? Quick Reference

### Change Theme Programmatically

```csharp
@inject ThemeService ThemeService

// Apply preset
await ThemeService.ApplyPresetAsync("Ocean", "Dark");

// Toggle mode
await ThemeService.ToggleModeAsync();

// Custom theme
await ThemeService.ApplyCustomThemeAsync(new ThemeColors
{
    Primary = "#ff6b6b",
    Secondary = "#4ecdc4",
    Accent = "#ffe66d"
}, "Light");
```

### Use in Styles

```css
/* Any component, any package */
.my-component {
    background-color: var(--color-surface);
    color: var(--color-text-primary);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-sm);
    transition: all var(--transition-fast);
}
```

---

## ? Verification Checklist

- [x] MainLayout.razor initializes ThemeService globally
- [x] tail-theme.css provides all 23 CSS variables
- [x] _Layout.cshtml includes global CSS
- [x] localStorage persistence working
- [x] Theme changes apply to all components
- [x] Dark/light mode toggle functional
- [x] All packages can use CSS variables
- [x] Theme Manager provides complete control
- [x] Smooth transitions throughout
- [x] No component-specific setup required

---

## ?? Result

**You now have a complete, global theme system that:**

1. **Works everywhere** - All packages, all components
2. **Persists** - localStorage saves preferences
3. **Updates instantly** - Real-time theme changes
4. **Requires no setup** - Just use CSS variables
5. **Professional** - 23 variables, 5 themes, smooth transitions
6. **Easy to use** - Theme Manager provides GUI control

**?? Your entire component library is now theme-aware and globally consistent!**

---

**Status:** ? **Complete and Ready**  
**Last Updated:** December 2024  
**Tested:** ? Docs project  
**Applies To:** All 7 packages + Docs

---

## ?? Navigation

- **Theme Manager:** `/theme-manager`
- **Quick Selector:** `/theme-selector-demo`
- **Integration Guide:** `/docs/theme-integration`
- **Phase 2 Complete:** `/docs/phase2-completion`
