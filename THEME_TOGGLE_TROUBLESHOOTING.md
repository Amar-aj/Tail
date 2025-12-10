# Theme Toggle Troubleshooting Guide

## Issue: Theme not applying/reflecting in document

### Problem
The theme toggle saves to localStorage but the dark mode doesn't apply to the website - the page stays in light mode even when clicking the toggle.

### Root Cause
1. **Tailwind CSS dark mode not configured** - Tailwind needs `darkMode: 'class'` in config
2. **Flash of wrong theme** - Theme applied after page loads causes flash
3. **Missing `dark` class** - JavaScript not applying `dark` class to `<html>` element

### ? Solution Implemented

#### 1. Updated `_Host.cshtml`
Added three critical pieces:

**A. Tailwind Dark Mode Config**
```html
<script>
    tailwind.config = {
        darkMode: 'class', // ? CRITICAL: Enables class-based dark mode
        theme: {
            extend: {}
        }
    }
</script>
```

**B. Pre-load Theme Script (Before Page Renders)**
```html
<script>
    (function() {
        try {
            const theme = localStorage.getItem('tail-blazor-theme');
            if (theme === 'Dark') {
                document.documentElement.classList.add('dark');
            } else if (theme === 'Light') {
                document.documentElement.classList.remove('dark');
            } else {
                // Check system preference if no saved theme
                if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                    document.documentElement.classList.add('dark');
                }
            }
        } catch (e) {
            console.error('Error loading theme:', e);
        }
    })();
</script>
```

**C. Proper Script Order**
```html
<!-- 1. Load Tailwind first -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- 2. Configure dark mode -->
<script>tailwind.config = { darkMode: 'class' }</script>

<!-- 3. Apply saved theme BEFORE page renders -->
<script>(function() { /* theme loading */ })();</script>
```

#### 2. Enhanced CSS (`app.css`)
```css
/* Ensure root element has background */
html {
    background-color: #f9fafb; /* Light mode */
}

html.dark {
    background-color: #111827; /* Dark mode */
}

/* Smooth transitions */
* {
    transition-property: background-color, border-color, color;
    transition-duration: 200ms;
}
```

#### 3. Component Fallback
Added fallback in `TailThemeToggle.razor`:
```csharp
private async Task ApplyThemeDirectly()
{
    try {
        var isDark = Theme.Mode == ThemeMode.Dark;
        var script = isDark 
            ? "document.documentElement.classList.add('dark')" 
            : "document.documentElement.classList.remove('dark')";
        await JS.InvokeVoidAsync("eval", script);
    } catch (Exception ex) {
        Console.WriteLine($"Error in fallback theme apply: {ex.Message}");
    }
}
```

---

## How It Works Now

### 1. Initial Page Load
```
User opens page
    ?
Pre-load script runs (before render)
    ?
Check localStorage for 'tail-blazor-theme'
    ?
If 'Dark' ? Add 'dark' class to <html>
If 'Light' ? Remove 'dark' class
If null ? Check system preference
    ?
Page renders with correct theme
    ?
No flash of wrong theme ?
```

### 2. Theme Toggle Click
```
User clicks toggle button
    ?
Component toggles Theme.Mode
    ?
Save to localStorage ('Dark' or 'Light')
    ?
Apply to document:
  - Add/remove 'dark' class on <html>
    ?
Tailwind CSS applies dark: classes
    ?
UI updates instantly ?
```

### 3. Theme Persistence
```
User closes browser
    ?
Theme saved in localStorage
    ?
User returns later
    ?
Pre-load script reads localStorage
    ?
Applies saved theme before render
    ?
User sees same theme they chose ?
```

---

## Verification Steps

### 1. Check Tailwind Config
Open browser DevTools ? Console, run:
```javascript
console.log(tailwind.config);
// Should show: { darkMode: 'class', ... }
```

### 2. Check HTML Class
DevTools ? Elements, inspect `<html>` tag:
```html
<!-- Light mode -->
<html lang="en">

<!-- Dark mode -->
<html lang="en" class="dark">
```

### 3. Check localStorage
DevTools ? Application ? Local Storage, look for:
```
Key: tail-blazor-theme
Value: "Dark" or "Light"
```

### 4. Test Theme Toggle
1. Click theme toggle button
2. Open DevTools ? Elements
3. Watch `<html>` element - should see `class="dark"` appear/disappear
4. Refresh page - theme should persist

---

## Common Issues & Fixes

### Issue 1: "Theme toggles but page stays light"
**Symptom:** Button changes icon, localStorage updates, but page doesn't change appearance

**Cause:** Tailwind `darkMode: 'class'` not configured

**Fix:** Check `_Host.cshtml` has:
```html
<script>
    tailwind.config = {
        darkMode: 'class' // ? Must be 'class', not 'media'
    }
</script>
```

### Issue 2: "Flash of light theme on page load"
**Symptom:** Page briefly shows light mode, then switches to dark

**Cause:** Theme applied after page renders

