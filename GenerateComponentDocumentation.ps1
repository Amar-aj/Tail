# Tail.Blazor Component Documentation Generator
# This script analyzes all components and generates/updates documentation structure
# Run: .\GenerateComponentDocumentation.ps1

param(
    [switch]$Preview = $false,
    [switch]$Force = $false
)

$ErrorActionPreference = "Stop"
$componentsPath = "d:\Users\AMAR\source\repos\Tail\src\components"
$docsPath = "d:\Users\AMAR\source\repos\Tail\docs\Tail.Blazor.Docs\Pages"

# Category mapping
$categories = @{
    "buttons" = @{
        "folder" = "Buttons"
        "displayName" = "Buttons"
        "icon" = "button"
    }
    "charts" = @{
        "folder" = "Charts"
        "displayName" = "Charts"
        "icon" = "chart"
    }
    "core" = @{
        "folder" = "Core"
        "displayName" = "Core"
        "icon" = "cog"
    }
    "data" = @{
        "folder" = "Data"
        "displayName" = "Data"
        "icon" = "table"
    }
    "feedback" = @{
        "folder" = "Feedback"
        "displayName" = "Feedback"
        "icon" = "bell"
    }
    "forms" = @{
        "folder" = "Forms"
        "displayName" = "Forms"
        "icon" = "input"
    }
    "icons" = @{
        "folder" = "Icons"
        "displayName" = "Icons"
        "icon" = "star"
    }
    "layout" = @{
        "folder" = "Layout"
        "displayName" = "Layout"
        "icon" = "layout"
    }
    "navigation" = @{
        "folder" = "Navigation"
        "displayName" = "Navigation"
        "icon" = "menu"
    }
    "utils" = @{
        "folder" = "Utils"
        "displayName" = "Utilities"
        "icon" = "tool"
    }
    "validators" = @{
        "folder" = "Validators"
        "displayName" = "Validators"
        "icon" = "check"
    }
    "visualization" = @{
        "folder" = "Visualization"
        "displayName" = "Visualization"
        "icon" = "chart-pie"
    }
}

# ============================================================================
# SECTION 1: Discover all components
# ============================================================================

Write-Host "========== DISCOVERING COMPONENTS ==========" -ForegroundColor Cyan

$allComponents = @{}
$allComponentsArray = @()

foreach ($category in $categories.Keys) {
    $categoryPath = Join-Path $componentsPath $category
    if (-not (Test-Path $categoryPath)) { continue }
    
    $allComponents[$category] = @()
    
    $projects = Get-ChildItem -Path $categoryPath -Directory -Exclude "Tail.Blazor.Core.Base", "Tail.Blazor.Core.Theme"
    
    foreach ($project in $projects) {
        $csproj = Get-ChildItem -Path $project.FullName -Filter "*.csproj" -ErrorAction SilentlyContinue
        
        if ($csproj) {
            $componentName = $project.Name
            $allComponents[$category] += $componentName
            $allComponentsArray += [PSCustomObject]@{
                Category = $category
                ComponentName = $componentName
                ComponentFolder = $project.Name
                CsProjectPath = $csproj.FullName
            }
        }
    }
}

Write-Host "Found $($allComponentsArray.Count) components across $($allComponents.Keys.Count) categories" -ForegroundColor Green

$allComponentsArray | Group-Object Category | ForEach-Object {
    Write-Host "  $($_.Name): $($_.Count) components" -ForegroundColor Gray
}

# ============================================================================
# SECTION 2: Check existing documentation pages
# ============================================================================

Write-Host "`n========== ANALYZING DOCUMENTATION PAGES ==========" -ForegroundColor Cyan

$docAnalysis = @()

foreach ($component in $allComponentsArray) {
    $category = $component.Category
    $componentName = $component.ComponentName
    
    # Expected doc page path
    $categoryDocsFolder = Join-Path $docsPath "Components" $categories[$category].folder
    $expectedDocPage = Join-Path $categoryDocsFolder "$componentName.razor"
    
    $docExists = Test-Path $expectedDocPage
    
    # Try to find the component's main .razor file
    $componentPath = Split-Path $component.CsProjectPath
    $razorFiles = Get-ChildItem -Path $componentPath -Filter "*.razor" -Exclude "*.razor.cs" -ErrorAction SilentlyContinue
    
    # Check if component has any implementation
    $componentImplemented = $razorFiles.Count -gt 0
    
    $docAnalysis += [PSCustomObject]@{
        Category = $category
        ComponentName = $componentName
        DocPageExists = $docExists
        ComponentImplemented = $componentImplemented
        DocPagePath = $expectedDocPage
        ComponentRazorFiles = $razorFiles.Count
    }
}

