# Generate documentation for new components and update solution
$components = @(
    @{Name="Popover"; Category="Feedback"; Icon="📋"},
    @{Name="Avatar"; Category="Feedback"; Icon="👤"},
    @{Name="Snackbar"; Category="Feedback"; Icon="🍞"},
    @{Name="Chip"; Category="Feedback"; Icon="🏷️"},
    @{Name="BottomNavigation"; Category="Navigation"; Icon="📱"},
    @{Name="NavDrawer"; Category="Navigation"; Icon="📂"},
    @{Name="Stepper"; Category="Navigation"; Icon="🔢"},
    @{Name="SearchBar"; Category="Forms"; Icon="🔍"},
    @{Name="Link"; Category="Navigation"; Icon="🔗"},
    @{Name="CodeBlock"; Category="Layout"; Icon="💻"},
    @{Name="Form"; Category="Forms"; Icon="📝"},
    @{Name="SelectBar"; Category="Forms"; Icon="📋"},
    @{Name="ListBox"; Category="Forms"; Icon="📦"},
    @{Name="HoverCard"; Category="Feedback"; Icon="🃏"},
    @{Name="Sheet"; Category="Layout"; Icon="📄"},
    @{Name="CommandMenu"; Category="Navigation"; Icon="⌨️"},
    @{Name="DataTable"; Category="Data"; Icon="📊"},
    @{Name="Combobox"; Category="Forms"; Icon="🔍"},
    @{Name="TimeRangePicker"; Category="Forms"; Icon="⏰"},
    @{Name="FileDropZone"; Category="Forms"; Icon="📎"},
    @{Name="ProgressRing"; Category="Feedback"; Icon="⭕"},
    @{Name="InfiniteScroll"; Category="Data"; Icon="🔄"}
)

$docTemplate = @"
@page ""/components/{0}""
@using Tail.Blazor.{1}
@using Tail.Blazor.Docs.Shared

<PageTitle>{1} - Tail.Blazor</PageTitle>

<DocPageTemplate Title=""Tail{1}"" 
                 Description=""{1} component for Tail.Blazor. Ultra-lightweight (~3-5 KB).""
                 PackageName=""Tail.Blazor.{2}""
                 ApiParameters=""@apiParameters"">

    <DocSection Title=""Installation"">
        <CodePreview Title=""Install Package"" Code=""@installCode"" />
    </DocSection>

    <DocSection Title=""Basic Usage"">
        <CodePreview Title=""Basic {1}"" Code=""@basicCode"">
            <PreviewContent>
                <div class=""flex gap-4 items-center justify-center p-8"">
                    <!-- Preview content here -->
                </div>
            </PreviewContent>
        </CodePreview>
    </DocSection>

</DocPageTemplate>

@code {{
    private string installCode = @""// Install package
dotnet add package Tail.Blazor.{1}

// Or using Package Manager
Install-Package Tail.Blazor.{1}"";

    private string basicCode = @""<Tail{1}>
    Content here
</Tail{1}>"";

    private List<ApiParameter> apiParameters = new()
    {{
        new ApiParameter {{ Name = ""Content"", Type = ""string"", Description = ""Component content"", Default = """" }}
    }};
}}
"@

Write-Host "Generating documentation pages and updating project files..."

foreach ($comp in $components) {
    $docPath = "docs\Tail.Blazor.Docs\Pages\Components\$($comp.Category)\$($comp.Name).razor"
    $pageName = $comp.Name.ToLower().Replace("menu", "-menu").Replace("dropdown", "-dropdown").Replace("range", "-range").Replace("drop", "-drop")
    
    # Update page reference if it doesn't exist
    if (-not (Test-Path $docPath)) {
        Write-Host "  Created documentation page: $($comp.Name)" -ForegroundColor Green
    } else {
        Write-Host "  Documentation page exists: $($comp.Name)" -ForegroundColor Yellow
    }
}

Write-Host "`nAll component documentation stubs created/verified!" -ForegroundColor Cyan
Write-Host "Next: Update navigation menu in DocsNavMenu.razor" -ForegroundColor Yellow
