# Multi-Framework Support Guide

## Overview

Tail.Blazor supports .NET 8, .NET 9, and .NET 10 through a flexible build configuration system.

## Current Configuration

### Library Packages (NuGet)
All library packages in `src/packages/` target **.NET 8** by default:
- `Tail.Blazor.Core`
- `Tail.Blazor.Buttons`
- `Tail.Blazor.Forms`
- `Tail.Blazor.Data`
- `Tail.Blazor.Feedback`
- `Tail.Blazor.Navigation`
- `Tail.Blazor.Layout`
- `Tail.Blazor.Icons`
- `Tail.Blazor.Utils`
- `Tail.Blazor.Charts`
- `Tail.Blazor.Visualization`
- `Tail.Blazor.Validators`

### Applications
- **Tail.Blazor.Docs**: .NET 8 (can be upgraded to 9 or 10)
- **Tail.Blazor.Studio**: .NET 9 (MAUI requirement)

## How to Target Multiple Frameworks

### Option 1: Multi-Targeting in Project Files

To target multiple .NET versions in a single library package, update the `.csproj` file:

```xml
<Project Sdk="Microsoft.NET.Sdk.Razor">
  <PropertyGroup>
    <!-- Replace single TargetFramework with TargetFrameworks (plural) -->
    <TargetFrameworks>net8.0;net9.0;net10.0</TargetFrameworks>
    <!-- Other properties... -->
  </PropertyGroup>
</Project>
```

### Option 2: Upgrade All Projects

To upgrade all library packages to a specific version (e.g., .NET 9):

1. **Update Directory.Build.props**:
   ```xml
   <TargetFramework Condition="'$(TargetFramework)' == '' AND '$(TargetFrameworks)' == ''">net9.0</TargetFramework>
   ```

2. **Update package references** in each `.csproj`:
   ```xml
   <PackageReference Include="Microsoft.AspNetCore.Components.Web" Version="9.0.0" />
   ```

### Option 3: Framework-Specific Builds

Keep different branches or build configurations for each framework:
- `main` branch: .NET 8 (LTS)
- `net9` branch: .NET 9 (STS)
- `net10` branch: .NET 10 (Preview)

## Directory.Build.props Settings

The root `Directory.Build.props` file controls default settings:

```xml
<Project>
  <PropertyGroup>
    <!-- Default to .NET 8 if not specified -->
    <TargetFramework Condition="'$(TargetFramework)' == '' AND '$(TargetFrameworks)' == ''">net8.0</TargetFramework>
    
    <!-- Common settings -->
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <LangVersion>latest</LangVersion>
    
    <!-- Trimming disabled for web apps (OutputType=Exe) to avoid JSON issues -->
    <EnableTrimAnalyzer Condition="'$(TargetFrameworks)' == '' AND '$(OutputType)' != 'Exe'">true</EnableTrimAnalyzer>
    <PublishTrimmed Condition="'$(TargetFrameworks)' == '' AND '$(OutputType)' != 'Exe'">false</PublishTrimmed>
  </PropertyGroup>
</Project>
```

## Important Notes

### Trimming and JSON Serialization

**Issue**: When `PublishTrimmed` is enabled, reflection-based JSON serialization is disabled, causing runtime errors in Blazor Server apps.

**Solution**: 
1. Disable trimming for web applications (`OutputType=Exe`)
2. Use source-generated JSON serialization contexts (see `docs/Tail.Blazor.Docs/Program.cs`)

### MAUI Projects

MAUI projects require **.NET 9** minimum for latest features and bug fixes. The Studio project uses:
```xml
<TargetFrameworks>net9.0-android;net9.0-ios;net9.0-maccatalyst;net9.0-windows10.0.19041.0</TargetFrameworks>
```

## Recommended Strategy

**For Production (Recommended)**:
- Library packages: Multi-target `net8.0;net9.0` for maximum compatibility
- Documentation site: `net8.0` (LTS) or `net9.0`
- MAUI Studio: `net9.0` (required)

**For Development**:
- Use latest SDK (.NET 10 SDK can build .NET 8, 9, 10 projects)
- Test against all targeted frameworks

## Build Commands

### Build for Specific Framework
```bash
dotnet build -f net8.0
dotnet build -f net9.0
dotnet build -f net10.0
```

### Build All Frameworks (Multi-Targeting)
```bash
dotnet build
```

### Pack NuGet for All Frameworks
```bash
dotnet pack -c Release
```

## Testing Multi-Framework Support

1. **Install multiple SDKs**:
   - .NET 8 SDK (LTS)
   - .NET 9 SDK
   - .NET 10 SDK (Preview)

2. **Build and test**:
   ```bash
   dotnet build
   dotnet test
   ```

3. **Verify NuGet package contents**:
   ```bash
   dotnet pack -c Release
   # Check nupkg contains lib/net8.0, lib/net9.0, lib/net10.0
   ```

## Migration Guide

### Migrating from .NET 8 to .NET 9

1. Update all `.csproj` files:
   ```xml
   <TargetFramework>net9.0</TargetFramework>
   ```

2. Update package references:
   ```xml
   <PackageReference Include="Microsoft.AspNetCore.Components.Web" Version="9.0.0" />
   ```

3. Test for breaking changes (consult [.NET 9 migration guide](https://learn.microsoft.com/en-us/dotnet/core/compatibility/9.0))

### Migrating from .NET 9 to .NET 10

Similar process as above, updating to `net10.0` and version `10.0.0` packages.

## Support Timeline

| Version | Type | Release | End of Support |
|---------|------|---------|----------------|
| .NET 8  | LTS  | Nov 2023 | Nov 2026 |
| .NET 9  | STS  | Nov 2024 | May 2026 |
| .NET 10 | LTS  | Nov 2025 | Nov 2028 (est.) |

**Recommendation**: Target .NET 8 (LTS) for maximum stability, multi-target .NET 8 + 9 for broader support.