$missingDocs = @($docAnalysis | Where-Object { -not $_.DocPageExists })
$missingImplementations = @($docAnalysis | Where-Object { -not $_.ComponentImplemented })

Write-Host "Total Components: $($docAnalysis.Count)" -ForegroundColor Green
Write-Host "Documentation Pages Existing: $($($docAnalysis | Where-Object { $_.DocPageExists }).Count)" -ForegroundColor Green
Write-Host "Documentation Pages Missing: $($missingDocs.Count)" -ForegroundColor Yellow
Write-Host "Components Without Implementation: $($missingImplementations.Count)" -ForegroundColor Yellow

if ($Preview) {
    Write-Host "`nMissing Documentation Pages:" -ForegroundColor Yellow
    $missingDocs | ForEach-Object {
        Write-Host "  - $($_.Category)/$($_.ComponentName)" -ForegroundColor Gray
    }
    
    Write-Host "`nComponents Without Implementation:" -ForegroundColor Yellow
    $missingImplementations | ForEach-Object {
        Write-Host "  - $($_.Category)/$($_.ComponentName)" -ForegroundColor Gray
    }
}

# ============================================================================
# SECTION 3: Generate documentation page templates
# ============================================================================

Write-Host "`n========== GENERATING DOCUMENTATION TEMPLATES ==========" -ForegroundColor Cyan

function New-DocPageTemplate {
    param(
        [string]$ComponentName,
        [string]$Category
    )
    
    $categoryDisplay = $categories[$Category].displayName
    
    $template = @"
@page "/components/$($Category.ToLower())/$($ComponentName.ToLower().Replace('tail.blazor.', ''))"
@using Tail.Blazor.Docs.Shared

<DocPageTemplate Title="$ComponentName" Category="$categoryDisplay">

    <Description>
        A brief description of the $ComponentName component and its primary use cases.
    </Description>

    <Features>
        <FeatureItem Icon="check">Basic feature or capability</FeatureItem>
        <FeatureItem Icon="check">Another key feature</FeatureItem>
        <FeatureItem Icon="check">Third feature</FeatureItem>
    </Features>

    <Example Title="Basic Usage">
        <ComponentExample>
            <!-- Add basic component example here -->
            <!-- Use actual Tail.Blazor components for demonstration -->
        </ComponentExample>
    </Example>

    <Example Title="Advanced Usage">
        <ComponentExample>
            <!-- Add advanced usage example -->
        </ComponentExample>
    </Example>

    <ApiDocumentation>
        <ApiSection Title="Parameters">
            <ApiParameter Name="ParamName" Type="string">
                Description of the parameter.
            </ApiParameter>
        </ApiSection>

        <ApiSection Title="Events">
            <ApiParameter Name="EventName" Type="EventCallback">
                Description of the event.
            </ApiParameter>
        </ApiSection>

        <ApiSection Title="CSS Classes">
            <p>This component supports Tailwind CSS classes for styling.</p>
        </ApiSection>
    </ApiDocumentation>

</DocPageTemplate>
"@
    
    return $template
}

$generatedCount = 0
    $categoryFolder = $categories[$doc.Category].folder
    $categoryDocsPath = Join-Path $docsPath "Components" $categoryFolder
    
    # Create category folder if it doesn't exist
    if (-not (Test-Path $categoryDocsPath)) {
        New-Item -ItemType Directory -Path $categoryDocsPath -Force | Out-Null
        Write-Host "Created folder: Components/$categoryFolder" -ForegroundColor Green
    }
    
    # Generate template
    $template = New-DocPageTemplate -ComponentName $doc.ComponentName -Category $doc.Category
    $docPagePath = $doc.DocPagePath
    
    if (-not (Test-Path $docPagePath) -or $Force) {
        Set-Content -Path $docPagePath -Value $template -Force
        Write-Host "✓ Generated: Components/$categoryFolder/$($doc.ComponentName).razor" -ForegroundColor Green
        $generatedCount++
    } else {
        Write-Host "⊘ Skipped: Components/$categoryFolder/$($doc.ComponentName).razor (already exists)" -ForegroundColor Gray
        $skippedCount++
    }
}

Write-Host "`nGenerated: $generatedCount doc pages" -ForegroundColor Green
Write-Host "Skipped: $skippedCount doc pages (already exist)" -ForegroundColor Gray

