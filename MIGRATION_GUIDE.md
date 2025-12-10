# ?? Migration Guide - Adding Tail.Blazor to Existing Projects

## Overview

This guide helps you integrate Tail.Blazor into an **existing Blazor application**.

---

## Pre-Migration Checklist

- [ ] Backup your project
- [ ] Commit current changes to Git
- [ ] Test current application
- [ ] Note which UI frameworks you're currently using (Bootstrap, MudBlazor, etc.)

---

## Step-by-Step Migration

### Step 1: Install Tail.Blazor Packages

```bash
cd YourExistingProject

# Core package (required)
dotnet add package Tail.Blazor.Core

# Add packages based on your needs
dotnet add package Tail.Blazor.Buttons
dotnet add package Tail.Blazor.Forms
dotnet add package Tail.Blazor.Layout
dotnet add package Tail.Blazor.Navigation
dotnet add package Tail.Blazor.Feedback
dotnet add package Tail.Blazor.Data
```

### Step 2: Update Program.cs

Add Tail.Blazor services **before** `builder.Build()`:

**Blazor Server:**
```csharp
using Tail.Blazor.Core;
using Tail.Blazor.Core.Extensions;

var builder = WebApplication.CreateBuilder(args);

// ... existing services ...
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();

// Add Tail.Blazor
builder.Services.AddTailBlazor(config =>
{
    config.ThemeMode = ThemeMode.Light;
    config.ThemePalette = ThemePalette.Blue;
    config.UseGradients = true;
});
builder.Services.AddTailBlazorTheme();

var app = builder.Build();
// ... rest of configuration ...
```

**Blazor WebAssembly:**
```csharp
using Tail.Blazor.Core;
using Tail.Blazor.Core.Extensions;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.RootComponents.Add<App>("#app");
builder.RootComponents.Add<HeadOutlet>("head::after");

// ... existing services ...

// Add Tail.Blazor
builder.Services.AddTailBlazor(config =>
{
    config.ThemeMode = ThemeMode.Light;
});
builder.Services.AddTailBlazorTheme();

await builder.Build().RunAsync();
```

### Step 3: Add Tailwind CSS to HTML

**For Blazor Server** - Edit `Pages/_Host.cshtml`:

Find the `<head>` section and add **before** your existing CSS:

```html
<head>
    <!-- Existing meta tags -->
    
    <!-- ADD THESE: Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {}
            }
        }
    </script>
    
    <!-- ADD THIS: Theme initialization -->
    <script>
        (function() {
            try {
                const themeSettingsJson = localStorage.getItem('tail-blazor-theme-settings');
                const legacyTheme = localStorage.getItem('tail-blazor-theme');
                
                let isDark = false;
                let colors = null;
                
                if (themeSettingsJson) {
                    const settings = JSON.parse(themeSettingsJson);
                    isDark = settings.Mode === 'Dark';
                    colors = settings.Colors;
                } else if (legacyTheme) {
                    isDark = legacyTheme === 'Dark';
                }
                
                if (isDark) {
                    document.documentElement.classList.add('dark');
                } else {
                    document.documentElement.classList.remove('dark');
                    if (!themeSettingsJson && !legacyTheme && 
                        window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                        document.documentElement.classList.add('dark');
                    }
                }
                
                if (colors) {
                    const root = document.documentElement;
                    root.style.setProperty('--color-primary', colors.Primary || '#3b82f6');
                    root.style.setProperty('--color-secondary', colors.Secondary || '#8b5cf6');
                    root.style.setProperty('--color-accent', colors.Accent || '#ec4899');
                    root.style.setProperty('--color-success', colors.Success || '#10b981');
                    root.style.setProperty('--color-warning', colors.Warning || '#f59e0b');
                    root.style.setProperty('--color-danger', colors.Danger || '#ef4444');
                    root.style.setProperty('--color-info', colors.Info || '#3b82f6');
                    root.style.setProperty('--color-background', colors.Background || '#ffffff');
                    root.style.setProperty('--color-surface', colors.Surface || '#f9fafb');
                    root.style.setProperty('--color-text-primary', colors.TextPrimary || '#111827');
                    root.style.setProperty('--color-text-secondary', colors.TextSecondary || '#6b7280');
                    root.style.setProperty('--color-border', colors.Border || '#e5e7eb');
                }
            } catch (e) {
                console.error('Error loading theme:', e);
            }
        })();
    </script>
    
    <!-- Existing CSS files -->
    <link href="css/site.css" rel="stylesheet" />
    <link href="css/app.css" rel="stylesheet" />
    <!-- ... -->
</head>
```

**For Blazor WebAssembly** - Edit `wwwroot/index.html` (same changes as above)

### Step 4: Create or Update app.css

Create or edit `wwwroot/css/app.css` and **add** these theme variables:

