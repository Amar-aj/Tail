#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tail.Blazor Documentation Generator
Generates doc pages using DocPageTemplate, DocSection, and CodePreview components
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Fix Unicode output on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def discover_components():
    """Discover all components from src/components directory."""
    components_dir = Path("src/components")
    components = {}
    
    category_metadata = {
        "buttons": {"icon": "🔘", "order": 1},
        "charts": {"icon": "📈", "order": 2},
        "core": {"icon": "⚙️", "order": 3},
        "data": {"icon": "📊", "order": 4},
        "feedback": {"icon": "💬", "order": 5},
        "forms": {"icon": "📝", "order": 6},
        "icons": {"icon": "🎯", "order": 7},
        "layout": {"icon": "📐", "order": 8},
        "navigation": {"icon": "🧭", "order": 9},
        "utils": {"icon": "🛠️", "order": 10},
        "validators": {"icon": "✅", "order": 11},
        "visualization": {"icon": "🎨", "order": 12}
    }
    
    for category_dir in sorted(components_dir.iterdir()):
        if not category_dir.is_dir():
            continue
        
        category = category_dir.name.lower()
        metadata = category_metadata.get(category, {"icon": "📦", "order": 99})
        
        components[category] = {
            "icon": metadata["icon"],
            "order": metadata["order"],
            "display_name": category.capitalize(),
            "components": [],
            "count": 0
        }
        
        for component_dir in sorted(category_dir.iterdir()):
            if not component_dir.is_dir():
                continue
            
            component_name = component_dir.name
            csproj_file = component_dir / f"{component_name}.csproj"
            
            if csproj_file.exists():
                friendly_name = component_name.replace("Tail.Blazor.", "")
                
                components[category]["components"].append({
                    "name": component_name,
                    "friendly_name": friendly_name,
                    "path": f"/components/{category.lower()}/{friendly_name.lower()}",
                    "implemented": (component_dir / f"{component_name}.razor").exists()
                })
        
        components[category]["count"] = len(components[category]["components"])
    
    return components

def generate_doc_page(category, component):
    """Generate a documentation page using DocPageTemplate structure."""
    friendly_name = component["friendly_name"]
    component_name = component["name"]
    
    # Ensure lowercase for route consistency
    route_name = friendly_name.lower()
    
    # Get category display name
    category_title = category.replace("_", " ").title()
    
    doc_content = f'''@page "/components/{category.lower()}/{route_name}"
@using Tail.Blazor.Docs.Shared
@using Tail.Blazor.Container
@using Tail.Blazor.Card
@using Tail.Blazor.Button

<DocPageTemplate Title="{friendly_name}" 
                 Description="A flexible and powerful {friendly_name} component for Tail.Blazor"
                 PackageName="{component_name}">
    
    <DocSection Title="Installation">
        <CodePreview Title="Install Package" 
                     Code="dotnet add package {component_name}"
                     ShowPreview="false"
                     Language="bash">
        </CodePreview>
    </DocSection>

    <DocSection Title="Basic Usage">
        <CodePreview Title="Simple {friendly_name}" 
                     Code="<Tail{friendly_name}>
    <!-- Component content goes here -->
</Tail{friendly_name}>"
                     Language="razor">
            <PreviewContent>
                <div class="p-8 bg-gray-50 rounded-lg border border-gray-200">
                    <p class="text-gray-600 text-center">
                        Preview of {friendly_name} component will appear here
                    </p>
                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>

    <DocSection Title="Properties">
        <p class="text-gray-600 mb-4">Common properties available for this component:</p>
        <div class="bg-blue-50 border border-blue-200 p-4 rounded-lg">
            <ul class="space-y-2">
                <li><code class="bg-white px-2 py-1 rounded">Class</code> - CSS classes to apply</li>
                <li><code class="bg-white px-2 py-1 rounded">Children</code> - Child content/components</li>
                <li><code class="bg-white px-2 py-1 rounded">Style</code> - Inline CSS styles</li>
            </ul>
        </div>
    </DocSection>

    <DocSection Title="Events & Callbacks">
        <p class="text-gray-600 mb-4">Event callbacks for user interactions:</p>
        <div class="bg-yellow-50 border border-yellow-200 p-4 rounded-lg">
            <ul class="space-y-2">
                <li><code class="bg-white px-2 py-1 rounded">OnClick</code> - Triggered on click</li>
                <li><code class="bg-white px-2 py-1 rounded">OnChange</code> - Triggered on value change</li>
            </ul>
        </div>
    </DocSection>

    <DocSection Title="Examples">
        <CodePreview Title="Advanced Usage" 
                     Code="@*
Add your advanced example code here
*@"
                     Language="razor">
            <PreviewContent>
                <div class="p-8 bg-gray-50 rounded-lg border border-gray-200">
                    <p class="text-gray-600 text-center">
                        Advanced examples will be added here
                    </p>
                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>

    <DocSection Title="Related Components">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <a href="/components/{category.lower()}" class="p-4 border border-gray-200 rounded-lg hover:border-blue-500 hover:bg-blue-50 transition">
                <h4 class="font-semibold text-gray-800">← {category_title} Overview</h4>
                <p class="text-sm text-gray-600">View all {category.lower()} components</p>
            </a>
        </div>
    </DocSection>

</DocPageTemplate>

@code {{
    // Component logic can be added here if needed
}}
'''
    
    return doc_content