# ============================================================================
# SECTION 4: Generate Navigation Menu JSON
# ============================================================================

Write-Host "`n========== GENERATING NAVIGATION MENU ==========" -ForegroundColor Cyan

$navMenu = @{
    version = "1.0.0"
    lastUpdated = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
    menu = @()
}

# Add main sections
$mainSections = @(
    @{ label = "Getting Started"; path = "/getting-started"; icon = "rocket" }
    @{ label = "Components"; path = "#"; icon = "cube"; isGroup = $true }
    @{ label = "Theming"; path = "/theming"; icon = "palette" }
    @{ label = "API"; path = "/api"; icon = "code" }
    @{ label = "FAQ"; path = "/faq"; icon = "question" }
)

foreach ($section in $mainSections) {
    $menuItem = [PSCustomObject]@{
        label = $section.label
        path = $section.path
        icon = $section.icon
        children = @()
    }
    
    # Add component categories as children
    if ($section.label -eq "Components") {
        foreach ($categoryKey in $categories.Keys | Sort-Object) {
            if ($allComponents[$categoryKey].Count -gt 0) {
                $categoryItem = [PSCustomObject]@{
                    label = $categories[$categoryKey].displayName
                    path = "/components/$categoryKey"
                    icon = $categories[$categoryKey].icon
                    children = @()
                }
                
                # Add individual components
                foreach ($component in ($allComponents[$categoryKey] | Sort-Object)) {
                    $componentUrl = $component.ToLower().Replace('tail.blazor.', '')
                    $componentItem = [PSCustomObject]@{
                        label = $component
                        path = "/components/$categoryKey/$componentUrl"
                        icon = "component"
                    }
                    $categoryItem.children += $componentItem
                }
                
                $menuItem.children += $categoryItem
            }
        }
    }
    
    $navMenu.menu += $menuItem
}

# Save navigation menu
$navMenuPath = Join-Path $docsPath "Components" "NavMenu.json"
$navMenuJson = $navMenu | ConvertTo-Json -Depth 10
Set-Content -Path $navMenuPath -Value $navMenuJson -Force

Write-Host "✓ Generated NavMenu.json at: Pages/Components/NavMenu.json" -ForegroundColor Green

# ============================================================================
# SECTION 5: Generate Scope Page Content
# ============================================================================

Write-Host "`n========== GENERATING SCOPE PAGE ==========" -ForegroundColor Cyan

$scopePageContent = @"
@page "/scope"
@using System.Collections.Generic
@using System.Linq

<PageTitle>Tail.Blazor Component Scope</PageTitle>

<div class="container mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold mb-2">Component Scope & Documentation Status</h1>
    <p class="text-gray-600 text-lg mb-8">Complete inventory of all Tail.Blazor components with documentation status.</p>

    <div class="mb-8 p-4 bg-blue-50 border border-blue-200 rounded-lg">
        <p class="text-sm text-gray-700">
            <strong>Last Updated:</strong> $(Get-Date -Format 'MMMM d, yyyy at h:mm tt')
        </p>
        <p class="text-sm text-gray-700 mt-2">
            <strong>Total Components:</strong> $($allComponentsArray.Count) | 
            <strong>Documentation Complete:</strong> $($($docAnalysis | Where-Object { $_.DocPageExists }).Count) | 
            <strong>Missing Docs:</strong> $($missingDocs.Count)
        </p>
    </div>

    <div class="grid gap-6">
"@

