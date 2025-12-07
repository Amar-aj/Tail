# Building the Tail.Blazor Solution

## Quick Start - Library Packages Only

If you want to build just the library packages (recommended for NuGet development):

```bash
# Build all library packages
foreach ($proj in (Get-ChildItem -Path "src/packages" -Filter "*.csproj" -Recurse)) { 
    dotnet build $proj.FullName 
}

# Or build specific package
dotnet build src/packages/Tail.Blazor.Core/Tail.Blazor.Core.csproj
dotnet build src/packages/Tail.Blazor.Buttons/Tail.Blazor.Buttons.csproj
```

## Building Documentation Site

```bash
dotnet build docs/Tail.Blazor.Docs/Tail.Blazor.Docs.csproj
dotnet run --project docs/Tail.Blazor.Docs/Tail.Blazor.Docs.csproj
```

## Building MAUI Studio (Optional)

### Prerequisites

The MAUI Studio project requires .NET MAUI workloads to be installed:

```bash
# Check installed workloads
dotnet workload list

# Install MAUI workloads (if not present)
dotnet workload install maui
dotnet workload install maui-windows
dotnet workload install maui-android
dotnet workload install maui-ios
dotnet workload install maui-maccatalyst
```

### Build MAUI Studio

**Windows:**
```bash
dotnet build apps/Tail.Blazor.Studio/Tail.Blazor.Studio.csproj -f net9.0-windows10.0.19041.0
dotnet run --project apps/Tail.Blazor.Studio/Tail.Blazor.Studio.csproj -f net9.0-windows10.0.19041.0
```

**Android:**
```bash
dotnet build apps/Tail.Blazor.Studio/Tail.Blazor.Studio.csproj -f net9.0-android
```

**iOS/macOS:**
```bash
dotnet build apps/Tail.Blazor.Studio/Tail.Blazor.Studio.csproj -f net9.0-ios
dotnet build apps/Tail.Blazor.Studio/Tail.Blazor.Studio.csproj -f net9.0-maccatalyst
```

### Common MAUI Issues

**Issue: "The type 'Color' was not found"**
- **Cause:** MAUI workloads not installed
- **Solution:** Run `dotnet workload install maui`

**Issue: "StaticWebAssetsPrepareForRun does not exist"**
- **Cause:** Version mismatch or workload issue
- **Solution:** 
  1. Clean and restore: `dotnet clean && dotnet restore`
  2. Ensure .NET 9 SDK is installed
  3. Reinstall MAUI workload: `dotnet workload install maui --force`

## Building Everything

### Option 1: Build Library Packages + Docs Only (Recommended)

```bash
cd D:\Users\AMAR\source\repos\Tail

# Build all library packages
Get-ChildItem -Path "src/packages" -Filter "*.csproj" -Recurse | ForEach-Object { 
    Write-Host "Building $($_.Name)..." -ForegroundColor Green
    dotnet build $_.FullName --no-restore
}

# Build docs
dotnet build docs/Tail.Blazor.Docs/Tail.Blazor.Docs.csproj --no-restore
```

### Option 2: Build Including MAUI (Requires Workloads)

```bash
# Full solution build
dotnet build Tail.Blazor.sln
```

## Troubleshooting

### MAUI Workload Not Found

```bash
# Update workloads
dotnet workload update

# List available workloads
dotnet workload search maui

# Install specific version
dotnet workload install maui --version 9.0.0
```

### Clean Build

```bash
# Clean everything
dotnet clean Tail.Blazor.sln

# Remove obj and bin folders
Get-ChildItem -Path "." -Include obj,bin -Recurse -Directory | Remove-Item -Recurse -Force

# Restore and rebuild
dotnet restore
dotnet build
```

### Platform-Specific MAUI Builds

You can build for specific platforms by targeting specific frameworks:

```bash
# Windows only
dotnet build apps/Tail.Blazor.Studio/Tail.Blazor.Studio.csproj /p:TargetFramework=net9.0-windows10.0.19041.0

# Android only
dotnet build apps/Tail.Blazor.Studio/Tail.Blazor.Studio.csproj /p:TargetFramework=net9.0-android

# iOS only (macOS required)
dotnet build apps/Tail.Blazor.Studio/Tail.Blazor.Studio.csproj /p:TargetFramework=net9.0-ios

# macCatalyst only (macOS required)
dotnet build apps/Tail.Blazor.Studio/Tail.Blazor.Studio.csproj /p:TargetFramework=net9.0-maccatalyst
```

## CI/CD Considerations

### GitHub Actions / Azure DevOps

For CI/CD pipelines that don't need MAUI:

```yaml
# Build library packages only
- run: |
    dotnet build src/packages/Tail.Blazor.Core/Tail.Blazor.Core.csproj
    dotnet build src/packages/Tail.Blazor.Buttons/Tail.Blazor.Buttons.csproj
    # ... other packages
    dotnet build docs/Tail.Blazor.Docs/Tail.Blazor.Docs.csproj
```

For full builds including MAUI:

```yaml
# Install MAUI workloads first
- run: dotnet workload install maui
- run: dotnet build Tail.Blazor.sln
```

## Package NuGet Packages

```bash
# Pack all library packages
Get-ChildItem -Path "src/packages" -Filter "*.csproj" -Recurse | ForEach-Object { 
    dotnet pack $_.FullName -c Release -o "D:\Users\AMAR\source\repos\Tail\artifacts"
}

# Or pack entire solution
dotnet pack Tail.Blazor.sln -c Release -o artifacts
```

## Summary

**For Most Developers:**
- Build library packages individually
- Build and run documentation site
- Skip MAUI Studio unless needed

**For MAUI Studio Development:**
- Install .NET MAUI workloads
- Build for specific target platform
- Use platform-specific SDK (Windows SDK, Android SDK, Xcode)

**Current Build Status:**
- ? All 12 library packages build successfully
- ? Documentation site builds and runs
- ?? MAUI Studio requires workload installation
