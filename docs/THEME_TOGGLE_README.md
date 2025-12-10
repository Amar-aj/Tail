# TailThemeToggle Component

A beautiful, accessible theme toggle component for Tail.Blazor with automatic local storage persistence and system preference detection.

## Features

- ? **Automatic Local Storage** - Persists theme preference across sessions
- ? **System Preference Detection** - Automatically detects user's OS theme preference
- ? **Multiple Styles** - Icon, Button, and Outlined variants
- ? **Smooth Animations** - Beautiful transitions between themes
- ? **Customizable Labels** - Custom text for light/dark modes
- ? **Event Callbacks** - React to theme changes
- ? **Fully Accessible** - ARIA labels and keyboard navigation

## Basic Usage

```razor
@using Tail.Blazor.Core.Theme

<!-- Simple icon toggle -->
<TailThemeToggle />

<!-- With label -->
<TailThemeToggle ShowLabel="true" />

<!-- Button style -->
<TailThemeToggle 
    Style="ThemeToggleStyle.Button" 
    ShowLabel="true" />

<!-- With event callback -->
<TailThemeToggle OnThemeChanged="HandleThemeChanged" />

@code {
    private void HandleThemeChanged(ThemeMode mode)
    {
        Console.WriteLine($"Theme changed to: {mode}");
    }
}
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `ShowLabel` | `bool` | `false` | Show text label next to icon |
| `Style` | `ThemeToggleStyle` | `Icon` | Button style: Icon, Button, or Outlined |
| `LightModeLabel` | `string?` | `"Light"` | Custom label for light mode |
| `DarkModeLabel` | `string?` | `"Dark"` | Custom label for dark mode |
| `OnThemeChanged` | `EventCallback<ThemeMode>` | - | Callback when theme changes |
| `CssClass` | `string?` | `null` | Additional CSS classes |

## Styles

### Icon (Default)
```razor
<TailThemeToggle />
```
Simple icon button with hover effects.

### Button
```razor
<TailThemeToggle Style="ThemeToggleStyle.Button" ShowLabel="true" />
```
Full button with background and padding.

### Outlined
```razor
<TailThemeToggle Style="ThemeToggleStyle.Outlined" ShowLabel="true" />
```
Button with border outline.

## Custom Styling

```razor
<TailThemeToggle 
    CssClass="bg-gradient-to-r from-purple-500 to-pink-500 text-white"
    ShowLabel="true" />
```

## Custom Labels

```razor
<TailThemeToggle 
    ShowLabel="true"
    LightModeLabel="?? Day Mode"
    DarkModeLabel="?? Night Mode" />
```

## How It Works

1. **Initial Load**
   - Checks local storage for saved preference
   - Falls back to system preference if no saved theme
   - Applies theme to document root

2. **Toggle Action**
   - Switches between Light and Dark modes
   - Saves preference to local storage
   - Applies theme classes to HTML element
   - Triggers event callback if provided

3. **Persistence**
   - Theme preference stored in `localStorage`
   - Automatically restored on page load
   - Works across browser tabs

## Local Storage

The component uses the key `tail-blazor-theme` to store the theme preference in localStorage.

You can customize the storage key by modifying the component's `StorageKey` constant:

```csharp
private const string StorageKey = "my-custom-theme-key";
```

## Integration with ThemeProvider

The component automatically integrates with the `ThemeEngine` service:

```razor
@using Tail.Blazor.Core.Theme

<ThemeProvider>
    <!-- Your app content -->
    <div class="min-h-screen bg-gray-50 dark:bg-gray-900">
        <!-- Theme toggle can be placed anywhere -->
        <nav>
            <TailThemeToggle />
        </nav>
        
        <!-- Content with theme-aware classes -->
        <main class="text-gray-900 dark:text-white">
            @Body
        </main>
    </div>
</ThemeProvider>
```

## Accessibility

The component includes:
- ARIA labels for screen readers
- Keyboard navigation support
- Focus indicators
- Semantic HTML
- Descriptive tooltips

## Browser Support

- Modern browsers with localStorage support
- Graceful degradation for older browsers
- System preference detection via `prefers-color-scheme`

## Examples

### Navigation Bar
```razor
<nav class="flex items-center justify-between p-4">
    <div class="logo">My App</div>
    <TailThemeToggle />
</nav>
```

### Settings Page
```razor
<div class="settings">
    <h2>Appearance</h2>
    <div class="flex items-center justify-between">
        <span>Theme Mode</span>
        <TailThemeToggle 
            Style="ThemeToggleStyle.Button"
            ShowLabel="true" />
    </div>
</div>
```

### With Dropdown Menu
```razor
<div class="menu">
    <button>Settings</button>
    <div class="dropdown">
        <div class="menu-item">
            <span>Dark Mode</span>
            <TailThemeToggle />
        </div>
    </div>
</div>
```

## Troubleshooting

### Theme not persisting
- Check browser console for localStorage errors
- Ensure JavaScript is enabled
- Verify wwwroot/theme-toggle.js is included

### Theme not applying
- Ensure ThemeProvider wraps your app
- Check that Tailwind dark mode is configured
- Verify HTML has `dark` class when in dark mode

### System preference not detected
- Check browser support for `prefers-color-scheme`
- Ensure no errors in browser console
- Try clearing localStorage and refreshing

## License

MIT License - Part of Tail.Blazor component library
