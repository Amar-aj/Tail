# CodePreview Component - Quick Reference Guide

## ?? Overview

The `CodePreview` component is a reusable documentation component that displays code examples with live previews and one-click copy functionality.

---

## ?? Basic Usage

### Simple Example
```razor
<CodePreview Title="My Component" Code="@myCode">
    <PreviewContent>
        <TailButton>Click Me</TailButton>
    </PreviewContent>
</CodePreview>

@code {
    private string myCode = @"<TailButton>Click Me</TailButton>";
}
```

---

## ?? All Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `Title` | string? | null | Section title displayed at top |
| `Code` | string | "" | Code string to display and copy |
| `ShowPreview` | bool | true | Show live preview section |
| `ShowCode` | bool | true | Show code block section |
| `ShowCopyButton` | bool | true | Show copy to clipboard button |
| `Language` | string | "razor" | Syntax highlighting language |
| `CssClass` | string? | null | Additional CSS classes for container |
| `PreviewContent` | RenderFragment? | null | Content for preview section |
| `ChildContent` | RenderFragment? | null | Fallback content if no PreviewContent |

---

## ?? Usage Patterns

### 1. Full Example (Preview + Code)
```razor
<CodePreview Title="Button Variants" Code="@buttonCode">
    <PreviewContent>
        <div class="flex gap-2">
            <TailButton Variant="ButtonVariant.Primary">Primary</TailButton>
            <TailButton Variant="ButtonVariant.Success">Success</TailButton>
        </div>
    </PreviewContent>
</CodePreview>

@code {
    private string buttonCode = @"<TailButton Variant=""ButtonVariant.Primary"">Primary</TailButton>
<TailButton Variant=""ButtonVariant.Success"">Success</TailButton>";
}
```

### 2. Code Only (No Preview)
```razor
<CodePreview 
    Title="Installation" 
    Code="@installCode"
    ShowPreview="false"
    Language="bash" />

@code {
    private string installCode = "dotnet add package Tail.Blazor.Buttons";
}
```

### 3. Preview Only (No Code)
```razor
<CodePreview 
    Title="Live Demo" 
    Code=""
    ShowCode="false">
    <PreviewContent>
        <InteractiveDemo />
    </PreviewContent>
</CodePreview>
```

### 4. Interactive Example
```razor
<CodePreview Title="Counter Button" Code="@counterCode">
    <PreviewContent>
        <TailButton OnClick="Increment">
            Clicked: @count times
        </TailButton>
        <button @onclick="Reset" class="ml-2 text-sm text-gray-600">Reset</button>
    </PreviewContent>
</CodePreview>

@code {
    private int count = 0;
    private void Increment() => count++;
    private void Reset() => count = 0;
    
    private string counterCode = @"@code {
    private int count = 0;
    private void Increment() => count++;
}

<TailButton OnClick=""Increment"">
    Clicked: @count times
</TailButton>";
}
```

### 5. Multiple Language Support
```razor
<!-- C# Code -->
<CodePreview 
    Title="C# Code-Behind" 
    Code="@csharpCode"
    ShowPreview="false"
    Language="csharp" />

<!-- CSS Code -->
<CodePreview 
    Title="Custom Styles" 
    Code="@cssCode"
    ShowPreview="false"
    Language="css" />

@code {
    private string csharpCode = @"public class MyService
{
    public string GetMessage() => ""Hello World"";
}";

    private string cssCode = @".my-component {
    display: flex;
    gap: 1rem;
}";
}
```

### 6. With Real-Time Feedback
```razor
<CodePreview Title="Form Example" Code="@formCode">
    <PreviewContent>
        <TailInput 
            Label="Name" 
            Value="@name" 
            ValueChanged="v => name = v" 
            Placeholder="Enter your name" />
        @if (!string.IsNullOrEmpty(name))
        {
            <p class="mt-2 text-sm text-gray-600 dark:text-gray-400">
                Hello, @name!
            </p>
        }
    </PreviewContent>
</CodePreview>

@code {
    private string? name;
    private string formCode = @"<TailInput 
    Label=""Name"" 
    Value=""@name"" 
    ValueChanged=""v => name = v"" 
    Placeholder=""Enter your name"" />";
}
```

