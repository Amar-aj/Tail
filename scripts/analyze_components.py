#!/usr/bin/env python3
"""
Tail.Blazor Component Documentation Generator
Analyzes all components and generates/updates documentation structure
"""

import os
import json
from pathlib import Path
from datetime import datetime

# Paths
COMPONENTS_PATH = Path(r"d:\Users\AMAR\source\repos\Tail\src\components")
DOCS_PATH = Path(r"d:\Users\AMAR\source\repos\Tail\docs\Tail.Blazor.Docs\Pages")
COMPONENTS_DOCS_PATH = DOCS_PATH / "Components"

# Category definitions
CATEGORIES = {
    "buttons": {"folder": "Buttons", "displayName": "Buttons", "icon": "button"},
    "charts": {"folder": "Charts", "displayName": "Charts", "icon": "chart"},
    "core": {"folder": "Core", "displayName": "Core", "icon": "cog"},
    "data": {"folder": "Data", "displayName": "Data", "icon": "table"},
    "feedback": {"folder": "Feedback", "displayName": "Feedback", "icon": "bell"},
    "forms": {"folder": "Forms", "displayName": "Forms", "icon": "input"},
    "icons": {"folder": "Icons", "displayName": "Icons", "icon": "star"},
    "layout": {"folder": "Layout", "displayName": "Layout", "icon": "layout"},
    "navigation": {"folder": "Navigation", "displayName": "Navigation", "icon": "menu"},
    "utils": {"folder": "Utils", "displayName": "Utilities", "icon": "tool"},
    "validators": {"folder": "Validators", "displayName": "Validators", "icon": "check"},
    "visualization": {"folder": "Visualization", "displayName": "Visualization", "icon": "chart-pie"},
}

def discover_components():
    """Discover all components in the src/components directory"""
    all_components = {}
    components_list = []
    
    for category in CATEGORIES.keys():
        category_path = COMPONENTS_PATH / category
        if not category_path.exists():
            continue
        
        all_components[category] = []
        
        # Find all project directories
        for project_dir in category_path.iterdir():
            if project_dir.is_dir() and project_dir.name not in ['Tail.Blazor.Core.Base', 'Tail.Blazor.Core.Theme']:
                # Check if it has a .csproj file
                csproj_files = list(project_dir.glob("*.csproj"))
                if csproj_files:
                    component_name = project_dir.name
                    all_components[category].append(component_name)
                    components_list.append({
                        "category": category,
                        "componentName": component_name,
                        "componentPath": str(project_dir),
                        "csprojPath": str(csproj_files[0])
                    })
    
    return all_components, components_list

def check_documentation():
    """Check which components have documentation"""
    all_components, components_list = discover_components()
    analysis = []
    
    for component in components_list:
        category = component["category"]
        component_name = component["componentName"]
        component_path = Path(component["componentPath"])
        
        # Expected doc page path
        category_docs_folder = COMPONENTS_DOCS_PATH / CATEGORIES[category]["folder"]
        expected_doc_page = category_docs_folder / f"{component_name}.razor"
        
        # Check if doc exists
        doc_exists = expected_doc_page.exists()
        
        # Check if component has .razor files
        razor_files = list(component_path.glob("*.razor"))
        component_implemented = len(razor_files) > 0
        
        analysis.append({
            "category": category,
            "componentName": component_name,
            "docExists": doc_exists,
            "docPath": str(expected_doc_page),
            "implemented": component_implemented,
            "razorCount": len(razor_files)
        })
    
    return all_components, components_list, analysis

def generate_nav_menu(all_components):
    """Generate navigation menu JSON"""
    nav_menu = {
        "version": "1.0.0",
        "lastUpdated": datetime.now().isoformat(),
        "menu": []
    }
    
    # Main sections
    main_sections = [
        {"label": "Getting Started", "path": "/getting-started", "icon": "rocket"},
        {"label": "Components", "path": "#", "icon": "cube", "isGroup": True},
        {"label": "Theming", "path": "/theming", "icon": "palette"},
        {"label": "API", "path": "/api", "icon": "code"},
        {"label": "FAQ", "path": "/faq", "icon": "question"}
    ]
    
    for section in main_sections:
        menu_item = {
            "label": section["label"],
            "path": section["path"],
            "icon": section["icon"],
            "children": []
        }
        
        # Add component categories as children
        if section["label"] == "Components":
            for category_key in sorted(CATEGORIES.keys()):
                if category_key in all_components and all_components[category_key]:
                    category_item = {
                        "label": CATEGORIES[category_key]["displayName"],
                        "path": f"/components/{category_key}",
                        "icon": CATEGORIES[category_key]["icon"],
                        "children": []
                    }
                    
                    # Add individual components
                    for component in sorted(all_components[category_key]):
                        component_url = component.lower().replace("tail.blazor.", "")
                        component_item = {
                            "label": component,
                            "path": f"/components/{category_key}/{component_url}",
                            "icon": "component"
                        }
                        category_item["children"].append(component_item)
                    
                    menu_item["children"].append(category_item)
        
        nav_menu["menu"].append(menu_item)
    
    return nav_menu

def main():
    print("=" * 70)
    print("TAIL.BLAZOR COMPONENT DOCUMENTATION ANALYZER")
    print("=" * 70)
    
    # Discover components
    print("\n[1/3] Discovering components...")
    all_components, components_list, analysis = check_documentation()
    
    total_components = len(components_list)
    implemented_components = sum(1 for c in analysis if c["implemented"])
    documented_components = sum(1 for c in analysis if c["docExists"])
    missing_docs = sum(1 for c in analysis if not c["docExists"])
    
    print(f"\n✓ Found {total_components} total components")
    print(f"✓ {implemented_components} components implemented")
    print(f"✓ {documented_components} components documented")
    print(f"⚠ {missing_docs} components missing documentation")
    
    # Summary by category
    print("\nComponents by Category:")
    for category_key in sorted(CATEGORIES.keys()):
        if category_key in all_components and all_components[category_key]:
            count = len(all_components[category_key])
            print(f"  {CATEGORIES[category_key]['displayName']}: {count} components")
    
    # Generate navigation menu
    print("\n[2/3] Generating navigation menu...")
    nav_menu = generate_nav_menu(all_components)
    nav_menu_path = COMPONENTS_DOCS_PATH / "NavMenu.json"
    
    with open(nav_menu_path, 'w') as f:
        json.dump(nav_menu, f, indent=2, default=str)
    
    print(f"✓ NavMenu.json created")
    
    # Print missing documentation
    print("\n[3/3] Missing Documentation:")
    missing_by_category = {}
    for item in analysis:
        if not item["docExists"]:
            cat = item["category"]
            if cat not in missing_by_category:
                missing_by_category[cat] = []
            missing_by_category[cat].append(item["componentName"])
    
    if missing_by_category:
        for category_key in sorted(missing_by_category.keys()):
            print(f"\n  {CATEGORIES[category_key]['displayName']}:")
            for component in sorted(missing_by_category[category_key]):
                print(f"    - {component}")
    else:
        print("  ✓ All components are documented!")
    
    # Print report
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total Components: {total_components}")
    print(f"Documented: {documented_components}")
    print(f"Missing Documentation: {missing_docs}")
    print(f"Coverage: {(documented_components/total_components*100):.1f}%")
    print("=" * 70)

if __name__ == "__main__":
    main()