**Fix:** Pre-load script must run BEFORE `<body>` content:
```html
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>tailwind.config = { darkMode: 'class' }</script>
    <script>
        // Theme loading script HERE, in <head>
    </script>
</head>
<body>
    <!-- Content here -->
</body>
```

### Issue 3: "Console error: Cannot read property 'classList'"
**Symptom:** JavaScript error in console

**Cause:** Trying to access `document.documentElement` before it exists

**Fix:** Wrap in try-catch and ensure script runs after `<html>` element exists (it always does, so this is rare)

### Issue 4: "Dark mode works but colors are wrong"
**Symptom:** Page turns dark but components don't look right

**Cause:** Components not using `dark:` Tailwind classes

**Fix:** Ensure all components use proper dark mode classes:
```html
<!-- ? Good -->
<div class="bg-white dark:bg-gray-800 text-gray-900 dark:text-white">

<!-- ? Bad -->
<div class="bg-white text-gray-900">
```

### Issue 5: "Theme doesn't persist across tabs"
**Symptom:** Opening new tab shows wrong theme

**Cause:** localStorage not being read on new page load

**Fix:** Ensure pre-load script runs on EVERY page load (it should if in `_Host.cshtml`)

---

## Testing Checklist

- [ ] Initial load shows correct theme (check localStorage)
- [ ] Toggle button switches theme immediately
- [ ] localStorage updates on toggle
- [ ] HTML `dark` class appears/disappears
- [ ] Background colors change
- [ ] Text colors change
- [ ] No console errors
- [ ] Refresh page preserves theme
- [ ] New tab opens with correct theme
- [ ] System preference detection works (clear localStorage to test)
- [ ] All components render correctly in both modes

---

## Browser DevTools Commands

### Check Current Theme
```javascript
// Check HTML class
document.documentElement.classList.contains('dark');

// Check localStorage
localStorage.getItem('tail-blazor-theme');

// Check system preference
window.matchMedia('(prefers-color-scheme: dark)').matches;
```

### Manually Set Theme
```javascript
// Set dark mode
document.documentElement.classList.add('dark');
localStorage.setItem('tail-blazor-theme', 'Dark');

// Set light mode
document.documentElement.classList.remove('dark');
localStorage.setItem('tail-blazor-theme', 'Light');

// Clear saved theme
localStorage.removeItem('tail-blazor-theme');
```

---

## Files Modified

1. **`docs/Tail.Blazor.Docs/Pages/_Host.cshtml`**
   - Added Tailwind config with `darkMode: 'class'`
   - Added pre-load theme script
   - Proper script ordering

2. **`docs/Tail.Blazor.Docs/wwwroot/css/app.css`**
   - Added `html` and `html.dark` background colors
   - Added smooth transitions
   - Enhanced dark mode support

3. **`src/packages/Tail.Blazor.Core/Theme/TailThemeToggle.razor`**
   - Added fallback theme application
   - Enhanced error handling
   - Improved JS module import

4. **`src/packages/Tail.Blazor.Core/wwwroot/theme-toggle.js`**
   - Already correct (no changes needed)

---

## Expected Behavior

### ? Light Mode
- HTML: `<html lang="en">`
- localStorage: `"Light"`
- Background: White/Gray
- Text: Dark
- Icons: Sun icon visible

### ? Dark Mode
- HTML: `<html lang="en" class="dark">`
- localStorage: `"Dark"`
- Background: Dark Gray/Black
- Text: Light
- Icons: Moon icon visible

---

## Additional Notes

### Why `darkMode: 'class'` instead of `'media'`?
- `'media'` uses `prefers-color-scheme` (system preference only)
- `'class'` uses HTML class, allowing manual override
- We want users to choose their theme, not be forced to system preference

### Why pre-load script in `<head>`?
- Prevents "flash of wrong theme" (FOUC)
- Runs before page renders
- No visual jitter for users

### Why not use a Blazor component for theme loading?
- Blazor components render AFTER initial HTML
- Would cause visible theme switch
- JavaScript runs instantly before any rendering

---

## Success Indicators

When working correctly, you should see:

1. **No flash** - Page loads with correct theme immediately
2. **Instant toggle** - Theme changes when clicking button
3. **Persistence** - Theme remembered on page refresh
4. **System respect** - Uses system preference if no saved theme
5. **Cross-tab** - All tabs use same theme
6. **Smooth animations** - Colors transition smoothly (200ms)

---

## Final Checklist

After applying fixes:

- [ ] Run `dotnet build` - No errors
- [ ] Run `dotnet run` - Docs site starts
- [ ] Open browser ? `http://localhost:5000`
- [ ] Click theme toggle - Page changes color
- [ ] Refresh page - Theme persists
- [ ] Open DevTools ? Elements - See `class="dark"` on `<html>`
- [ ] Open DevTools ? Application ? Local Storage - See `tail-blazor-theme`
- [ ] Clear localStorage ? Refresh - Uses system preference
- [ ] All components render correctly in both modes

? **If all checks pass, theme toggle is working!**

---

**Status:** ? Fixed and Documented  
**Date:** December 2024  
**Version:** 1.0.0
