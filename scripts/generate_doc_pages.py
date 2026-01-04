#!/usr/bin/env python3
"""
Generates documentation page templates for all Tail.Blazor components
"""

import os
import json
from pathlib import Path
from datetime import datetime

COMPONENTS_PATH = Path(r"d:\Users\AMAR\source\repos\Tail\src\components")
DOCS_PATH = Path(r"d:\Users\AMAR\source\repos\Tail\docs\Tail.Blazor.Docs\Pages")
COMPONENTS_DOCS_PATH = DOCS_PATH / "Components"

CATEGORIES = {
    "buttons": {"folder": "Buttons", "displayName": "Buttons"},
    "charts": {"folder": "Charts", "displayName": "Charts"},
    "core": {"folder": "Core", "displayName": "Core"},
    "data": {"folder": "Data", "displayName": "Data"},
    "feedback": {"folder": "Feedback", "displayName": "Feedback"},
    "forms": {"folder": "Forms", "displayName": "Forms"},
    "icons": {"folder": "Icons", "displayName": "Icons"},
    "layout": {"folder": "Layout", "displayName": "Layout"},
    "navigation": {"folder": "Navigation", "displayName": "Navigation"},
    "utils": {"folder": "Utils", "displayName": "Utilities"},
    "validators": {"folder": "Validators", "displayName": "Validators"},
    "visualization": {"folder": "Visualization", "displayName": "Visualization"},
}

DOC_TEMPLATE = '''@page "/components/{category}/{component_url}"
@using Tail.Blazor.Docs.Shared

<PageTitle>{component_name} - Tail.Blazor</PageTitle>

<div class="container mx-auto px-4 py-12">
    <div class="mb-8">
        <a href="/components/{category}" class="text-blue-600 hover:text-blue-700 text-sm font-medium">&larr; {category_display}</a>
        <h1 class="text-4xl font-bold mt-2">{component_name}</h1>
        <p class="text-gray-600 text-lg mt-2">A Tail.Blazor component for {component_description}</p>
    </div>

    <!-- Installation -->
    <section class="mb-12">
        <h2 class="text-2xl font-bold mb-4">Installation</h2>
        <div class="bg-gray-50 p-4 rounded-lg border border-gray-200">
            <p class="text-sm font-mono text-gray-800">
                dotnet add package {component_name}
            </p>
        </div>
    </section>

    <!-- Basic Usage -->
    <section class="mb-12">
        <h2 class="text-2xl font-bold mb-4">Basic Usage</h2>
        <p class="text-gray-700 mb-4">
            Add a brief description of the basic usage pattern here.
        </p>
        <div class="border rounded-lg p-6 bg-gradient-to-br from-blue-50 to-indigo-50">
            <!-- Add example using actual Tail.Blazor components -->
            <p class="text-gray-700">Example code will appear here</p>
        </div>
    </section>

    <!-- Properties/Parameters -->
    <section class="mb-12">
        <h2 class="text-2xl font-bold mb-4">Properties</h2>
        <div class="overflow-x-auto">
            <table class="min-w-full border-collapse">
                <thead class="bg-gray-100">
                    <tr>
                        <th class="border border-gray-300 px-4 py-2 text-left font-semibold">Property</th>
                        <th class="border border-gray-300 px-4 py-2 text-left font-semibold">Type</th>
                        <th class="border border-gray-300 px-4 py-2 text-left font-semibold">Default</th>
                        <th class="border border-gray-300 px-4 py-2 text-left font-semibold">Description</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="border border-gray-300 px-4 py-2">Property</td>
                        <td class="border border-gray-300 px-4 py-2"><code class="bg-gray-100 px-2 py-1 rounded">string</code></td>
                        <td class="border border-gray-300 px-4 py-2">-</td>
                        <td class="border border-gray-300 px-4 py-2">Description</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- Events -->
    <section class="mb-12">
        <h2 class="text-2xl font-bold mb-4">Events</h2>
        <p class="text-gray-700 mb-4">
            Add event callback documentation here.
        </p>
    </section>

    <!-- Examples -->
    <section class="mb-12">
        <h2 class="text-2xl font-bold mb-4">Examples</h2>
        <div class="space-y-6">
            <div class="border rounded-lg overflow-hidden">
                <div class="bg-gray-100 px-4 py-2 font-semibold">Example 1: Basic</div>
                <div class="p-6 bg-white">
                    <p class="text-gray-700">Add example code here</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Related Components -->
    <section class="mb-12">
        <h2 class="text-2xl font-bold mb-4">Related Components</h2>
        <ul class="space-y-2">
            <li><a href="#" class="text-blue-600 hover:underline">Component Link 1</a></li>
            <li><a href="#" class="text-blue-600 hover:underline">Component Link 2</a></li>
        </ul>
    </section>

</div>

@code {{
    // Component logic here if needed
}}
'''

