#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tail.Blazor Rich Documentation Generator
Generates comprehensive, responsive documentation pages from metadata
"""

import json
import sys
import html
from pathlib import Path
from datetime import datetime

# Fix Unicode output on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


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
    """Generate a rich documentation page."""
    friendly_name = metadata['friendly_name']
    description = metadata['description']
    parameters = metadata['parameters']
    events = metadata['events']
    enums = metadata['enums']
    
    # Build parameters table
    params_html = ""
    if parameters:
        params_html = f"""
    <DocSection Title="Properties & Parameters">
        <div class="overflow-x-auto">
            <table class="min-w-full border-collapse text-sm">
                <thead class="bg-gray-100 dark:bg-gray-800">
                    <tr>
                        <th class="border border-gray-300 dark:border-gray-600 px-4 py-2 text-left font-semibold">Property</th>
                        <th class="border border-gray-300 dark:border-gray-600 px-4 py-2 text-left font-semibold">Type</th>
                        <th class="border border-gray-300 dark:border-gray-600 px-4 py-2 text-left font-semibold">Default</th>
                        <th class="border border-gray-300 dark:border-gray-600 px-4 py-2 text-left font-semibold">Description</th>
                    </tr>
                </thead>
                <tbody>
"""
        for param in parameters:
            req = "✓ Required" if param['required'] else "Optional"
            default = param['default'] or "—"
            escaped_type = html.escape(param['type'])
            params_html += f"""                    <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                        <td class="border border-gray-300 dark:border-gray-600 px-4 py-2 font-mono text-blue-600 dark:text-blue-400">{param['name']}</td>
                        <td class="border border-gray-300 dark:border-gray-600 px-4 py-2 font-mono text-gray-700 dark:text-gray-300">{escaped_type}</td>
                        <td class="border border-gray-300 dark:border-gray-600 px-4 py-2 font-mono">{default}</td>
                        <td class="border border-gray-300 dark:border-gray-600 px-4 py-2 text-gray-700 dark:text-gray-300">{param['description'] or req}</td>
                    </tr>
"""
        params_html += """                </tbody>
            </table>
        </div>
    </DocSection>
"""
    
    # Build enums section
    enums_html = ""
    if enums:
        enums_html = f"""
    <DocSection Title="Enums & Options">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
"""
        for enum_name, enum_data in enums.items():
            enums_html += f"""            <TailCard Class="p-4">
                <Header>
                    <h4 class="font-semibold text-lg text-gray-900 dark:text-white">{enum_name}</h4>
                </Header>
                <ChildContent>
                    <ul class="space-y-2">
"""
            for member in enum_data['members']:
                enums_html += f"""                        <li class="flex items-center gap-2">
                            <span class="w-2 h-2 bg-blue-500 rounded-full"></span>
                            <code class="bg-gray-100 dark:bg-gray-800 px-2 py-1 rounded text-sm">{member}</code>
                        </li>
"""
            enums_html += """                    </ul>
                </ChildContent>
            </TailCard>
"""
        enums_html += """        </div>
    </DocSection>
"""
    
    # Build events section
    events_html = ""
    if events:
        events_html = f"""
    <DocSection Title="Events & Callbacks">
        <div class="space-y-4">
"""
        for event in events:
            events_html += f"""            <div class="border-l-4 border-blue-500 bg-blue-50 dark:bg-blue-900 dark:border-blue-400 p-4 rounded">
                <h4 class="font-semibold text-gray-900 dark:text-white mb-2">
                    <code class="text-blue-600 dark:text-blue-400">{event['name']}</code>
                </h4>
                <p class="text-sm text-gray-700 dark:text-gray-300 mb-2">
                    <strong>Parameter Type:</strong> <code class="bg-gray-200 dark:bg-gray-700 px-1 rounded">{event['parameter_type']}</code>
                </p>
                <p class="text-sm text-gray-700 dark:text-gray-300">{event['description'] or 'Raised when event occurs'}</p>
            </div>
"""
        events_html += """        </div>
    </DocSection>