# Add each category
foreach ($categoryKey in $categories.Keys | Sort-Object) {
    if ($allComponents[$categoryKey].Count -eq 0) { continue }
    
    $categoryDisplay = $categories[$categoryKey].displayName
    $components = $allComponents[$categoryKey] | Sort-Object
    $docsForCategory = $docAnalysis | Where-Object { $_.Category -eq $categoryKey }
    $completeDocs = @($docsForCategory | Where-Object { $_.DocPageExists }).Count
    $totalComponents = $components.Count
    
    $scopePageContent += @"

        <div class="border rounded-lg overflow-hidden">
            <div class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-6 py-4">
                <h2 class="text-xl font-bold">$categoryDisplay</h2>
                <p class="text-sm text-blue-100">$completeDocs / $totalComponents components documented</p>
            </div>
            
            <div class="overflow-x-auto">
                <table class="w-full text-sm">
                    <thead class="bg-gray-50 border-b">
                        <tr>
                            <th class="px-6 py-3 text-left font-semibold">Component</th>
                            <th class="px-6 py-3 text-left font-semibold">Package</th>
                            <th class="px-6 py-3 text-center font-semibold">Implemented</th>
                            <th class="px-6 py-3 text-center font-semibold">Documented</th>
                            <th class="px-6 py-3 text-left font-semibold">Status</th>
                        </tr>
                    </thead>
                    <tbody>
"@
    
    foreach ($component in $components) {
        $doc = $docsForCategory | Where-Object { $_.ComponentName -eq $component }
        $implemented = $doc.ComponentImplemented ? "✓" : "✗"
        $documented = $doc.DocPageExists ? "✓" : "✗"
        $implementedClass = $doc.ComponentImplemented ? "text-green-600" : "text-red-600"
        $documentedClass = $doc.DocPageExists ? "text-green-600" : "text-orange-600"
        $statusClass = ($doc.ComponentImplemented -and $doc.DocPageExists) ? "Complete" : ($doc.ComponentImplemented ? "Pending Docs" : "Incomplete")
        $statusColor = ($doc.ComponentImplemented -and $doc.DocPageExists) ? "bg-green-100 text-green-800" : ($doc.ComponentImplemented ? "bg-yellow-100 text-yellow-800" : "bg-red-100 text-red-800")
        
        $scopePageContent += @"

                        <tr class="border-b hover:bg-gray-50">
                            <td class="px-6 py-4 font-medium">$component</td>
                            <td class="px-6 py-4 text-gray-600"><code>$component</code></td>
                            <td class="px-6 py-4 text-center $implementedClass font-bold">$implemented</td>
                            <td class="px-6 py-4 text-center $documentedClass font-bold">$documented</td>
                            <td class="px-6 py-4">
                                <span class="inline-block px-3 py-1 rounded-full text-xs font-semibold $statusColor">
                                    $statusClass
                                </span>
                            </td>
                        </tr>
"@
    }
    
    $scopePageContent += @"

                    </tbody>
                </table>
            </div>
        </div>
"@
}

$scopePageContent += @"

    </div>

    <div class="mt-12 p-6 bg-gray-50 rounded-lg">
        <h3 class="text-xl font-bold mb-4">Legend</h3>
        <ul class="space-y-2">
            <li><span class="text-green-600 font-bold">✓</span> - Feature complete and documented</li>
            <li><span class="text-orange-600 font-bold">⊘</span> - Feature complete but documentation pending</li>
            <li><span class="text-red-600 font-bold">✗</span> - Feature not yet implemented</li>
        </ul>
    </div>
</div>

@code {
    // This page is automatically generated by GenerateComponentDocumentation.ps1
}
"@

$scopePath = Join-Path $docsPath "Scope.razor"
Set-Content -Path $scopePath -Value $scopePageContent -Force
Write-Host "✓ Updated Scope.razor with current component status" -ForegroundColor Green

# ============================================================================
# SECTION 6: Generate Summary Report
# ============================================================================

Write-Host "`n========== SUMMARY REPORT ==========" -ForegroundColor Cyan

$report = @"
╔════════════════════════════════════════════════════════════════╗
║        TAIL.BLAZOR COMPONENT DOCUMENTATION REPORT             ║
╚════════════════════════════════════════════════════════════════╝

COMPONENTS BY CATEGORY:
$($categories.Keys | Sort-Object | ForEach-Object {
    $count = $allComponents[$_].Count
    if ($count -gt 0) {
        $categoryDisplay = $categories[$_].displayName
        $formatted = "$($categoryDisplay): $count"
        "  {0,-40}" -f $formatted
    }
})

DOCUMENTATION STATUS:
  Total Components: $($allComponentsArray.Count)
  Documented: $($($docAnalysis | Where-Object { $_.DocPageExists }).Count)
  Missing Documentation: $($missingDocs.Count)
  Not Implemented: $($missingImplementations.Count)

FILES GENERATED:
  ✓ Documentation pages: $generatedCount
  ✓ Navigation menu: NavMenu.json
  ✓ Scope page: Scope.razor

NEXT STEPS:
  1. Review generated documentation templates
  2. Add component-specific examples and descriptions
  3. Link related components
  4. Update component images/screenshots
  5. Test all documentation links

════════════════════════════════════════════════════════════════
"@

Write-Host $report

# Save report to file
$reportPath = Join-Path $docsPath "DOCUMENTATION_STATUS.txt"
Set-Content -Path $reportPath -Value $report
Write-Host "`n✓ Report saved to: Pages/DOCUMENTATION_STATUS.txt" -ForegroundColor Green

Write-Host "`n========== COMPLETED ==========" -ForegroundColor Green