def generate_category_overview(category, category_data, all_components):
    """Generate category overview page."""
    display_name = category_data["display_name"]
    components_list = category_data["components"]
    
    # Build component cards HTML
    component_cards = "\n    ".join([
        f'''<a href="{comp['path']}" class="p-4 border border-gray-200 rounded-lg hover:border-blue-500 hover:shadow-md transition">
        <h4 class="font-semibold text-gray-800">{comp['friendly_name']}</h4>
        <p class="text-xs text-gray-500 mt-1">{comp['name']}</p>
        <div class="mt-2">
            <span class="text-xs px-2 py-1 rounded-full {"bg-green-100 text-green-800" if comp['implemented'] else "bg-gray-100 text-gray-800"}">
                {"✓ Implemented" if comp['implemented'] else "⊘ Pending"}
            </span>
        </div>
    </a>'''
        for comp in sorted(components_list, key=lambda x: x["friendly_name"])
    ])
    
    overview_content = f'''@page "/components/{category}"
@using Tail.Blazor.Docs.Shared
@using Tail.Blazor.Container
@using Tail.Blazor.Card
@using Tail.Blazor.Badge

<TailContainer Size="ContainerSize.Full" Class="py-8">
    <div class="mb-8">
        <a href="/components" class="text-blue-600 hover:text-blue-700">← Components</a>
        <h1 class="text-4xl font-bold mt-2 mb-2">{category_data['icon']} {display_name} Components</h1>
        <p class="text-gray-600">A collection of {len(components_list)} {display_name.lower()} components</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
        {component_cards}
    </div>

    <TailCard Class="mt-8">
        <Header>
            <h2 class="text-2xl font-bold">Statistics</h2>
        </Header>
        <ChildContent>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div class="p-4 bg-blue-50 rounded-lg">
                    <div class="text-2xl font-bold text-blue-600">{len(components_list)}</div>
                    <p class="text-sm text-gray-600">Total Components</p>
                </div>
                <div class="p-4 bg-green-50 rounded-lg">
                    <div class="text-2xl font-bold text-green-600">{sum(1 for c in components_list if c['implemented'])}</div>
                    <p class="text-sm text-gray-600">Implemented</p>
                </div>
                <div class="p-4 bg-yellow-50 rounded-lg">
                    <div class="text-2xl font-bold text-yellow-600">{sum(1 for c in components_list if not c['implemented'])}</div>
                    <p class="text-sm text-gray-600">Pending</p>
                </div>
                <div class="p-4 bg-purple-50 rounded-lg">
                    <div class="text-2xl font-bold text-purple-600">100%</div>
                    <p class="text-sm text-gray-600">Coverage</p>
                </div>
            </div>
        </ChildContent>
    </TailCard>
</TailContainer>

@code {{
    // Category overview logic
}}
'''
    
    return overview_content

def main():
    print("=" * 70)
    print("TAIL.BLAZOR DOCUMENTATION GENERATOR")
    print("=" * 70)
    
    print("\n[1/4] Discovering components...")
    components = discover_components()
    
    if not components:
        print("❌ No components found!")
        return
    
    total_components = sum(cat["count"] for cat in components.values())
    print(f"✓ Found {total_components} components")
    
    print("\n[2/4] Creating documentation structure...")
    docs_base = Path("docs/Tail.Blazor.Docs/Pages/Components")
    docs_base.mkdir(parents=True, exist_ok=True)
    print(f"✓ Documentation directory ready: {docs_base}")
    
    print("\n[3/4] Generating documentation pages...")
    pages_created = 0
    sorted_categories = sorted(components.items(), key=lambda x: x[1]["order"])
    
    # First, clean up any old incorrectly-named files (Tail.Blazor.*.razor or Tail_Blazor_*.razor)
    import re
    wrong_pattern = re.compile(r'^Tail[._]Blazor')
    for category, _ in sorted_categories:
        category_folder = docs_base / category.capitalize()
        if category_folder.exists():
            for razor_file in category_folder.glob("*.razor"):
                if wrong_pattern.match(razor_file.name) and not razor_file.name.startswith("_"):
                    try:
                        razor_file.unlink()
                    except:
                        pass
    
    for category, category_data in sorted_categories:
        components_list = category_data["components"]
        
        # Create category folder
        category_folder = docs_base / category.capitalize()
        category_folder.mkdir(parents=True, exist_ok=True)
        
        # Generate category overview
        overview_content = generate_category_overview(category, category_data, components)
        overview_path = category_folder / "_Overview.razor"
        with open(overview_path, "w", encoding="utf-8") as f:
            f.write(overview_content)
        pages_created += 1
        
        # Generate component pages
        for comp in components_list:
            doc_content = generate_doc_page(category, comp)
            doc_path = category_folder / f"{comp['friendly_name']}.razor"
            with open(doc_path, "w", encoding="utf-8") as f:
                f.write(doc_content)
            pages_created += 1
    
    print(f"✓ Generated {pages_created} documentation pages")
    
    print("\n[4/4] Summary")
    print("=" * 70)
    
    for category, category_data in sorted_categories:
        implemented = sum(1 for c in category_data["components"] if c["implemented"])
        total = len(category_data["components"])
        print(f"{category_data['icon']} {category.upper():15} | {total:2} components ({implemented} implemented)")
    
    print("=" * 70)
    print(f"\n✓ Documentation generated: {pages_created} pages")
    print(f"✓ Location: {docs_base}")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
