# Component Documentation Generation Strategy

## Overview
Automatic generation of comprehensive, responsive component documentation from source code using intelligent extraction and Tail.Blazor's native components.

---

## Phase 1: Component Analysis & Metadata Extraction

### 1.1 Extract Component Metadata
**Source:** Component `.razor` files and `.cs` code-behind

**Data to Extract:**
```
Component Information:
├── Name & FriendlyName
├── Description (from XML comments or README)
├── Package Name
├── Category
├── Version
└── Status (Stable/Beta/Experimental)

Parameters ([Parameter] attributes):
├── Name
├── Type
├── Default Value
├── Required/Optional
├── Description
└── Examples

Events ([Parameter] EventCallback):
├── Event Name
├── Parameters
├── Description
└── Usage Examples

Enums & Types:
├── ButtonVariant enum values (Primary, Secondary, Danger...)
├── ButtonSize enum values (Sm, Md, Lg...)
└── Each with descriptions
```

### 1.2 Script: `extract_component_metadata.py`
- Parses `.razor` files using regex/XML parsing
- Extracts `@code {}` blocks and C# properties
- Reads XML documentation comments
- Generates structured JSON metadata
- Output: `component_metadata.json`

---

## Phase 2: Example Generation

### 2.1 Create Component Examples
**Location:** `src/components/{category}/{ComponentName}/Examples/`

**Example Structure:**
```
Examples/
├── Basic.razor           # Simple usage
├── Variants.razor        # All variants (Primary, Secondary, etc)
├── Sizes.razor          # All sizes (Sm, Md, Lg)
├── States.razor         # Disabled, Loading, etc
├── Events.razor         # Click handlers, callbacks
└── Advanced.razor       # Complex combinations
```

### 2.2 Example Format (Razor Component)
```razor
@* Basic Button Example *@
<div class="flex gap-4">
    <TailButton>Click Me</TailButton>
    <TailButton Variant="ButtonVariant.Secondary">Secondary</TailButton>
</div>

@code {
    // Example code here
}
```

---

## Phase 3: Documentation Page Generation

### 3.1 Page Structure (Using Responsive Components)
```
┌─────────────────────────────────────────────────┐
│ Header with component name & description         │
├─────────────────────────────────────────────────┤
│                                                 │
│ Installation (Code preview with copy)           │
│                                                 │
│ Quick Start (Live example)                      │
│                                                 │
│ ┌──────────────────────────────────────────┐   │
│ │ Variants & Options                       │   │
│ │  ┌─────────────┬─────────────┐          │   │
│ │  │ Primary     │ Secondary   │          │   │
│ │  ├─────────────┼─────────────┤          │   │
│ │  │ Danger      │ Success     │          │   │
│ │  └─────────────┴─────────────┘          │   │
│ └──────────────────────────────────────────┘   │
│                                                 │
│ Properties Table (Responsive)                  │
│ │ Property │ Type │ Default │ Description │    │
│                                                 │
│ Events & Callbacks Section                     │
│                                                 │
│ Advanced Examples (Code & Preview)             │
│                                                 │
│ Related Components (Cards)                     │
│                                                 │
└─────────────────────────────────────────────────┘
```

### 3.2 Responsive UI/UX Components Used
- `TailContainer` - Responsive container (Full, Xl, Lg, Md, Sm)
- `TailGrid` - Responsive grid (col-1, md:col-2, lg:col-3)
- `TailCard` - Component showcase cards
- `TailButton` - Call-to-action buttons
- `TailTabs` - Switch between examples
- `CodePreview` - Your existing component (code + preview)
- `DocPageTemplate` - Your existing wrapper
- `DocSection` - Your existing section container

---

## Phase 4: Script Implementation

### 4.1 Enhanced `generate_rich_docs.py`
```
Main Script Flow:
├── [1] Load component metadata (extract_component_metadata.py output)
├── [2] Discover example files in each component folder
├── [3] For each component:
│   ├── Generate Installation section
│   ├── Generate Quick Start with first example
│   ├── Generate Variants grid (all enum values with visual preview)
│   ├── Generate Properties table (from metadata)
│   ├── Generate Events section (from metadata)
│   ├── Generate Examples tabs (each example file becomes a tab)
│   ├── Generate Related Components section
│   └── Wrap in DocPageTemplate with responsive grid
└── [5] Output: 121 complete documentation pages
```