---

## ?? Styling

### Container
The component has a default container style:
```css
.rounded-lg 
.border border-gray-200 dark:border-gray-700 
.overflow-hidden 
.mb-6
```

### Custom Styling
Add custom classes via `CssClass` parameter:
```razor
<CodePreview 
    Title="Custom Styled" 
    Code="@code"
    CssClass="shadow-xl border-2 border-blue-500" />
```

---

## ? Features

### Copy Button
- Automatically copies code to clipboard
- Shows "Copied!" confirmation for 2 seconds
- Fallback for browsers without Clipboard API

### Syntax Highlighting
- Uses Tailwind's pre-configured code styling
- Dark background (`bg-gray-900`)
- Light text (`text-gray-100`)
- Language-specific classes (`language-razor`, `language-csharp`, etc.)

### Dark Mode Support
- All colors adapt to dark mode
- Preview background: `bg-white dark:bg-gray-800`
- Code background: Always `bg-gray-900`
- Border colors: `border-gray-200 dark:border-gray-700`

---

## ?? Layout Options

### Side-by-Side (Custom)
```razor
<div class="grid md:grid-cols-2 gap-4">
    <CodePreview Title="Version 1" Code="@v1Code" ShowCode="false">
        <PreviewContent>
            <ComponentV1 />
        </PreviewContent>
    </CodePreview>
    
    <CodePreview Title="Version 2" Code="@v2Code" ShowCode="false">
        <PreviewContent>
            <ComponentV2 />
        </PreviewContent>
    </CodePreview>
</div>
```

### Stacked
```razor
<CodePreview Title="Example 1" Code="@code1">
    <PreviewContent><Component1 /></PreviewContent>
</CodePreview>

<CodePreview Title="Example 2" Code="@code2">
    <PreviewContent><Component2 /></PreviewContent>
</CodePreview>
```

---

## ?? Tips & Best Practices

### 1. Keep Code in Sync
Store code as variables to maintain single source of truth:
```csharp
@code {
    private string code = @"<TailButton>Click</TailButton>";
}
```

### 2. Use Verbatim Strings
Use `@"..."` for multi-line code:
```csharp
private string multiLineCode = @"<div>
    <TailButton>Button 1</TailButton>
    <TailButton>Button 2</TailButton>
</div>";
```

### 3. Escape Quotes
Double quotes inside verbatim strings:
```csharp
private string withQuotes = @"<TailButton Variant=""ButtonVariant.Primary"">";
```

### 4. Add Descriptions
Provide context above CodePreview:
```razor
<p class="text-gray-600 dark:text-gray-400 mb-4">
    This example shows how to use variants.
</p>
<CodePreview Title="Button Variants" Code="@code">
    <!-- ... -->
</CodePreview>
```

### 5. Group Related Examples
```razor
<section class="mb-12">
    <h2 class="text-2xl font-bold mb-4">Button Sizes</h2>
    <p class="mb-6">Available sizes: xs, sm, md, lg, xl</p>
    
    <CodePreview Title="All Sizes" Code="@sizesCode">
        <!-- ... -->
    </CodePreview>
</section>
```

### 6. Show Interactive State
```razor
<CodePreview Title="Loading State" Code="@loadingCode">
    <PreviewContent>
        <TailButton IsLoading="@isLoading" OnClick="SimulateLoad">
            @(isLoading ? "Loading..." : "Click to Load")
        </TailButton>
    </PreviewContent>
</CodePreview>

@code {
    private bool isLoading = false;
    
    private async Task SimulateLoad()
    {
        isLoading = true;
        StateHasChanged();
        await Task.Delay(2000);
        isLoading = false;
        StateHasChanged();
    }
}
```

