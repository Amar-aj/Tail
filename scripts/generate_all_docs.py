#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tail.Blazor All-In-One Documentation Generator
Comprehensive pipeline: Discovery → Extraction → Generation → Overviews → Navigation

Architecture based on SUMMARY.md:
- Modular utilities (shared base functions)
- Component discovery & analysis
- Metadata extraction (288+ parameters)
- Rich documentation generation (MudBlazor-style)
- Global & category overview pages
- Navigation menu generation (NavMenu.json)

Total: 114 components across 12 categories
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime

# Fix Unicode output on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# ============================================================================
# PHASE 1: COMPONENT DISCOVERY
# ============================================================================

CATEGORY_METADATA = {
    "buttons": {"icon": "🔘", "order": 1, "display": "Buttons"},
    "charts": {"icon": "📈", "order": 2, "display": "Charts"},
    "core": {"icon": "⚙️", "order": 3, "display": "Core"},
    "data": {"icon": "📊", "order": 4, "display": "Data"},
    "feedback": {"icon": "💬", "order": 5, "display": "Feedback"},
    "forms": {"icon": "📝", "order": 6, "display": "Forms"},
    "icons": {"icon": "🎯", "order": 7, "display": "Icons"},
    "layout": {"icon": "📐", "order": 8, "display": "Layout"},
    "navigation": {"icon": "🧭", "order": 9, "display": "Navigation"},
    "utils": {"icon": "🛠️", "order": 10, "display": "Utils"},
    "validators": {"icon": "✅", "order": 11, "display": "Validators"},
    "visualization": {"icon": "🎨", "order": 12, "display": "Visualization"}
}

# Generic component detection
GENERIC_COMPONENTS = ['DataGrid', 'ListView', 'VirtualScroll']

# Missing/not-implemented components (or libraries without components)
MISSING_COMPONENTS = ['Avatar', 'Chip', 'Popover', 'Snackbar', 'Tooltip', 
                     'InfiniteScroll', 'BottomNavigation', 'NavDrawer', 
                     'Core', 'Core.Base']  # Core packages are libraries, not components


def discover_components():
    """Phase 1: Discover all components from src/components."""
    components_dir = Path("src/components")
    components = {}
    
    if not components_dir.exists():
        print(f"  [ERROR] Components directory not found: {components_dir}")
        return components
    
    for category_dir in sorted(components_dir.iterdir()):
        if not category_dir.is_dir():
            continue
        
        category = category_dir.name.lower()
        metadata = CATEGORY_METADATA.get(category, {"icon": "📦", "order": 99, "display": category.capitalize()})
        
        components[category] = {
            "icon": metadata["icon"],
            "order": metadata["order"],
            "display_name": metadata["display"],
            "components": []
        }
        
        for component_dir in sorted(category_dir.iterdir()):
            if not component_dir.is_dir():
                continue
            
            component_name = component_dir.name
            csproj_file = component_dir / f"{component_name}.csproj"
            
            if csproj_file.exists():
                razor_file = next(component_dir.glob("*.razor"), None)
                friendly_name = component_name.replace("Tail.Blazor.", "")
                
                is_generic = friendly_name in GENERIC_COMPONENTS
                is_missing = friendly_name in MISSING_COMPONENTS
                
                components[category]["components"].append({
                    "name": component_name,
                    "friendly_name": friendly_name,
                    "path": str(component_dir),
                    "razor_file": str(razor_file) if razor_file else None,
                    "implemented": razor_file is not None,
                    "is_generic": is_generic,
                    "is_missing": is_missing,
                    "category": category
                })
    
    return components


# ============================================================================
# PHASE 2: METADATA EXTRACTION
# ============================================================================