### 4.2 Key Features
- **Responsive Grid Layout**: Automatically adjust columns based on content
- **Live Code + Preview**: Every example shows code and live preview
- **Tab Navigation**: Switch between Basic, Variants, States, Advanced
- **Property Tables**: Mobile-friendly responsive tables
- **Visual Variants Grid**: Show all variants with live previews
- **Copy Code Buttons**: Integrated with CodePreview component
- **Theme Consistent**: Uses your TailCSS + Tail.Blazor components
- **Mobile Optimized**: Full responsive design

---

## Phase 5: Implementation Steps

### Step 1: Run Metadata Extraction
```bash
python scripts/extract_component_metadata.py
# Output: scripts/component_metadata.json
```

### Step 2: Run Rich Documentation Generation
```bash
python scripts/generate_rich_docs.py
# Output: 114 documentation pages with 5 embedded example tabs each
# Location: docs/Tail.Blazor.Docs/Pages/Components/
```

### Step 3: Verify Build
```bash
dotnet build Tail.Blazor.sln -c Release
```

**Note:** Examples are embedded in documentation pages (in docs project only) to keep components lightweight.

### Step 4: Build & Verify
```bash
dotnet build Tail.Blazor.sln -c Release
```

---

## Example Output Structure

### Button Component Documentation
```
/components/buttons/button

┌─────────────────────────────────────┐
│ Button Component                    │
│ Flexible button component for       │
│ user interactions                   │
└─────────────────────────────────────┘

📦 Installation
$ dotnet add package Tail.Blazor.Button

🚀 Quick Start
[Live example of basic button]

🎨 Variants
┌─────────────┬─────────────┐
│ Primary     │ Secondary   │
│ [Preview]   │ [Preview]   │
├─────────────┼─────────────┤
│ Danger      │ Success     │
│ [Preview]   │ [Preview]   │
└─────────────┴─────────────┘

📋 Properties
Property    │ Type           │ Default │ Description
─────────────────────────────────────────────────
Variant     │ ButtonVariant  │ Primary │ Button style
Size        │ ButtonSize     │ Md      │ Button size
IsLoading   │ bool           │ false   │ Loading state

⚡ Events
OnClick     - Fired when button is clicked
OnValidate  - Custom validation callback

💡 Examples (Tabs)
[Basic] [Variants] [States] [Advanced]
[Live preview + Code for selected tab]

🔗 Related Components
[Card: ButtonGroup] [Card: FAB] [Card: IconButton]
```

---

## Benefits of This Approach

✅ **Automated**: Run script → Perfect docs  
✅ **Consistent**: Same structure for all 114 components  
✅ **Responsive**: Works on mobile, tablet, desktop  
✅ **Theme-aligned**: Uses your Tail.Blazor components  
✅ **Live Examples**: All examples are interactive  
✅ **Maintainable**: Update examples → docs auto-update  
✅ **Professional**: Enterprise-quality documentation  
✅ **Scalable**: Works for 114+ components effortlessly  

---

## Timeline

| Phase | Task | Time | Status |
|-------|------|------|--------|
| 1 | Create metadata extraction script | 1 hour | 📋 Plan |
| 2 | Create example files for 3-5 components | 2 hours | 📋 Plan |
| 3 | Create rich doc generation script | 3 hours | 📋 Plan |
| 4 | Test & refine on few components | 1 hour | 📋 Plan |
| 5 | Generate all 114 docs | 5 minutes | 📋 Plan |
| 6 | Build & verify | 1 minute | 📋 Plan |

---

## Next Steps

1. **Review this strategy** ✅ (this file)
2. **Approve script approach** (awaiting confirmation)
3. **Create example files** (for Buttons component first as test)
4. **Build metadata extractor** (extract_component_metadata.py)
5. **Build rich doc generator** (generate_rich_docs.py)
6. **Test on 3 components** (Buttons, Input, Card)
7. **Generate all 114 docs** (full automation)
8. **Verify build & responsiveness** (final QA)

---

**Document Generated:** January 4, 2026  
**Status:** Ready for Implementation  
**Approach:** Script-Based Automation with Native Component Reuse
