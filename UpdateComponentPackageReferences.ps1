# Script to update all component .csproj files with multi-framework AspNetCore.Components references
# This ensures proper version targeting for net8.0, net9.0, and net10.0
# Updated to properly handle dependency injection abstractions

param(
    [string]$ComponentsPath = "d:\Users\AMAR\source\repos\Tail\src\components",
    [switch]$WhatIf = $false
)

# Define the conditional AspNetCore package references to add
$conditionalRefs = @(
    @{ Include = "Microsoft.AspNetCore.Components"; Condition = "'`$(TargetFramework)' == 'net8.0'"; Version = "8.0.0" },
    @{ Include = "Microsoft.AspNetCore.Components.Web"; Condition = "'`$(TargetFramework)' == 'net8.0'"; Version = "8.0.0" },
    @{ Include = "Microsoft.AspNetCore.Components"; Condition = "'`$(TargetFramework)' == 'net9.0'"; Version = "9.*-*" },
    @{ Include = "Microsoft.AspNetCore.Components.Web"; Condition = "'`$(TargetFramework)' == 'net9.0'"; Version = "9.*-*" },
    @{ Include = "Microsoft.AspNetCore.Components"; Condition = "'`$(TargetFramework)' == 'net10.0'"; Version = "10.*-*" },
    @{ Include = "Microsoft.AspNetCore.Components.Web"; Condition = "'`$(TargetFramework)' == 'net10.0'"; Version = "10.*-*" }
)

# Find all component .csproj files
$projects = Get-ChildItem -Path $ComponentsPath -Recurse -Filter "*.csproj" | Where-Object { $_.Directory.Name.StartsWith("Tail.Blazor.") }

Write-Host "Found $($projects.Count) component projects to update" -ForegroundColor Cyan

$updatedCount = 0
$skippedCount = 0
$errorCount = 0

foreach ($project in $projects) {
    try {
        $projectPath = $project.FullName
        $projectName = $project.Directory.Name
        
        # Read the current content
        [xml]$xml = Get-Content $projectPath
        
        # Find or create the first ItemGroup with PackageReference
        $packageRefGroup = $xml.SelectSingleNode("//ItemGroup[PackageReference]")
        
        if ($null -eq $packageRefGroup) {
            Write-Host "⚠ SKIP: $projectName - No existing ItemGroup with PackageReference found" -ForegroundColor Yellow
            $skippedCount++
            continue
        }
        
        # Check if already has conditional references
        $hasConditional = $packageRefGroup.SelectNodes("PackageReference[@Condition]").Count -gt 0
        
        if ($hasConditional) {
            Write-Host "✓ SKIP: $projectName - Already has conditional PackageReferences" -ForegroundColor Green
            $skippedCount++
            continue
        }
        
        # Remove old unconditional PackageReferences for AspNetCore.Components only
        $oldRefs = $packageRefGroup.SelectNodes("PackageReference[contains(@Include, 'Microsoft.AspNetCore.Components')]")
        foreach ($ref in $oldRefs) {
            $packageRefGroup.RemoveChild($ref) | Out-Null
        }
        
        # Add the conditional references
        foreach ($ref in $conditionalRefs) {
            $newRefElement = $xml.CreateElement("PackageReference")
            $newRefElement.SetAttribute("Include", $ref.Include)
            $newRefElement.SetAttribute("Condition", $ref.Condition)
            $newRefElement.SetAttribute("Version", $ref.Version)
            $packageRefGroup.AppendChild($newRefElement) | Out-Null
        }
        
        # Ensure Microsoft.Extensions.DependencyInjection.Abstractions is present for Core projects with correct version
        if ($projectName -match "Core\.Base|Core\.Theme|^Tail\.Blazor\.Core$") {
            $hasExtensions = $packageRefGroup.SelectNodes("PackageReference[@Include='Microsoft.Extensions.DependencyInjection.Abstractions']").Count -gt 0
            if (-not $hasExtensions) {
                # Add conditional Extensions references matching the framework versions
                $extRefs = @(
                    @{ Condition = "'`$(TargetFramework)' == 'net8.0'"; Version = "8.0.0" },
                    @{ Condition = "'`$(TargetFramework)' == 'net9.0'"; Version = "9.*-*" },
                    @{ Condition = "'`$(TargetFramework)' == 'net10.0'"; Version = "10.*-*" }
                )
                
                foreach ($extRef in $extRefs) {
                    $extRefElement = $xml.CreateElement("PackageReference")
                    $extRefElement.SetAttribute("Include", "Microsoft.Extensions.DependencyInjection.Abstractions")
                    $extRefElement.SetAttribute("Condition", $extRef.Condition)
                    $extRefElement.SetAttribute("Version", $extRef.Version)
                    $packageRefGroup.AppendChild($extRefElement) | Out-Null
                }
            }
        }
        
        # Save the updated XML
        if (-not $WhatIf) {
            $xml.Save($projectPath)
            Write-Host "✓ UPDATED: $projectName" -ForegroundColor Cyan
        } else {
            Write-Host "→ WOULD UPDATE: $projectName" -ForegroundColor Blue
        }
        $updatedCount++
        
    } catch {
        Write-Host "✗ ERROR: $projectName - $_" -ForegroundColor Red
        $errorCount++
    }
}

Write-Host ""
Write-Host "========== SUMMARY ==========" -ForegroundColor Magenta
Write-Host "Updated:    $updatedCount" -ForegroundColor Cyan
Write-Host "Skipped:    $skippedCount" -ForegroundColor Green
Write-Host "Errors:     $errorCount" -ForegroundColor Red
Write-Host "Total:      $($projects.Count)" -ForegroundColor White
Write-Host ""

if ($WhatIf) {
    Write-Host "WhatIf mode - No changes were made. Run without -WhatIf to apply changes." -ForegroundColor Yellow
}