---

## ?? Troubleshooting

### Copy Button Not Working
**Problem:** Copy button doesn't copy code

**Solutions:**
1. Check browser supports Clipboard API
2. Ensure page is served over HTTPS (required for clipboard access)
3. Check browser console for errors

### Syntax Highlighting Not Applied
**Problem:** Code appears plain without colors

**Solution:**
1. Verify Tailwind CSS is loaded
2. Check code block has correct classes
3. Ensure no CSS conflicts

### Preview Not Showing
**Problem:** Preview section is blank

**Solutions:**
1. Check `ShowPreview` is `true`
2. Verify `PreviewContent` has content
3. Check for component errors in browser console

### Dark Mode Colors Wrong
**Problem:** Colors don't match theme

**Solutions:**
1. Ensure Tailwind dark mode is configured
2. Check `dark:` classes are present
3. Verify theme toggle is working

---

## ?? Complete Example

```razor
@page "/example"
@using Tail.Blazor.Buttons
@using Tail.Blazor.Docs.Shared

<div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold mb-8">Component Examples</h1>

    <!-- Example 1: Basic -->
    <section class="mb-12">
        <h2 class="text-3xl font-bold mb-4">Basic Button</h2>
        <p class="text-gray-600 dark:text-gray-400 mb-6">
            A simple button with primary variant.
        </p>
        
        <CodePreview Title="Primary Button" Code="@primaryCode">
            <PreviewContent>
                <TailButton Variant="ButtonVariant.Primary" OnClick="HandleClick">
                    Click Me
                </TailButton>
                @if (clicked)
                {
                    <p class="mt-2 text-green-600">Button clicked!</p>
                }
            </PreviewContent>
        </CodePreview>
    </section>

    <!-- Example 2: Interactive -->
    <section class="mb-12">
        <h2 class="text-3xl font-bold mb-4">Interactive Counter</h2>
        
        <CodePreview Title="Counter Example" Code="@counterCode">
            <PreviewContent>
                <div class="space-y-2">
                    <TailButton OnClick="Increment">Increment</TailButton>
                    <TailButton OnClick="Decrement" Variant="ButtonVariant.Danger">Decrement</TailButton>
                    <p class="text-lg">Count: @count</p>
                </div>
            </PreviewContent>
        </CodePreview>
    </section>

    <!-- Example 3: Code Only -->
    <section class="mb-12">
        <h2 class="text-3xl font-bold mb-4">Installation</h2>
        
        <CodePreview 
            Title="Package Installation" 
            Code="@installCode"
            ShowPreview="false"
            Language="bash" />
    </section>
</div>

@code {
    // State
    private bool clicked = false;
    private int count = 0;

    // Event handlers
    private void HandleClick() => clicked = true;
    private void Increment() => count++;
    private void Decrement() => count--;

    // Code samples
    private string primaryCode = @"<TailButton 
    Variant=""ButtonVariant.Primary"" 
    OnClick=""HandleClick"">
    Click Me
</TailButton>";

    private string counterCode = @"@code {
    private int count = 0;
    private void Increment() => count++;
    private void Decrement() => count--;
}

<TailButton OnClick=""Increment"">Increment</TailButton>
<TailButton OnClick=""Decrement"">Decrement</TailButton>
<p>Count: @count</p>";

    private string installCode = "dotnet add package Tail.Blazor.Buttons";
}
```

---

## ?? Summary

The `CodePreview` component provides:
- ? Live component demonstrations
- ? One-click code copying
- ? Syntax highlighting
- ? Dark mode support
- ? Flexible layout options
- ? Professional appearance
- ? Easy to use and maintain

Use it in all documentation pages for consistent, professional, and user-friendly examples!

---

**Status:** ? Ready to Use  
**Location:** `docs/Tail.Blazor.Docs/Shared/CodePreview.razor`  
**Version:** 1.0.0
