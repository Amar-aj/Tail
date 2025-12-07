# Tail.Blazor Documentation Guide

## Documentation Structure

The documentation site is organized into the following sections:

### Main Pages

1. **Home (`/`)** - Landing page with overview and quick links
2. **Getting Started (`/getting-started`)** - Installation and setup guide
3. **Components (`/components`)** - Component overview and links
4. **Theming (`/theming`)** - Theme customization guide
5. **Examples (`/examples`)** - Live examples and code samples
6. **API Reference (`/api`)** - Complete API documentation

### Component Documentation

Each component category has its own page:

- `/components/buttons` - Button components
- `/components/forms` - Form components
- `/components/layout` - Layout components
- `/components/navigation` - Navigation components
- `/components/feedback` - Feedback components
- `/components/data` - Data components

## Features

### User-Friendly Design
- ✅ Clean, modern UI with Tailwind CSS
- ✅ Dark mode support
- ✅ Responsive design
- ✅ Easy navigation with sidebar menu
- ✅ Code examples with syntax highlighting
- ✅ Live component demonstrations

### Content
- ✅ Installation instructions
- ✅ Configuration examples
- ✅ Component API reference
- ✅ Theme customization guide
- ✅ Best practices
- ✅ Code samples

### Navigation
- Sidebar menu for easy access
- Breadcrumb navigation
- Related links
- Search (can be added)

## Running the Documentation

```bash
cd docs/Tail.Blazor.Docs
dotnet restore
dotnet run
```

Visit `https://localhost:5001` or `http://localhost:5000` to view the documentation.

## Adding New Documentation

1. Create a new `.razor` file in `Pages/` or `Pages/Components/`
2. Add route with `@page` directive
3. Add to navigation menu in `Shared/NavMenu.razor`
4. Use Tail.Blazor components for consistent styling

## Documentation Best Practices

- Use clear, concise language
- Include code examples
- Show live component demos
- Provide API reference tables
- Include use cases and best practices
- Add screenshots where helpful

