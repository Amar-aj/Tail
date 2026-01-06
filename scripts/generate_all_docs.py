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
import textwrap

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
    
    # Capture [Parameter] or [CascadingParameter] with optional attribute arguments and allow newlines between attribute and property.
    # This pattern does NOT require a trailing semicolon because properties often omit it.
    pattern = r'\[(?:Parameter|CascadingParameter)(?:\(.*?\))?\]\s*(?:\r?\n\s*)?(?:public\s+)?([A-Za-z0-9_\.<>?\[\],\s]+?)\s+(\w+)\s*\{\s*get\s*;?\s*set\s*;?\s*\}\s*(?:=\s*([^\r\n;]+))?'

    for match in re.finditer(pattern, code_block, re.MULTILINE):
        param_type = re.sub(r'\s+', ' ', match.group(1).strip())
        param_name = match.group(2).strip()
        default_value = match.group(3).strip() if match.group(3) else None

        # Skip EventCallback parameters here; they are handled in extract_events
        if param_type.startswith("EventCallback"):
            continue
        
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


def extract_events(code_block):
    """Extract [Parameter] EventCallback properties."""
    events = []
    
    if not code_block:
        return events
    
    # Pattern for [Parameter] EventCallback declarations (allow newline between attribute and property, no required trailing semicolon)
    pattern = r'\[Parameter(?:\(.*?\))?\]\s*(?:\r?\n\s*)?(?:public\s+)?EventCallback(?:<([\w\.<>?,\s\[\]]+?)>)?\s+(\w+)\s*\{\s*get\s*;?\s*set\s*;?\s*\}'

    for match in re.finditer(pattern, code_block, re.MULTILINE):
        event_type = match.group(1).strip() if match.group(1) else "void"
        event_name = match.group(2).strip()
        
        # Generate description
        desc = generate_event_description(event_name, event_type)
        
        events.append({
            "name": event_name,
            "type": event_type,
            "description": desc,
            "category": "Callback"
        })
    
    return events


def extract_properties(code_block):
    """Extract public properties (non-parameter)."""
    properties = []
    
    if not code_block:
        return properties
    
    # Pattern for public properties that are NOT [Parameter] decorated
    pattern = r'^\s*(?!\[Parameter\])\s*public\s+([\w\.<>?,\s\[\]]+?)\s+(\w+)\s*(?:\{\s*(?:get|set)[^}]*\})?'
    
    for match in re.finditer(pattern, code_block, re.MULTILINE):
        prop_type = re.sub(r'\s+', ' ', match.group(1).strip())
        prop_name = match.group(2).strip()
        
        # Skip common non-property methods and keywords
        if any(x in prop_name for x in ['protected', 'private', 'internal', 'class', 'interface']):
            continue
        
        # Skip if it contains method-like patterns
        if '->' in prop_type or 'Func<' in prop_type:
            continue
        
        properties.append({
            "name": prop_name,
            "type": prop_type,
            "description": f"{prop_name} property"
        })
    
    return properties


def extract_methods(code_block):
    """Extract public methods."""
    methods = []
    
    if not code_block:
        return methods
    
    # Pattern for public methods
    pattern = r'^\s*public\s+(?:async\s+)?(?:Task<?.*?>?)?\s+(\w+)\s*\(([^)]*)\)'
    
    for match in re.finditer(pattern, code_block, re.MULTILINE):
        method_name = match.group(1).strip()
        params_str = match.group(2).strip()
        
        # Skip lifecycle methods and internal methods
        if any(x in method_name for x in ['OnInitialized', 'OnParametersSet', 'OnAfterRender', 'Dispose']):
            continue
        
        # Parse method parameters
        method_params = []
        if params_str:
            for param in params_str.split(','):
                parts = param.strip().rsplit(' ', 1)
                if len(parts) == 2:
                    method_params.append({"type": parts[0], "name": parts[1]})
        
        methods.append({
            "name": method_name,
            "parameters": method_params,
            "description": f"Invokes {method_name} method"
        })
    
    return methods


def extract_readme_content(component_path):
    """Extract features, examples, and all content from README.md."""
    readme_path = Path(component_path) / "README.md"
    content = {
        "features": [],
        "example_code": "",
        "description": "",
        "package_size": "",
        "examples": {},
        "namespace": "",
        "enums": {},
        "dependencies": [],
        "target_frameworks": []
    }
    
    if not readme_path.exists():
        return content
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Extract features section
        features_match = re.search(r'## Features\s*\n(.*?)(?=##|\Z)', text, re.DOTALL)
        if features_match:
            features_text = features_match.group(1)
            # Extract bullet points
            bullets = re.findall(r'- (.+?)(?=\n|$)', features_text)
            content["features"] = [b.strip() for b in bullets if b.strip()]
        
        # Extract usage example (first razor code block)
        usage_match = re.search(r'## Component Usage\s*\n\s*```razor\s*(.*?)\s*```', text, re.DOTALL)
        if usage_match:
            content["example_code"] = usage_match.group(1).strip()
        else:
            # Fallback to any first razor code block
            usage_match = re.search(r'```razor\s*(.*?)\s*```', text, re.DOTALL)
            if usage_match:
                content["example_code"] = usage_match.group(1).strip()
        
        # Extract description (first paragraph after title)
        desc_match = re.search(r'# .+?\n\n(.+?)(?=\n##)', text, re.DOTALL)
        if desc_match:
            content["description"] = desc_match.group(1).strip()
        
        # Extract namespace
        namespace_match = re.search(r'## Namespace\s*\n\s*```csharp\s*using\s+([^;]+);', text, re.DOTALL)
        if namespace_match:
            content["namespace"] = namespace_match.group(1).strip()
        
        # Extract all examples from Examples section
        examples_match = re.search(r'## Examples\s*\n(.*?)(?=## Base Class|## Dependencies|## Target Frameworks|## Package Information|\Z)', text, re.DOTALL)
        if examples_match:
            examples_text = examples_match.group(1)
            
            # Extract Quick Start
            quickstart_match = re.search(r'### Quick Start\s*\n(.*?)(?=### |\Z)', examples_text, re.DOTALL)
            if quickstart_match:
                code_match = re.search(r'```razor\s*(.*?)\s*```', quickstart_match.group(1), re.DOTALL)
                if code_match:
                    content["examples"]["quickstart"] = code_match.group(1).strip()
            
            # Extract Common Patterns
            patterns_match = re.search(r'### Common Patterns\s*\n(.*?)(?=### |\Z)', examples_text, re.DOTALL)
            if patterns_match:
                content["examples"]["patterns"] = patterns_match.group(1).strip()
            
            # Extract Basic Usage
            basic_match = re.search(r'### Basic Usage\s*\n(.*?)(?=### |\Z)', examples_text, re.DOTALL)
            if basic_match:
                code_match = re.search(r'```razor\s*(.*?)\s*```', basic_match.group(1), re.DOTALL)
                if code_match:
                    content["examples"]["basic"] = code_match.group(1).strip()
            
            # Extract Variants
            variants_match = re.search(r'### Variants\s*\n(.*?)(?=### |\Z)', examples_text, re.DOTALL)
            if variants_match:
                code_match = re.search(r'```razor\s*(.*?)\s*```', variants_match.group(1), re.DOTALL)
                if code_match:
                    content["examples"]["variants"] = code_match.group(1).strip()
            
            # Extract Sizes
            sizes_match = re.search(r'### Sizes\s*\n(.*?)(?=### |\Z)', examples_text, re.DOTALL)
            if sizes_match:
                code_match = re.search(r'```razor\s*(.*?)\s*```', sizes_match.group(1), re.DOTALL)
                if code_match:
                    content["examples"]["sizes"] = code_match.group(1).strip()
            
            # Extract States
            states_match = re.search(r'### States\s*\n(.*?)(?=### |\Z)', examples_text, re.DOTALL)
            if states_match:
                code_match = re.search(r'```razor\s*(.*?)\s*```', states_match.group(1), re.DOTALL)
                if code_match:
                    content["examples"]["states"] = code_match.group(1).strip()
            
            # Extract Event Handling
            events_match = re.search(r'### Event Handling\s*\n(.*?)(?=### |\Z)', examples_text, re.DOTALL)
            if events_match:
                code_match = re.search(r'```razor\s*(.*?)\s*```', events_match.group(1), re.DOTALL)
                if code_match:
                    full_code = code_match.group(1).strip()
                    content["examples"]["events"] = full_code
                    # Extract just the component markup (before @code block) for preview
                    markup_match = re.search(r'^(.*?)(?=\n@code|\Z)', full_code, re.DOTALL)
                    if markup_match:
                        content["examples"]["events_preview"] = markup_match.group(1).strip()
                    else:
                        # If no @code block, use the full code
                        content["examples"]["events_preview"] = full_code
            
            # Extract Parameter Combinations
            combinations_match = re.search(r'### Parameter Combinations\s*\n(.*?)(?=### |\Z)', examples_text, re.DOTALL)
            if combinations_match:
                code_match = re.search(r'```razor\s*(.*?)\s*```', combinations_match.group(1), re.DOTALL)
                if code_match:
                    content["examples"]["combinations"] = code_match.group(1).strip()
            
            # Extract Advanced Examples
            advanced_match = re.search(r'### Advanced Examples\s*\n(.*?)(?=### Real-World|## |\Z)', examples_text, re.DOTALL)
            if advanced_match:
                content["examples"]["advanced"] = advanced_match.group(1).strip()
            
            # Extract Real-World Example
            realworld_match = re.search(r'### Real-World Example\s*\n(.*?)(?=## |\Z)', examples_text, re.DOTALL)
            if realworld_match:
                code_match = re.search(r'```razor\s*(.*?)\s*```', realworld_match.group(1), re.DOTALL)
                if code_match:
                    content["examples"]["realworld"] = code_match.group(1).strip()
        
        # Extract package size
        size_match = re.search(r'Package Size\s*\n~?(.+?)(?=\n|$)', text)
        if size_match:
            content["package_size"] = size_match.group(1).strip()
        
        # Extract target frameworks
        frameworks_match = re.search(r'## Target Frameworks\s*\n(.*?)(?=## |\Z)', text, re.DOTALL)
        if frameworks_match:
            frameworks_text = frameworks_match.group(1)
            frameworks = re.findall(r'- \.NET (\d+\.\d+)', frameworks_text)
            content["target_frameworks"] = frameworks
        
        return content
    except Exception as e:
        return content