```css
/* Tail.Blazor Theme Variables */
:root {
    /* Theme colors */
    --color-primary: #3b82f6;
    --color-secondary: #8b5cf6;
    --color-accent: #ec4899;
    --color-success: #10b981;
    --color-warning: #f59e0b;
    --color-danger: #ef4444;
    --color-info: #3b82f6;
    --color-background: #ffffff;
    --color-surface: #f9fafb;
    --color-text-primary: #111827;
    --color-text-secondary: #6b7280;
    --color-border: #e5e7eb;
}

/* Dark mode overrides */
html.dark {
    --color-background: #111827;
    --color-surface: #1f2937;
    --color-text-primary: #f9fafb;
    --color-text-secondary: #d1d5db;
    --color-border: #374151;
}

/* Base styles */
html {
    background-color: var(--color-background);
}

body {
    background-color: var(--color-background);
    color: var(--color-text-primary);
    transition: background-color 0.3s ease, color 0.3s ease;
}

/* Theme utility classes */
.theme-card {
    background-color: var(--color-surface);
    border-color: var(--color-border);
    color: var(--color-text-primary);
}

.theme-button {
    background-color: var(--color-primary);
    color: white;
    transition: all 0.2s;
}

.theme-button:hover {
    filter: brightness(1.1);
}

.theme-input {
    background-color: var(--color-surface);
    border-color: var(--color-border);
    color: var(--color-text-primary);
}

.theme-input:focus {
    border-color: var(--color-primary);
    outline: none;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

/* Background utilities */
.bg-theme-primary { background-color: var(--color-primary) !important; }
.bg-theme-surface { background-color: var(--color-surface) !important; }

/* Text utilities */
.text-theme-primary { color: var(--color-text-primary) !important; }
.text-theme-secondary { color: var(--color-text-secondary) !important; }

/* Border utilities */
.border-theme { border-color: var(--color-border) !important; }

/* Smooth transitions */
* {
    transition-property: background-color, border-color, color;
    transition-duration: 200ms;
    transition-timing-function: ease-in-out;
}

/* Keep your existing styles below */
/* ... */
```

### Step 5: Update _Imports.razor

Add Tail.Blazor namespaces to `_Imports.razor`:

```razor
@* Existing imports *@
@using System.Net.Http
@using Microsoft.AspNetCore.Components
@using Microsoft.JSInterop
@* ... *@

@* ADD THESE: Tail.Blazor imports *@
@using Tail.Blazor.Core.Theme
@using Tail.Blazor.Buttons
@using Tail.Blazor.Forms
@using Tail.Blazor.Layout
@using Tail.Blazor.Navigation
@using Tail.Blazor.Feedback
@using Tail.Blazor.Data
```

### Step 6: Add Theme Toggle to Layout

Edit your `Shared/MainLayout.razor`:

```razor
@inherits LayoutComponentBase
@using Tail.Blazor.Core.Theme

<div class="page">
    <div class="sidebar">
        <NavMenu />
    </div>

    <main>
        <div class="top-row px-4">
            <!-- ADD THIS: Theme Toggle -->
            <TailThemeToggle />
            
            <!-- Your existing top-row content -->
            <a href="https://docs.microsoft.com/aspnet/" target="_blank">About</a>
        </div>

        <article class="content px-4">
            @Body
        </article>
    </main>
</div>
```

### Step 7: Build and Test

```bash
# Clean solution
dotnet clean

# Restore packages
dotnet restore

# Build
dotnet build

# Run
dotnet run
```

Visit your app:
- ? Theme toggle should appear
- ? Dark mode should work
- ? No console errors

---

## Gradual Component Migration

### Strategy: Replace Components Incrementally

Don't replace all components at once. Migrate page by page or component by component.

### Example: Migrating a Form Page

**Before (using plain HTML):**
```razor
@page "/contact"

<h1>Contact Us</h1>

<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <div class="form-group">
        <label>Name:</label>
        <InputText @bind-Value="model.Name" class="form-control" />
    </div>
    
    <div class="form-group">
        <label>Email:</label>
        <InputText @bind-Value="model.Email" class="form-control" />
    </div>
    
    <div class="form-group">
        <label>Message:</label>
        <InputTextArea @bind-Value="model.Message" class="form-control" />
    </div>
    
    <button type="submit" class="btn btn-primary">Send</button>
</EditForm>
```

**After (using Tail.Blazor):**
```razor
@page "/contact"
@using Tail.Blazor.Forms
@using Tail.Blazor.Buttons

<div class="container mx-auto px-4 py-8 max-w-2xl">
    <h1 class="text-3xl font-bold mb-6 text-gray-900 dark:text-white">
        Contact Us
    </h1>

    <div class="theme-card border rounded-lg p-6">
        <EditForm Model="@model" OnValidSubmit="HandleSubmit">
            <div class="space-y-4">
                <TailInput @bind-Value="model.Name" 
                          Label="Name" 
                          Placeholder="Enter your name" 
                          Required="true" />
                
                <TailInput @bind-Value="model.Email" 
                          Label="Email" 
                          Type="email" 
                          Placeholder="your@email.com" 
                          Required="true" />
                
                <TailTextarea @bind-Value="model.Message" 
                             Label="Message" 
                             Rows="6" 
                             Required="true" />
                
                <TailButton Variant="ButtonVariant.Primary" 
                           Type="submit" 
                           IsLoading="@isSubmitting">
                    Send Message
                </TailButton>
            </div>
        </EditForm>
    </div>
</div>

@code {
    private ContactModel model = new();
    private bool isSubmitting = false;
    
    private async Task HandleSubmit()
    {
        isSubmitting = true;
        // Your submit logic
        await Task.Delay(1000);
        isSubmitting = false;
    }
}
```

