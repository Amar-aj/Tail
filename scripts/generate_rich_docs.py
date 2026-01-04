#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tail.Blazor Rich Documentation Generator
Generates comprehensive, MudBlazor-style documentation pages from metadata
"""

import json
import sys
import html
import re
from pathlib import Path
from datetime import datetime

# Fix Unicode output on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def escape_razor_code(code):
    """Escape code for use in Razor @"" strings."""
    if not code:
        return ""
    # Replace " with "" for C# verbatim string escaping
    code = code.replace('"', '""')
    # Replace newlines with \n
    code = code.replace('\n', '\\n')
    return code


def get_component_examples(component_name, friendly_name, category, parameters):
    """Generate comprehensive examples based on component type and parameters."""
    # Handle component names with dots (e.g., "Core.Theme" -> "TailCore.Theme")
    if '.' in friendly_name:
        component_tag = component_name.replace('Tail.Blazor.', 'Tail')
    else:
        component_tag = f"Tail{friendly_name}"
    
    examples = {}
    
    # Check for variant parameter
    has_variant = any('variant' in p['name'].lower() for p in parameters)
    has_size = any('size' in p['name'].lower() for p in parameters)
    has_color = any('color' in p['name'].lower() for p in parameters)
    has_disabled = any('disabled' in p['name'].lower() for p in parameters)
    has_loading = any('loading' in p['name'].lower() or 'isloading' in p['name'].lower() for p in parameters)
    has_icon = any('icon' in p['name'].lower() for p in parameters)
    
    # Basic example
    if category.lower() == 'buttons':
        examples['basic'] = f'<{component_tag}>Click Me</{component_tag}>'
    elif category.lower() == 'forms':
        examples['basic'] = f'<{component_tag} Placeholder="Enter text..." />'
    elif category.lower() == 'feedback':
        examples['basic'] = f'<{component_tag}>Sample Content</{component_tag}>'
    else:
        examples['basic'] = f'<{component_tag} />'
    
    # Variants example
    if has_variant:
        variant_param = next((p for p in parameters if 'variant' in p['name'].lower()), None)
        if variant_param:
            variant_type = variant_param['type']
            examples['variants'] = f'''<{component_tag} Variant="{variant_type}.Primary">Primary</{component_tag}>
<{component_tag} Variant="{variant_type}.Secondary">Secondary</{component_tag}>
<{component_tag} Variant="{variant_type}.Outline">Outline</{component_tag}>'''
    
    # Sizes example
    if has_size:
        size_param = next((p for p in parameters if 'size' in p['name'].lower()), None)
        if size_param:
            size_type = size_param['type']
            examples['sizes'] = f'''<{component_tag} Size="{size_type}.Sm">Small</{component_tag}>
<{component_tag} Size="{size_type}.Md">Medium</{component_tag}>
<{component_tag} Size="{size_type}.Lg">Large</{component_tag}>'''
    
    # States example
    if has_disabled or has_loading:
        states_code = []
        if has_disabled:
            states_code.append(f'<{component_tag} Disabled="true">Disabled</{component_tag}>')
        if has_loading:
            states_code.append(f'<{component_tag} IsLoading="true">Loading</{component_tag}>')
        if states_code:
            examples['states'] = '\n'.join(states_code)
    
    # Icons example
    if has_icon:
        examples['icons'] = f'''<{component_tag}>
    <IconStart>
        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
    </IconStart>
    With Icon
</{component_tag}>'''
    
    return examples


def create_mudblazor_style_sections(component_name, friendly_name, category, parameters, enums, component_tag):
    """Create MudBlazor-style feature sections with descriptions, previews, and code."""
    sections_html = ""
    
    # Group parameters by feature
    feature_groups = {
        'Variants': [],
        'Sizes': [],
        'Colors': [],
        'States': [],
        'Icons': [],
        'Content': [],
        'Events': [],
        'Other': []
    }
    
    for param in parameters:
        param_name = param['name'].lower()
        if 'variant' in param_name or 'style' in param_name or 'appearance' in param_name:
            feature_groups['Variants'].append(param)
        elif 'size' in param_name:
            feature_groups['Sizes'].append(param)
        elif 'color' in param_name or 'theme' in param_name:
            feature_groups['Colors'].append(param)
        elif 'disabled' in param_name or 'loading' in param_name or 'active' in param_name or 'selected' in param_name:
            feature_groups['States'].append(param)
        elif 'icon' in param_name:
            feature_groups['Icons'].append(param)
        elif 'label' in param_name or 'title' in param_name or 'text' in param_name or 'content' in param_name or 'placeholder' in param_name:
            feature_groups['Content'].append(param)
        elif 'onclick' in param_name or 'onchange' in param_name or 'callback' in param_name or 'event' in param_name:
            feature_groups['Events'].append(param)
        else:
            feature_groups['Other'].append(param)
    
    # Generate examples
    examples = get_component_examples(component_name, friendly_name, category, parameters)
    
    # Create sections for each feature group that has parameters
    section_descriptions = {
        'Variants': 'Different visual variants and styles for various use cases. Each variant provides a distinct appearance while maintaining consistent functionality.',
        'Sizes': 'Size options to fit different layouts and contexts. Choose from extra small to extra large sizes.',
        'Colors': 'Color and theming customizations. Supports theme variables for consistent styling across your application.',
        'States': 'Component states like disabled, loading, and active. Control the interactive state of the component.',
        'Icons': 'Icon integration and customization. Add icons to enhance visual communication.',
        'Content': 'Text content, labels, and placeholders. Customize the displayed text and help text.',
        'Events': 'Event handlers and callbacks. Respond to user interactions and component lifecycle events.',
        'Other': 'Additional configuration options and advanced features.'
    }
    
    # Generate Variants section (like "Filled Buttons" in MudBlazor)
    if feature_groups['Variants'] and 'variants' in examples:
        variant_param = feature_groups['Variants'][0]
        variant_type = variant_param['type']
        
        # Get enum values if available
        variant_values = []
        if enums and variant_type in enums:
            variant_values = enums[variant_type]['members']
        else:
            # Common variant values
            variant_values = ['Primary', 'Secondary', 'Success', 'Warning', 'Danger', 'Info', 'Outline', 'Text']
        
        sections_html += f'''
    <DocSection Title="Variants">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Different visual variants provide distinct appearances while maintaining consistent functionality. The <code class="px-1 py-0.5 rounded text-sm" style="background-color: var(--color-surface-2); color: var(--color-text-primary);">{variant_param['name']}</code> property controls the variant style.
        </p>
        <CodePreview Title="Variants" Code="@variantsCode">
            <PreviewContent>
                <div class="flex flex-wrap gap-3 p-4">
'''
        
        # Generate preview for each variant
        for variant in variant_values[:6]:  # Limit to 6 variants
            sections_html += f'''                    <{component_tag} Variant="{variant_type}.{variant}">{variant}</{component_tag}>
'''
        
        sections_html += f'''                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>
'''
    
    # Generate Sizes section
    if feature_groups['Sizes'] and 'sizes' in examples:
        size_param = feature_groups['Sizes'][0]
        size_type = size_param['type']
        
        size_values = []
        if enums and size_type in enums:
            size_values = enums[size_type]['members']
        else:
            size_values = ['Xs', 'Sm', 'Md', 'Lg', 'Xl']
        
        sections_html += f'''
    <DocSection Title="Sizes">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Size options to fit different layouts and contexts. Choose from extra small to extra large sizes.
        </p>
        <CodePreview Title="Size Options" Code="@sizesCode">
            <PreviewContent>
                <div class="flex flex-wrap items-center gap-3 p-4">
'''
        
        for size in size_values:
            sections_html += f'''                    <{component_tag} Size="{size_type}.{size}">{size}</{component_tag}>
'''
        
        sections_html += '''                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>
'''
    
    # Generate States section (like "Disabled" in MudBlazor)
    if feature_groups['States']:
        sections_html += f'''
    <DocSection Title="States">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Component states control the interactive behavior and visual appearance. Use <code class="px-1 py-0.5 rounded text-sm" style="background-color: var(--color-surface-2); color: var(--color-text-primary);">Disabled</code> to prevent interaction, or <code class="px-1 py-0.5 rounded text-sm" style="background-color: var(--color-surface-2); color: var(--color-text-primary);">IsLoading</code> to show a loading state.
        </p>
        <CodePreview Title="Component States" Code="@statesCode">
            <PreviewContent>
                <div class="flex flex-wrap gap-3 p-4">
'''
        
        if any('disabled' in p['name'].lower() for p in feature_groups['States']):
            sections_html += f'''                    <{component_tag} Disabled="true">Disabled</{component_tag}>
'''
        if any('loading' in p['name'].lower() or 'isloading' in p['name'].lower() for p in feature_groups['States']):
            sections_html += f'''                    <{component_tag} IsLoading="true">Loading...</{component_tag}>
'''
        if any('active' in p['name'].lower() or 'selected' in p['name'].lower() for p in feature_groups['States']):
            sections_html += f'''                    <{component_tag} IsActive="true">Active</{component_tag}>
'''
        
        sections_html += '''                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>
'''
    
    # Generate Icons section
    if feature_groups['Icons'] and 'icons' in examples:
        icon_example = examples['icons'].replace('"', '&quot;')
        sections_html += f'''
    <DocSection Title="Icons">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Add icons to enhance visual communication. Icons can be placed at the start or end of the component.
        </p>
        <CodePreview Title="With Icons" Code="@iconsCode">
            <PreviewContent>
                <div class="space-y-3 p-4">
                    <{component_tag}>
                        <IconStart>
                            <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                            </svg>
                        </IconStart>
                        With Icon
                    </{component_tag}>
                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>
'''
    
    # Generate Colors section (like "Drop Shadow" in MudBlazor - a specific feature)
    if feature_groups['Colors']:
        color_param = feature_groups['Colors'][0]
        sections_html += f'''
    <DocSection Title="Colors & Theming">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Color and theming customizations. The <code class="px-1 py-0.5 rounded text-sm" style="background-color: var(--color-surface-2); color: var(--color-text-primary);">{color_param['name']}</code> property controls the color scheme. All components support CSS variables for theming.
        </p>
        <CodePreview Title="Color Options" Code="@colorsCode">
            <PreviewContent>
                <div class="flex flex-wrap gap-3 p-4">
                    <{component_tag} Variant="ButtonVariant.Primary">Primary</{component_tag}>
                    <{component_tag} Variant="ButtonVariant.Success">Success</{component_tag}>
                    <{component_tag} Variant="ButtonVariant.Warning">Warning</{component_tag}>
                    <{component_tag} Variant="ButtonVariant.Danger">Danger</{component_tag}>
                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>
'''
    
    return sections_html


def load_metadata():
    """Load component metadata from JSON file."""
    metadata_file = Path('scripts/component_metadata.json')
    if not metadata_file.exists():
        print("❌ Error: component_metadata.json not found!")
        print("   Run: python scripts/extract_component_metadata.py")
        sys.exit(1)
    
    with open(metadata_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_doc_page(category, component_name, metadata):
    """Generate a MudBlazor-style documentation page."""
    friendly_name = metadata['friendly_name']
    description = metadata.get('description', f'{friendly_name} component for Tail.Blazor')
    parameters = metadata.get('parameters', [])
    events = metadata.get('events', [])
    enums = metadata.get('enums', {})
    
    tail_name = f"Tail{friendly_name}"
    
    # Clean description
    description = description.split('\n')[0].strip() if description else f'{friendly_name} component'
    description = description.replace('#', '').replace('##', '').strip()
    
    # Determine component tag
    if '.' in friendly_name:
        component_tag = component_name.replace('Tail.Blazor.', 'Tail')
    else:
        component_tag = f"Tail{friendly_name}"
    
    # Generate examples
    examples = get_component_examples(component_name, friendly_name, category, parameters)
    
    # Build API parameters table
    api_params = []
    for param in parameters:
        default_val = param.get('default', '-')
        if default_val and default_val != 'null' and default_val != '-':
            # Clean default value
            default_val = default_val.replace('new()', '').replace('new List', '').strip()
            if not default_val or default_val == 'null':
                default_val = '-'
        
        api_params.append({
            'name': param['name'],
            'type': param['type'],
            'default': default_val or '-',
            'description': param.get('description', '') or f'{param["name"]} parameter'
        })
    
    # Generate MudBlazor-style sections
    feature_sections = create_mudblazor_style_sections(component_name, friendly_name, category, parameters, enums, component_tag)
    
    # Ensure we have basic code examples
    if 'variants' not in examples and any('variant' in p['name'].lower() for p in parameters):
        variant_type = next((p['type'] for p in parameters if 'variant' in p['name'].lower()), None)
        if variant_type:
            examples['variants'] = f'''<{component_tag} Variant="{variant_type}.Primary">Primary</{component_tag}>
<{component_tag} Variant="{variant_type}.Secondary">Secondary</{component_tag}>
<{component_tag} Variant="{variant_type}.Outline">Outline</{component_tag}>'''
    
    if 'sizes' not in examples and any('size' in p['name'].lower() for p in parameters):
        size_type = next((p['type'] for p in parameters if 'size' in p['name'].lower()), None)
        if size_type:
            examples['sizes'] = f'''<{component_tag} Size="{size_type}.Sm">Small</{component_tag}>
<{component_tag} Size="{size_type}.Md">Medium</{component_tag}>
<{component_tag} Size="{size_type}.Lg">Large</{component_tag}>'''
    
    if 'states' not in examples:
        states = []
        if any('disabled' in p['name'].lower() for p in parameters):
            states.append(f'<{component_tag} Disabled="true">Disabled</{component_tag}>')
        if any('loading' in p['name'].lower() or 'isloading' in p['name'].lower() for p in parameters):
            states.append(f'<{component_tag} IsLoading="true">Loading...</{component_tag}>')
        if states:
            examples['states'] = '\n'.join(states)
    
    # Build events section
    events_html = ""
    if events:
        events_html = f'''
    <DocSection Title="Events">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Event callbacks allow you to respond to user interactions and component lifecycle events.
        </p>
        <div class="space-y-4">
'''
        for event in events:
            events_html += f'''            <div class="p-4 rounded-lg border-l-4" style="background-color: var(--color-surface-2); border-color: var(--color-primary);">
                <h4 class="font-semibold mb-2" style="color: var(--color-text-primary);">
                    <code class="px-2 py-1 rounded text-sm" style="background-color: var(--color-surface); color: var(--color-primary);">{event['name']}</code>
                </h4>
                <p class="text-sm mb-2" style="color: var(--color-text-secondary);">
                    <strong>Type:</strong> <code class="px-1 py-0.5 rounded text-xs" style="background-color: var(--color-surface); color: var(--color-text-primary);">EventCallback&lt;{event.get('parameter_type', 'void')}&gt;</code>
                </p>
                <p class="text-sm" style="color: var(--color-text-secondary);">{event.get('description', 'Raised when event occurs')}</p>
            </div>
'''
        events_html += '''        </div>
    </DocSection>
'''
    
    # Determine component namespace
    component_namespace = component_name  # e.g., "Tail.Blazor.Button"
    
    # Handle special cases for component names with dots
    if '.' in friendly_name:
        # For components like "Core.Theme", use the full namespace
        component_tag = component_name.replace('Tail.Blazor.', 'Tail')
    else:
        component_tag = f"Tail{friendly_name}"
    
    # Generic components that need type parameters
    generic_components = ['DataGrid', 'ListView', 'VirtualScroll', 'Tree', 'PivotDataGrid']
    is_generic = friendly_name in generic_components
    
    # Generate complete page
    doc_page = f'''@page "/components/{category.lower()}/{friendly_name.lower()}"
@using Tail.Blazor.Docs.Shared
@using Microsoft.AspNetCore.Components
@using {component_namespace}

<PageTitle>{friendly_name} - Tail.Blazor</PageTitle>

<DocPageTemplate Title="{friendly_name}" 
                 Description="{description}"
                 PackageName="{component_name}"
                 ApiParameters="@apiParameters">
    
    <DocSection Title="Installation">
        <CodePreview Title="Install Package" Code="@installCode" ShowPreview="false" />
    </DocSection>

    <DocSection Title="Basic Usage">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Represents a {friendly_name.lower()} component with material design theme and comes with multiple functions.
        </p>
        <CodePreview Title="Basic {friendly_name}" Code="@basicCode">
            <PreviewContent>
                <div class="p-4">
                    @if (isGeneric)
                    {{
                        <p class="text-sm" style="color: var(--color-text-secondary);">See code examples for proper usage with type parameters.</p>
                    }}
                    else
                    {{
                        {examples.get('basic', f'<{component_tag} />')}
                    }}
                </div>
            </PreviewContent>
                </CodePreview>
    </DocSection>
{feature_sections}{events_html}
    <DocSection Title="Features">
        <div style="color: var(--color-text-primary);">
            <ul class="space-y-2" style="list-style: disc; padding-left: 1.5rem;">
                <li>Full theme support with CSS variables</li>
                <li>Responsive design for all screen sizes</li>
                <li>Smooth transitions and animations</li>
                <li>Accessibility features built-in</li>
                <li>Lightweight and performant</li>
                <li>Type-safe with IntelliSense support</li>
'''
    
    # Add feature-specific items
    if any('variant' in p['name'].lower() for p in parameters):
        doc_page += '                <li>Multiple variants for different use cases</li>\n'
    if any('size' in p['name'].lower() for p in parameters):
        doc_page += '                <li>Size options from extra small to extra large</li>\n'
    if any('icon' in p['name'].lower() for p in parameters):
        doc_page += '                <li>Icon support with flexible placement</li>\n'
    if any('disabled' in p['name'].lower() for p in parameters):
        doc_page += '                <li>Disabled and loading states</li>\n'
    
    doc_page += '''            </ul>
        </div>
    </DocSection>
</DocPageTemplate>

@code {
'''
    
    # Add code variables
    doc_page += f'    private bool isGeneric = {str(is_generic).lower()};\n\n'
    doc_page += f'    private string installCode = @"dotnet add package {component_name}";\n\n'
    
    if is_generic:
        basic_example = f'@* {friendly_name} requires type parameter. Example: <{component_tag} T="YourModel">...</{component_tag}> *@'
    else:
        basic_example = examples.get("basic", f"<{component_tag} />")
    doc_page += f'    private string basicCode = @"{escape_razor_code(basic_example)}";\n\n'
    
    if 'variants' in examples:
        variants_example = examples["variants"]
        doc_page += f'    private string variantsCode = @"{escape_razor_code(variants_example)}";\n\n'
    if 'sizes' in examples:
        sizes_example = examples["sizes"]
        doc_page += f'    private string sizesCode = @"{escape_razor_code(sizes_example)}";\n\n'
    if 'states' in examples:
        states_example = examples["states"]
        doc_page += f'    private string statesCode = @"{escape_razor_code(states_example)}";\n\n'
    if 'icons' in examples:
        icons_example = examples["icons"]
        doc_page += f'    private string iconsCode = @"{escape_razor_code(icons_example)}";\n\n'
    
    # Add colors code if needed
    if any('color' in p['name'].lower() or 'variant' in p['name'].lower() for p in parameters):
        variant_type = next((p['type'] for p in parameters if 'variant' in p['name'].lower()), 'ButtonVariant')
        colors_example = f'<{component_tag} Variant="{variant_type}.Primary">Primary</{component_tag}>\n<{component_tag} Variant="{variant_type}.Success">Success</{component_tag}>\n<{component_tag} Variant="{variant_type}.Warning">Warning</{component_tag}>\n<{component_tag} Variant="{variant_type}.Danger">Danger</{component_tag}>'
        doc_page += f'    private string colorsCode = @"{escape_razor_code(colors_example)}";\n\n'
    
    # Add API parameters
    doc_page += '    private List<DocPageTemplate.ApiParameter> apiParameters = new()\n    {\n'
    for param in api_params:
        desc = param['description'].replace('"', '\\"').replace('\n', ' ').replace('\r', '')
        param_type = param['type'].replace('<', '&lt;').replace('>', '&gt;')
        default_val = str(param['default']).replace('"', '\\"')
        doc_page += f'        new DocPageTemplate.ApiParameter {{ Name = "{param["name"]}", Type = "{param_type}", Default = "{default_val}", Description = "{desc}" }},\n'
    
    # Remove last comma
    if api_params:
        doc_page = doc_page.rstrip(',\n') + '\n'
    
    doc_page += '    };\n}\n'
    
    return doc_page


def main():
    print("=" * 70)
    print("TAIL.BLAZOR MUDSTYLE DOCUMENTATION GENERATOR")
    print("=" * 70)
    
    print("\n[1/3] Loading component metadata...")
    metadata = load_metadata()
    print("✓ Metadata loaded")
    
    print("\n[2/3] Creating MudBlazor-style documentation pages...")
    docs_base = Path("docs/Tail.Blazor.Docs/Pages/Components")
    pages_created = 0
    
    for category in sorted(metadata.keys(), 
                          key=lambda x: metadata[x]['order']):
        cat_data = metadata[category]
        category_folder = docs_base / category.capitalize()
        category_folder.mkdir(parents=True, exist_ok=True)
        
        for component_name, comp_meta in cat_data['components'].items():
            doc_content = generate_doc_page(category, component_name, comp_meta)
            friendly_name = comp_meta['friendly_name']
            doc_path = category_folder / f"{friendly_name}.razor"
            
            with open(doc_path, 'w', encoding='utf-8') as f:
                f.write(doc_content)
            
            pages_created += 1
    
    print(f"✓ Generated {pages_created} MudBlazor-style documentation pages")
    
    print("\n[3/3] Summary")
    print("=" * 70)
    
    total_components = 0
    for category in sorted(metadata.keys(), 
                          key=lambda x: metadata[x]['order']):
        cat_data = metadata[category]
        comp_count = len(cat_data['components'])
        total_components += comp_count
        total_params = sum(
            len(comp['parameters']) 
            for comp in cat_data['components'].values()
        )
        total_events = sum(
            len(comp['events']) 
            for comp in cat_data['components'].values()
        )
        print(f"{cat_data['icon']} {category.upper():15} | {comp_count:2} components | "
              f"{total_params:3} parameters | {total_events:2} events")
    
    print("=" * 70)
    print(f"\n✓ MudBlazor-style documentation generated!")
    print(f"✓ Total pages: {pages_created}")
    print(f"✓ Total components: {total_components}")
    print(f"✓ Location: {docs_base}")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
