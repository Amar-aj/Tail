#!/usr/bin/env python3
"""
Tail.Blazor Component Analyzer
Discovers components and generates NavMenu.json with proper hierarchy
"""

import json
from pathlib import Path
from datetime import datetime

def discover_components():
    """Discover all components from src/components directory."""
    components_dir = Path("src/components")
    components = {}
    
    if not components_dir.exists():
        print(f"❌ Components directory not found: {components_dir}")
        return components
    
    # Category metadata: icon, order
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
            
            # Check if .csproj exists
            csproj_file = component_dir / f"{component_name}.csproj"
            if csproj_file.exists():
                # Check for .razor implementation
                razor_file = next(component_dir.glob("*.razor"), None)
                is_implemented = razor_file is not None
                
                # Extract friendly name: "Tail.Blazor.Button" -> "Button"
                friendly_name = component_name.replace("Tail.Blazor.", "")
                
                components[category]["components"].append({
                    "name": component_name,
                    "friendly_name": friendly_name,
                    "path": f"/components/{category.lower()}/{friendly_name.lower()}",
                    "implemented": is_implemented
                })
        
        components[category]["count"] = len(components[category]["components"])
    
    return components

def generate_nav_menu(components):
    """Generate NavMenu.json matching DocsNavMenu.razor structure."""
    nav_menu = {
        "version": "1.0.0",
        "lastUpdated": datetime.now().isoformat(),
        "menu": [
            {
                "label": "Getting Started",
                "path": "/getting-started",
                "icon": "🚀",
                "children": []
            },
            {
                "label": "Components",
                "path": "#",
                "icon": "📦",
                "children": []
            },
            {
                "label": "Theming",
                "path": "/theming",
                "icon": "🎨",
                "children": []
            },
            {
                "label": "API",
                "path": "/api",
                "icon": "📚",
                "children": []
            },
            {
                "label": "FAQ",
                "path": "/faq",
                "icon": "❓",
                "children": []
            }
        ]
    }
    
    # Build components section
    components_section = nav_menu["menu"][1]
    
    # Sort categories by order
    sorted_categories = sorted(components.items(), key=lambda x: x[1]["order"])
    
    for category, category_data in sorted_categories:
        category_components = category_data["components"]
        
        category_item = {
            "label": category_data["display_name"],
            "path": f"/components/{category}",
            "icon": category_data["icon"],
            "componentCount": category_data["count"],
            "children": [
                {
                    "label": comp["friendly_name"],
                    "path": comp["path"],
                    "icon": "📄",
                    "package": comp["name"]
                }
                for comp in sorted(category_components, key=lambda x: x["friendly_name"])
            ]
        }
        
        components_section["children"].append(category_item)
    
    return nav_menu

def main():
    print("=" * 70)
    print("TAIL.BLAZOR COMPONENT ANALYZER")
    print("=" * 70)
    
    print("\n[1/3] Discovering components...")
    components = discover_components()
    
    if not components:
        print("❌ No components found!")
        return
    
    total_components = sum(cat["count"] for cat in components.values())
    print(f"✓ Found {total_components} components across {len(components)} categories")
    
    print("\n[2/3] Generating navigation menu...")
    nav_menu = generate_nav_menu(components)
    
    # Save NavMenu.json
    nav_menu_path = Path("docs/Tail.Blazor.Docs/Pages/Components/NavMenu.json")
    nav_menu_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(nav_menu_path, "w") as f:
        json.dump(nav_menu, f, indent=2)
    
    print(f"✓ NavMenu.json generated at: {nav_menu_path}")
    
    print("\n[3/3] Component inventory by category:")
    print("=" * 70)
    
    sorted_categories = sorted(components.items(), key=lambda x: x[1]["order"])
    
    for category, category_data in sorted_categories:
        components_list = category_data["components"]
        implemented = sum(1 for c in components_list if c["implemented"])
        
        print(f"\n{category_data['icon']} {category.upper()}")
        print(f"   Total: {len(components_list)} | Implemented: {implemented}")
        
        for comp in sorted(components_list, key=lambda x: x["friendly_name"]):
            status = "✓" if comp["implemented"] else "✗"
            print(f"   {status} {comp['friendly_name']}")
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total Components: {total_components}")
    print(f"Total Categories: {len(components)}")
    print(f"NavMenu.json: ✓ Generated")
    print("=" * 70 + "\n")
    
    return components

if __name__ == "__main__":
    main()
