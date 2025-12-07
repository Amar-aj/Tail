namespace Tail.Blazor.Charts.Models;

/// <summary>
/// Represents a data point in a chart.
/// </summary>
public class ChartDataPoint
{
    /// <summary>
    /// The label for this data point.
    /// </summary>
    public string Label { get; set; } = string.Empty;
    
    /// <summary>
    /// The numeric value.
    /// </summary>
    public double Value { get; set; }
    
    /// <summary>
    /// Optional color for this data point.
    /// </summary>
    public string? Color { get; set; }
    
    /// <summary>
    /// Optional additional data.
    /// </summary>
    public Dictionary<string, object>? Metadata { get; set; }
}

/// <summary>
/// Represents a series of data points.
/// </summary>
public class ChartSeries
{
    /// <summary>
    /// Name of the series.
    /// </summary>
    public string Name { get; set; } = string.Empty;
    
    /// <summary>
    /// Data points in this series.
    /// </summary>
    public List<ChartDataPoint> Data { get; set; } = new();
    
    /// <summary>
    /// Color for this series.
    /// </summary>
    public string? Color { get; set; }
}
