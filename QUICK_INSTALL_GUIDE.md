# ?? Tail.Blazor - Quick Installation Guide

## 5-Minute Setup

### Step 1: Create Blazor Project (1 min)

```bash
# Choose one:
dotnet new blazorserver -o MyApp    # Blazor Server
dotnet new blazorwasm -o MyApp      # Blazor WebAssembly
dotnet new blazor -o MyApp          # Blazor Web App (.NET 8+)

cd MyApp
```

### Step 2: Install Packages (1 min)

```bash
# Install core + common packages
dotnet add package Tail.Blazor.Core
dotnet add package Tail.Blazor.Buttons
dotnet add package Tail.Blazor.Forms
dotnet add package Tail.Blazor.Layout
```

### Step 3: Configure Services (1 min)

Edit `Program.cs`:

```csharp
using Tail.Blazor.Core;
using Tail.Blazor.Core.Extensions;

// ... existing code ...

// Add these lines before builder.Build():
builder.Services.AddTailBlazor(config => {
    config.ThemeMode = ThemeMode.Light;
});
builder.Services.AddTailBlazorTheme();
```

### Step 4: Add Tailwind CSS (1 min)

Add to `_Host.cshtml` (Blazor Server) or `index.html` (WebAssembly) in `<head>`:

```html
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>
<script>
    tailwind.config = { darkMode: 'class' }
</script>

<!-- Theme Init (copy from full docs) -->
<script>
    (function() {
        try {
            const settings = JSON.parse(localStorage.getItem('tail-blazor-theme-settings') || '{}');
            if (settings.Mode === 'Dark') {
                document.documentElement.classList.add('dark');
            }
            if (settings.Colors) {
                Object.entries(settings.Colors).forEach(([key, value]) => {
                    document.documentElement.style.setProperty(
                        `--color-${key.toLowerCase()}`, value
                    );
                });
            }
        } catch (e) {}
    })();
</script>

<link href="css/app.css" rel="stylesheet" />
```

### Step 5: Create app.css (1 min)

Create `wwwroot/css/app.css`:

```css
:root {
    --color-primary: #3b82f6;
    --color-background: #ffffff;
    --color-surface: #f9fafb;
    --color-text-primary: #111827;
    --color-border: #e5e7eb;
}

html.dark {
    --color-background: #111827;
    --color-surface: #1f2937;
    --color-text-primary: #f9fafb;
    --color-border: #374151;
}

body {
    background-color: var(--color-background);
    color: var(--color-text-primary);
}

.theme-card {
    background-color: var(--color-surface);
    border-color: var(--color-border);
}

.theme-button {
    background-color: var(--color-primary);
    color: white;
}

.theme-button:hover { filter: brightness(1.1); }
```

---

## ? Verify Installation

Create `Pages/Test.razor`:

```razor
@page "/test"
@using Tail.Blazor.Buttons
@using Tail.Blazor.Core.Theme

<div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold mb-4 text-gray-900 dark:text-white">
        Tail.Blazor Test
    </h1>
    
    <div class="mb-4">
        <TailThemeToggle />
    </div>
    
    <div class="theme-card border rounded-lg p-6 max-w-md">
        <h2 class="text-2xl font-semibold mb-4 text-gray-900 dark:text-white">
            Welcome!
        </h2>
        
        <div class="flex gap-2">
            <TailButton Variant="ButtonVariant.Primary">Primary</TailButton>
            <TailButton Variant="ButtonVariant.Success">Success</TailButton>
            <TailButton Variant="ButtonVariant.Danger">Danger</TailButton>
        </div>
    </div>
</div>
```

Run: `dotnet run`

Visit: `http://localhost:5000/test`

**Expected:**
- ? Buttons render with colors
- ? Theme toggle works
- ? Dark mode changes colors
- ? Card has themed background

---

## ?? All Available Packages

```bash
dotnet add package Tail.Blazor.Core           # Required
dotnet add package Tail.Blazor.Buttons        # Button components
dotnet add package Tail.Blazor.Forms          # Form inputs
dotnet add package Tail.Blazor.Layout         # Cards, grids, panels
dotnet add package Tail.Blazor.Navigation     # Tabs, menus, breadcrumbs
dotnet add package Tail.Blazor.Feedback       # Alerts, toasts, spinners
dotnet add package Tail.Blazor.Data           # Data grids, tables
dotnet add package Tail.Blazor.Charts         # Chart components
dotnet add package Tail.Blazor.Icons          # Icon library
dotnet add package Tail.Blazor.Utils          # Utility components
dotnet add package Tail.Blazor.Validators     # Form validation
dotnet add package Tail.Blazor.Visualization  # Data visualization
```

---

## ?? Add Theme Selector (Optional)

For advanced theming:

```razor
@page "/themes"
@using Tail.Blazor.Core.Theme

<div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold mb-6 text-gray-900 dark:text-white">
        Choose Your Theme
    </h1>
    
    <!-- 5 preset themes + custom theme creator -->
    <TailThemeSelector ShowPreview="true" />
</div>
```

**Features:**
- ?? Ocean (blue)
- ?? Forest (green)
- ?? Sunset (orange)
- ?? Purple Haze
- ?? Midnight (dark blue)
- ?? Custom theme creator

---

## ?? Next Steps

1. **Read Full Docs:** `README_USER_DOCUMENTATION.md`
2. **Explore Components:** Visit `/components` route
3. **Try Examples:** Visit `/examples` route
4. **Customize Themes:** Visit `/theme-selector-demo` route

---

## ?? Troubleshooting

### Theme not applying?
1. Check `app.css` has CSS variables
2. Verify theme init script in HTML
3. Ensure `AddTailBlazorTheme()` is called

### Components not found?
Add to `_Imports.razor`:
```razor
@using Tail.Blazor.Buttons
@using Tail.Blazor.Forms
@using Tail.Blazor.Core.Theme
```

### Build errors?
```bash
dotnet clean
dotnet restore
dotnet build
```

---

**That's it! You're ready to build with Tail.Blazor!** ??

For detailed documentation, see `README_USER_DOCUMENTATION.md`
