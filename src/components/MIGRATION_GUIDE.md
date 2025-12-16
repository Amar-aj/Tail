# Component Migration Guide

## Overview

This guide explains how to migrate components from the meta-packages (`src/packages/`) to individual component packages (`src/components/`).

## Migration Process

### Step 1: Update Namespace

Each component package uses its own namespace:
- **Meta-package**: `Tail.Blazor.Buttons` (plural)
- **Individual package**: `Tail.Blazor.Button` (singular)

### Step 2: Copy Component Files

1. Copy `.razor` component files
2. Copy component-specific enums (update namespace)
3. Copy component-specific models (update namespace)
4. Copy any JavaScript files in `wwwroot/` if needed

### Step 3: Update References

- Update namespace declarations
- Update `using` statements
- Ensure all dependencies reference `Tail.Blazor.Core`

### Step 4: Test

- Build the individual package
- Verify it compiles independently
- Test component functionality

## Migration Checklist

### For Each Component Package:

- [ ] Copy component `.razor` file
- [ ] Copy/update enums (change namespace)
- [ ] Copy/update models (change namespace)
- [ ] Copy JavaScript files (if any)
- [ ] Update namespace in all files
- [ ] Update `_Imports.razor` if needed
- [ ] Test build
- [ ] Test component functionality

## Example: Button Component Migration

### Before (Meta-package):
```csharp
namespace Tail.Blazor.Buttons;

public enum ButtonVariant { ... }
```

### After (Individual package):
```csharp
namespace Tail.Blazor.Button;

public enum ButtonVariant { ... }
```

## Status

- ✅ **Tail.Blazor.Button** - Component and enums migrated
- ⏳ **All other components** - Pending migration

## Next Steps

1. Migrate remaining button components (IconButton, ToggleButton, etc.)
2. Migrate form components
3. Migrate feedback components
4. Continue with remaining categories

