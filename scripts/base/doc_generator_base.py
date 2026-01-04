#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Base Documentation Generator
Shared utilities and functions for all category-specific generators
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
    # Replace newlines with \n (but preserve @"" verbatim string format)
    code = code.replace('\n', '\\n')
    # Don't escape braces - they're needed for Razor code blocks
    return code


def get_component_tag(component_name, friendly_name):
    """Get the component tag name for Razor markup."""
    if '.' in friendly_name:
        return component_name.replace('Tail.Blazor.', 'Tail')
    else:
        return f"Tail{friendly_name}"


def is_generic_component(friendly_name):
    """Check if component is generic and requires type parameters."""
    generic_components = ['DataGrid', 'ListView', 'VirtualScroll', 'Tree', 'PivotDataGrid']
    return friendly_name in generic_components


def get_basic_example(component_tag, category, is_generic=False):
    """Generate basic usage example."""
    if is_generic:
        return f'@* {component_tag.replace("Tail", "")} requires type parameter. Example: <{component_tag} T="YourModel">...</{component_tag}> *@'
    
    if category.lower() == 'buttons':
        return f'<{component_tag}>Click Me</{component_tag}>'
    elif category.lower() == 'forms':
        return f'<{component_tag} Placeholder="Enter text..." />'
    elif category.lower() == 'feedback':
        return f'<{component_tag}>Sample Content</{component_tag}>'
    else:
        return f'<{component_tag} />'


def generate_variants_example(component_tag, variant_type, variant_values=None):
    """Generate variants example code."""
    if variant_values is None or len(variant_values) == 0:
        variant_values = ['Primary', 'Success', 'Outline']  # Reduced default set
    
    examples = []
    for variant in variant_values[:6]:  # Limit to 6 variants
        examples.append(f'<{component_tag} Variant="{variant_type}.{variant}">{variant}</{component_tag}>')
    return '\n'.join(examples)


def generate_sizes_example(component_tag, size_type, size_values=None):
    """Generate sizes example code."""
    if size_values is None or len(size_values) == 0:
        size_values = ['Sm', 'Md', 'Lg']  # Reduced default set
    
    examples = []
    for size in size_values:
        examples.append(f'<{component_tag} Size="{size_type}.{size}">{size}</{component_tag}>')
    return '\n'.join(examples)


def generate_states_example(component_tag, has_disabled=True, has_loading=True, has_active=False):
    """Generate states example code."""
    examples = []
    if has_disabled:
        examples.append(f'<{component_tag} Disabled="true">Disabled</{component_tag}>')
    if has_loading:
        examples.append(f'<{component_tag} IsLoading="true">Loading...</{component_tag}>')
    if has_active:
        examples.append(f'<{component_tag} IsActive="true">Active</{component_tag}>')
    return '\n'.join(examples) if examples else None


def generate_icons_example(component_tag):
    """Generate icons example code."""
    return f'''<{component_tag}>
    <IconStart>
        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
    </IconStart>
    With Icon
</{component_tag}>'''


def create_api_parameters_list(parameters):
    """Create API parameters list for DocPageTemplate."""
    api_params = []
    for param in parameters:
        default_val = param.get('default', '-')
        if default_val and default_val not in ['null', '-', '']:
            # Clean default value
            default_val = str(default_val).replace('new()', '').replace('new List', '').strip()
            if not default_val or default_val == 'null':
                default_val = '-'
        else:
            default_val = '-'
        
        desc = param.get('description', '') or f'{param["name"]} parameter'
        desc = desc.replace('"', '\\"').replace('\n', ' ').replace('\r', '')
        
        param_type = param['type'].replace('<', '&lt;').replace('>', '&gt;')
        
        api_params.append({
            'name': param['name'],
            'type': param_type,
            'default': str(default_val),
            'description': desc
        })
    
    return api_params


def create_events_section(events):
    """Create events section HTML."""
    if not events:
        return ""
    
    events_html = f'''
    <DocSection Title="Events">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Event callbacks allow you to respond to user interactions and component lifecycle events.
        </p>
        <div class="space-y-4">
'''
    for event in events:
        event_type = event.get('parameter_type', 'void')
        event_desc = event.get('description', 'Raised when event occurs')
        events_html += f'''            <div class="p-4 rounded-lg border-l-4" style="background-color: var(--color-surface-2); border-color: var(--color-primary);">
                <h4 class="font-semibold mb-2" style="color: var(--color-text-primary);">
                    <code class="px-2 py-1 rounded text-sm" style="background-color: var(--color-surface); color: var(--color-primary);">{event['name']}</code>
                </h4>
                <p class="text-sm mb-2" style="color: var(--color-text-secondary);">
                    <strong>Type:</strong> <code class="px-1 py-0.5 rounded text-xs" style="background-color: var(--color-surface); color: var(--color-text-primary);">EventCallback&lt;{event_type}&gt;</code>
                </p>
                <p class="text-sm" style="color: var(--color-text-secondary);">{event_desc}</p>
            </div>
'''
    events_html += '''        </div>
    </DocSection>
'''
    return events_html


def create_features_list(parameters):
    """Create features list based on available parameters."""
    features = [
        "Full theme support with CSS variables",
        "Responsive design for all screen sizes",
        "Smooth transitions and animations",
        "Accessibility features built-in",
        "Lightweight and performant",
        "Type-safe with IntelliSense support"
    ]
    
    if any('variant' in p['name'].lower() for p in parameters):
        features.append("Multiple variants for different use cases")
    if any('size' in p['name'].lower() for p in parameters):
        features.append("Size options from extra small to extra large")
    if any('icon' in p['name'].lower() for p in parameters):
        features.append("Icon support with flexible placement")
    if any('disabled' in p['name'].lower() for p in parameters):
        features.append("Disabled and loading states")
    if any('color' in p['name'].lower() or 'theme' in p['name'].lower() for p in parameters):
        features.append("Customizable color schemes")
    if any('validation' in p['name'].lower() or 'validator' in p['name'].lower() for p in parameters):
        features.append("Built-in validation support")
    
    return features


def load_metadata():
    """Load component metadata from JSON file."""
    metadata_file = Path('scripts/component_metadata.json')
    if not metadata_file.exists():
        print("❌ Error: component_metadata.json not found!")
        print("   Run: python scripts/extract_component_metadata.py")
        sys.exit(1)
    
    with open(metadata_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_doc_page(doc_path, content):
    """Save documentation page to file."""
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    # Use utf-8-sig to handle BOM and ensure proper encoding
    with open(doc_path, 'w', encoding='utf-8-sig', errors='replace') as f:
        f.write(content)

