# Tail.Blazor Documentation Scripts

This folder contains automation scripts for generating and maintaining Tail.Blazor documentation.

## Scripts Overview

### 1. `analyze_components.py`
**Purpose:** Discovers all components and generates the navigation menu structure.

**What it does:**
- Scans `src/components/` directory structure
- Discovers all component projects (folders with `.csproj` files)
- Analyzes implementation status
- Generates `NavMenu.json` with hierarchical structure matching `DocsNavMenu.razor`
- Outputs detailed component inventory by category

**Usage:**
```bash
python scripts/analyze_components.py
```

**Output:**
- `docs/Tail.Blazor.Docs/Pages/Components/NavMenu.json` - Navigation structure for docs site
- Console report with component inventory

**Categories (12 Total):**
- 🔘 Buttons (6 components)
- 📈 Charts (2 components)
- ⚙️ Core (3 components)
- 📊 Data (11 components)
- 💬 Feedback (19 components)
- 📝 Forms (26 components)
- 🎯 Icons (1 component)
- 📐 Layout (12 components)
- 🧭 Navigation (17 components)
- 🛠️ Utils (2 components)
- ✅ Validators (9 components)
- 🎨 Visualization (6 components)

---

### 2. `generate_doc_pages.py`
**Purpose:** Generates documentation pages for all components using Tail.Blazor components.

**What it does:**
- Discovers all components (same as analyze_components.py)
- Generates category overview pages (`_Overview.razor`)
- Generates individual component documentation pages
- Uses reusable components:
  - `DocPageTemplate.razor` - Main doc page template
  - `DocSection.razor` - Content sections
  - `CodePreview.razor` - Code examples with preview
- Includes standard sections: Installation, Basic Usage, Properties, Events, Examples, Related Components

**Usage:**
```bash
python scripts/generate_doc_pages.py
```

**Output:**
- `docs/Tail.Blazor.Docs/Pages/Components/{Category}/{ComponentName}.razor` (126 files total)
- Category overview pages at `docs/Tail.Blazor.Docs/Pages/Components/{Category}/_Overview.razor` (12 files)

**Generated Page Structure:**
Each component page includes:
```
- Installation section (dotnet add package command)
- Basic Usage example
- Properties documentation
- Events & Callbacks
- Advanced Examples
- Related Components links
```

---

## Workflow

### Initial Setup
Run both scripts in order to set up documentation:

```bash
# Step 1: Analyze components and generate navigation
python scripts/analyze_components.py

# Step 2: Generate documentation pages
python scripts/generate_doc_pages.py

# Step 3: Build project
dotnet build
```

### Adding New Components

1. **Create component** in `src/components/{category}/Tail.Blazor.{ComponentName}/`
2. **Run analyzer** to update navigation:
   ```bash
   python scripts/analyze_components.py
   ```
3. **Run generator** to create doc page:
   ```bash
   python scripts/generate_doc_pages.py
   ```
4. **Customize** the generated doc page with component-specific examples
5. **Build** and test

### Updating Components

- If you **rename** a component, re-run both scripts
- If you **add** properties/events, update the generated doc page manually
- If you **reorganize** categories, update `category_metadata` in scripts

---

## NavMenu.json Structure

The generated `NavMenu.json` follows this structure:

```json
{
  "version": "1.0.0",
  "lastUpdated": "2026-01-04T...",
  "menu": [
    {
      "label": "Components",
      "path": "#",
      "icon": "📦",
      "children": [
        {
          "label": "Buttons",
          "path": "/components/buttons",
          "icon": "🔘",
          "componentCount": 6,
          "children": [
            {
              "label": "Button",
              "path": "/components/buttons/button",
              "icon": "📄",
              "package": "Tail.Blazor.Button"
            }
          ]
        }
      ]
    }
  ]
}
```

---

## Documentation Page Template

Generated pages use this structure:

```razor
@page "/components/{category}/{component-name}"
@using Tail.Blazor.Docs.Shared

<DocPageTemplate Title="ComponentName" 
                 Description="Component description"
                 PackageName="Tail.Blazor.ComponentName">
    
    <DocSection Title="Installation">
        <!-- Installation code -->
    </DocSection>

    <DocSection Title="Basic Usage">
        <!-- Basic usage example -->
    </DocSection>

    <!-- More sections... -->
    
</DocPageTemplate>
```

---

## Automation & Maintenance

### Automatic Regeneration
Both scripts are **safe to run repeatedly**:
- `analyze_components.py` always overwrites `NavMenu.json`
- `generate_doc_pages.py` overwrites template pages (not custom content)

### Version Control
- ✅ Track: Script files (`analyze_components.py`, `generate_doc_pages.py`)
- ⚠️ Review: Generated `NavMenu.json` (check for new/removed components)
- ⚠️ Review: Generated doc pages (template structure changes)
- ✅ Track: Custom doc page content modifications

### Best Practices
1. Run scripts after adding/removing components
2. Customize generated doc pages with real examples
3. Keep component names consistent (Tail.Blazor.ComponentName)
4. Update category names only in script metadata
5. Use scripts as source of truth for navigation structure

---

## Troubleshooting

### NavMenu.json not generated
- Ensure `src/components/` directory exists
- Check `docs/Tail.Blazor.Docs/Pages/Components/` folder is writable
- Verify component project directories have `.csproj` files

### Doc pages not generating
- Ensure Python 3.8+ is installed
- Check disk space
- Verify `docs/Tail.Blazor.Docs/Pages/Components/` exists
- Run in project root directory

### Components not discovered
- Components must be in `src/components/{category}/` folders
- Component folders must contain `.csproj` file
- Category name must match metadata in scripts

---

## Statistics

- **Total Components:** 114
- **Total Categories:** 12
- **Generated Pages:** 126 (114 components + 12 overviews)
- **NavMenu Routes:** 140+ (includes all categories and components)

---

## Related Files

- **DocsNavMenu.razor** - Navigation component (uses NavMenu.json)
- **DocPageTemplate.razor** - Template used in generated pages
- **DocSection.razor** - Section wrapper component
- **CodePreview.razor** - Code example component
- **DOCUMENTATION_COMPLETE_GUIDE.md** - Full documentation guide

---

**Last Updated:** January 4, 2026  
**Scripts Version:** 1.0.0  
**Status:** ✅ Production Ready
