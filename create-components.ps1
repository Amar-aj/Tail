# Bulk Component Creation Script for Tail.Blazor
$baseComponentPath = "d:\Users\AMAR\source\repos\Tail\src\components"

$componentsToCreate = @(
    ("Stepper", "feedback"),
    ("SearchBar", "feedback"),
    ("Link", "navigation"),
    ("CodeBlock", "utils"),
    ("Form", "forms"),
    ("SelectBar", "forms"),
    ("ListBox", "forms"),
    ("HoverCard", "feedback"),
    ("Sheet", "layout"),
    ("CommandMenu", "navigation"),
    ("DataTable", "data"),
    ("Combobox", "forms"),
    ("TimeRangePicker", "forms"),
    ("FileDropZone", "forms"),
    ("ProgressRing", "feedback"),
    ("Wizard", "feedback"),
    ("LazyLoad", "utils"),
    ("Swipeable", "utils"),
    ("PullToRefresh", "utils"),
    ("SortableList", "data"),
    ("DropdownMenu", "navigation"),
    ("Toolbar", "layout"),
    ("TabBar", "navigation"),
    ("StepperInput", "forms"),
    ("CalendarView", "utils"),
    ("Skeleton", "feedback"),
    ("Badge", "feedback"),
    ("Tag", "feedback"),
    ("Alert", "feedback"),
    ("Progress", "feedback"),
    ("Modal", "feedback"),
    ("Drawer", "layout"),
    ("Sidebar", "layout"),
    ("Breadcrumb", "navigation"),
    ("Pagination", "navigation"),
    ("Tabs", "navigation"),
    ("Tree", "data"),
    ("Timeline", "data"),
    ("Carousel", "visualization"),
    ("Gallery", "visualization"),
    ("Grid", "layout"),
    ("Flex", "layout"),
    ("Container", "layout"),
    ("Divider", "layout"),
    ("Spacer", "layout"),
    ("Aspect", "layout"),
    ("VirtualKeyboard", "forms"),
    ("DrawingCanvas", "visualization"),
    ("Carousel3D", "visualization"),
    ("VideoPlayer", "visualization"),
    ("AudioPlayer", "visualization"),
    ("Heatmap", "visualization"),
    ("ColorPalette", "visualization"),
    ("Spinner", "feedback"),
    ("Loader", "feedback"),
    ("Shimmer", "feedback"),
    ("Wave", "feedback"),
    ("Ripple", "feedback"),
    ("Toast", "feedback"),
    ("Notification", "feedback"),
    ("Message", "feedback"),
    ("Input", "forms"),
    ("Textarea", "forms"),
    ("Checkbox", "forms"),
    ("Radio", "forms"),
    ("Toggle", "forms"),
    ("Slider", "forms"),
    ("RangeSlider", "forms"),
    ("DatePicker", "forms"),
    ("TimePicker", "forms"),
    ("ColorPicker", "forms")
)

function New-ComponentFiles {
    param(
        [string]$ComponentName,
        [string]$Category
    )
    
    $packageName = "Tail.Blazor.$ComponentName"
    $componentPath = Join-Path $baseComponentPath $Category "Tail.Blazor.$ComponentName"
    
    New-Item -ItemType Directory -Path $componentPath -Force | Out-Null
    
    $razorContent = "@namespace Tail.Blazor.$ComponentName`n@using Tail.Blazor.Core.Base`n`n<div class='component' @attributes='AdditionalAttributes'>`n    @ChildContent`n</div>`n`n@code {`n    [Parameter]`n    public RenderFragment ChildContent { get; set; }`n    [Parameter(CaptureUnmatchedValues = true)]`n    public Dictionary<string, object> AdditionalAttributes { get; set; }`n}"
    
    $razorFile = Join-Path $componentPath "$ComponentName.razor"
    [System.IO.File]::WriteAllText($razorFile, $razorContent)
    
    $csprojContent = "<Project Sdk='Microsoft.NET.Sdk.Razor'>`n<PropertyGroup>`n<TargetFrameworks>net8.0;net9.0;net10.0</TargetFrameworks>`n<Nullable>enable</Nullable>`n<ImplicitUsings>enable</ImplicitUsings>`n<Version>1.0.0</Version>`n<Authors>Tail.Blazor</Authors>`n<LangVersion>latest</LangVersion>`n<RazorLangVersion>7.0</RazorLangVersion>`n<IncludeSymbols>true</IncludeSymbols>`n<SymbolPackageFormat>snupkg</SymbolPackageFormat>`n</PropertyGroup>`n<ItemGroup>`n<SupportedPlatform Include='browser' />`n</ItemGroup>`n<ItemGroup>`n<PackageReference Include='Microsoft.AspNetCore.Components.Web' Version='8.0.0' />`n</ItemGroup>`n<ItemGroup>`n<ProjectReference Include='..\..\core\Tail.Blazor.Core.Base\Tail.Blazor.Core.Base.csproj' />`n</ItemGroup>`n</Project>"
    
    $csprojFile = Join-Path $componentPath "$packageName.csproj"
    [System.IO.File]::WriteAllText($csprojFile, $csprojContent)
}

$count = 0
foreach ($comp in $componentsToCreate) {
    New-ComponentFiles -ComponentName $comp[0] -Category $comp[1]
    $count++
}

Write-Host "Created $count components successfully" -ForegroundColor Green
