#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Documentation Section Generator
Generates MudBlazor-style feature sections
"""

# Import will be handled by sys.path
try:
    from doc_generator_base import escape_razor_code
except ImportError:
    # Fallback for direct execution
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    from doc_generator_base import escape_razor_code


def create_variants_section(component_tag, variant_param, variant_type, variant_values, enums, is_generic=False):
    """Create Variants section."""
    if not variant_param:
        return ""
    
    # Get enum values if available
    if enums and variant_type in enums:
        variant_values = enums[variant_type]['members']
    elif not variant_values:
        # Default fallback - use common values, but prefer actual enum values
        variant_values = ['Primary', 'Success', 'Warning', 'Danger', 'Info', 'Outline']
    
    # Clean variant_type - remove any "var" or invalid types
    if variant_type.startswith('var') or variant_type == 'var' or len(variant_type) < 3:
        variant_type = 'ButtonVariant'  # Default fallback
    
    sections_html = f'''
    <DocSection Title="Variants">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Different visual variants provide distinct appearances while maintaining consistent functionality. The <code class="px-1 py-0.5 rounded text-sm" style="background-color: var(--color-surface-2); color: var(--color-text-primary);">{variant_param['name']}</code> property controls the variant style.
        </p>
        <CodePreview Title="Variants" Code="@variantsCode">
            <PreviewContent>
                <div class="p-4">
                    <p class="text-sm" style="color: var(--color-text-secondary);">See code example above for usage.</p>
                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>
'''
    return sections_html


def create_sizes_section(component_tag, size_param, size_type, size_values, enums):
    """Create Sizes section."""
    if not size_param:
        return ""
    
    if enums and size_type in enums:
        size_values = enums[size_type]['members']
    elif not size_values:
        # Default fallback - use common values
        size_values = ['Sm', 'Md', 'Lg']  # Reduced to common ones
    
    sections_html = f'''
    <DocSection Title="Sizes">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Size options to fit different layouts and contexts. Choose from extra small to extra large sizes.
        </p>
        <CodePreview Title="Size Options" Code="@sizesCode">
            <PreviewContent>
                <div class="p-4">
                    <p class="text-sm" style="color: var(--color-text-secondary);">See code example above for usage.</p>
                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>
'''
    return sections_html


def create_states_section(component_tag, feature_groups):
    """Create States section."""
    if not feature_groups.get('States'):
        return ""
    
    sections_html = f'''
    <DocSection Title="States">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Component states control the interactive behavior and visual appearance. Use <code class="px-1 py-0.5 rounded text-sm" style="background-color: var(--color-surface-2); color: var(--color-text-primary);">Disabled</code> to prevent interaction, or <code class="px-1 py-0.5 rounded text-sm" style="background-color: var(--color-surface-2); color: var(--color-text-primary);">IsLoading</code> to show a loading state.
        </p>
        <CodePreview Title="Component States" Code="@statesCode">
            <PreviewContent>
                <div class="p-4">
                    <p class="text-sm" style="color: var(--color-text-secondary);">See code example above for usage.</p>
                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>
'''
    return sections_html


def create_icons_section(component_tag):
    """Create Icons section."""
    sections_html = f'''
    <DocSection Title="Icons">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Add icons to enhance visual communication. Icons can be placed at the start or end of the component.
        </p>
        <CodePreview Title="With Icons" Code="@iconsCode">
            <PreviewContent>
                <div class="p-4">
                    <p class="text-sm" style="color: var(--color-text-secondary);">See code example above for usage.</p>
                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>
'''
    return sections_html


def create_colors_section(component_tag, color_param, variant_type):
    """Create Colors & Theming section."""
    if not color_param:
        return ""
    
    sections_html = f'''
    <DocSection Title="Colors & Theming">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Color and theming customizations. The <code class="px-1 py-0.5 rounded text-sm" style="background-color: var(--color-surface-2); color: var(--color-text-primary);">{color_param['name']}</code> property controls the color scheme. All components support CSS variables for theming.
        </p>
        <CodePreview Title="Color Options" Code="@colorsCode">
            <PreviewContent>
                <div class="p-4">
                    <p class="text-sm" style="color: var(--color-text-secondary);">See code example above for usage.</p>
                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>
'''
    return sections_html


def group_parameters_by_feature(parameters):
    """Group parameters by feature type."""
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
    
    return feature_groups