def extract_namespace(component_path, component_name):
    """Extract namespace from _Imports.razor or infer from component name."""
    namespace = None
    
    # Try _Imports.razor first
    imports_path = Path(component_path) / "_Imports.razor"
    if imports_path.exists():
        try:
            with open(imports_path, 'r', encoding='utf-8') as f:
                content = f.read()
                namespace_match = re.search(r'@namespace\s+([^\s]+)', content)
                if namespace_match:
                    namespace = namespace_match.group(1).strip()
        except Exception:
            pass
    
    # If not found, try to find in any .razor file
    if not namespace:
        for razor_file in Path(component_path).glob("*.razor"):
            try:
                with open(razor_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    namespace_match = re.search(r'@namespace\s+([^\s]+)', content)
                    if namespace_match:
                        namespace = namespace_match.group(1).strip()
                        break
            except Exception:
                continue
    
    # Fallback: infer from component name
    if not namespace:
        namespace = component_name
    
    return namespace


def extract_csproj_info(component_path, component_name):
    """Extract information from .csproj file."""
    csproj_path = Path(component_path) / f"{component_name}.csproj"
    
    info = {
        "target_frameworks": [],
        "dependencies": [],
        "project_references": [],
        "version": "1.0.0",
        "authors": "Tail.Blazor Core Team",
        "company": "Tail.Blazor",
        "product": component_name,
        "description": f"{component_name} component for Tail.Blazor",
        "license": "MIT",
        "repository_url": "https://github.com/tailblazor/tailblazor",
        "package_project_url": "https://tailblazor.com"
    }
    
    if not csproj_path.exists():
        return info
    
    try:
        with open(csproj_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract TargetFrameworks
        tf_match = re.search(r'<TargetFrameworks>(.*?)</TargetFrameworks>', content, re.DOTALL)
        if tf_match:
            frameworks = [f.strip() for f in tf_match.group(1).split(';') if f.strip()]
            info["target_frameworks"] = frameworks
        else:
            # Try TargetFramework (singular)
            tf_match = re.search(r'<TargetFramework>(.*?)</TargetFramework>', content)
            if tf_match:
                info["target_frameworks"] = [tf_match.group(1).strip()]
        
        # Extract PackageReference dependencies
        package_refs = re.findall(r'<PackageReference\s+Include="([^"]+)"(?:\s+Version="([^"]+)")?', content)
        for pkg_name, pkg_version in package_refs:
            version = pkg_version if pkg_version else "latest"
            info["dependencies"].append({"name": pkg_name, "version": version, "type": "Package"})
        
        # Extract ProjectReference dependencies
        project_refs = re.findall(r'<ProjectReference\s+Include="([^"]+)"', content)
        for proj_path in project_refs:
            # Extract project name from path
            proj_name = Path(proj_path).stem
            info["project_references"].append({"name": proj_name, "type": "Project"})
            info["dependencies"].append({"name": proj_name, "version": "local", "type": "Project"})
        
        # Extract package metadata
        version_match = re.search(r'<Version>(.*?)</Version>', content)
        if version_match:
            info["version"] = version_match.group(1).strip()
        
        authors_match = re.search(r'<Authors>(.*?)</Authors>', content)
        if authors_match:
            info["authors"] = authors_match.group(1).strip()
        
        company_match = re.search(r'<Company>(.*?)</Company>', content)
        if company_match:
            info["company"] = company_match.group(1).strip()
        
        product_match = re.search(r'<Product>(.*?)</Product>', content)
        if product_match:
            info["product"] = product_match.group(1).strip()
        
        desc_match = re.search(r'<Description>(.*?)</Description>', content)
        if desc_match:
            info["description"] = desc_match.group(1).strip()
        
        license_match = re.search(r'<PackageLicenseExpression>(.*?)</PackageLicenseExpression>', content)
        if license_match:
            info["license"] = license_match.group(1).strip()
        
        repo_match = re.search(r'<RepositoryUrl>(.*?)</RepositoryUrl>', content)
        if repo_match:
            info["repository_url"] = repo_match.group(1).strip()
        
        url_match = re.search(r'<PackageProjectUrl>(.*?)</PackageProjectUrl>', content)
        if url_match:
            info["package_project_url"] = url_match.group(1).strip()
        
    except Exception as e:
        pass
    
    return info


def extract_all_enums(component_path):
    """Extract all enums from component C# files."""
    enums = {}
    namespace = None
    
    try:
        for cs_file in Path(component_path).glob("*.cs"):
            with open(cs_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract namespace if present
            ns_match = re.search(r'namespace\s+([^\s\{]+)', content)
            if ns_match:
                namespace = ns_match.group(1).strip()
            
            # Find all enum definitions
            enum_pattern = r'public\s+enum\s+(\w+)\s*\{(.*?)\}'
            for match in re.finditer(enum_pattern, content, re.DOTALL):
                enum_name = match.group(1)
                enum_body = match.group(2)
                
                # Extract enum values
                enum_values = re.findall(r'(\w+)\s*(?:=\s*\d+)?[,}]', enum_body)
                values = [v.strip() for v in enum_values if v.strip()]
                
                # Extract description if available (look for XML comment before enum)
                # Search backwards from the enum definition
                enum_start = match.start()
                before_enum = content[:enum_start]
                # Look for the last /// comment before this enum
                comment_pattern = r'///\s*<summary>\s*(.*?)\s*</summary>'
                comment_matches = list(re.finditer(comment_pattern, before_enum, re.DOTALL))
                description = ""
                if comment_matches:
                    # Get the last comment before the enum
                    last_comment = comment_matches[-1]
                    # Check if it's close to the enum (within reasonable distance)
                    if enum_start - last_comment.end() < 200:
                        description = last_comment.group(1).strip()
                
                if not description:
                    description = f"{enum_name} enum"
                
                # Store with both short name and full name
                full_name = f"{namespace}.{enum_name}" if namespace else enum_name
                enum_data = {
                    "name": enum_name,
                    "full_name": full_name,
                    "values": values,
                    "description": description
                }
                enums[enum_name] = enum_data
                if namespace:
                    enums[full_name] = enum_data
    except Exception as e:
        pass
    
    return enums


def extract_using_directives(component_path):
    """Extract @using directives from razor files to determine imported namespaces."""
    using_directives = []
    
    # Check _Imports.razor first
    imports_path = Path(component_path) / "_Imports.razor"
    if imports_path.exists():
        try:
            with open(imports_path, 'r', encoding='utf-8') as f:
                content = f.read()
                using_matches = re.findall(r'@using\s+([^\s]+)', content)
                using_directives.extend([m.strip() for m in using_matches])
        except Exception:
            pass
    
    # Check all .razor files
    for razor_file in Path(component_path).glob("*.razor"):
        try:
            with open(razor_file, 'r', encoding='utf-8') as f:
                content = f.read()
                using_matches = re.findall(r'@using\s+([^\s]+)', content)
                using_directives.extend([m.strip() for m in using_matches])
        except Exception:
            continue
    
    return list(set(using_directives))  # Remove duplicates


def extract_base_class_info(code_block, component_path):
    """Extract base class information from @inherits or class declaration."""
    base_class = None
    
    # Try to find @inherits directive in razor file
    for razor_file in Path(component_path).glob("*.razor"):
        try:
            with open(razor_file, 'r', encoding='utf-8') as f:
                content = f.read()
                inherits_match = re.search(r'@inherits\s+([^\s]+)', content)
                if inherits_match:
                    base_class = inherits_match.group(1).strip()
                    break
        except Exception:
            continue
    
    # If not found, try to find in code block
    if not base_class and code_block:
        class_match = re.search(r'public\s+(?:partial\s+)?class\s+\w+\s*:\s*([^\s\{]+)', code_block)
        if class_match:
            base_class = class_match.group(1).strip()
    
    # Default base class for Tail.Blazor components
    if not base_class:
        base_class = "TailComponentBase"
    
    return base_class


def generate_component_readme(component_meta):
    """Generate comprehensive README.md for a component based on extracted metadata."""
    name = component_meta['name']
    friendly_name = component_meta['friendly_name']
    package_path = Path(component_meta['path'])
    readme_path = package_path / "README.md"
    params = component_meta.get('parameters', [])
    events = component_meta.get('events', [])
    properties = component_meta.get('properties', [])
    methods = component_meta.get('methods', [])
    classes = component_meta.get('classes', [])
    type_params = component_meta.get('type_params', [])
    features = component_meta.get('features', []) or [f"Rich {friendly_name} component"]
    description = component_meta.get('description', f"{friendly_name} component for Tail.Blazor")
    namespace = component_meta.get('namespace', name)
    csproj_info = component_meta.get('csproj_info', {})
    enums = component_meta.get('enums', {})
    base_class = component_meta.get('base_class', 'TailComponentBase')
    
    # Determine component tag name
    if '.' in friendly_name:
        component_tag = name.replace('Tail.Blazor.', 'Tail')
    else:
        component_tag = f"Tail{friendly_name}"

    def md_escape(text):
        if not text:
            return ''
        return str(text).replace('|', '\\|').replace('\n', ' ')

    md_lines = []
    
    # Title and Description
    md_lines.append(f"# {name}")
    md_lines.append("")
    md_lines.append(description)
    md_lines.append("")
    
    # Installation
    md_lines.append("## Installation")
    md_lines.append("")
    md_lines.append("```bash")
    md_lines.append(f"dotnet add package {name}")
    md_lines.append("```")
    md_lines.append("")
    
    # Features
    md_lines.append("## Features")
    md_lines.append("")
    if features:
        for feature in features:
            md_lines.append(f"- {feature}")
    else:
        md_lines.append(f"- Rich {friendly_name} component for Blazor applications")
    md_lines.append("")
    
    # Namespace
    md_lines.append("## Namespace")
    md_lines.append("")
    md_lines.append("```csharp")
    md_lines.append(f"using {namespace};")
    md_lines.append("```")
    md_lines.append("")
    
    # Component Usage
    md_lines.append("## Component Usage")
    md_lines.append("")
    usage_code = component_meta.get('example_code', '').strip()
    if not usage_code:
        if component_meta.get('is_generic', False):
            usage_code = f"<{component_tag} T=\"YourModel\">Content</{component_tag}>"
        else:
            usage_code = f"<{component_tag}>Content</{component_tag}>"
    md_lines.append("```razor")
    md_lines.append(usage_code)
    md_lines.append("```")
    md_lines.append("")
    
    # Parameters
    md_lines.append("## Parameters")
    md_lines.append("")
    if params:
        md_lines.append("| Name | Type | Default | Description |")
        md_lines.append("| --- | --- | --- | --- |")
        for p in params:
            default_val = p.get('default', '-') or '-'
            if default_val in ['""', "''"]:
                default_val = '-'
            md_lines.append(f"| **{md_escape(p['name'])}** | `{md_escape(p['type'])}` | {md_escape(default_val)} | {md_escape(p.get('description', ''))} |")
    else:
        md_lines.append("No parameters exposed.")
    md_lines.append("")
    
    # Events
    md_lines.append("## Events")
    md_lines.append("")
    if events:
        md_lines.append("| Event | Type | Description |")
        md_lines.append("| --- | --- | --- |")
        for e in events:
            event_type = e.get('type', 'void')
            if event_type and event_type != 'void':
                event_type = f"`EventCallback<{event_type}>`"
            else:
                event_type = "`EventCallback`"
            md_lines.append(f"| **{md_escape(e['name'])}** | {event_type} | {md_escape(e.get('description', ''))} |")
    else:
        md_lines.append("No events exposed.")
    md_lines.append("")
    
    # Enums
    if enums:
        md_lines.append("## Enums")
        md_lines.append("")
        for enum_name, enum_data in enums.items():
            md_lines.append(f"### {enum_name}")
            md_lines.append("")
            md_lines.append(f"```csharp")
            md_lines.append(f"public enum {enum_name}")
            md_lines.append("{")
            for value in enum_data.get('values', []):
                md_lines.append(f"    {value},")
            md_lines.append("}")
            md_lines.append("```")
            md_lines.append("")
            if enum_data.get('description'):
                md_lines.append(f"{enum_data['description']}")
                md_lines.append("")
    
    # Examples - Comprehensive section
    md_lines.append("## Examples")
    md_lines.append("")
    md_lines.append("This section provides comprehensive examples to help you get started with the component.")
    md_lines.append("")
    
    # Helper function to find enum
    def find_enum(param_type, enums_dict):
        enum_name = param_type.split('.')[-1]
        enum_data = enums_dict.get(enum_name, {})
        if not enum_data:
            for name, data in enums_dict.items():
                if enum_name.lower() in name.lower() or name.lower() in enum_name.lower():
                    return data
        return enum_data
    
    # Extract common parameters for examples
    variant_param = next((p for p in params if 'variant' in p['name'].lower()), None)
    size_param = next((p for p in params if 'size' in p['name'].lower()), None)
    disabled_param = next((p for p in params if 'disabled' in p['name'].lower()), None)
    loading_param = next((p for p in params if 'loading' in p['name'].lower() or 'isloading' in p['name'].lower()), None)
    
    # Quick Start Guide
    md_lines.append("### Quick Start")
    md_lines.append("")
    md_lines.append("Get up and running in seconds:")
    md_lines.append("")
    md_lines.append("```razor")
    md_lines.append("@page \"/quickstart\"")
    md_lines.append(f"@using {namespace}")
    md_lines.append("")
    has_child = any('renderfragment' in p['type'].lower() for p in params)
    if has_child:
        md_lines.append(f"<{component_tag}>")
        md_lines.append("    Hello, World!")
        md_lines.append(f"</{component_tag}>")
    else:
        md_lines.append(f"<{component_tag} />")
    md_lines.append("```")
    md_lines.append("")
    
    # Common Patterns
    md_lines.append("### Common Patterns")
    md_lines.append("")
    md_lines.append("Frequently used patterns and combinations:")
    md_lines.append("")
    
    patterns = []
    
    # Pattern 1: Basic with variant
    if variant_param:
        variant_enum = find_enum(variant_param['type'], enums)
        if variant_enum and variant_enum.get('values'):
            patterns.append(("Primary Action", f"""```razor
<{component_tag} Variant="{variant_param['type']}.{variant_enum['values'][0]}">
    Primary Action
</{component_tag}>
```"""))
    
    # Pattern 2: With size
    if size_param:
        size_enum = find_enum(size_param['type'], enums)
        if size_enum and size_enum.get('values'):
            patterns.append(("Medium Size", f"""```razor
<{component_tag} Size="{size_param['type']}.{size_enum['values'][len(size_enum['values'])//2] if len(size_enum['values']) > 2 else size_enum['values'][0]}">
    Medium Size
</{component_tag}>
```"""))
    
    # Pattern 3: With event
    if events:
        patterns.append(("With Click Handler", f"""```razor
<{component_tag} {events[0]['name']}="() => Console.WriteLine(\"Clicked\")">
    Click Me
</{component_tag}>
```"""))
    
    # Pattern 4: Disabled state
    if disabled_param:
        patterns.append(("Disabled State", f"""```razor
<{component_tag} Disabled="true">
    Disabled
</{component_tag}>
```"""))
    
    if patterns:
        for pattern_title, pattern_code in patterns[:4]:  # Show first 4 patterns
            md_lines.append(f"**{pattern_title}**")
            md_lines.append("")
            md_lines.append(pattern_code)
            md_lines.append("")
    
    # Basic example
    md_lines.append("### Basic Usage")
    md_lines.append("")
    md_lines.append("The simplest way to use the component:")
    md_lines.append("")
    md_lines.append("```razor")
    if component_meta.get('is_generic', False):
        md_lines.append(f"<{component_tag} T=\"YourModel\">Content</{component_tag}>")
    else:
        has_child = any('renderfragment' in p['type'].lower() for p in params)
        if has_child:
            md_lines.append(f"<{component_tag}>Content</{component_tag}>")
        else:
            md_lines.append(f"<{component_tag} />")
    md_lines.append("```")
    md_lines.append("")
    
    # Variants example if variant parameter exists
    variant_param = next((p for p in params if 'variant' in p['name'].lower()), None)
    if variant_param:
        variant_type = variant_param['type']
        variant_enum = find_enum(variant_type, enums)
        if variant_enum and variant_enum.get('values'):
            md_lines.append("### Variants")
            md_lines.append("")
            md_lines.append("Different visual variants for various use cases:")
            md_lines.append("")
            md_lines.append("```razor")
            for value in variant_enum['values']:
                md_lines.append(f'<{component_tag} Variant="{variant_type}.{value}">{value}</{component_tag}>')
            md_lines.append("```")
            md_lines.append("")
    
    # Sizes example if size parameter exists
    size_param = next((p for p in params if 'size' in p['name'].lower()), None)
    if size_param:
        size_type = size_param['type']
        size_enum = find_enum(size_type, enums)
        if size_enum and size_enum.get('values'):
            md_lines.append("### Sizes")
            md_lines.append("")
            md_lines.append("Size options to fit different layouts and contexts:")
            md_lines.append("")
            md_lines.append("```razor")
            for value in size_enum['values']:
                md_lines.append(f'<{component_tag} Size="{size_type}.{value}">{value}</{component_tag}>')
            md_lines.append("```")
            md_lines.append("")
    
    # States examples
    if disabled_param or loading_param:
        md_lines.append("### States")
        md_lines.append("")
        md_lines.append("Component states for different interaction scenarios:")
        md_lines.append("")
        md_lines.append("```razor")
        if disabled_param:
            md_lines.append(f"@* Disabled state *@")
            md_lines.append(f"<{component_tag} Disabled=\"true\">Disabled</{component_tag}>")
            md_lines.append("")
        if loading_param:
            md_lines.append(f"@* Loading state *@")
            md_lines.append(f"<{component_tag} IsLoading=\"true\">Loading...</{component_tag}>")
            md_lines.append("")
        if disabled_param and loading_param:
            md_lines.append(f"@* Both disabled and loading *@")
            md_lines.append(f"<{component_tag} Disabled=\"true\" IsLoading=\"true\">Processing</{component_tag}>")
        md_lines.append("```")
        md_lines.append("")
    
    # Events example if events exist
    if events:
        md_lines.append("### Event Handling")
        md_lines.append("")
        md_lines.append("Handle user interactions with event callbacks:")
        md_lines.append("")
        md_lines.append("```razor")
        first_event = events[0]
        event_name = first_event['name']
        event_type = first_event.get('type', 'void')
        
        # Check if event_type is a custom type (not a standard .NET type)
        standard_types = ['void', 'string', 'int', 'bool', 'double', 'float', 'decimal', 'DateTime', 
                         'MouseEventArgs', 'KeyboardEventArgs', 'ChangeEventArgs', 'FocusEventArgs']
        is_custom_type = event_type and event_type != 'void' and not any(
            event_type.startswith(st) or event_type == st for st in standard_types
        )
        
        # Use fully qualified namespace for custom types
        if is_custom_type and '.' not in event_type:
            event_type_qualified = f"{namespace}.{event_type}"
        else:
            event_type_qualified = event_type
        
        if event_type and event_type != 'void':
            md_lines.append(f"<{component_tag} {event_name}=\"Handle{event_name}\">")
            md_lines.append("    Click Me")
            md_lines.append(f"</{component_tag}>")
            md_lines.append("")
            md_lines.append("@code {")
            md_lines.append(f"    private void Handle{event_name}({event_type_qualified} args)")
            md_lines.append("    {")
            md_lines.append("        // Handle the event")
            md_lines.append("        Console.WriteLine($\"Event triggered: {args}\");")
            md_lines.append("    }")
        else:
            md_lines.append(f"<{component_tag} {event_name}=\"Handle{event_name}\">")
            md_lines.append("    Click Me")
            md_lines.append(f"</{component_tag}>")
            md_lines.append("")
            md_lines.append("@code {")
            md_lines.append(f"    private void Handle{event_name}()")
            md_lines.append("    {")
            md_lines.append("        // Handle the event")
            md_lines.append("        Console.WriteLine(\"Event triggered\");")
            md_lines.append("    }")
        md_lines.append("}")
        md_lines.append("```")
        md_lines.append("")
    
    # Parameter combinations
    md_lines.append("### Parameter Combinations")
    md_lines.append("")
    md_lines.append("Combine multiple parameters for advanced usage:")
    md_lines.append("")
    md_lines.append("```razor")
    
    # Build combination example
    combo_attrs = []
    if variant_param:
        variant_enum = find_enum(variant_param['type'], enums)
        if variant_enum and variant_enum.get('values'):
            combo_attrs.append(f'{variant_param["name"]}="{variant_param["type"]}.{variant_enum["values"][0]}"')
    
    if size_param:
        size_enum = find_enum(size_param['type'], enums)
        if size_enum and size_enum.get('values'):
            combo_attrs.append(f'{size_param["name"]}="{size_param["type"]}.{size_enum["values"][1] if len(size_enum["values"]) > 1 else size_enum["values"][0]}"')
    
    # Add other common parameters
    for p in params[:5]:  # Limit to first 5 additional params
        p_name = p['name'].lower()
        if any(x in p_name for x in ['variant', 'size', 'disabled', 'loading', 'childcontent']):
            continue
        
        p_type = p['type'].lower()
        if 'bool' in p_type:
            combo_attrs.append(f'{p["name"]}="true"')
        elif 'string' in p_type:
            combo_attrs.append(f'{p["name"]}="Sample {p["name"]}"')
        elif 'int' in p_type or 'double' in p_type:
            combo_attrs.append(f'{p["name"]}="10"')
    
    has_child = any('renderfragment' in p['type'].lower() for p in params)
    if combo_attrs:
        attrs_str = ' '.join(combo_attrs)
        if has_child:
            md_lines.append(f"<{component_tag} {attrs_str}>")
            md_lines.append("    Combined Parameters")
            md_lines.append(f"</{component_tag}>")
        else:
            md_lines.append(f"<{component_tag} {attrs_str} />")
    else:
        if has_child:
            md_lines.append(f"<{component_tag}>")
            md_lines.append("    Content")
            md_lines.append(f"</{component_tag}>")
        else:
            md_lines.append(f"<{component_tag} />")
    
    md_lines.append("```")
    md_lines.append("")
    
    # Advanced examples
    advanced_examples = []
    
    # With icons if icon parameters exist
    icon_start = next((p for p in params if 'iconstart' in p['name'].lower() or 'iconstart' in p['name']), None)
    icon_end = next((p for p in params if 'iconend' in p['name'].lower() or 'iconend' in p['name']), None)
    
    if icon_start or icon_end:
        icon_example = f"""```razor
<{component_tag}>
    <IconStart>
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
    </IconStart>
    Button Text
    <IconEnd>
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
        </svg>
    </IconEnd>
</{component_tag}>
```"""
        advanced_examples.append(("With Icons", icon_example))
    
    # With conditional rendering
    if disabled_param or loading_param:
        toggle_button = ""
        if events:
            toggle_button = f"""<{component_tag} OnClick="ToggleProcessing">
    Toggle State
</{component_tag}>

"""
        conditional_example = f"""```razor
@code {{
    private bool isProcessing = false;
    private bool isDisabled = false;
}}

<{component_tag} Disabled="@isDisabled" IsLoading="@isProcessing">
    @if (isProcessing)
    {{
        <text>Processing...</text>
    }}
    else
    {{
        <text>Submit</text>
    }}
</{component_tag}>

{toggle_button}@code {{
    private void ToggleProcessing()
    {{
        isProcessing = !isProcessing;
        isDisabled = isProcessing;
    }}
}}
```"""
        advanced_examples.append(("Conditional Rendering", conditional_example))
    
    # With data binding
    value_param = next((p for p in params if 'value' in p['name'].lower() and 'changed' not in p['name'].lower()), None)
    changed_event = next((e for e in events if 'changed' in e['name'].lower() or 'change' in e['name'].lower()), None)
    
    if value_param and changed_event:
        binding_example = f"""```razor
@code {{
    private string componentValue = "";
}}

<{component_tag} @bind-Value="componentValue" {changed_event['name']}="OnValueChanged">
    Bound Component
</{component_tag}>

<p>Current Value: @componentValue</p>

@code {{
    private void OnValueChanged()
    {{
        Console.WriteLine($"Value changed to: {{componentValue}}");
    }}
}}
```"""
        advanced_examples.append(("Data Binding", binding_example))
    
    # With styling
    style_param = next((p for p in params if 'style' in p['name'].lower() or 'class' in p['name'].lower()), None)
    if style_param:
        style_example = f"""```razor
@* Using Style parameter *@
<{component_tag} Style="background-color: #3b82f6; color: white;">
    Custom Styled
</{component_tag}>

@* Using Class parameter *@
<{component_tag} Class="my-custom-class shadow-lg">
    With Custom Class
</{component_tag}>
```"""
        advanced_examples.append(("Custom Styling", style_example))
    
    # With tooltip
    tooltip_param = next((p for p in params if 'tooltip' in p['name'].lower()), None)
    if tooltip_param:
        tooltip_example = f"""```razor
<{component_tag} Tooltip="This is a helpful tooltip">
    Hover for Tooltip
</{component_tag}>
```"""
        advanced_examples.append(("With Tooltip", tooltip_example))
    
    # With full width
    fullwidth_param = next((p for p in params if 'fullwidth' in p['name'].lower() or 'fullwidth' in p['name']), None)
    if fullwidth_param:
        fullwidth_example = f"""```razor
<div class="w-full">
    <{component_tag} FullWidth="true">
        Full Width Component
    </{component_tag}>
</div>
```"""
        advanced_examples.append(("Full Width", fullwidth_example))
    
    # Additional examples based on specific parameters
    # Loading with custom text
    loading_text_param = next((p for p in params if 'loadingtext' in p['name'].lower()), None)
    if loading_param and loading_text_param:
        advanced_examples.append(("Loading with Custom Text", f"""```razor
<{component_tag} IsLoading="true" LoadingText="Saving...">
    Save
</{component_tag}>

<{component_tag} IsLoading="true" ShowDefaultLoadingText="true">
    Submit
</{component_tag}>
```"""))
    
    # Multiple events
    if len(events) > 1:
        multi_event_example = f"""```razor
<{component_tag} 
    {events[0]['name']}="OnFirstEvent"
    {events[1]['name']}="OnSecondEvent">
    Multiple Events
</{component_tag}>

@code {{
    private void OnFirstEvent()
    {{
        Console.WriteLine("First event triggered");
    }}
    
    private void OnSecondEvent()
    {{
        Console.WriteLine("Second event triggered");
    }}
}}
```"""
        advanced_examples.append(("Multiple Event Handlers", multi_event_example))
    
    # Form integration
    if events:
        form_example = f"""```razor
<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    
    <{component_tag} Type="submit">
        Submit Form
    </{component_tag}>
</EditForm>

@code {{
    private MyModel model = new();
    
    private void HandleSubmit()
    {{
        // Process form submission
        Console.WriteLine("Form submitted successfully");
    }}
}}
```"""
        advanced_examples.append(("Form Integration", form_example))
    
    # Accessibility
    aria_param = next((p for p in params if 'aria' in p['name'].lower() or 'label' in p['name'].lower()), None)
    if aria_param or tooltip_param:
        acc_attrs = []
        if aria_param:
            acc_attrs.append(f'{aria_param["name"]}="Primary action button"')
        if tooltip_param:
            acc_attrs.append(f'{tooltip_param["name"]}="Click to perform action"')
        
        if acc_attrs:
            accessibility_example = f"""```razor
@* Accessible component with ARIA label and tooltip *@
<{component_tag} {' '.join(acc_attrs)}>
    Accessible Button
</{component_tag}>
```"""
            advanced_examples.append(("Accessibility", accessibility_example))
    
    # Display advanced examples
    if advanced_examples:
        md_lines.append("### Advanced Examples")
        md_lines.append("")
        md_lines.append("More complex usage scenarios:")
        md_lines.append("")
        for title, code in advanced_examples:
            md_lines.append(f"#### {title}")
            md_lines.append("")
            md_lines.append(code)
            md_lines.append("")
    
    # Real-world scenario
    md_lines.append("### Real-World Example")
    md_lines.append("")
    md_lines.append("A complete example showing practical usage:")
    md_lines.append("")
    md_lines.append("```razor")
    md_lines.append("@page \"/example\"")
    md_lines.append("")
    md_lines.append("<h3>Component Demo</h3>")
    md_lines.append("")
    md_lines.append("<div class=\"space-y-4\">")
    
    # Build a realistic example
    example_attrs = []
    if variant_param:
        variant_enum = find_enum(variant_param['type'], enums)
        if variant_enum and variant_enum.get('values'):
            example_attrs.append(f'{variant_param["name"]}="{variant_param["type"]}.{variant_enum["values"][0]}"')
    
    if size_param:
        size_enum = find_enum(size_param['type'], enums)
        if size_enum and size_enum.get('values'):
            example_attrs.append(f'{size_param["name"]}="{size_param["type"]}.{size_enum["values"][1] if len(size_enum["values"]) > 1 else size_enum["values"][0]}"')
    
    if events:
        example_attrs.append(f'{events[0]["name"]}="HandleAction"')
    
    attrs_str = ' '.join(example_attrs) if example_attrs else ''
    
    has_child = any('renderfragment' in p['type'].lower() for p in params)
    if has_child:
        md_lines.append(f"    <{component_tag} {attrs_str}>")
        md_lines.append("        Action Button")
        md_lines.append(f"    </{component_tag}>")
    else:
        md_lines.append(f"    <{component_tag} {attrs_str} />")
    
    md_lines.append("</div>")
    md_lines.append("")
    md_lines.append("@code {")
    if events:
        event_type = events[0].get('type', 'void')
        if event_type and event_type != 'void':
            md_lines.append(f"    private void HandleAction({event_type} args)")
        else:
            md_lines.append("    private void HandleAction()")
        md_lines.append("    {")
        md_lines.append("        // Perform action")
        md_lines.append("        Console.WriteLine(\"Action executed\");")
        md_lines.append("    }")
    else:
        md_lines.append("    // Component logic here")
    md_lines.append("}")
    md_lines.append("```")
    md_lines.append("")
    
    # Base Class
    md_lines.append("## Base Class")
    md_lines.append("")
    md_lines.append(f"The component inherits from `{base_class}` (from `Tail.Blazor.Core.Base`), which provides:")
    md_lines.append("")
    md_lines.append("- `Class` parameter for additional CSS classes")
    md_lines.append("- `AdditionalAttributes` parameter for additional HTML attributes")
    md_lines.append("")
    
    # Dependencies
    md_lines.append("## Dependencies")
    md_lines.append("")
    dependencies = csproj_info.get('dependencies', [])
    if dependencies:
        md_lines.append("- `Tail.Blazor.Core.Base` (required)")
        for dep in dependencies:
            if dep['name'] != 'Tail.Blazor.Core.Base':
                dep_name = dep['name']
                if dep['type'] == 'Project':
                    md_lines.append(f"- `{dep_name}`")
                else:
                    md_lines.append(f"- `{dep_name}`")
    else:
        md_lines.append("- `Tail.Blazor.Core.Base` (required)")
        md_lines.append("- `Microsoft.AspNetCore.Components`")
        md_lines.append("- `Microsoft.AspNetCore.Components.Web`")
    md_lines.append("")
    
    # Target Frameworks
    md_lines.append("## Target Frameworks")
    md_lines.append("")
    target_frameworks = csproj_info.get('target_frameworks', [])
    if target_frameworks:
        for tf in target_frameworks:
            md_lines.append(f"- .NET {tf.replace('net', '').replace('.0', '')}")
    else:
        md_lines.append("- .NET 8.0")
        md_lines.append("- .NET 9.0")
        md_lines.append("- .NET 10.0")
    md_lines.append("")
    
    # Package Information
    md_lines.append("## Package Information")
    md_lines.append("")
    md_lines.append(f"- **Package ID**: `{name}`")
    md_lines.append(f"- **Version**: {csproj_info.get('version', '1.0.0')}")
    md_lines.append(f"- **License**: {csproj_info.get('license', 'MIT')}")
    md_lines.append(f"- **Authors**: {csproj_info.get('authors', 'Tail.Blazor Core Team')}")
    md_lines.append(f"- **Repository**: {csproj_info.get('repository_url', 'https://github.com/tailblazor/tailblazor')}")
    md_lines.append("")

    readme_path.write_text('\n'.join(md_lines), encoding='utf-8')


def extract_enum_values(component_path, enum_name):
    """Extract enum values from component C# files."""
    values = []
    
    try:
        # Look for enum files in component directory
        for cs_file in Path(component_path).glob("*.cs"):
            with open(cs_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Look for the enum definition
            pattern = rf'public enum {enum_name}\s*\{{(.*?)\}}'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                enum_body = match.group(1)
                # Extract enum values
                enum_values = re.findall(r'(\w+)\s*(?:=\s*\d+)?[,}]', enum_body)
                values = [v.strip() for v in enum_values if v.strip()]
                break
    except Exception as e:
        pass
    
    return values


def extract_type_parameters(razor_content):
    """Extract @typeparam declarations to capture generic data types."""
    if not razor_content:
        return []
    type_params = re.findall(r'@typeparam\s+([A-Za-z_]\w*)', razor_content)
    # Preserve order while deduplicating
    seen = set()
    ordered_params = []
    for param in type_params:
        if param not in seen:
            seen.add(param)
            ordered_params.append(param)
    return ordered_params


def extract_class_info(code_block):
    """Extract partial class declarations from the @code block."""
    classes = []
    if not code_block:
        return classes
    pattern = r'public\s+partial\s+class\s+(\w+)\s*(?::\s*([^\s\{]+))?'
    seen = set()
    for match in re.finditer(pattern, code_block):
        class_name = match.group(1)
        base_type = match.group(2) if match.group(2) else ""
        if class_name in seen:
            continue
        seen.add(class_name)
        classes.append({"name": class_name, "base_type": base_type})
    return classes


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


def generate_event_description(event_name, event_type):
    """Auto-generate event callback descriptions."""
    event_lower = event_name.lower()
    
    descriptions = {
        'changed': f'Raised when value changes',
        'click': f'Raised when component is clicked',
        'onchange': f'Raised on value change',
        'onclick': f'Raised on click',
        'onblur': f'Raised when focus is lost',
        'onfocus': f'Raised when focus is gained',
        'onkeydown': f'Raised on key down',
        'onkeyup': f'Raised on key up',
        'onmousedown': f'Raised on mouse down',
        'onmouseup': f'Raised on mouse up',
        'onmouseover': f'Raised on mouse over',
        'onmouseout': f'Raised on mouse out',
        'oninput': f'Raised on input',
        'onsubmit': f'Raised on form submit',
        'onselected': f'Raised when item is selected',
        'onclosed': f'Raised when closed',
        'onopened': f'Raised when opened',
    }
    
    for keyword, desc in descriptions.items():
        if keyword in event_lower:
            return desc
    
    if event_type and event_type != 'void':
        return f'Raised with {event_type} value'
    
    return f'{event_name} callback'


def extract_component_metadata(component_info):
    """Extract metadata for a single component."""
    if not component_info['razor_file']:
        csproj_info = extract_csproj_info(component_info['path'], component_info['name'])
        return {
            "name": component_info['name'],
            "friendly_name": component_info['friendly_name'],
            "category": component_info['category'],
            "path": component_info['path'],
            "description": f"{component_info['friendly_name']} component",
            "parameters": [],
            "events": [],
            "properties": [],
            "methods": [],
            "classes": [],
            "type_params": [],
            "features": [],
            "package_size": "",
            "example_code": "",
            "is_generic": component_info.get('is_generic', False),
            "is_missing": component_info.get('is_missing', False),
            "namespace": extract_namespace(component_info['path'], component_info['name']),
            "csproj_info": csproj_info,
            "enums": {},
            "base_class": None
        }
    
    code_block = extract_razor_code(component_info['razor_file'])
    try:
        razor_content = Path(component_info['razor_file']).read_text(encoding='utf-8')
    except Exception:
        razor_content = ""
    
    # Extract @using directives FIRST to help with parameter type resolution
    using_directives = extract_using_directives(component_info['path'])
    
    # Extract parameters - now with context of using directives
    parameters = extract_parameters(code_block)
    events = extract_events(code_block)
    properties = extract_properties(code_block)
    methods = extract_methods(code_block)
    classes = extract_class_info(code_block)
    type_params = extract_type_parameters(razor_content)
    
    # Extract README content
    readme_content = extract_readme_content(component_info['path'])
    
    # Extract additional metadata
    namespace = extract_namespace(component_info['path'], component_info['name'])
    csproj_info = extract_csproj_info(component_info['path'], component_info['name'])
    enums = extract_all_enums(component_info['path'])
    base_class = extract_base_class_info(code_block, component_info['path'])
    
    return {
        "name": component_info['name'],
        "friendly_name": component_info['friendly_name'],
        "category": component_info['category'],
        "path": component_info['path'],
        "description": readme_content.get("description", f"{component_info['friendly_name']} component for Tail.Blazor"),
        "parameters": parameters,
        "events": events,
        "properties": properties,
        "methods": methods,
        "classes": classes,
        "type_params": type_params,
        "features": readme_content.get("features", []),
        "package_size": readme_content.get("package_size", ""),
        "example_code": readme_content.get("example_code", ""),
        "is_generic": component_info.get('is_generic', False),
        "is_missing": component_info.get('is_missing', False),
        "namespace": namespace,
        "csproj_info": csproj_info,
        "enums": enums,
        "base_class": base_class,
        "using_directives": using_directives
    }


# ============================================================================
# PHASE 3: DOCUMENTATION GENERATION
# ============================================================================

def escape_razor_code(code):
    """Escape code for Razor @"" verbatim strings."""
    if not code:
        return ""
    return code.replace('"', '""')


def get_component_examples(component_meta, parameters, events):
    """Generate feature-based examples from component metadata, parameters, and events."""
    name = component_meta['name']
    friendly_name = component_meta['friendly_name']
    category = component_meta['category']
    is_generic = component_meta.get('is_generic', False)
    
    if '.' in friendly_name:
        component_tag = name.replace('Tail.Blazor.', 'Tail')
    else:
        component_tag = f"Tail{friendly_name}"
    
    if is_generic:
        return {"basic": f'@* {friendly_name} requires type parameter *@'}
    
    examples = {}

    preview_inputs = list(parameters) + [
        {"name": e["name"], "type": f'EventCallback<{e["type"]}>', "source": "event"}
        for e in events
    ]

    def type_in_component(t):
        comp_path = Path(component_meta['path']) if component_meta.get('path') else None
        if not comp_path or not comp_path.exists():
            return False
        for p in comp_path.rglob("*.cs"):
            try:
                text = p.read_text(encoding="utf-8")
                if re.search(rf"\b{re.escape(t)}\b", text):
                    return True
            except Exception:
                continue
        return False

    def enum_values(t):
        comp_path = Path(component_meta['path']) if component_meta.get('path') else None
        if not comp_path or not comp_path.exists():
            return []
        for p in comp_path.rglob("*.cs"):
            try:
                text = p.read_text(encoding="utf-8")
                match = re.search(rf"enum\s+{re.escape(t)}\s*\{{([^}}]+)\}}", text, re.MULTILINE | re.DOTALL)
                if match:
                    raw = match.group(1)
                    candidates = re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*)\b\s*(?:,|=)", raw)
                    items = [m.group(1) for m in candidates]
                    if items:
                        return items
            except Exception:
                continue
        return []

    def qualify_type(t):
        if '.' in t:
            return t
        if type_in_component(t):
            return f"{name}.{t}"
        return t

    def attr_sample(p):
        p_name = p['name']
        p_type = p['type']
        lower = p_name.lower()
        # Skip child content and render fragments
        if 'renderfragment' in p_type.lower() or p_type.strip() == 'RenderFragment':
            return None
        if 'eventcallback' in p_type.lower():
            if 'click' in lower:
                return f'{p_name}="() => Console.WriteLine(\"{p_name}\")"'
            return f'{p_name}="args => Console.WriteLine(\"{p_name}\")"'
        if p_type.lower() in ['bool', 'boolean']:
            return f'{p_name}="true"'
        if p_type.lower().startswith('string'):
            return f'{p_name}="Sample {p_name}"'
        if 'int' in p_type.lower() or 'double' in p_type.lower() or 'float' in p_type.lower() or 'decimal' in p_type.lower():
            return f'{p_name}="1"'
        if 'variant' in lower:
            return f'{p_name}="{qualify_type(p_type)}.Primary"'
        if 'size' in lower:
            return f'{p_name}="{qualify_type(p_type)}.Md"'
        if 'color' in lower:
            return f'{p_name}="var(--color-primary)"'
        return None

    has_child_content = any('renderfragment' in p['type'].lower() or p['type'].strip() == 'RenderFragment' for p in parameters)

    def build_attrs(limit=4):
        attrs = []
        for p in preview_inputs:
            sample = attr_sample(p)
            if sample:
                attrs.append(sample)
            if len(attrs) >= limit:
                break
        return ' '.join(attrs)
    
    # Use extracted example from README if available
    if component_meta.get('example_code'):
        extracted_example = component_meta['example_code']
        # Try to extract just the component usage part
        razor_match = re.search(r'<Tail\w+.*?(?:</Tail\w+>|/>)', extracted_example, re.DOTALL)
        if razor_match:
            examples['basic'] = razor_match.group(0)
        else:
            examples['basic'] = extracted_example
    else:
        attrs = build_attrs()
        if has_child_content:
            examples['basic'] = f'<{component_tag} {attrs}>Sample {friendly_name}</{component_tag}>' if attrs else f'<{component_tag}>Sample {friendly_name}</{component_tag}>'
        else:
            examples['basic'] = f'<{component_tag} {attrs} />' if attrs else f'<{component_tag} />'
    
    # Generate variants examples - SIMPLE, NO UNDEFINED VARIABLES
    variant_type = next((p['type'] for p in parameters if 'variant' in p['name'].lower()), None)
    if variant_type:
        vtype = qualify_type(variant_type)
        enum_items = enum_values(variant_type)
        if not enum_items:
            enum_items = ['Primary', 'Success', 'Warning']
        preview_items = enum_items[:3] if len(enum_items) >= 3 else enum_items
        variants_markup = []
        for item in preview_items:
            variants_markup.append(f'<{component_tag} Variant="{vtype}.{item}">{item}</{component_tag}>')
        examples['variants'] = "\n".join(variants_markup)
    
    # Generate sizes examples - SIMPLE, NO UNDEFINED VARIABLES
    size_type = next((p['type'] for p in parameters if 'size' in p['name'].lower()), None)
    if size_type:
        if size_type.lower() in ['int', 'double', 'float', 'decimal']:
            examples['sizes'] = f'''<{component_tag} Size="12">Small</{component_tag}>
<{component_tag} Size="16">Medium</{component_tag}>
<{component_tag} Size="24">Large</{component_tag}>'''
        else:
            stype = qualify_type(size_type)
            examples['sizes'] = f'''<{component_tag} Size="{stype}.Sm">Small</{component_tag}>
<{component_tag} Size="{stype}.Md">Medium</{component_tag}>
<{component_tag} Size="{stype}.Lg">Large</{component_tag}>'''

    # Generate events example if events exist
    if events:
        event_attr = attr_sample({"name": events[0]['name'], "type": f'EventCallback<{events[0]["type"]}>', "source": "event"})
        attrs = build_attrs(limit=2)
        combined_attrs = ' '.join(filter(None, [attrs, event_attr]))
        if has_child_content:
            examples['events'] = f'<{component_tag} {combined_attrs}>Interact</{component_tag}>' if combined_attrs else f'<{component_tag}>Interact</{component_tag}>'
        else:
            examples['events'] = f'<{component_tag} {combined_attrs} />' if combined_attrs else f'<{component_tag} />'
    
    return examples


def generate_doc_page(component_meta):
    """Generate MudBlazor-style documentation page."""
    name = component_meta['name']
    friendly_name = component_meta['friendly_name']
    category = component_meta['category']
    params = component_meta['parameters']
    type_params = component_meta.get('type_params', [])
    classes = component_meta.get('classes', [])
    features = component_meta.get('features', [])
    package_size = component_meta.get('package_size', '')
    is_generic = component_meta.get('is_generic', False)
    is_missing = component_meta.get('is_missing', False)
    
    component_tag = f"Tail{friendly_name}" if '.' not in friendly_name else name.replace('Tail.Blazor.', 'Tail')
    
    # Get examples from README first (preferred), then generate if not available
    readme_examples = component_meta.get('readme_examples', {})
    generated_examples = get_component_examples(component_meta, params, component_meta.get('events', []))
    
    # Merge: prefer README examples, fallback to generated
    examples = {}
    for key in ['basic', 'variants', 'sizes', 'states', 'events', 'combinations', 'quickstart', 'patterns', 'advanced', 'realworld']:
        if key in readme_examples and readme_examples[key]:
            examples[key] = readme_examples[key]
        elif key in generated_examples:
            examples[key] = generated_examples[key]
    
    def find_enum(enum_type, enums_list):
        """Find enum by type name."""
        if not enum_type or not enums_list:
            return None
        # Try exact match first
        for enum in enums_list:
            if enum.get('name') == enum_type or enum.get('name') == enum_type.split('.')[-1]:
                return enum
        return None
    
    def get_preview_markup(example_name):
        """Extract clean, compilable Razor markup for PreviewUI from examples."""
        value = examples.get(example_name, "")
        if not value:
            return None
        
        # Extract just the component markup (before @code block)
        parts = re.split(r'\n@code\s*\{', value, 1)
        markup = parts[0].strip() if parts else value
        
        # Remove @page and @using directives (already in the page)
        markup = re.sub(r'@page\s+"[^"]*"\s*\n?', '', markup)
        markup = re.sub(r'@using\s+[^\s]+\s*\n?', '', markup)
        
        # Remove all event handler attributes (OnClick, OnValueChanged, @bind-Value, etc.)
        markup = re.sub(r'\s+On[A-Z]\w+="[^"]*"', '', markup)
        markup = re.sub(r'\s+On\w+="[^"]*"', '', markup)
        markup = re.sub(r'\s+@[a-zA-Z-]+="[^"]*"', '', markup)
        markup = re.sub(r'\s+@bind-\w+="[^"]*"', '', markup)
        markup = re.sub(r'\s+\w+Changed="[^"]*"', '', markup)
        markup = re.sub(r'\s+\w+Click="[^"]*"', '', markup)
        markup = re.sub(r'\s+\w+="Handle[^"]*"', '', markup)
        markup = re.sub(r'\s+\w+="\(\)\s*=>[^"]*"', '', markup)
        
        # Remove comments that might cause issues
        markup = re.sub(r'@\*.*?\*@', '', markup, flags=re.DOTALL)
        
        # ALWAYS use fully qualified namespaces for all enum references
        namespace = component_meta.get('namespace', name)
        if namespace:
            # Build enum namespace map from component's parameters and enums
            enum_to_namespace_map = {}
            
            # First, map enums defined in this component
            component_enums = component_meta.get('enums', [])
            if isinstance(component_enums, list):
                for enum_data in component_enums:
                    if isinstance(enum_data, dict):
                        enum_name = enum_data.get('name', '')
                        if enum_name:
                            enum_to_namespace_map[enum_name] = namespace
            
            # Then, check parameters to see what enum types are actually used
            params_list = component_meta.get('parameters', [])
            using_directives = component_meta.get('using_directives', [])
            
            for param in params_list:
                param_type = param.get('type', '')
                if param_type:
                    # Extract enum name (last part after dots)
                    enum_name = param_type.split('.')[-1]
                    # If type is fully qualified, use that namespace
                    if '.' in param_type:
                        enum_ns = '.'.join(param_type.split('.')[:-1])
                        # Only override if not already mapped (component's own enums take precedence)
                        if enum_name not in enum_to_namespace_map:
                            enum_to_namespace_map[enum_name] = enum_ns
                    elif enum_name not in enum_to_namespace_map:
                        # Unqualified type - DYNAMICALLY resolve from @using directives
                        enum_found = False
                        
                        # Strategy 1: Direct pattern matching for common enum names
                        # ButtonSize, ButtonVariant -> Tail.Blazor.Button
                        if enum_name in ['ButtonSize', 'ButtonVariant']:
                            for using_ns in using_directives:
                                if 'Tail.Blazor.Button' in using_ns or using_ns == 'Tail.Blazor.Button':
                                    enum_to_namespace_map[enum_name] = 'Tail.Blazor.Button'
                                    enum_found = True
                                    break
                        
                        # Strategy 2: Extract base name from enum and match with using directives
                        # e.g., "InputSize" -> base "Input" -> match "Tail.Blazor.Input"
                        if not enum_found:
                            # Remove common suffixes to get base component name
                            base_name = enum_name
                            for suffix in ['Size', 'Variant', 'Type', 'Position', 'Placement', 'Style', 'State', 'Level', 'Mode', 'Direction', 'Alignment', 'Orientation', 'Theme', 'Shape']:
                                if enum_name.endswith(suffix):
                                    base_name = enum_name[:-len(suffix)]
                                    break
                            
                            # Match base name with using directives
                            for using_ns in using_directives:
                                # Check if base name appears in the namespace
                                # e.g., "Input" in "Tail.Blazor.Input"
                                if base_name in using_ns and 'Tail.Blazor' in using_ns:
                                    enum_to_namespace_map[enum_name] = using_ns
                                    enum_found = True
                                    break
                        
                        # Strategy 3: For enum names that start with a component name
                        # e.g., "ButtonSize" starts with "Button" -> check for "Tail.Blazor.Button"
                        if not enum_found:
                            # Try to extract component name from enum name
                            for using_ns in using_directives:
                                if 'Tail.Blazor' in using_ns:
                                    # Get the component name from namespace (last part)
                                    ns_parts = using_ns.split('.')
                                    if len(ns_parts) >= 3:
                                        component_name = ns_parts[-1]  # e.g., "Button" from "Tail.Blazor.Button"
                                        # Check if enum name starts with this component name
                                        if enum_name.startswith(component_name):
                                            enum_to_namespace_map[enum_name] = using_ns
                                            enum_found = True
                                            break
                        
                        # Strategy 4: Default to component namespace if still not found
                        if not enum_found:
                            enum_to_namespace_map[enum_name] = namespace
            
            # Replace all enum references with fully qualified names
            for enum_name, enum_ns in enum_to_namespace_map.items():
                # Pattern: EnumName.Value -> Namespace.EnumName.Value
                # Match enum references that are NOT already fully qualified
                pattern = rf'(?<!\.)\b{enum_name}\.'
                qualified_pattern = f'{enum_ns}.{enum_name}.'
                # Only replace if not already qualified with this namespace
                if re.search(pattern, markup):
                    # Check if already has this namespace prefix
                    if qualified_pattern not in markup:
                        # Check if it has a different namespace (don't replace those)
                        if f'.{enum_name}.' not in markup:
                            markup = re.sub(pattern, qualified_pattern, markup)
            
            # Also fix any remaining unqualified enum patterns using dynamic detection
            enum_pattern = r'(?<!\.)\b([A-Z][a-zA-Z]*(?:Size|Variant|Type|Position|Placement|Style|State|Level|Mode|Direction|Alignment|Orientation|Theme|Shape))\.([A-Z][a-zA-Z0-9]*)'
            def qualify_enum(match):
                enum_type = match.group(1)
                enum_value = match.group(2)
                # Use the map if available (from parameter analysis)
                if enum_type in enum_to_namespace_map:
                    return f'{enum_to_namespace_map[enum_type]}.{enum_type}.{enum_value}'
                
                # Dynamic fallback: check using directives for enum namespace
                for using_ns in using_directives:
                    if 'Tail.Blazor' in using_ns:
                        # Extract component name from namespace (e.g., "Button" from "Tail.Blazor.Button")
                        ns_parts = using_ns.split('.')
                        if len(ns_parts) >= 3:
                            component_name = ns_parts[-1]
                            # Check if enum type starts with or contains this component name
                            if enum_type.startswith(component_name) or component_name in enum_type:
                                return f'{using_ns}.{enum_type}.{enum_value}'
                
                # Final fallback to component namespace
                return f'{namespace}.{enum_type}.{enum_value}'
            
            markup = re.sub(enum_pattern, qualify_enum, markup)
        
        # Clean up whitespace
        markup = re.sub(r'\n\s*\n\s*\n+', '\n\n', markup)
        markup = markup.strip()
        
        return markup if markup else None

    def safe_example(name):
        value = examples.get(name, "")
        if not value:
            return '<div style="color: var(--color-text-secondary); padding: 24px; text-align: center;">Preview not available.</div>'
        
        # Clean up PreviewUI content - remove @code blocks and event handlers
        # Remove @code blocks (including multiline) - be very aggressive
        value = re.sub(r'@code\s*\{[^}]*\}', '', value, flags=re.DOTALL)
        value = re.sub(r'\n\s*@code\s*\{.*?\n\s*\}', '', value, flags=re.DOTALL)
        value = re.sub(r'@code.*?\{.*?\}', '', value, flags=re.DOTALL)
        
        # Remove all event handler attributes (OnClick, OnValueChanged, @bind-Value, etc.)
        # Match any attribute that starts with On or @ - be very aggressive
        value = re.sub(r'\s+On[A-Z]\w+="[^"]*"', '', value)
        value = re.sub(r'\s+On\w+="[^"]*"', '', value)
        value = re.sub(r'\s+@[a-zA-Z-]+="[^"]*"', '', value)
        value = re.sub(r'\s+@bind-\w+="[^"]*"', '', value)
        value = re.sub(r'\s+\w+Changed="[^"]*"', '', value)
        value = re.sub(r'\s+\w+Click="[^"]*"', '', value)
        # Remove any attribute with Handle in the value
        value = re.sub(r'\s+\w+="Handle[^"]*"', '', value)
        value = re.sub(r'\s+\w+="\(\)\s*=>[^"]*"', '', value)
        
        # Remove @page and @using directives for preview
        value = re.sub(r'@page\s+"[^"]*"\s*\n?', '', value)
        value = re.sub(r'@using\s+[^\s]+\s*\n?', '', value)
        
        # Remove empty lines and extra whitespace
        value = re.sub(r'\n\s*\n\s*\n', '\n\n', value)
        
        # Fix enum type references to use fully qualified names
        namespace = component_meta.get('namespace', name)
        # Fix common enum patterns - replace unqualified enum types with qualified ones
        # But only if the enum type matches the component's namespace
        # For now, just remove enum values from preview to avoid type conflicts
        # Or use the component's namespace
        if namespace and namespace != name:
            # Replace common enum patterns with qualified names
            enum_types = ['ButtonSize', 'ButtonVariant', 'Size', 'Variant']
            for enum_type in enum_types:
                # Only replace if it's not already qualified and matches component namespace pattern
                pattern = rf'\b{enum_type}\.'
                if pattern in value and f'{namespace}.{enum_type}' not in value:
                    # Check if this component has this enum
                    component_enums = component_meta.get('enums', {})
                    if enum_type in component_enums or any(enum_type in k for k in component_enums.keys()):
                        value = re.sub(pattern, f'{namespace}.{enum_type}.', value)
        
        return value.strip()
    
    # Build page header
    doc_page = f'@page "/components/{category.lower()}/{friendly_name.lower()}"\n'
    
    # Add @using directive only if not generic and not missing
    if not is_generic and not is_missing:
        doc_page += f'@using {name}\n'
    
    doc_page += '@using Tail.Blazor.Docs.Shared\n'
    doc_page += '@using Tail.Blazor.Tabs\n\n'
    
    doc_page += f'''<DocPageTemplate Title="{friendly_name}"
                 Description="{friendly_name} component for Tail.Blazor"
                 PackageName="{name}"
                 ApiParameters="@apiParameters">
    
    <DocSection Title="Installation">
        <CodePreview Code="@installCode" CodeElementId="install-code" />
    </DocSection>
'''
    
    # Add Features section if available
    if features:
        doc_page += '''    <DocSection Title="Features">
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--color-text-primary);">
'''
        for feature in features:
            # Escape any HTML in features
            feature_escaped = feature.replace('<', '&lt;').replace('>', '&gt;')
            doc_page += f'            <li>{feature_escaped}</li>\n'
        doc_page += '''        </ul>
    </DocSection>
'''
    
    # Add Package Info section if available
    if package_size:
        doc_page += f'''    <DocSection Title="Package Information">
        <div style="background-color: var(--color-surface-2); padding: 16px; border-radius: 8px; color: var(--color-text-primary);">
            <p><strong>Size:</strong> {package_size}</p>
        </div>
    </DocSection>
'''
    
    doc_page += '''    <DocSection Title="Basic Usage">
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
        basic_preview_markup = get_preview_markup("basic")
        if not basic_preview_markup:
            # Fallback: create a simple component instance
            basic_preview_markup = f"<{component_tag}>Content</{component_tag}>"
        
        doc_page += f'''        <TailTabs ActiveIndex="0">
            <Items>
                <TailTabItem Label="Preview" />
                <TailTabItem Label="Code" />
            </Items>
            <Content>
                <TailTabPanel>
                    <PreviewUI>
{textwrap.indent(basic_preview_markup, ' ' * 24)}
                    </PreviewUI>
                </TailTabPanel>
                <TailTabPanel>
                    <CodePreview Code="@basicCode" CodeElementId="basic-code" />
                </TailTabPanel>
            </Content>
        </TailTabs>
'''
    
    doc_page += '    </DocSection>\n'
    
    # Add Quick Start section if available
    if 'quickstart' in examples and not is_generic and not is_missing:
        quickstart_preview = get_preview_markup("quickstart")
        if not quickstart_preview:
            quickstart_preview = f"<{component_tag}>Hello, World!</{component_tag}>"
        
        doc_page += '''
    <DocSection Title="Quick Start">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Get up and running in seconds.
        </p>
        <TailTabs ActiveIndex="0">
            <Items>
                <TailTabItem Label="Preview" />
                <TailTabItem Label="Code" />
            </Items>
            <Content>
                <TailTabPanel>
                    <PreviewUI>
''' + textwrap.indent(quickstart_preview, ' ' * 24) + '''
                    </PreviewUI>
                </TailTabPanel>
                <TailTabPanel>
                    <CodePreview Code="@quickstartCode" CodeElementId="quickstart-code" />
                </TailTabPanel>
            </Content>
        </TailTabs>
    </DocSection>
'''
    
    # Add Common Patterns section if available
    if 'patterns' in examples and not is_generic and not is_missing:
        doc_page += '''
    <DocSection Title="Common Patterns">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Frequently used patterns and combinations.
        </p>
        <CodePreview Code="@patternsCode" CodeElementId="patterns-code" />
    </DocSection>
'''
    
    # Add feature sections
    if 'variants' in examples and not is_generic and not is_missing:
        doc_page += '''
    <DocSection Title="Variants">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Different visual variants for various use cases.
        </p>
        <TailTabs ActiveIndex="0">
            <Items>
                <TailTabItem Label="Preview" />
                <TailTabItem Label="Code" />
            </Items>
            <Content>
                <TailTabPanel>
                    <PreviewUI>
''' + textwrap.indent(get_preview_markup("variants") or _generate_fallback_variants(component_tag, namespace, params, enums), ' ' * 20) + '''
                    </PreviewUI>
                </TailTabPanel>
                <TailTabPanel>
                    <CodePreview Code="@variantsCode" CodeElementId="variants-code" />
                </TailTabPanel>
            </Content>
        </TailTabs>
    </DocSection>
'''
    
    if 'sizes' in examples and not is_generic and not is_missing:
        doc_page += '''
    <DocSection Title="Sizes">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Size options to fit different layouts and contexts.
        </p>
        <TailTabs ActiveIndex="0">
            <Items>
                <TailTabItem Label="Preview" />
                <TailTabItem Label="Code" />
            </Items>
            <Content>
                <TailTabPanel>
                    <PreviewUI>
''' + textwrap.indent(get_preview_markup("sizes") or _generate_fallback_sizes(component_tag, namespace, params, enums), ' ' * 20) + '''
                    </PreviewUI>
                </TailTabPanel>
                <TailTabPanel>
                    <CodePreview Code="@sizesCode" CodeElementId="sizes-code" />
                </TailTabPanel>
            </Content>
        </TailTabs>
    </DocSection>
'''
    
    # Add States section if available
    if 'states' in examples and not is_generic and not is_missing:
        states_preview = get_preview_markup("states")
        if not states_preview:
            states_preview = f"<{component_tag} Disabled=\"true\">Disabled</{component_tag}>"
        
        doc_page += '''
    <DocSection Title="States">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Component states for different interaction scenarios.
        </p>
        <TailTabs ActiveIndex="0">
            <Items>
                <TailTabItem Label="Preview" />
                <TailTabItem Label="Code" />
            </Items>
            <Content>
                <TailTabPanel>
                    <PreviewUI>
''' + textwrap.indent(states_preview, ' ' * 20) + '''
                    </PreviewUI>
                </TailTabPanel>
                <TailTabPanel>
                    <CodePreview Code="@statesCode" CodeElementId="states-code" />
                </TailTabPanel>
            </Content>
        </TailTabs>
    </DocSection>
'''
    
    # Add Event Handling section if available
    if 'events' in examples and not is_generic and not is_missing:
        events_preview = get_preview_markup("events")
        if not events_preview:
            # Fallback: just show component without any attributes
            events_preview = f"<{component_tag}>Click Me</{component_tag}>"
        
        doc_page += '''
    <DocSection Title="Event Handling">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Handle user interactions with event callbacks.
        </p>
        <TailTabs ActiveIndex="0">
            <Items>
                <TailTabItem Label="Preview" />
                <TailTabItem Label="Code" />
            </Items>
            <Content>
                <TailTabPanel>
                    <PreviewUI>
''' + textwrap.indent(events_preview, ' ' * 20) + '''
                    </PreviewUI>
                </TailTabPanel>
                <TailTabPanel>
                    <CodePreview Code="@eventsCode" CodeElementId="events-code" />
                </TailTabPanel>
            </Content>
        </TailTabs>
    </DocSection>
'''
    
    # Add Parameter Combinations section if available
    if 'combinations' in examples and not is_generic and not is_missing:
        doc_page += '''
    <DocSection Title="Parameter Combinations">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            Combine multiple parameters for advanced usage.
        </p>
        <CodePreview Code="@combinationsCode" CodeElementId="combinations-code" />
    </DocSection>
'''
    
    # Add Advanced Examples section if available
    if 'advanced' in examples and not is_generic and not is_missing:
        doc_page += '''
    <DocSection Title="Advanced Examples">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            More complex usage scenarios.
        </p>
        <CodePreview Code="@advancedCode" CodeElementId="advanced-code" />
    </DocSection>
'''
    
    # Add Real-World Example section if available
    if 'realworld' in examples and not is_generic and not is_missing:
        doc_page += '''
    <DocSection Title="Real-World Example">
        <p class="mb-4" style="color: var(--color-text-secondary);">
            A complete example showing practical usage.
        </p>
        <CodePreview Code="@realworldCode" CodeElementId="realworld-code" />
    </DocSection>
'''
    
    # Add API Reference sections before closing DocPageTemplate
    if params or component_meta.get('events') or component_meta.get('properties') or component_meta.get('methods') or type_params or classes:
        doc_page += '''
    <DocSection Title="API Reference">
        <!-- Parameters/Properties Table -->
'''
        if type_params:
            doc_page += '''        <div class="mb-6">
            <h3 class="text-lg font-semibold mb-3" style="color: var(--color-text-primary);">Type Parameters</h3>
            <div class="overflow-x-auto">
                <table style="width: 100%; border-collapse: collapse; color: var(--color-text-primary);">
                    <thead style="background-color: var(--color-surface-2);">
                        <tr>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Name</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Description</th>
                        </tr>
                    </thead>
                    <tbody>
'''
            for tparam in type_params:
                doc_page += f'''                        <tr>
                            <td style="padding: 10px; border: 1px solid var(--color-border);"><code>{tparam}</code></td>
                            <td style="padding: 10px; border: 1px solid var(--color-border);">Generic type parameter for typed data</td>
                        </tr>
'''
            doc_page += '''                    </tbody>
                </table>
            </div>
        </div>
'''

        if classes:
            doc_page += '''        <div class="mb-6">
            <h3 class="text-lg font-semibold mb-3" style="color: var(--color-text-primary);">Class</h3>
            <div class="overflow-x-auto">
                <table style="width: 100%; border-collapse: collapse; color: var(--color-text-primary);">
                    <thead style="background-color: var(--color-surface-2);">
                        <tr>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Class</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Base Type</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Description</th>
                        </tr>
                    </thead>
                    <tbody>
'''
            for cls in classes:
                base_type = (cls.get("base_type") or "-").replace('<', '&lt;').replace('>', '&gt;')
                doc_page += f'''                        <tr>
                            <td style="padding: 10px; border: 1px solid var(--color-border);"><code>{cls.get("name", "")}</code></td>
                            <td style="padding: 10px; border: 1px solid var(--color-border);"><code>{base_type}</code></td>
                            <td style="padding: 10px; border: 1px solid var(--color-border);">Component backing class</td>
                        </tr>
'''
            doc_page += '''                    </tbody>
                </table>
            </div>
        </div>
'''
        if params:
            doc_page += '''        <div class="mb-6">
            <h3 class="text-lg font-semibold mb-3" style="color: var(--color-text-primary);">Properties</h3>
            <div class="overflow-x-auto">
                <table style="width: 100%; border-collapse: collapse; color: var(--color-text-primary);">
                    <thead style="background-color: var(--color-surface-2);">
                        <tr>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Name</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Type</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Default</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Description</th>
                        </tr>
                    </thead>
                    <tbody>
'''
            for param in params:
                default_val = param.get('default', '-') or '-'
                if default_val == '""' or default_val == "''":
                    default_val = '-'
                # Escape angle brackets in type names to avoid Razor parsing issues
                param_type = param["type"].replace('<', '&lt;').replace('>', '&gt;')
                doc_page += f'''                        <tr>
                            <td style="padding: 10px; border: 1px solid var(--color-border);"><code>{param["name"]}</code></td>
                            <td style="padding: 10px; border: 1px solid var(--color-border);"><code>{param_type}</code></td>
                            <td style="padding: 10px; border: 1px solid var(--color-border);">{default_val}</td>
                            <td style="padding: 10px; border: 1px solid var(--color-border);">{param["description"]}</td>
                        </tr>
'''
            doc_page += '''                    </tbody>
                </table>
            </div>
        </div>
'''
        
        # Events section
        events = component_meta.get('events', [])
        if events:
            doc_page += '''        <div class="mb-6">
            <h3 class="text-lg font-semibold mb-3" style="color: var(--color-text-primary);">Events</h3>
            <div class="overflow-x-auto">
                <table style="width: 100%; border-collapse: collapse; color: var(--color-text-primary);">
                    <thead style="background-color: var(--color-surface-2);">
                        <tr>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Event</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Type</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Description</th>
                        </tr>
                    </thead>
                    <tbody>
'''
            for event in events:
                event_type = event["type"].replace('<', '&lt;').replace('>', '&gt;')
                doc_page += f'''                        <tr>
                            <td style="padding: 10px; border: 1px solid var(--color-border);"><code>{event["name"]}</code></td>
                            <td style="padding: 10px; border: 1px solid var(--color-border);"><code>{event_type}</code></td>
                            <td style="padding: 10px; border: 1px solid var(--color-border);">{event["description"]}</td>
                        </tr>
'''
            doc_page += '''                    </tbody>
                </table>
            </div>
        </div>
'''
        
        # Properties section
        properties = component_meta.get('properties', [])
        if properties:
            doc_page += '''        <div class="mb-6">
            <h3 class="text-lg font-semibold mb-3" style="color: var(--color-text-primary);">Public Properties</h3>
            <div class="overflow-x-auto">
                <table style="width: 100%; border-collapse: collapse; color: var(--color-text-primary);">
                    <thead style="background-color: var(--color-surface-2);">
                        <tr>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Property</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Type</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Description</th>
                        </tr>
                    </thead>
                    <tbody>
'''
            for prop in properties:
                prop_type = prop["type"].replace('<', '&lt;').replace('>', '&gt;')
                doc_page += f'''                        <tr>
                            <td style="padding: 10px; border: 1px solid var(--color-border);"><code>{prop["name"]}</code></td>
                            <td style="padding: 10px; border: 1px solid var(--color-border);"><code>{prop_type}</code></td>
                            <td style="padding: 10px; border: 1px solid var(--color-border);">{prop["description"]}</td>
                        </tr>
'''
            doc_page += '''                    </tbody>
                </table>
            </div>
        </div>
'''
        
        # Methods section
        methods = component_meta.get('methods', [])
        if methods:
            doc_page += '''        <div class="mb-6">
            <h3 class="text-lg font-semibold mb-3" style="color: var(--color-text-primary);">Public Methods</h3>
            <div class="overflow-x-auto">
                <table style="width: 100%; border-collapse: collapse; color: var(--color-text-primary);">
                    <thead style="background-color: var(--color-surface-2);">
                        <tr>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Method</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Parameters</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--color-border);">Description</th>
                        </tr>
                    </thead>
                    <tbody>
'''
            for method in methods:
                params_str = ', '.join([f"{p['name']}: {p['type']}" for p in method.get('parameters', [])])
                params_str = params_str.replace('<', '&lt;').replace('>', '&gt;')
                if not params_str:
                    params_str = 'None'
                doc_page += f'''                        <tr>
                            <td style="padding: 10px; border: 1px solid var(--color-border);"><code>{method["name"]}()</code></td>
                            <td style="padding: 10px; border: 1px solid var(--color-border);"><code>{params_str}</code></td>
                            <td style="padding: 10px; border: 1px solid var(--color-border);">{method["description"]}</td>
                        </tr>
'''
            doc_page += '''                    </tbody>
                </table>
            </div>
        </div>
'''
        doc_page += '    </DocSection>\n'
    
    # Close DocPageTemplate BEFORE adding @code section
    doc_page += '</DocPageTemplate>\n\n@code {\n'
    
    # Add code variables
    doc_page += f'    private bool isGeneric = {str(is_generic).lower()};\n'
    doc_page += f'    private bool isMissing = {str(is_missing).lower()};\n\n'
    
    # Installation code
    doc_page += f'    private string installCode = "dotnet add package {name}";\n\n'
    
    # Basic example codes
    basic_code = escape_razor_code(examples.get("basic", ""))
    doc_page += f'    private string basicCode = @"{basic_code}";\n\n'
    
    # Variants
    if 'variants' in examples:
        variants_escaped = escape_razor_code(examples["variants"])
        doc_page += f'    private string variantsCode = @"\n{variants_escaped}\n";\n\n'
    
    # Sizes
    if 'sizes' in examples:
        sizes_escaped = escape_razor_code(examples["sizes"])
        doc_page += f'    private string sizesCode = @"\n{sizes_escaped}\n";\n\n'
    
    # States - only code for Code tab
    if 'states' in examples:
        states_escaped = escape_razor_code(examples["states"])
        doc_page += f'    private string statesCode = @"\n{states_escaped}\n";\n\n'
    else:
        doc_page += '    private string statesCode = @"\n<TailComponent Disabled=""true"">Disabled</TailComponent>\n";\n\n'
    
    # Quick Start
    if 'quickstart' in examples:
        quickstart_escaped = escape_razor_code(examples["quickstart"])
        doc_page += f'    private string quickstartCode = @"\n{quickstart_escaped}\n";\n\n'
    
    # Patterns
    if 'patterns' in examples:
        patterns_escaped = escape_razor_code(examples["patterns"])
        doc_page += f'    private string patternsCode = @"\n{patterns_escaped}\n";\n\n'
    
    # Events - fix custom types to use fully qualified names
    if 'events' in examples:
        events_code = examples["events"]
        # Replace custom types with fully qualified names
        namespace = component_meta.get('namespace', name)
        # List of custom types that need qualification
        custom_types = ['FilterCriteria', 'NotificationItem', 'ContextMenuItem', 
                       'FloatingActionMenuItem', 'MenuItemClickArgs', 'ScrollSpyItem']
        for custom_type in custom_types:
            # Replace unqualified type references with fully qualified ones
            pattern = rf'\b{custom_type}\b'
            if re.search(pattern, events_code) and f'{namespace}.{custom_type}' not in events_code:
                events_code = re.sub(pattern, f'{namespace}.{custom_type}', events_code)
        
        events_escaped = escape_razor_code(events_code)
        doc_page += f'    private string eventsCode = @"\n{events_escaped}\n";\n\n'
    
    # Combinations
    if 'combinations' in examples:
        combinations_escaped = escape_razor_code(examples["combinations"])
        doc_page += f'    private string combinationsCode = @"\n{combinations_escaped}\n";\n\n'
    
    # Advanced
    if 'advanced' in examples:
        advanced_escaped = escape_razor_code(examples["advanced"])
        doc_page += f'    private string advancedCode = @"\n{advanced_escaped}\n";\n\n'
    
    # Real-World
    if 'realworld' in examples:
        realworld_escaped = escape_razor_code(examples["realworld"])
        doc_page += f'    private string realworldCode = @"\n{realworld_escaped}\n";\n\n'
    
    # API parameters (keep for backward compatibility)
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
               style="background-color: var(--color-primary); color: var(--color-text-on-primary);">
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
            status_badge = '<span class="text-xs px-2 py-1 rounded" style="background-color: var(--color-warning); color: var(--color-text-on-primary);">Generic</span>'
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
    
    # Phase 3: Generate/refresh README files from metadata
    print("\n[3/6] Generating component README files...")
    print("-" * 70)
    readmes_created = 0
    for category, cat_data in all_metadata.items():
        for comp_name, comp_meta in cat_data["components"].items():
            if comp_meta.get("is_missing"):
                continue
            generate_component_readme(comp_meta)
            # Refresh metadata from newly written README
            readme_info = extract_readme_content(comp_meta["path"])
            comp_meta["features"] = readme_info.get("features", comp_meta.get("features", []))
            comp_meta["package_size"] = readme_info.get("package_size", comp_meta.get("package_size", ""))
            comp_meta["example_code"] = readme_info.get("example_code", comp_meta.get("example_code", ""))
            comp_meta["readme_examples"] = readme_info.get("examples", {})
            comp_meta["namespace"] = readme_info.get("namespace", comp_meta.get("namespace", ""))
            if readme_info.get("description"):
                comp_meta["description"] = readme_info["description"]
            readmes_created += 1
    print(f"  [OK] Generated/updated {readmes_created} README.md files")
    
    # Phase 4: Generate Documentation Pages
    print("\n[4/6] Generating documentation pages...")
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
    
    # Phase 5: Generate Overview Pages
    print("\n[5/6] Generating overview pages...")
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
    
    # Phase 6: Generate Navigation
    print("\n[6/6] Generating navigation menu...")
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
    print(f"  ✓ READMEs: {readmes_created}")
    print(f"  ✓ Component Pages: {pages_created}")
    print(f"  ✓ Global Overview: 1")
    print(f"  ✓ Category Overviews: {category_overviews}")
    print(f"  ✓ Navigation: NavMenu.json")
    print(f"  ✓ Location: {docs_base}")
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    main()
