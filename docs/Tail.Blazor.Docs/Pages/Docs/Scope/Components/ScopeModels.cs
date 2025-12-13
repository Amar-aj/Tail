namespace Tail.Blazor.Docs.Pages.Docs.Scope.Components;

public class PackageDetail
{
    public string Name { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public int ComponentCount { get; set; }
    public List<string> Components { get; set; } = new();
    public List<string> KeyFeatures { get; set; } = new();
    public int ParameterCount { get; set; }
    public int EventCount { get; set; }
    public int MethodCount { get; set; }
    public bool DocsSynced { get; set; }
    public bool HasExamples { get; set; }
    public bool HasApiReference { get; set; }
    public bool HasCodeSamples { get; set; }
}

public class MissingFeature
{
    public string Icon { get; set; } = string.Empty;
    public string Name { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public string Category { get; set; } = string.Empty;
    public string Priority { get; set; } = string.Empty;
}

public class PackageStatus
{
    public string Name { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public int ComponentCount { get; set; }
    public string Status { get; set; } = "Planned";
}

public class FeatureStatus
{
    public string Name { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public bool IsComplete { get; set; }
}

public class UpdateInfo
{
    public string Title { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public DateTime Date { get; set; }
}