### Migration Priority

1. **Start with new pages** - Use Tail.Blazor for all new features
2. **High-traffic pages** - Migrate frequently used pages first
3. **Forms** - Replace form components for better UX
4. **Buttons** - Quick wins, easy to replace
5. **Layout** - Migrate cards, panels, grids
6. **Complex components** - Migrate last (tables, charts)

---

## Compatibility with Existing Frameworks

### Bootstrap
? **Can coexist** - Tailwind and Bootstrap can work together
- Keep Bootstrap for existing components
- Use Tail.Blazor for new components
- Gradually migrate

### MudBlazor / Radzen / other UI libs
? **Can coexist** - Multiple UI libraries can work together
- Keep existing components
- Add Tail.Blazor alongside
- No conflicts expected

### Custom CSS
? **Fully compatible** - Tail.Blazor won't override your styles
- Your CSS continues to work
- Tail.Blazor uses scoped styles
- Use `theme-*` classes to adopt theming

---

## Troubleshooting Migration Issues

### Issue: CSS Conflicts

**Problem:** Existing Bootstrap/other CSS conflicts with Tailwind.

**Solution:**
```html
<!-- Load Tailwind AFTER other CSS frameworks -->
<link href="bootstrap.min.css" rel="stylesheet" />
<link href="app.css" rel="stylesheet" />
<script src="https://cdn.tailwindcss.com"></script>
```

### Issue: Theme Not Applying

**Problem:** Components don't use theme colors.

**Solution:**
1. Verify theme init script is in HTML
2. Check `app.css` has CSS variables
3. Use `.theme-card`, `.theme-button` classes
4. Or use CSS variables: `var(--color-primary)`

### Issue: Dark Mode Conflicts

**Problem:** Existing dark mode conflicts with Tail.Blazor.

**Solution:**
```css
/* In your app.css, wrap existing dark mode styles */
html.dark .your-existing-selector {
    /* Your dark mode styles */
}

/* Tail.Blazor dark mode won't conflict */
```

### Issue: Build Errors

**Problem:** Package restore or build fails.

**Solution:**
```bash
# Clean everything
dotnet clean
rm -rf bin obj

# Restore
dotnet restore

# Build
dotnet build
```

### Issue: JavaScript Errors

**Problem:** Theme toggle doesn't work.

**Solution:**
1. Check browser console for errors
2. Verify `localStorage` is accessible
3. Ensure theme init script runs before Blazor
4. Check for ad blockers blocking scripts

---

## Rollback Plan

If you need to rollback:

### Option 1: Git Revert
```bash
git log --oneline
git revert <commit-hash>
```

### Option 2: Manual Removal

1. Remove packages:
```bash
dotnet remove package Tail.Blazor.Core
dotnet remove package Tail.Blazor.Buttons
# ... etc
```

2. Remove service registrations from `Program.cs`
3. Remove theme scripts from HTML
4. Remove `@using` statements from `_Imports.razor`
5. Build and test

---

## Post-Migration Checklist

- [ ] All pages load without errors
- [ ] Theme toggle works
- [ ] Dark mode works
- [ ] Forms submit correctly
- [ ] Buttons respond to clicks
- [ ] Existing functionality unchanged
- [ ] No console errors
- [ ] Mobile responsive
- [ ] Accessibility maintained
- [ ] Performance acceptable

---

## Performance Considerations

### Tailwind CDN vs. Build Process

**CDN (What we use in setup):**
- ? Easy setup
- ? No build step
- ?? Larger file size
- ?? All Tailwind classes included

**Build Process (Production recommended):**
```bash
# Install Tailwind CLI
npm install -D tailwindcss

# Generate minimal CSS
npx tailwindcss -i ./wwwroot/css/app.css -o ./wwwroot/css/tailwind.css --minify
```

Then use `tailwind.css` instead of CDN for production.

---

## Next Steps

1. ? **Test thoroughly** - Ensure everything works
2. ?? **Read full docs** - See `README_USER_DOCUMENTATION.md`
3. ?? **Explore themes** - Visit `/theme-selector-demo`
4. ?? **Add more components** - Gradually migrate existing UI
5. ?? **Deploy** - Push to production when ready

---

## Need Help?

- ?? **Documentation:** `README_USER_DOCUMENTATION.md`
- ?? **Issues:** Create GitHub issue
- ?? **Discussions:** GitHub Discussions
- ?? **Support:** Check GitHub repository

---

**Happy Migrating!** ??

The gradual migration approach ensures your app stays stable while you benefit from Tail.Blazor's features.