def discover_components():
    """Discover all components"""
    all_components = {}
    
    for category in CATEGORIES.keys():
        category_path = COMPONENTS_PATH / category
        if not category_path.exists():
            continue
        
        all_components[category] = []
        
        for project_dir in category_path.iterdir():
            if project_dir.is_dir() and project_dir.name not in ['Tail.Blazor.Core.Base', 'Tail.Blazor.Core.Theme']:
                csproj_files = list(project_dir.glob("*.csproj"))
                if csproj_files:
                    all_components[category].append(project_dir.name)
    
    return all_components

def generate_doc_pages(all_components):
    """Generate documentation pages for all components"""
    total = 0
    created = 0
    
    print("\n" + "="*70)
    print("GENERATING DOCUMENTATION PAGES")
    print("="*70 + "\n")
    
    for category_key in sorted(CATEGORIES.keys()):
        if category_key not in all_components or not all_components[category_key]:
            continue
        
        category_display = CATEGORIES[category_key]["displayName"]
        category_folder = CATEGORIES[category_key]["folder"]
        
        docs_category_path = COMPONENTS_DOCS_PATH / category_folder
        docs_category_path.mkdir(parents=True, exist_ok=True)
        
        print(f"\n{category_display}:")
        
        for component_name in sorted(all_components[category_key]):
            component_url = component_name.lower().replace("tail.blazor.", "")
            doc_file = docs_category_path / f"{component_name}.razor"
            
            # Generate content
            component_description = component_name.replace("Tail.Blazor.", "").replace(".", " ").lower()
            content = DOC_TEMPLATE.format(
                category=category_key,
                component_url=component_url,
                component_name=component_name,
                category_display=category_display,
                component_description=component_description
            )
            
            total += 1
            
            # Write file
            doc_file.write_text(content, encoding='utf-8')
            created += 1
            
            print(f"  ✓ {component_name}.razor")
    
    print(f"\n{'='*70}")
    print(f"Created {created} documentation pages")
    print(f"{'='*70}\n")

def generate_category_overview_pages(all_components):
    """Generate category overview pages"""
    print("GENERATING CATEGORY OVERVIEW PAGES\n")
    
    for category_key in sorted(CATEGORIES.keys()):
        if category_key not in all_components or not all_components[category_key]:
            continue
        
        category_display = CATEGORIES[category_key]["displayName"]
        category_folder = CATEGORIES[category_key]["folder"]
        components = sorted(all_components[category_key])
        
        # Generate component list HTML
        components_html = "\n".join([
            f'''            <a href="/components/{category_key}/{comp.lower().replace('tail.blazor.', '')}" class="block p-4 border rounded-lg hover:shadow-lg hover:border-blue-400 transition">
                <h3 class="font-bold text-lg">{comp}</h3>
                <p class="text-gray-600 text-sm">Click to view documentation</p>
            </a>'''
            for comp in components
        ])
        
        category_overview = f'''@page "/components/{category_key}"

<PageTitle>{category_display} Components - Tail.Blazor</PageTitle>

<div class="container mx-auto px-4 py-12">
    <div class="mb-8">
        <a href="/components" class="text-blue-600 hover:text-blue-700 text-sm font-medium">&larr; All Components</a>
        <h1 class="text-4xl font-bold mt-2">{category_display} Components</h1>
        <p class="text-gray-600 text-lg mt-2">A collection of {len(components)} {category_display.lower()} components for Tail.Blazor.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
{components_html}
    </div>
</div>

@code {{
    // Category page logic here
}}
'''
        
        overview_file = COMPONENTS_DOCS_PATH / category_folder / "_Overview.razor"
        overview_file.write_text(category_overview, encoding='utf-8')
        
        print(f"  ✓ {category_folder}/_Overview.razor")

def main():
    print("\n" + "="*70)
    print("TAIL.BLAZOR DOCUMENTATION GENERATOR")
    print("="*70)
    
    # Discover components
    print("\n[1/3] Discovering components...")
    all_components = discover_components()
    
    total_components = sum(len(comps) for comps in all_components.values())
    print(f"✓ Found {total_components} components")
    
    # Generate documentation pages
    print("\n[2/3] Generating documentation pages...")
    generate_doc_pages(all_components)
    
    # Generate category overview pages
    print("[3/3] Generating category overview pages...")
    generate_category_overview_pages(all_components)
    
    print("\n" + "="*70)
    print("COMPLETED SUCCESSFULLY!")
    print("="*70)
    print("\nNext steps:")
    print("1. Review generated documentation pages")
    print("2. Add component-specific examples and descriptions")
    print("3. Link related components")
    print("4. Test all documentation links")
    print("\n")

if __name__ == "__main__":
    main()