"""
    
    # Generate complete page
    doc_page = f'''@page "/components/{category.lower()}/{friendly_name.lower()}"
@using Tail.Blazor.Docs.Shared
@using Tail.Blazor.Container
@using Tail.Blazor.Card
@using Tail.Blazor.Button
@using Tail.Blazor.Grid

<PageTitle>{friendly_name} - Tail.Blazor Docs</PageTitle>

<DocPageTemplate Title="{friendly_name}" 
                 Description="{description}"
                 PackageName="{component_name}">
    
    <!-- Installation Section -->
    <DocSection Title="Installation">
        <div class="space-y-4">
            <p class="text-gray-700 dark:text-gray-300">
                Install the {friendly_name} component package via NuGet:
            </p>
            <CodePreview Title="NuGet Package Installation" 
                         Code="dotnet add package {component_name}"
                         ShowPreview="false"
                         Language="bash">
            </CodePreview>
            <p class="text-sm text-gray-600 dark:text-gray-400">
                Or download from <a href="https://www.nuget.org/packages/{component_name}" class="text-blue-600 dark:text-blue-400 hover:underline">NuGet.org</a>
            </p>
        </div>
    </DocSection>

    <!-- Quick Start Section -->
    <DocSection Title="Quick Start">
        <p class="text-gray-700 dark:text-gray-300 mb-4">
            Get started with the {friendly_name} component in minutes:
        </p>
        <CodePreview Title="Basic Usage" 
                     Code="@basicUsageCode"
                     Language="razor">
            <PreviewContent>
                <div class="p-4 bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-blue-900 dark:to-indigo-900 rounded-lg">
                    <p class="text-gray-700 dark:text-gray-300">Live preview will appear here when component examples are added.</p>
                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>
{params_html}{enums_html}{events_html}
    <!-- Usage Examples Section -->
    <DocSection Title="Usage Examples">
        <div class="space-y-6">
            <div class="p-4 bg-blue-50 dark:bg-blue-900 border border-blue-200 dark:border-blue-800 rounded-lg">
                <p class="text-sm text-blue-900 dark:text-blue-200">
                    <strong>💡 Tip:</strong> Examples are embedded below. Each tab shows complete, working code you can copy and use.
                </p>
            </div>
            
            <TailTabs>
                <TabItem Title="Basic Usage" Active="true">
                    <CodePreview Title="Minimal Example" 
                                 Code="@minimalExampleCode"
                                 Language="razor"
                                 ShowPreview="true">
                        <PreviewContent>
                            <div class="p-6 bg-gray-50 dark:bg-gray-800 rounded-lg text-center">
                                <p class="text-gray-700 dark:text-gray-300">Default {friendly_name} component</p>
                            </div>
                        </PreviewContent>
                    </CodePreview>
                </TabItem>
                
                <TabItem Title="With All Parameters">
                    <CodePreview Title="Complete Parameter Usage" 
                                 Code="@withParametersCode"
                                 Language="razor"
                                 ShowPreview="true">
                        <PreviewContent>
                            <div class="p-6 bg-gray-50 dark:bg-gray-800 rounded-lg">
                                <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">See the Properties table above for all available parameters.</p>
                            </div>
                        </PreviewContent>
                    </CodePreview>
                </TabItem>
                
                <TabItem Title="Event Handling">
                    <CodePreview Title="Handling Events" 
                                 Code="@eventHandlingCode"
                                 Language="razor"
                                 ShowPreview="true">
                        <PreviewContent>
                            <div class="p-6 bg-gray-50 dark:bg-gray-800 rounded-lg">
                                <p class="text-sm text-gray-600 dark:text-gray-400">See Events & Callbacks section for available events.</p>
                            </div>
                        </PreviewContent>
                    </CodePreview>
                </TabItem>
                
                <TabItem Title="Responsive Layout">
                    <CodePreview Title="Using with Responsive Grid" 
                                 Code="@responsiveLayoutCode"
                                 Language="razor"
                                 ShowPreview="true">
                        <PreviewContent>
                            <div class="p-6 bg-gray-50 dark:bg-gray-800 rounded-lg">
                                <p class="text-sm text-gray-600 dark:text-gray-400">Component works great in responsive grids and containers.</p>
                            </div>
                        </PreviewContent>
                    </CodePreview>
                </TabItem>
                
                <TabItem Title="Dark Mode">
                    <CodePreview Title="Dark Mode Support" 
                                 Code="@darkModeCode"
                                 Language="razor"
                                 ShowPreview="true">
                        <PreviewContent>
                            <div class="p-6 bg-gray-50 dark:bg-gray-800 rounded-lg">
                                <p class="text-sm text-gray-600 dark:text-gray-400">Full dark mode support included automatically.</p>
                            </div>
                        </PreviewContent>
                    </CodePreview>
                </TabItem>
            </TailTabs>
        </div>
    </DocSection>

    <!-- Related Components Section -->
    <DocSection Title="Related Components">
        <TailContainer Size="ContainerSize.Full">
            <TailGrid Columns="1" ColumnsMd="2" ColumnsLg="3" Gap="4">
                <TailCard Class="hover:shadow-lg transition-shadow">
                    <Header>
                        <h4 class="font-semibold text-gray-900 dark:text-white">Button</h4>
                    </Header>
                    <ChildContent>
                        <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
                            Basic button component for user interactions.
                        </p>
                        <a href="/components/buttons/button" class="text-blue-600 dark:text-blue-400 hover:underline text-sm">
                            View Documentation →
                        </a>
                    </ChildContent>
                </TailCard>

                <TailCard Class="hover:shadow-lg transition-shadow">
                    <Header>
                        <h4 class="font-semibold text-gray-900 dark:text-white">Icon Button</h4>
                    </Header>
                    <ChildContent>
                        <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
                            Button component with icon support.
                        </p>
                        <a href="/components/buttons/iconbutton" class="text-blue-600 dark:text-blue-400 hover:underline text-sm">
                            View Documentation →
                        </a>
                    </ChildContent>
                </TailCard>

                <TailCard Class="hover:shadow-lg transition-shadow">
                    <Header>
                        <h4 class="font-semibold text-gray-900 dark:text-white">Button Group</h4>
                    </Header>
                    <ChildContent>
                        <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
                            Group multiple buttons together.
                        </p>
                        <a href="/components/buttons/buttongroup" class="text-blue-600 dark:text-blue-400 hover:underline text-sm">
                            View Documentation →
                        </a>
                    </ChildContent>
                </TailCard>
            </TailGrid>
        </TailContainer>
    </DocSection>

    <!-- Best Practices Section -->
    <DocSection Title="Best Practices">
        <div class="space-y-4">
            <div class="bg-amber-50 dark:bg-amber-900 border-l-4 border-amber-500 p-4 rounded">
                <h4 class="font-semibold text-amber-900 dark:text-amber-100 mb-2">✓ Do</h4>
                <ul class="text-sm text-amber-800 dark:text-amber-200 space-y-1 list-disc list-inside">
                    <li>Use clear, descriptive labels for user action</li>
                    <li>Provide visual feedback for loading states</li>
                    <li>Keep button text concise and actionable</li>
                </ul>
            </div>
            <div class="bg-red-50 dark:bg-red-900 border-l-4 border-red-500 p-4 rounded">
                <h4 class="font-semibold text-red-900 dark:text-red-100 mb-2">✗ Don't</h4>
                <ul class="text-sm text-red-800 dark:text-red-200 space-y-1 list-disc list-inside">
                    <li>Use buttons for navigation (use links instead)</li>
                    <li>Disable buttons without explanation</li>
                    <li>Mix too many button styles on same page</li>
                </ul>
            </div>
        </div>
    </DocSection>

</DocPageTemplate>

@code {{
    private string basicUsageCode = "<{friendly_name}></{friendly_name}>";
    private string minimalExampleCode = "<{friendly_name}></{friendly_name}>";
    private string withParametersCode = "@* Refer to Properties & Parameters section above *@\\n<{friendly_name} @* parameters here *@></{friendly_name}>";
    private string eventHandlingCode = "<{friendly_name} @* events from Events section above *@ ></{friendly_name}>\\n\\n@code {{\\n    void OnEventHandler(parameter) {{ }}\\n}}";
    private string responsiveLayoutCode = "<TailGrid Columns=\\"1\\" ColumnsMd=\\"2\\" ColumnsLg=\\"3\\" Gap=\\"4\\">\\n    <{friendly_name}></{friendly_name}>\\n    <{friendly_name}></{friendly_name}>\\n    <{friendly_name}></{friendly_name}>\\n</TailGrid>";
    private string darkModeCode = "<!-- {friendly_name} automatically supports dark mode -->\\n<{friendly_name}></{friendly_name}>\\n\\n<!-- Pair with dark mode classes if needed -->\\n<div class=\\"dark:bg-gray-900 dark:text-white\\">\\n    <{friendly_name}></{friendly_name}>\\n</div>";
}}
'''
    
    return doc_page


def main():
    print("=" * 70)
    print("TAIL.BLAZOR RICH DOCUMENTATION GENERATOR")
    print("=" * 70)
    
    print("\n[1/3] Loading component metadata...")
    metadata = load_metadata()
    print("✓ Metadata loaded")
    
    print("\n[2/3] Creating documentation pages...")
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
    
    print(f"✓ Generated {pages_created} documentation pages")
    
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
    print(f"\n✓ Rich documentation generated!")
    print(f"✓ Total pages: {pages_created}")
    print(f"✓ Total components: {total_components}")
    print(f"✓ Location: {docs_base}")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
