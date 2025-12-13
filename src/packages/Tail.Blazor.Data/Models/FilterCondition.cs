namespace Tail.Blazor.Data.Models;

/// <summary>
/// Represents a filter condition for advanced filtering.
/// </summary>
public class FilterCondition
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Column { get; set; } = string.Empty;
    public FilterOperator Operator { get; set; } = FilterOperator.Contains;
    public object? Value { get; set; }
    public FilterLogic Logic { get; set; } = FilterLogic.And;
}

/// <summary>
/// Filter operators for comparison.
/// </summary>
public enum FilterOperator
{
    Equals,
    NotEquals,
    Contains,
    NotContains,
    StartsWith,
    EndsWith,
    GreaterThan,
    GreaterThanOrEqual,
    LessThan,
    LessThanOrEqual,
    IsEmpty,
    IsNotEmpty,
    In,
    NotIn
}

/// <summary>
/// Logic operator for combining filter conditions.
/// </summary>
public enum FilterLogic
{
    And,
    Or
}

/// <summary>
/// Represents a saved filter preset.
/// </summary>
public class FilterPreset
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Name { get; set; } = string.Empty;
    public string? Description { get; set; }
    public List<FilterCondition> Conditions { get; set; } = new();
    public DateTime CreatedAt { get; set; } = DateTime.Now;
}

