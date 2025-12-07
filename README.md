# Tail.Blazor Framework

**Ultra-lightweight, high-performance, modular Blazor component library** built with C#, Razor components, and Tailwind CSS using zero or minimal JavaScript.

## 🚀 Key Features

- **Ultra-Lightweight**: Core package only 48 KB (vs 200-250 KB for competitors)
- **High Performance**: Component render < 3 ms (average)
- **Zero-JS Components**: 90% of library requires no JavaScript
- **Modular Architecture**: 12 independent NuGet packages - install only what you need
- **100% Tailwind CSS**: Native Tailwind styling, no custom CSS
- **Native AOT Ready**: Full support for Native AOT compilation
- **Tree-Shaking**: 100% support - unused components eliminated at build time

## 📦 Packages

| Package | Size | Description |
|---------|------|-------------|
| **Tail.Blazor.Core** | 48 KB | Base classes, theme engine, config |
| **Tail.Blazor.Buttons** | 22 KB | All button types, FAB |
| **Tail.Blazor.Forms** | 95 KB | Inputs, Selects, Validation |
| **Tail.Blazor.Data** | 110 KB | DataGrid, ListView, Scheduler, Tree |
| **Tail.Blazor.Feedback** | 70 KB | Dialog, Toast, Alert, Spinner |
| **Tail.Blazor.Navigation** | 80 KB | Sidebar, Menu, Tabs, Accordion |
| **Tail.Blazor.Layout** | 45 KB | Card, Panel, Grid, Container |
| **Tail.Blazor.Icons** | 15 KB | Heroicons, Lucide, Custom SVG |
| **Tail.Blazor.Utils** | 28 KB | JS interop helpers (minimal) |
| **Tail.Blazor.Charts** | 65 KB | Pie, Bar, Line, Area Charts |
| **Tail.Blazor.Visualization** | 75 KB | Gauges, GoogleMap, QRCode |
| **Tail.Blazor.Validators** | 35 KB | Validation suite |

## 🏗️ Project Structure

```
Tail.Blazor/
├── src/
│   └── packages/          # 12 NuGet packages
│       ├── Tail.Blazor.Core
│       ├── Tail.Blazor.Buttons
│       ├── Tail.Blazor.Forms
│       ├── Tail.Blazor.Data
│       ├── Tail.Blazor.Feedback
│       ├── Tail.Blazor.Navigation
│       ├── Tail.Blazor.Layout
│       ├── Tail.Blazor.Icons
│       ├── Tail.Blazor.Utils
│       ├── Tail.Blazor.Charts
│       ├── Tail.Blazor.Visualization
│       └── Tail.Blazor.Validators
├── apps/
│   └── Tail.Blazor.Studio  # Visual designer (MAUI Hybrid)
└── docs/
    └── Tail.Blazor.Docs    # Documentation site
```

## 📋 Requirements

- .NET 8.0 SDK or later
- Visual Studio 2022 / VS Code / Rider

## 🚀 Quick Start

### Install Core Package

```bash
dotnet add package Tail.Blazor.Core
```

### Install Additional Packages (as needed)

```bash
dotnet add package Tail.Blazor.Buttons
dotnet add package Tail.Blazor.Forms
dotnet add package Tail.Blazor.Layout
```

### Configure Services

```csharp
using Tail.Blazor.Core;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();
builder.Services.AddTailBlazor(); // Add Tail.Blazor services
```

### Use Components

```razor
@using Tail.Blazor.Buttons

<TailButton Variant="ButtonVariant.Primary" Size="ButtonSize.Md">
    Click Me
</TailButton>
```

## 📖 Documentation

Full documentation available at [tailblazor.com](https://tailblazor.com)

## 📄 License

MIT License - Free for commercial use

## 🤝 Contributing

Contributions welcome! Please see our contributing guidelines.

---

**Built with ❤️ for performance and developer experience**

