# ?? Tail.Blazor - Complete User Documentation

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Quick Start](#quick-start)
4. [Theme System](#theme-system)
5. [Components](#components)
6. [Configuration](#configuration)
7. [Examples](#examples)
8. [Troubleshooting](#troubleshooting)

---

## Overview

**Tail.Blazor** is a comprehensive Blazor component library built with Tailwind CSS, offering 30+ production-ready components with:

- ?? **5 Preset Themes** with light & dark modes (10 variations)
- ?? **Custom Theme Support** with color pickers
- ?? **localStorage Persistence** - themes survive page reloads
- ? **Instant Theme Switching** - no page reload needed
- ?? **Responsive Design** - works on all devices
- ? **Accessible** - WCAG AA compliant
- ?? **Modern CSS** - CSS variables for easy customization

### Package Structure

```
Tail.Blazor.Core         - Core functionality & theme system
Tail.Blazor.Buttons      - Button components
Tail.Blazor.Forms        - Form input components
Tail.Blazor.Layout       - Layout components (cards, grids)
Tail.Blazor.Navigation   - Navigation components
Tail.Blazor.Feedback     - Feedback components (alerts, toasts)
Tail.Blazor.Data         - Data components (grids, tables)
Tail.Blazor.Charts       - Chart components
Tail.Blazor.Icons        - Icon components
Tail.Blazor.Utils        - Utility components
Tail.Blazor.Validators   - Validation components
Tail.Blazor.Visualization - Visualization components
```

---

## Installation

### Prerequisites

- **.NET 8.0 SDK** or higher
- **Visual Studio 2022** (v17.8+) or **Visual Studio Code** with C# extension
- **Node.js** (optional, for Tailwind CLI)

### Step 1: Create a New Blazor Project

#### Option A: Blazor Server
```bash
dotnet new blazorserver -o MyBlazorApp
cd MyBlazorApp
```

#### Option B: Blazor WebAssembly
```bash
dotnet new blazorwasm -o MyBlazorApp
cd MyBlazorApp
```

#### Option C: Blazor Web App (.NET 8+)
```bash
dotnet new blazor -o MyBlazorApp
cd MyBlazorApp
```

### Step 2: Install Tail.Blazor Packages

Install the core package and any additional packages you need:

```bash
# Core package (required)
dotnet add package Tail.Blazor.Core

# Additional packages (optional)
dotnet add package Tail.Blazor.Buttons
dotnet add package Tail.Blazor.Forms
dotnet add package Tail.Blazor.Layout
dotnet add package Tail.Blazor.Navigation
dotnet add package Tail.Blazor.Feedback
dotnet add package Tail.Blazor.Data
```

**Or install all at once:**
```bash
dotnet add package Tail.Blazor.Core
dotnet add package Tail.Blazor.Buttons
dotnet add package Tail.Blazor.Forms
dotnet add package Tail.Blazor.Layout
dotnet add package Tail.Blazor.Navigation
dotnet add package Tail.Blazor.Feedback
dotnet add package Tail.Blazor.Data
dotnet add package Tail.Blazor.Charts
dotnet add package Tail.Blazor.Icons
dotnet add package Tail.Blazor.Utils
dotnet add package Tail.Blazor.Validators
dotnet add package Tail.Blazor.Visualization
```

### Step 3: Configure Services

**For Blazor Server or Blazor Web App**, edit `Program.cs`:

```csharp
using Tail.Blazor.Core;
using Tail.Blazor.Core.Theme;
using Tail.Blazor.Core.Extensions;

var builder = WebApplication.CreateBuilder(args);

// Add Blazor services
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();

// Add Tail.Blazor services
builder.Services.AddTailBlazor(config =>
{
    config.ThemeMode = ThemeMode.Light;
    config.ThemePalette = ThemePalette.Blue;
    config.UseGradients = true;
});

// Add Theme Service (for advanced theming)
builder.Services.AddTailBlazorTheme();

var app = builder.Build();

// Configure middleware
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();

app.MapBlazorHub();
app.MapFallbackToPage("/_Host");

app.Run();
```

**For Blazor WebAssembly**, edit `Program.cs`:

```csharp
using Microsoft.AspNetCore.Components.Web;
using Microsoft.AspNetCore.Components.WebAssembly.Hosting;
using Tail.Blazor.Core;
using Tail.Blazor.Core.Extensions;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.RootComponents.Add<App>("#app");
builder.RootComponents.Add<HeadOutlet>("head::after");

builder.Services.AddScoped(sp => new HttpClient 
{ 
    BaseAddress = new Uri(builder.HostEnvironment.BaseAddress) 
});

// Add Tail.Blazor services
builder.Services.AddTailBlazor(config =>
{
    config.ThemeMode = ThemeMode.Light;
    config.ThemePalette = ThemePalette.Blue;
});

// Add Theme Service
builder.Services.AddTailBlazorTheme();

await builder.Build().RunAsync();
```

### Step 4: Add Tailwind CSS

Add Tailwind CSS to your `_Host.cshtml` (Blazor Server) or `index.html` (Blazor WebAssembly):

**For Blazor Server** (`Pages/_Host.cshtml`):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Blazor App</title>
    <base href="~/" />
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {}
            }
        }
    </script>
    
    <!-- Theme Initialization Script -->
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
    
    <link href="css/app.css" rel="stylesheet" />
</head>
<body>
    <component type="typeof(App)" render-mode="ServerPrerendered" />
    <script src="_framework/blazor.server.js"></script>
</body>
</html>
```

**For Blazor WebAssembly** (`wwwroot/index.html`):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Blazor App</title>
    <base href="/" />
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {}
            }
        }
    </script>
    
    <!-- Same theme initialization script as above -->
    
    <link href="css/app.css" rel="stylesheet" />
</head>
<body>
    <div id="app">Loading...</div>
    <script src="_framework/blazor.webassembly.js"></script>
</body>
</html>
```

### Step 5: Create app.css

Create `wwwroot/css/app.css` with theme variables:

```css
/* Theme CSS Variables */
:root {
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

html.dark {
    --color-background: #111827;
    --color-surface: #1f2937;
    --color-text-primary: #f9fafb;
    --color-text-secondary: #d1d5db;
    --color-border: #374151;
}

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
    box-shadow: 0 0 0 3px rgba(var(--color-primary-rgb), 0.1);
}

/* Smooth transitions */
* {
    transition-property: background-color, border-color, color;
    transition-duration: 200ms;
    transition-timing-function: ease-in-out;
}
```

---

## Quick Start

### 1. Add Theme Toggle to Your App

Add the theme toggle to your `MainLayout.razor` or `NavMenu.razor`:

```razor
@using Tail.Blazor.Core.Theme

<div class="navbar">
    <h1>My App</h1>
    
    <!-- Simple theme toggle -->
    <TailThemeToggle />
</div>
```

### 2. Use Your First Component

Create a page with Tail.Blazor components:

```razor
@page "/example"
@using Tail.Blazor.Buttons
@using Tail.Blazor.Forms

<PageTitle>Example Page</PageTitle>

<div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold mb-6 text-gray-900 dark:text-white">
        Welcome to Tail.Blazor!
    </h1>
    
    <!-- Buttons -->
    <div class="mb-6">
        <TailButton Variant="ButtonVariant.Primary" OnClick="HandleClick">
            Click Me
        </TailButton>
        <TailButton Variant="ButtonVariant.Success">
            Success
        </TailButton>
        <TailButton Variant="ButtonVariant.Danger">
            Danger
        </TailButton>
    </div>
    
    <!-- Form -->
    <div class="theme-card border rounded-lg p-6 max-w-md">
        <h2 class="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
            Contact Form
        </h2>
        
        <TailInput @bind-Value="name" Label="Name" Placeholder="Enter your name" />
        <TailInput @bind-Value="email" Label="Email" Type="email" Placeholder="Enter your email" />
        <TailTextarea @bind-Value="message" Label="Message" Placeholder="Enter your message" />
        
        <TailButton Variant="ButtonVariant.Primary" OnClick="SubmitForm">
            Submit
        </TailButton>
    </div>
</div>

@code {
    private string name = "";
    private string email = "";
    private string message = "";
    
    private void HandleClick()
    {
        // Handle button click
    }
    
    private void SubmitForm()
    {
        // Handle form submission
    }
}
```

### 3. Add Theme Selector (Optional)

For advanced theme customization, add the theme selector:

```razor
@page "/themes"
@using Tail.Blazor.Core.Theme

<PageTitle>Theme Selector</PageTitle>

<div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold mb-6 text-gray-900 dark:text-white">
        Choose Your Theme
    </h1>
    
    <TailThemeSelector ShowPreview="true" />
</div>
```

---

## Theme System

### Available Themes

Tail.Blazor includes **5 preset themes**, each with **light and dark modes**:

| Theme | Description | Primary Color (Light/Dark) |
|-------|-------------|---------------------------|
| ?? **Ocean** | Cool blue ocean vibes | `#0ea5e9` / `#38bdf8` |
| ?? **Forest** | Natural green forest | `#10b981` / `#34d399` |
| ?? **Sunset** | Warm sunset colors | `#f97316` / `#fb923c` |
| ?? **Purple Haze** | Rich purple gradient | `#8b5cf6` / `#a78bfa` |
| ?? **Midnight** | Deep blue midnight | `#3b82f6` / `#60a5fa` |

### Using Themes Programmatically

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
    Accent = "#ffe66d",
    Background = "#ffffff",
    Surface = "#f9fafb",
    TextPrimary = "#111827",
    TextSecondary = "#6b7280",
    Border = "#e5e7eb"
};
await ThemeService.ApplyCustomThemeAsync(customColors, "Light");

// Listen to theme changes
protected override async Task OnInitializedAsync()
{
    await ThemeService.InitializeAsync();
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
```

### Using Theme Classes

Apply theme-aware styling to your components:

```html
<!-- Card with theme colors -->
<div class="theme-card border rounded-lg p-6">
    <h3 class="text-gray-900 dark:text-white">Themed Card</h3>
    <p class="text-gray-600 dark:text-gray-400">Description</p>
    <button class="theme-button px-4 py-2 rounded-lg">Action</button>
</div>

<!-- Input with theme colors -->
<input type="text" class="theme-input w-full px-3 py-2 border rounded-lg" />

<!-- Using CSS variables directly -->
<div style="background-color: var(--color-surface); color: var(--color-text-primary);">
    Custom styled content
</div>
```

---

## Components

### Buttons (`Tail.Blazor.Buttons`)

```razor
@using Tail.Blazor.Buttons

<!-- Basic button -->
<TailButton Variant="ButtonVariant.Primary">Click Me</TailButton>

<!-- Button with click handler -->
<TailButton Variant="ButtonVariant.Success" OnClick="HandleClick">
    Save
</TailButton>

<!-- Button sizes -->
<TailButton Size="ButtonSize.Xs">Extra Small</TailButton>
<TailButton Size="ButtonSize.Sm">Small</TailButton>
<TailButton Size="ButtonSize.Md">Medium</TailButton>
<TailButton Size="ButtonSize.Lg">Large</TailButton>
<TailButton Size="ButtonSize.Xl">Extra Large</TailButton>

<!-- Button styles -->
<TailButton Style="ButtonStyle.Solid">Solid</TailButton>
<TailButton Style="ButtonStyle.Outline">Outline</TailButton>
<TailButton Style="ButtonStyle.Soft">Soft</TailButton>
<TailButton Style="ButtonStyle.Ghost">Ghost</TailButton>

<!-- Loading button -->
<TailButton IsLoading="@isLoading" OnClick="LoadData">
    Load Data
</TailButton>

<!-- Disabled button -->
<TailButton Disabled="true">Disabled</TailButton>

<!-- Icon button -->
<TailIconButton Variant="ButtonVariant.Primary">
    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
    </svg>
</TailIconButton>

<!-- Button group -->
<TailButtonGroup>
    <TailButton>Left</TailButton>
    <TailButton>Middle</TailButton>
    <TailButton>Right</TailButton>
</TailButtonGroup>
```

### Forms (`Tail.Blazor.Forms`)

```razor
@using Tail.Blazor.Forms

<!-- Text input -->
<TailInput @bind-Value="name" 
           Label="Name" 
           Placeholder="Enter your name" 
           Required="true" />

<!-- Email input -->
<TailInput @bind-Value="email" 
           Label="Email" 
           Type="email" 
           Placeholder="your@email.com" />

<!-- Password input -->
<TailInput @bind-Value="password" 
           Label="Password" 
           Type="password" />

<!-- Textarea -->
<TailTextarea @bind-Value="description" 
              Label="Description" 
              Rows="5" />

<!-- Select -->
<TailSelect @bind-Value="selectedOption" 
            Label="Choose Option">
    <option value="1">Option 1</option>
    <option value="2">Option 2</option>
    <option value="3">Option 3</option>
</TailSelect>

<!-- Checkbox -->
<TailCheckbox @bind-Value="agreed" 
              Label="I agree to the terms" />

<!-- Radio buttons -->
<TailRadioGroup @bind-Value="selectedValue" Label="Choose One">
    <TailRadio Value="1" Label="Option 1" />
    <TailRadio Value="2" Label="Option 2" />
    <TailRadio Value="3" Label="Option 3" />
</TailRadioGroup>

<!-- Switch -->
<TailSwitch @bind-Value="enabled" 
            Label="Enable notifications" />

<!-- Slider -->
<TailSlider @bind-Value="volume" 
            Label="Volume" 
            Min="0" 
            Max="100" />

<!-- Date picker -->
<TailDatePicker @bind-Value="selectedDate" 
                Label="Select Date" />

<!-- Color picker -->
<TailColorPicker @bind-Value="selectedColor" 
                 Label="Choose Color" />

<!-- File upload -->
<TailFileUpload @bind-Files="uploadedFiles" 
                Label="Upload Files" 
                Multiple="true" 
                Accept=".pdf,.doc,.docx" />
```

### Layout (`Tail.Blazor.Layout`)

```razor
@using Tail.Blazor.Layout

<!-- Card -->
<TailCard Header="Card Title" Footer="Card Footer">
    <p>Card content goes here.</p>
</TailCard>

<!-- Grid -->
<TailGrid Columns="3" Gap="GridGap.Md">
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
</TailGrid>

<!-- Responsive grid -->
<TailGrid Columns="1" MdColumns="2" LgColumns="4" Gap="GridGap.Lg">
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
    <div>Item 4</div>
</TailGrid>

<!-- Container -->
<TailContainer Size="ContainerSize.Lg">
    <p>Container content with max-width constraint</p>
</TailContainer>

<!-- Divider -->
<p>Content above</p>
<TailDivider Text="OR" />
<p>Content below</p>

<!-- Panel -->
<TailPanel Title="Panel Title" Subtitle="Panel subtitle">
    <p>Panel content</p>
</TailPanel>
```

### Navigation (`Tail.Blazor.Navigation`)

```razor
@using Tail.Blazor.Navigation

<!-- Tabs -->
<TailTabs Tabs="@tabItems" 
          ActiveTab="@activeTab" 
          ActiveTabChanged="OnTabChanged" />

<!-- Breadcrumb -->
<TailBreadcrumb Items="@breadcrumbItems" />

<!-- Accordion -->
<TailAccordion>
    <TailAccordionItem Title="Section 1" IsExpanded="true">
        <p>Content for section 1</p>
    </TailAccordionItem>
    <TailAccordionItem Title="Section 2">
        <p>Content for section 2</p>
    </TailAccordionItem>
</TailAccordion>

<!-- Steps -->
<TailSteps Steps="@stepItems" CurrentStep="2" />

<!-- Menu -->
<TailMenu>
    <TailMenuItem Text="Home" Icon="??" Href="/" />
    <TailMenuItem Text="About" Icon="??" Href="/about" />
    <TailMenuItem Text="Contact" Icon="??" Href="/contact" />
</TailMenu>

<!-- Sidebar -->
<TailSidebar IsCollapsed="false" Collapsible="true">
    <HeaderContent>
        <h3>Menu</h3>
    </HeaderContent>
    <ChildContent>
        <TailMenu>
            <TailMenuItem Text="Dashboard" />
            <TailMenuItem Text="Settings" />
        </TailMenu>
    </ChildContent>
</TailSidebar>
```

### Feedback (`Tail.Blazor.Feedback`)

```razor
@using Tail.Blazor.Feedback

<!-- Alert -->
<TailAlert Variant="AlertVariant.Success" 
           Title="Success!" 
           Dismissible="true">
    Operation completed successfully.
</TailAlert>

<!-- Badge -->
<TailBadge Variant="BadgeVariant.Primary">New</TailBadge>
<TailBadge Variant="BadgeVariant.Success" ShowDot="true">Active</TailBadge>

<!-- Progress bar -->
<TailProgress Value="75" ShowLabel="true" />

<!-- Circular progress -->
<TailProgressBarCircular Value="60" Size="100" ShowLabel="true" />

<!-- Spinner -->
<TailSpinner Size="SpinnerSize.Md" Color="SpinnerColor.Primary" />

<!-- Skeleton loader -->
<TailSkeleton Type="SkeletonType.Text" Lines="3" />

<!-- Toast (show programmatically) -->
@code {
    [Inject] private IToastService ToastService { get; set; }
    
    private void ShowToast()
    {
        ToastService.ShowSuccess("Action completed!", "Success");
    }
}
```

---

## Configuration

### Theme Configuration

Configure default theme in `Program.cs`:

```csharp
builder.Services.AddTailBlazor(config =>
{
    // Set default theme mode
    config.ThemeMode = ThemeMode.Light; // or ThemeMode.Dark
    
    // Set default color palette
    config.ThemePalette = ThemePalette.Blue; // or Green, Purple, Red, Orange
    
    // Enable gradients
    config.UseGradients = true;
    
    // Set gradient direction
    config.GradientDirection = "to-r"; // to-r, to-br, to-t, etc.
});
```

### Custom Color Palette

Apply a custom color palette:

```csharp
var customPalette = new CustomColorPalette
{
    Primary = "#ff6b6b",
    Secondary = "#4ecdc4",
    Accent = "#ffe66d"
};

var themeEngine = new ThemeEngine();
themeEngine.ApplyPalette(customPalette);
```

---

## Examples

### Example 1: Contact Form

```razor
@page "/contact"
@using Tail.Blazor.Forms
@using Tail.Blazor.Buttons

<div class="container mx-auto px-4 py-8 max-w-2xl">
    <div class="theme-card border rounded-lg p-8">
        <h1 class="text-3xl font-bold mb-6 text-gray-900 dark:text-white">
            Contact Us
        </h1>
        
        <EditForm Model="@model" OnValidSubmit="HandleSubmit">
            <DataAnnotationsValidator />
            
            <div class="space-y-4">
                <TailInput @bind-Value="model.Name" 
                          Label="Name" 
                          Placeholder="John Doe" 
                          Required="true" />
                
                <TailInput @bind-Value="model.Email" 
                          Label="Email" 
                          Type="email" 
                          Placeholder="john@example.com" 
                          Required="true" />
                
                <TailInput @bind-Value="model.Subject" 
                          Label="Subject" 
                          Placeholder="How can we help?" />
                
                <TailTextarea @bind-Value="model.Message" 
                             Label="Message" 
                             Placeholder="Your message here..." 
                             Rows="6" 
                             Required="true" />
                
                <div class="flex gap-2">
                    <TailButton Variant="ButtonVariant.Primary" 
                               Type="submit" 
                               IsLoading="@isSubmitting">
                        Send Message
                    </TailButton>
                    <TailButton Variant="ButtonVariant.Secondary" 
                               Style="ButtonStyle.Outline" 
                               OnClick="Reset">
                        Reset
                    </TailButton>
                </div>
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
        await Task.Delay(2000); // Simulate API call
        isSubmitting = false;
        
        // Show success message
        // Clear form
        model = new();
    }
    
    private void Reset()
    {
        model = new();
    }
    
    public class ContactModel
    {
        [Required]
        public string Name { get; set; } = "";
        
        [Required, EmailAddress]
        public string Email { get; set; } = "";
        
        public string Subject { get; set; } = "";
        
        [Required]
        public string Message { get; set; } = "";
    }
}
```

### Example 2: Dashboard

```razor
@page "/dashboard"
@using Tail.Blazor.Layout
@using Tail.Blazor.Buttons
@using Tail.Blazor.Feedback

<div class="container mx-auto px-4 py-8">
    <div class="flex items-center justify-between mb-8">
        <h1 class="text-4xl font-bold text-gray-900 dark:text-white">
            Dashboard
        </h1>
        <TailButton Variant="ButtonVariant.Primary">
            <span class="mr-2">+</span> New Item
        </TailButton>
    </div>
    
    <!-- Stats Grid -->
    <TailGrid Columns="1" MdColumns="2" LgColumns="4" Gap="GridGap.Lg" CssClass="mb-8">
        <TailCard>
            <div class="text-center">
                <div class="text-4xl font-bold text-blue-600 dark:text-blue-400">1,234</div>
                <div class="text-sm text-gray-600 dark:text-gray-400 mt-1">Total Users</div>
            </div>
        </TailCard>
        
        <TailCard>
            <div class="text-center">
                <div class="text-4xl font-bold text-green-600 dark:text-green-400">567</div>
                <div class="text-sm text-gray-600 dark:text-gray-400 mt-1">Active Sessions</div>
            </div>
        </TailCard>
        
        <TailCard>
            <div class="text-center">
                <div class="text-4xl font-bold text-orange-600 dark:text-orange-400">89</div>
                <div class="text-sm text-gray-600 dark:text-gray-400 mt-1">Pending Tasks</div>
            </div>
        </TailCard>
        
        <TailCard>
            <div class="text-center">
                <div class="text-4xl font-bold text-purple-600 dark:text-purple-400">$12.3K</div>
                <div class="text-sm text-gray-600 dark:text-gray-400 mt-1">Revenue</div>
            </div>
        </TailCard>
    </TailGrid>
    
    <!-- Recent Activity -->
    <TailCard Header="Recent Activity">
        <div class="space-y-4">
            <div class="flex items-center justify-between py-2 border-b border-gray-200 dark:border-gray-700">
                <div>
                    <div class="font-medium text-gray-900 dark:text-white">New user registered</div>
                    <div class="text-sm text-gray-600 dark:text-gray-400">2 minutes ago</div>
                </div>
                <TailBadge Variant="BadgeVariant.Success">New</TailBadge>
            </div>
            
            <div class="flex items-center justify-between py-2 border-b border-gray-200 dark:border-gray-700">
                <div>
                    <div class="font-medium text-gray-900 dark:text-white">Order #1234 completed</div>
                    <div class="text-sm text-gray-600 dark:text-gray-400">15 minutes ago</div>
                </div>
                <TailBadge Variant="BadgeVariant.Info">Order</TailBadge>
            </div>
            
            <div class="flex items-center justify-between py-2">
                <div>
                    <div class="font-medium text-gray-900 dark:text-white">System backup completed</div>
                    <div class="text-sm text-gray-600 dark:text-gray-400">1 hour ago</div>
                </div>
                <TailBadge Variant="BadgeVariant.Success">System</TailBadge>
            </div>
        </div>
    </TailCard>
</div>
```

---

## Troubleshooting

### Theme not applying

**Problem:** Theme colors not showing on components.

**Solution:**
1. Ensure theme initialization script is in `_Host.cshtml` or `index.html`
2. Check that `app.css` has theme CSS variables
3. Verify `ThemeService` is registered in `Program.cs`
4. Use `.theme-card`, `.theme-button` classes or CSS variables

### Dark mode not working

**Problem:** Dark mode toggle doesn't work.

**Solution:**
1. Check Tailwind config has `darkMode: 'class'`
2. Ensure theme toggle component is added
3. Verify `localStorage` is accessible
4. Check browser console for errors

### Build errors

**Problem:** Package reference errors.

**Solution:**
```bash
# Clean and restore
dotnet clean
dotnet restore
dotnet build
```

### Components not found

**Problem:** Component namespace errors.

**Solution:**
Add using statements to `_Imports.razor`:
```razor
@using Tail.Blazor.Buttons
@using Tail.Blazor.Forms
@using Tail.Blazor.Layout
@using Tail.Blazor.Navigation
@using Tail.Blazor.Feedback
@using Tail.Blazor.Core.Theme
```

---

## Support & Resources

### Documentation
- **Online Docs:** Visit your deployed docs site
- **Component Reference:** `/components` route
- **Theme Guide:** `/theme-selector-demo` route
- **Examples:** `/examples` route

### GitHub
- **Repository:** https://github.com/Amar-aj/Tail
- **Issues:** Report bugs and request features
- **Discussions:** Ask questions and share ideas

### Community
- **Discord:** Join our community (link coming soon)
- **Stack Overflow:** Tag questions with `tail-blazor`

---

## Version History

### v1.0.0 (Current)
- ? 12 component packages
- ? 30+ components
- ? 5 preset themes with light/dark modes
- ? Custom theme support
- ? localStorage persistence
- ? Comprehensive documentation

---

## License

Tail.Blazor is licensed under the **MIT License**.

---

**Happy Coding with Tail.Blazor!** ??

For more examples and detailed API documentation, visit your documentation site at `/components`.
