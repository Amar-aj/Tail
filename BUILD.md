# Building Tail.Blazor

## Prerequisites

- .NET 8.0 SDK or later
- Visual Studio 2022 / VS Code / Rider

## Building All Projects

```bash
# Restore packages
dotnet restore

# Build solution
dotnet build Tail.Blazor.sln

# Build in Release mode
dotnet build Tail.Blazor.sln -c Release
```

## Building Individual Packages

```bash
# Build Core package
dotnet build src/packages/Tail.Blazor.Core/Tail.Blazor.Core.csproj

# Build Buttons package
dotnet build src/packages/Tail.Blazor.Buttons/Tail.Blazor.Buttons.csproj
```

## Creating NuGet Packages

```bash
# Pack all packages
dotnet pack Tail.Blazor.sln -c Release

# Pack individual package
dotnet pack src/packages/Tail.Blazor.Core/Tail.Blazor.Core.csproj -c Release
```

## Running Documentation Site

```bash
cd docs/Tail.Blazor.Docs
dotnet run
```

## Running Studio (MAUI)

```bash
cd apps/Tail.Blazor.Studio
dotnet build -t:Run -f net8.0-windows10.0.19041.0
```

## Testing

```bash
# Run all tests (when test projects are added)
dotnet test
```

## Performance Targets

- Component render: < 3 ms (average)
- Bundle size: Core 48 KB, individual modules ≤ 80 KB
- JavaScript: < 10 KB total
- Memory: < 2 MB runtime overhead

