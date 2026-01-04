#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tail.Blazor Component Metadata Extractor
Extracts component metadata (properties, events, enums) from .razor and .cs files
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


def extract_xml_comment(text, keyword):
    """Extract XML comment content for a specific line."""
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if keyword in line:
            # Look backward for summary comment
            for j in range(i-1, max(0, i-10), -1):
                if '<summary>' in lines[j]:
                    summary_start = j
                    for k in range(summary_start, i):
                        if '</summary>' in lines[k]:
                            match = re.search(r'<summary>(.*?)</summary>', 
                                            '\n'.join(lines[summary_start:k+1]), re.DOTALL)
                            if match:
                                return match.group(1).strip()
                    break
    return ""


def extract_razor_code(file_path):
    """Extract @code block from razor file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find @code { ... }
    match = re.search(r'@code\s*\{(.*?)\n\}', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def extract_parameters(code_block):
    """Extract [Parameter] properties from code block."""
    parameters = []
    
    # Find all [Parameter] declarations
    pattern = r'\[Parameter\]\s+(?:public\s+)?(\w+(?:<.*?>)?)\s+(\w+)\s*(?:\{.*?\})?(?:=\s*([^;]+))?;'
    
    for match in re.finditer(pattern, code_block, re.DOTALL):
        param_type = match.group(1).strip()
        param_name = match.group(2).strip()
        default_value = match.group(3).strip() if match.group(3) else None
        
        # Get description from comment
        desc = extract_xml_comment(code_block, f'public {param_type} {param_name}')
        
        parameters.append({
            'name': param_name,
            'type': param_type,
            'default': default_value,
            'required': default_value is None,
            'description': desc
        })
    
    return parameters


def extract_events(code_block):
    """Extract [Parameter] EventCallback properties."""
    events = []
    
    pattern = r'\[Parameter\]\s+(?:public\s+)?EventCallback(?:<(\w+)>)?\s+(\w+)\s*(?:\{.*?\})?;'
    
    for match in re.finditer(pattern, code_block):
        event_type = match.group(1).strip() if match.group(1) else 'void'
        event_name = match.group(2).strip()
        
        desc = extract_xml_comment(code_block, f'EventCallback {event_name}')
        
        events.append({
            'name': event_name,
            'parameter_type': event_type,
            'description': desc
        })
    
    return events


def extract_enums(file_path):
    """Extract enum definitions from .cs files."""
    enums = {}
    
    # Find .cs files in component directory
    component_dir = file_path.parent
    for cs_file in component_dir.glob('*.cs'):
        with open(cs_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find enum definitions
        enum_pattern = r'public\s+enum\s+(\w+)\s*\{([^}]+)\}'
        for match in re.finditer(enum_pattern, content, re.DOTALL):
            enum_name = match.group(1)
            enum_members = match.group(2)
            
            members = []
            for member_line in enum_members.split(','):
                member = member_line.strip().split('=')[0].strip()
                if member:
                    members.append(member)
            
            enums[enum_name] = {
                'members': members,
                'source': cs_file.name
            }
    
    return enums


def extract_component_metadata(component_dir):
    """Extract metadata from a component directory."""
    razor_file = None
    
    # Find main .razor file
    for f in component_dir.glob('*.razor'):
        if not f.name.startswith('_'):
            razor_file = f
            break
    
    if not razor_file:
        return None
    
    component_name = component_dir.name
    friendly_name = component_name.replace('Tail.Blazor.', '')
    
    # Read README for description
    description = ""
    readme = component_dir / 'README.md'
    if readme.exists():
        with open(readme, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            description = ''.join(lines[:5]).strip()
    
    # Extract code block
    code_block = extract_razor_code(razor_file)
    
    # Extract parameters, events, and enums
    parameters = extract_parameters(code_block)
    events = extract_events(code_block)
    enums = extract_enums(component_dir)
    
    return {
        'name': component_name,
        'friendly_name': friendly_name,
        'description': description,
        'parameters': parameters,
        'events': events,
        'enums': enums,
        'main_file': razor_file.name,
        'extracted_at': datetime.now().isoformat()
    }


def discover_and_extract():
    """Discover all components and extract metadata."""
    components_dir = Path('src/components')
    metadata = {}
    
    category_metadata = {
        'buttons': {'icon': '🔘', 'order': 1},
        'charts': {'icon': '📈', 'order': 2},
        'core': {'icon': '⚙️', 'order': 3},
        'data': {'icon': '📊', 'order': 4},
        'feedback': {'icon': '💬', 'order': 5},
        'forms': {'icon': '📝', 'order': 6},
        'icons': {'icon': '🎯', 'order': 7},
        'layout': {'icon': '📐', 'order': 8},
        'navigation': {'icon': '🧭', 'order': 9},
        'utils': {'icon': '🛠️', 'order': 10},
        'validators': {'icon': '✅', 'order': 11},
        'visualization': {'icon': '🎨', 'order': 12}
    }
    
    for category_dir in sorted(components_dir.iterdir()):
        if not category_dir.is_dir():
            continue
        
        category = category_dir.name.lower()
        cat_meta = category_metadata.get(category, {'icon': '📦', 'order': 99})
        
        metadata[category] = {
            'icon': cat_meta['icon'],
            'order': cat_meta['order'],
            'display_name': category.capitalize(),
            'components': {}
        }
        
        for component_dir in sorted(category_dir.iterdir()):
            if not component_dir.is_dir():
                continue
            
            csproj = component_dir / f'{component_dir.name}.csproj'
            if csproj.exists():
                comp_meta = extract_component_metadata(component_dir)
                if comp_meta:
                    metadata[category]['components'][component_dir.name] = comp_meta
    
    return metadata


def main():
    print("=" * 70)
    print("TAIL.BLAZOR COMPONENT METADATA EXTRACTOR")
    print("=" * 70)
    
    print("\n[1/3] Discovering components...")
    metadata = discover_and_extract()
    
    total_components = sum(
        len(cat['components']) 
        for cat in metadata.values()
    )
    print(f"✓ Found {total_components} components")
    
    print("\n[2/3] Extracting metadata...")
    
    total_params = 0
    total_events = 0
    
    for category, cat_data in metadata.items():
        for comp_name, comp_data in cat_data['components'].items():
            total_params += len(comp_data['parameters'])
            total_events += len(comp_data['events'])
    
    print(f"✓ Extracted {total_params} parameters")
    print(f"✓ Extracted {total_events} event callbacks")
    
    print("\n[3/3] Saving metadata...")
    output_file = Path('scripts/component_metadata.json')
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Metadata saved: {output_file}")
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    for category in sorted(metadata.keys(), 
                          key=lambda x: metadata[x]['order']):
        cat_data = metadata[category]
        comp_count = len(cat_data['components'])
        print(f"{cat_data['icon']} {category.upper():15} | {comp_count:2} components")
    
    print("=" * 70)
    print(f"\n✓ Metadata extraction complete!")
    print(f"✓ File: {output_file}")
    print(f"✓ Total components: {total_components}")
    print(f"✓ Total parameters: {total_params}")
    print(f"✓ Total events: {total_events}")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