def extract_razor_code(file_path):
    """Extract @code block from .razor file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        code_blocks = []
        pattern = r'@code\s*\{(.*?)(?=\n@code|\Z)'
        
        for match in re.finditer(pattern, content, re.DOTALL):
            code_blocks.append(match.group(1).strip())
        
        return '\n'.join(code_blocks) if code_blocks else ""
    except Exception as e:
        return ""


def extract_parameters(code_block):
    """Extract [Parameter] properties with types and defaults."""
    parameters = []
    
    if not code_block:
        return parameters
    
    # Pattern for [Parameter] declarations
    pattern = r'^\s*\[Parameter\]\s+(?:public\s+)?([\w\.<>?,\s\[\]]+?)\s+(\w+)\s*(?:\{\s*get[^}]*set[^}]*\})?\s*(?:=\s*([^;]+))?;'
    
    for match in re.finditer(pattern, code_block, re.MULTILINE | re.DOTALL):
        param_type = re.sub(r'\s+', ' ', match.group(1).strip())
        param_name = match.group(2).strip()
        default_value = match.group(3).strip() if match.group(3) else None
        
        # Clean default value
        if default_value and any(x in default_value for x in ['=>', 'return', '{', 'var ']):
            default_value = None
        
        # Generate description
        desc = generate_parameter_description(param_name, param_type)
        
        parameters.append({
            "name": param_name,
            "type": param_type,
            "default": default_value,
            "description": desc
        })
    
    return parameters


def generate_parameter_description(param_name, param_type):
    """Auto-generate parameter descriptions."""
    param_lower = param_name.lower()
    
    descriptions = {
        'variant': 'Visual variant style for the component',
        'size': 'Size of the component',
        'disabled': 'Whether the component is disabled',
        'loading': 'Whether the component is in loading state',
        'icon': 'Icon to display',
        'label': 'Label text for the component',
        'placeholder': 'Placeholder text',
        'color': 'Color scheme for the component',
        'value': 'Current value of the component',
        'changed': 'Event callback raised when value changes',
        'click': 'Event callback raised when clicked',
        'style': 'Additional CSS styles',
        'class': 'Additional CSS classes',
        'required': 'Whether the component is required',
        'readonly': 'Whether the component is read-only',
        'visible': 'Whether the component is visible',
        'min': 'Minimum value constraint',
        'max': 'Maximum value constraint',
        'step': 'Step value for numeric inputs',
        'pattern': 'Validation pattern (regex)',
        'maxlength': 'Maximum length of input',
        'items': 'Data items collection'
    }
    
    for keyword, desc in descriptions.items():
        if keyword in param_lower:
            return desc
    
    return f'{param_name} parameter'


def extract_component_metadata(component_info):
    """Extract metadata for a single component."""
    if not component_info['razor_file']:
        return {
            "name": component_info['name'],
            "friendly_name": component_info['friendly_name'],
            "category": component_info['category'],
            "description": f"{component_info['friendly_name']} component",
            "parameters": [],
            "events": [],
            "is_generic": component_info.get('is_generic', False),
            "is_missing": component_info.get('is_missing', False)
        }
    
    code_block = extract_razor_code(component_info['razor_file'])
    parameters = extract_parameters(code_block)
    
    return {
        "name": component_info['name'],
        "friendly_name": component_info['friendly_name'],
        "category": component_info['category'],
        "description": f"{component_info['friendly_name']} component for Tail.Blazor",
        "parameters": parameters,
        "events": [],
        "is_generic": component_info.get('is_generic', False),
        "is_missing": component_info.get('is_missing', False)
    }


# ============================================================================
# PHASE 3: DOCUMENTATION GENERATION
# ============================================================================

def escape_razor_code(code):
    """Escape code for Razor @"" verbatim strings."""
    if not code:
        return ""
    return code.replace('"', '""')


def get_component_examples(component_name, friendly_name, category, parameters, is_generic):
    """Generate feature-based examples."""
    if '.' in friendly_name:
        component_tag = component_name.replace('Tail.Blazor.', 'Tail')
    else:
        component_tag = f"Tail{friendly_name}"
    
    if is_generic:
        return {"basic": f'@* {friendly_name} requires type parameter *@'}
    
    examples = {}
    
    # Basic example
    if category.lower() == 'buttons':
        examples['basic'] = f'<{component_tag}>Click Me</{component_tag}>'
    elif category.lower() == 'forms':
        examples['basic'] = f'<{component_tag} Placeholder="Enter text..." />'
    else:
        examples['basic'] = f'<{component_tag} />'
    
    # Variants
    if any('variant' in p['name'].lower() for p in parameters):
        variant_param = next((p for p in parameters if 'variant' in p['name'].lower()), None)
        if variant_param:
            vtype = variant_param['type']
            examples['variants'] = f'''<{component_tag} Variant="{vtype}.Primary">Primary</{component_tag}>
<{component_tag} Variant="{vtype}.Secondary">Secondary</{component_tag}>
<{component_tag} Variant="{vtype}.Outline">Outline</{component_tag}>'''
    
    # Sizes
    if any('size' in p['name'].lower() for p in parameters):
        size_param = next((p for p in parameters if 'size' in p['name'].lower()), None)
        if size_param:
            stype = size_param['type']
            examples['sizes'] = f'''<{component_tag} Size="{stype}.Sm">Small</{component_tag}>
<{component_tag} Size="{stype}.Md">Medium</{component_tag}>
<{component_tag} Size="{stype}.Lg">Large</{component_tag}>'''
    
    # States
    states_code = []
    if any('disabled' in p['name'].lower() for p in parameters):
        states_code.append(f'<{component_tag} Disabled="true">Disabled</{component_tag}>')
    if any('loading' in p['name'].lower() for p in parameters):
        states_code.append(f'<{component_tag} IsLoading="true">Loading</{component_tag}>')
    if states_code:
        examples['states'] = '\n'.join(states_code)
    
    return examples


def generate_doc_page(component_meta):
    """Generate MudBlazor-style documentation page."""
    name = component_meta['name']
    friendly_name = component_meta['friendly_name']
    category = component_meta['category']
    params = component_meta['parameters']
    is_generic = component_meta.get('is_generic', False)
    is_missing = component_meta.get('is_missing', False)
    
    component_tag = f"Tail{friendly_name}" if '.' not in friendly_name else name.replace('Tail.Blazor.', 'Tail')
    
    # Generate examples
    examples = get_component_examples(name, friendly_name, category, params, is_generic)
    
    # Build page header
    doc_page = f'@page "/components/{category.lower()}/{friendly_name.lower()}"\n'
    
    # Add @using directive only if not generic and not missing
    if not is_generic and not is_missing:
        doc_page += f'@using {name}\n'
    
    doc_page += '@using Tail.Blazor.Docs.Shared\n\n'
    
    doc_page += f'''<DocPageTemplate Title="{friendly_name}"
                 Description="{friendly_name} component for Tail.Blazor"
                 PackageName="{name}"
                 ApiParameters="@apiParameters">
    
    <DocSection Title="Installation">
        <CodePreview Title="Package Installation" Code="@installCode" ShowPreview="false" Language="bash" />
    </DocSection>

    <DocSection Title="Basic Usage">
'''
    
    if is_generic:
        doc_page += f'''        <div class="p-4 rounded-lg mb-4" style="background-color: var(--color-surface-2); color: var(--color-text-primary);">
            <p class="font-medium">⚠️ Generic Component</p>
            <p class="text-sm mt-2">This component requires a type parameter. Example:</p>
            <code class="block mt-2 p-2 rounded" style="background-color: var(--color-surface-1);">
                &lt;{component_tag} T="YourModel"&gt;...&lt;/{component_tag}&gt;
            </code>
        </div>
'''
    elif is_missing:
        doc_page += '''        <div class="p-4 rounded-lg mb-4" style="background-color: var(--color-surface-2); color: var(--color-text-primary);">
            <p class="font-medium">🚧 Coming Soon</p>
            <p class="text-sm mt-2">This component is planned but not yet implemented.</p>
        </div>
'''
    else:
        doc_page += '        <CodePreview Title="Basic Example" Code="@basicCode" ShowPreview="false" Language="razor" />\n'
    
    doc_page += '    </DocSection>\n'
    
    # Add feature sections
    if 'variants' in examples and not is_generic and not is_missing:
        doc_page += '''
    <DocSection Title="Variants">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Different visual variants for various use cases.
        </p>
        <CodePreview Title="Variant Options" Code="@variantsCode" ShowPreview="false" Language="razor" />
    </DocSection>
'''
    
    if 'sizes' in examples and not is_generic and not is_missing:
        doc_page += '''
    <DocSection Title="Sizes">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Size options to fit different layouts and contexts.
        </p>
        <CodePreview Title="Size Options" Code="@sizesCode" ShowPreview="false" Language="razor" />
    </DocSection>
'''
    
    if 'states' in examples and not is_generic and not is_missing:
        doc_page += '''
    <DocSection Title="States">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Component states like disabled and loading.
        </p>
        <CodePreview Title="Component States" Code="@statesCode" ShowPreview="false" Language="razor" />
    </DocSection>
'''
    
    doc_page += '''
    <DocSection Title="Features">
        <ul class="space-y-2" style="list-style: disc; padding-left: 1.5rem;">
            <li>Full theme support with CSS variables</li>
            <li>Responsive design</li>
            <li>Accessibility features built-in</li>
            <li>Type-safe with IntelliSense</li>
        </ul>
    </DocSection>
</DocPageTemplate>

@code {
'''
    
    # Add code variables
    doc_page += f'    private bool isGeneric = {str(is_generic).lower()};\n'
    doc_page += f'    private bool isMissing = {str(is_missing).lower()};\n\n'
    doc_page += f'    private string installCode = @"dotnet add package {name}";\n\n'
    
    basic_code = escape_razor_code(examples.get("basic", ""))
    doc_page += f'    private string basicCode = @"{basic_code}";\n\n'
    
    if 'variants' in examples:
        variants_escaped = escape_razor_code(examples["variants"])
        doc_page += f'    private string variantsCode = @"\n{variants_escaped}\n";\n\n'
    
    if 'sizes' in examples:
        sizes_escaped = escape_razor_code(examples["sizes"])
        doc_page += f'    private string sizesCode = @"\n{sizes_escaped}\n";\n\n'
    
    if 'states' in examples:
        states_escaped = escape_razor_code(examples["states"])
        doc_page += f'    private string statesCode = @"\n{states_escaped}\n";\n\n'
    else:
        doc_page += '    private string statesCode = @"\n<TailComponent Disabled=""true"">Disabled</TailComponent>\n";\n\n'
    
    # API parameters
    doc_page += '    private List<DocPageTemplate.ApiParameter> apiParameters = new()\n    {\n'
    for param in params:
        default_val = param.get('default', '-') or '-'
        # Handle empty strings properly
        if default_val == '""' or default_val == "''":
            default_val = '-'
        elif default_val and default_val.strip():
            # Escape quotes properly
            default_val = default_val.replace('"', '""')
        else:
            default_val = '-'
        
        desc = param.get('description', '').replace('"', '""')
        doc_page += f'        new() {{ Name = "{param["name"]}", Type = "{param["type"]}", '
        doc_page += f'Default = "{default_val}", Description = "{desc}" }},\n'
    doc_page += '    };\n}\n'
    
    return doc_page


# ============================================================================
# PHASE 4: OVERVIEW PAGES GENERATION
# ============================================================================

def generate_global_overview(components_by_category, total_params):
    """Generate global _Overview.razor page."""
    total_components = sum(len(cat['components']) for cat in components_by_category.values())
    total_categories = len(components_by_category)
    
    page = '''@page "/components"
@using Tail.Blazor.Docs.Shared

<PageTitle>Components - Tail.Blazor</PageTitle>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Hero Section -->
    <div class="text-center mb-12">
        <h1 class="text-4xl font-bold mb-4" style="color: var(--color-text-primary);">
            Tail.Blazor Components
        </h1>
        <p class="text-xl mb-6" style="color: var(--color-text-secondary);">
            A comprehensive collection of ''' + str(total_components) + ''' production-ready Blazor components
        </p>
        
        <!-- Quick Stats -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-3xl mx-auto mb-8">
            <div class="p-4 rounded-lg" style="background-color: var(--color-surface-2);">
                <div class="text-3xl font-bold" style="color: var(--color-primary);">''' + str(total_components) + '''</div>
                <div class="text-sm" style="color: var(--color-text-secondary);">Components</div>
            </div>
            <div class="p-4 rounded-lg" style="background-color: var(--color-surface-2);">
                <div class="text-3xl font-bold" style="color: var(--color-primary);">''' + str(total_categories) + '''</div>
                <div class="text-sm" style="color: var(--color-text-secondary);">Categories</div>
            </div>
            <div class="p-4 rounded-lg" style="background-color: var(--color-surface-2);">
                <div class="text-3xl font-bold" style="color: var(--color-primary);">''' + str(total_params) + '''+</div>
                <div class="text-sm" style="color: var(--color-text-secondary);">Parameters</div>
            </div>
            <div class="p-4 rounded-lg" style="background-color: var(--color-surface-2);">
                <div class="text-3xl font-bold" style="color: var(--color-primary);">100%</div>
                <div class="text-sm" style="color: var(--color-text-secondary);">Documented</div>
            </div>
        </div>
    </div>

    <!-- Component Categories Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
'''
    
    sorted_categories = sorted(components_by_category.items(), key=lambda x: x[1]["order"])
    
    for category, cat_data in sorted_categories:
        components = cat_data["components"]
        comp_count = len(components)
        icon = cat_data["icon"]
        display_name = cat_data["display_name"]
        
        # Get first 6 components to show
        shown_comps = sorted(components, key=lambda x: x["friendly_name"])[:6]
        remaining = comp_count - len(shown_comps)
        
        page += f'''        <!-- {display_name} Category -->
        <div class="p-6 rounded-lg border-2 transition-all hover:shadow-lg" 
             style="background-color: var(--color-surface-1); border-color: var(--color-border);">
            <div class="flex items-center mb-4">
                <span class="text-3xl mr-3">{icon}</span>
                <h2 class="text-2xl font-bold" style="color: var(--color-text-primary);">{display_name}</h2>
            </div>
            <p class="mb-4 text-sm" style="color: var(--color-text-secondary);">
                {display_name} components for Tail.Blazor
            </p>
            <div class="text-sm mb-3" style="color: var(--color-text-secondary);">
                <strong>{comp_count} components</strong>
            </div>
            <div class="space-y-1">
'''
        
        for comp in shown_comps:
            friendly = comp["friendly_name"]
            page += f'''                <a href="/components/{category}/{friendly.lower()}" class="block text-sm hover:underline" style="color: var(--color-primary);">{friendly}</a>
'''
        
        if remaining > 0:
            page += f'''                <div class="text-xs pt-1" style="color: var(--color-text-tertiary);">+ {remaining} more components...</div>
'''
        
        page += '''            </div>
        </div>

'''
    
    page += '''    </div>

    <!-- Getting Started Section -->
    <div class="mt-12 p-8 rounded-lg" style="background-color: var(--color-surface-2);">
        <h2 class="text-2xl font-bold mb-4" style="color: var(--color-text-primary);">
            Getting Started
        </h2>
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Install any component package via NuGet:
        </p>
        <div class="p-4 rounded font-mono text-sm" style="background-color: var(--color-surface-1); color: var(--color-text-primary);">
            dotnet add package Tail.Blazor.Button
        </div>
        <p class="mt-4" style="color: var(--color-text-secondary);">
            All components are independently packaged for maximum flexibility and minimal bundle size.
        </p>
        <div class="mt-6">
            <a href="/getting-started" class="inline-block px-6 py-3 rounded-lg font-medium transition-colors"
               style="background-color: var(--color-primary); color: white;">
                View Installation Guide →
            </a>
        </div>
    </div>
</div>
'''
    
    return page


def generate_category_overview(category, cat_data, all_metadata):
    """Generate category-specific _Overview.razor page."""
    components = cat_data["components"]
    icon = cat_data["icon"]
    display_name = cat_data["display_name"]
    comp_count = len(components)
    
    # Calculate total parameters for this category
    total_params = sum(len(all_metadata[category]["components"][comp["name"]]["parameters"]) 
                      for comp in components)
    
    page = f'''@page "/components/{category}"
@using Tail.Blazor.Docs.Shared

<PageTitle>{display_name} Components - Tail.Blazor</PageTitle>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Category Header -->
    <div class="mb-8">
        <div class="flex items-center mb-4">
            <span class="text-5xl mr-4">{icon}</span>
            <div>
                <h1 class="text-4xl font-bold" style="color: var(--color-text-primary);">
                    {display_name} Components
                </h1>
                <p class="text-lg mt-2" style="color: var(--color-text-secondary);">
                    {comp_count} components with {total_params}+ parameters
                </p>
            </div>
        </div>
    </div>

    <!-- Components Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
'''
    
    sorted_comps = sorted(components, key=lambda x: x["friendly_name"])
    
    for comp in sorted_comps:
        friendly = comp["friendly_name"]
        comp_name = comp["name"]
        comp_meta = all_metadata[category]["components"][comp_name]
        param_count = len(comp_meta["parameters"])
        is_generic = comp_meta.get("is_generic", False)
        is_missing = comp_meta.get("is_missing", False)
        
        status_badge = ""
        if is_generic:
            status_badge = '<span class="text-xs px-2 py-1 rounded" style="background-color: var(--color-warning); color: white;">Generic</span>'
        elif is_missing:
            status_badge = '<span class="text-xs px-2 py-1 rounded" style="background-color: var(--color-surface-3); color: var(--color-text-secondary);">Coming Soon</span>'
        
        page += f'''        <!-- {friendly} Component -->
        <a href="/components/{category}/{friendly.lower()}" 
           class="block p-6 rounded-lg border-2 transition-all hover:shadow-lg hover:border-opacity-70"
           style="background-color: var(--color-surface-1); border-color: var(--color-border); text-decoration: none;">
            <div class="flex items-center justify-between mb-3">
                <h3 class="text-xl font-semibold" style="color: var(--color-text-primary);">
                    {friendly}
                </h3>
                {status_badge}
            </div>
            <p class="text-sm mb-3" style="color: var(--color-text-secondary);">
                {comp_meta["description"]}
            </p>
            <div class="flex items-center justify-between text-xs" style="color: var(--color-text-tertiary);">
                <span>{param_count} parameters</span>
                <span class="font-mono">{comp_name}</span>
            </div>
        </a>

'''
    
    page += f'''    </div>

    <!-- Category Navigation -->
    <div class="mt-8 flex justify-between items-center">
        <a href="/components" class="text-sm hover:underline" style="color: var(--color-primary);">
            ← Back to All Components
        </a>
        <div class="text-sm" style="color: var(--color-text-secondary);">
            Total: {comp_count} components
        </div>
    </div>
</div>
'''
    
    return page


# ============================================================================
# PHASE 5: NAVIGATION MENU GENERATION
# ============================================================================

def generate_nav_menu(components_by_category):
    """Generate NavMenu.json for DocsNavMenu.razor."""
    nav_menu = {
        "version": "1.0.0",
        "lastUpdated": datetime.now().isoformat(),
        "totalComponents": sum(len(cat['components']) for cat in components_by_category.values()),
        "menu": [
            {"label": "Getting Started", "path": "/getting-started", "icon": "🚀"},
            {"label": "Components", "path": "#", "icon": "📦", "children": []},
            {"label": "Theming", "path": "/theming", "icon": "🎨"},
            {"label": "API", "path": "/api", "icon": "📚"}
        ]
    }
    
    components_section = nav_menu["menu"][1]
    sorted_categories = sorted(components_by_category.items(), key=lambda x: x[1]["order"])
    
    for category, cat_data in sorted_categories:
        components = cat_data["components"]
        
        category_item = {
            "label": cat_data["display_name"],
            "path": f"/components/{category}",
            "icon": cat_data["icon"],
            "count": len(components),
            "children": [
                {
                    "label": comp["friendly_name"],
                    "path": f"/components/{category}/{comp['friendly_name'].lower()}",
                    "package": comp["name"]
                }
                for comp in sorted(components, key=lambda x: x["friendly_name"])
            ]
        }
        
        components_section["children"].append(category_item)
    
    return nav_menu


# ============================================================================
# MAIN PIPELINE
# ============================================================================

def main():
    print("=" * 70)
    print("TAIL.BLAZOR ALL-IN-ONE DOCUMENTATION GENERATOR")
    print("Discovery → Extraction → Generation → Overviews → Navigation")
    print("=" * 70)
    
    # Phase 1: Discovery
    print("\n[1/5] Discovering components...")
    print("-" * 70)
    components_by_category = discover_components()
    
    total_components = sum(len(cat['components']) for cat in components_by_category.values())
    print(f"  [OK] Found {total_components} components across {len(components_by_category)} categories")
    
    # Phase 2: Extraction
    print("\n[2/5] Extracting metadata...")
    print("-" * 70)
    all_metadata = {}
    total_params = 0
    
    for category, cat_data in components_by_category.items():
        all_metadata[category] = {
            "icon": cat_data["icon"],
            "order": cat_data["order"],
            "display_name": cat_data["display_name"],
            "components": {}
        }
        
        for comp_info in cat_data["components"]:
            metadata = extract_component_metadata(comp_info)
            all_metadata[category]["components"][metadata["name"]] = metadata
            total_params += len(metadata["parameters"])
    
    print(f"  [OK] Extracted {total_params} parameters from {total_components} components")
    
    # Phase 3: Generate Documentation Pages
    print("\n[3/5] Generating documentation pages...")
    print("-" * 70)
    docs_base = Path("docs/Tail.Blazor.Docs/Pages/Components")
    pages_created = 0
    
    for category, cat_data in all_metadata.items():
        category_folder = docs_base / category.capitalize()
        category_folder.mkdir(parents=True, exist_ok=True)
        
        for component_name, comp_meta in cat_data["components"].items():
            doc_content = generate_doc_page(comp_meta)
            friendly_name = comp_meta["friendly_name"]
            doc_path = category_folder / f"{friendly_name}.razor"
            
            with open(doc_path, 'w', encoding='utf-8') as f:
                f.write(doc_content)
            
            pages_created += 1
    
    print(f"  [OK] Generated {pages_created} documentation pages")
    
    # Phase 4: Generate Overview Pages
    print("\n[4/5] Generating overview pages...")
    print("-" * 70)
    
    # Global overview
    global_overview = generate_global_overview(components_by_category, total_params)
    global_overview_path = docs_base / "_Overview.razor"
    
    with open(global_overview_path, 'w', encoding='utf-8') as f:
        f.write(global_overview)
    
    print(f"  [OK] Global overview: _Overview.razor")
    
    # Category overviews
    category_overviews = 0
    for category, cat_data in components_by_category.items():
        category_folder = docs_base / category.capitalize()
        category_folder.mkdir(parents=True, exist_ok=True)
        
        category_overview = generate_category_overview(category, cat_data, all_metadata)
        category_overview_path = category_folder / "_Overview.razor"
        
        with open(category_overview_path, 'w', encoding='utf-8') as f:
            f.write(category_overview)
        
        category_overviews += 1
    
    print(f"  [OK] Category overviews: {category_overviews} pages")
    
    # Phase 5: Generate Navigation
    print("\n[5/5] Generating navigation menu...")
    print("-" * 70)
    nav_menu = generate_nav_menu(components_by_category)
    nav_menu_path = docs_base / "NavMenu.json"
    
    with open(nav_menu_path, 'w', encoding='utf-8') as f:
        json.dump(nav_menu, f, indent=2)
    
    print(f"  [OK] NavMenu.json generated")
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    for category in sorted(all_metadata.keys(), key=lambda x: all_metadata[x]["order"]):
        cat_data = all_metadata[category]
        comp_count = len(cat_data["components"])
        cat_params = sum(len(comp["parameters"]) for comp in cat_data["components"].values())
        
        print(f"{cat_data['icon']} {category.upper():15} | {comp_count:3} components | {cat_params:4} parameters")
    
    print("=" * 70)
    print(f"\n[COMPLETE] All-in-one documentation generator finished!")
    print(f"  ✓ Components: {total_components}")
    print(f"  ✓ Parameters: {total_params}")
    print(f"  ✓ Component Pages: {pages_created}")
    print(f"  ✓ Global Overview: 1")
    print(f"  ✓ Category Overviews: {category_overviews}")
    print(f"  ✓ Navigation: NavMenu.json")
    print(f"  ✓ Location: {docs_base}")
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    main()
