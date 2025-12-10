# ?? Theme Usage Guide - Quick Reference

## Problem Fixed
? **Themes now properly apply to all components and areas**

---

## How to Use Themes in Your Components

### Method 1: Theme Utility Classes (Recommended)

```html
<!-- Card with theme colors -->
<div class="theme-card border p-4 rounded-lg">
    <h3 class="text-gray-900 dark:text-white">Title</h3>
    <p class="text-gray-600 dark:text-gray-400">Description</p>
    <button class="theme-button px-4 py-2 rounded-lg">
        Action
    </button>
</div>

<!-- Input with theme colors -->
<input type="text" class="theme-input w-full px-3 py-2 border rounded-lg" />
```

### Method 2: CSS Variables

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

### Method 3: Inline Styles (Dynamic)

```razor
<div style="background-color: @currentSettings.Colors.Primary">
    Themed content
</div>

<div style="background-color: var(--color-surface)">
    Content
</div>
```

### Method 4: Theme-Aware Tailwind Classes

```html
<div class="bg-theme-surface text-theme-primary border-theme">
    <!-- Uses CSS variables -->
</div>

<button class="bg-theme-primary text-white">
    <!-- Primary color button -->
</button>
```

---

## Available CSS Variables

```css
--color-primary          /* Main brand color */
--color-secondary        /* Supporting color */
--color-accent          /* Highlight color */
--color-success         /* Success state */
--color-warning         /* Warning state */
--color-danger          /* Error state */
--color-info            /* Info state */
--color-background      /* Page background */
--color-surface         /* Component surfaces */
--color-text-primary    /* Primary text */
--color-text-secondary  /* Secondary text */
--color-border          /* Borders */
```

---

## Available Utility Classes

### Backgrounds
```css
.bg-theme-primary
.bg-theme-secondary
.bg-theme-accent
.bg-theme-surface
.bg-theme-background
```

### Text Colors
```css
.text-theme-primary          /* Uses text color */
.text-theme-secondary        /* Uses secondary text */
.text-theme-color-primary    /* Uses primary color */
.text-theme-color-secondary  /* Uses secondary color */
.text-theme-color-accent     /* Uses accent color */
```

### Borders
```css
.border-theme
.border-theme-primary
```

### Components
```css
.theme-card      /* Themed card (surface + border) */
.theme-button    /* Themed button (primary + hover) */
.theme-input     /* Themed input (surface + border + focus) */
```

---

## Example: Complete Themed Component

```razor
<div class="theme-card border rounded-lg p-6">
    <!-- Header -->
    <div class="flex items-center justify-between mb-4">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white">
            Themed Card
        </h2>
        <button class="theme-button px-4 py-2 rounded-lg">
            Action
        </button>
    </div>
    
    <!-- Content -->
    <p class="text-gray-700 dark:text-gray-300 mb-4">
        This card uses theme colors and will adapt when the theme changes.
    </p>
    
    <!-- Form -->
    <div class="space-y-3">
        <div>
            <label class="block text-sm font-medium mb-1 text-gray-700 dark:text-gray-300">
                Input Label
            </label>
            <input type="text" 
                   class="theme-input w-full px-3 py-2 border rounded-lg" 
                   placeholder="Enter text..." />
        </div>
        
        <button class="theme-button px-4 py-2 rounded-lg w-full">
            Submit
        </button>
    </div>
</div>
```

---

## Initialize Theme in Your Pages

```csharp
@page "/my-page"
@using Tail.Blazor.Core.Theme
@inject ThemeService ThemeService
@implements IDisposable

<div class="theme-card border p-4">
    <!-- Your content -->
</div>

@code {
    protected override async Task OnInitializedAsync()
    {
        // Initialize theme
        await ThemeService.InitializeAsync();
        
        // Listen to theme changes
        ThemeService.OnThemeChanged += OnThemeChanged;
    }
    
    private void OnThemeChanged()
    {
        InvokeAsync(StateHasChanged);
    }
    
    public void Dispose()
    {
        ThemeService.OnThemeChanged -= OnThemeChanged;
    }
}
```

---

## Testing Your Themed Component

1. **Start the app**
   ```bash
   dotnet run
   ```

2. **Visit theme selector**
   ```
   http://localhost:5000/theme-selector-demo
   ```

3. **Test scenarios:**
   - ? Select Ocean theme ? Components should be blue
   - ? Select Forest theme ? Components should be green
   - ? Toggle Dark mode ? Colors should invert
   - ? Reload page ? Theme should persist
   - ? Check console ? Should see "Theme applied" message

---

## Debugging

### Check if theme is loaded
```javascript
// Open browser console
localStorage.getItem('tail-blazor-theme-settings')
// Should return JSON with theme settings
```

### Check CSS variables
```javascript
// Get current primary color
getComputedStyle(document.documentElement)
    .getPropertyValue('--color-primary')
// Should return color like "#38bdf8"
```

### Check dark mode
```javascript
// Check if dark class is present
document.documentElement.classList.contains('dark')
// Should return true or false
```

---

## Best Practices

### ? DO:
- Use `.theme-card`, `.theme-button` for consistent styling
- Use `text-gray-900 dark:text-white` for typography
- Initialize theme in `OnInitializedAsync()`
- Listen to `OnThemeChanged` event
- Use CSS variables for custom components

### ? DON'T:
- Don't use hard-coded colors like `bg-blue-500`
- Don't forget to dispose event handlers
- Don't skip theme initialization
- Don't use only light mode colors

---

## Migration Checklist

Updating existing components:

- [ ] Replace `bg-white` ? `theme-card`
- [ ] Replace `bg-blue-500` ? `theme-button`
- [ ] Replace `border-gray-200` ? `border-theme`
- [ ] Add dark mode variants: `dark:text-white`
- [ ] Initialize theme in page
- [ ] Test with all 5 themes
- [ ] Test light and dark modes

---

**Quick Summary:**
1. Use `.theme-card`, `.theme-button`, `.theme-input` classes
2. Add `text-gray-900 dark:text-white` for text
3. Initialize with `await ThemeService.InitializeAsync()`
4. Listen to `ThemeService.OnThemeChanged`
5. Test with different themes!

**Now all components will properly respond to theme changes!** ??
