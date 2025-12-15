namespace Tail.Blazor.Docs.Pages.Docs.Scope.Models;

// Supporting classes for architecture analysis
public class PackageArchitecture
{
    public string Type { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public List<string> Structure { get; set; } = new();
    public List<string> Pros { get; set; } = new();
    public List<string> Cons { get; set; } = new();
    public string ExampleUsage { get; set; } = string.Empty;
    public string BundleSizeExample { get; set; } = string.Empty;
}

public class ArchitectureComparison
{
    public List<SizeComparison> SizeComparison { get; set; } = new();
    public List<PerformanceComparison> PerformanceComparison { get; set; } = new();
    public string RecommendedApproach { get; set; } = string.Empty;
    public List<string> ImplementationStrategy { get; set; } = new();
    public string PropertiesManagementRecommendation { get; set; } = string.Empty;
}

public class SizeComparison
{
    public string Scenario { get; set; } = string.Empty;
    public string PackageBased { get; set; } = string.Empty;
    public string ComponentBased { get; set; } = string.Empty;
    public string Savings { get; set; } = string.Empty;
}

public class PerformanceComparison
{
    public string Metric { get; set; } = string.Empty;
    public string PackageBased { get; set; } = string.Empty;
    public string ComponentBased { get; set; } = string.Empty;
    public string Winner { get; set; } = string.Empty;
}

public class ImplementationPlan
{
    public string Title { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public List<ImplementationPhase> Phases { get; set; } = new();
    public List<string> KeyPrinciples { get; set; } = new();
    public List<string> Benefits { get; set; } = new();
}

public class ImplementationPhase
{
    public string Name { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public List<string> Tasks { get; set; } = new();
    public string EstimatedDuration { get; set; } = string.Empty;
    public string Status { get; set; } = "Planned";
}

public class FolderStructure
{
    public string RootPath { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public List<FolderItem> Structure { get; set; } = new();
}

public class FolderItem
{
    public string Name { get; set; } = string.Empty;
    public string Type { get; set; } = "Folder"; // Folder, File, Component
    public string Description { get; set; } = string.Empty;
    public List<FolderItem> Children { get; set; } = new();
    public string Size { get; set; } = string.Empty;
}

