using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Data.Models;

/// <summary>
/// Represents a column in a data grid.
/// </summary>
public class DataGridColumn
{
    /// <summary>
    /// Column title displayed in header.
    /// </summary>
    public string Title { get; set; } = string.Empty;
    
    /// <summary>
    /// Property name to bind to.
    /// </summary>
    public string Property { get; set; } = string.Empty;
    
    /// <summary>
    /// Optional column width (e.g., "100px", "20%").
    /// </summary>
    public string? Width { get; set; }
    
    /// <summary>
    /// Whether this column is sortable.
    /// </summary>
    public bool Sortable { get; set; } = true;
    
    /// <summary>
    /// Whether this column is filterable.
    /// </summary>
    public bool Filterable { get; set; } = true;
    
    /// <summary>
    /// CSS classes to apply to cells in this column.
    /// </summary>
    public string? CssClass { get; set; }
    
    /// <summary>
    /// Custom header template.
    /// </summary>
    public RenderFragment<DataGridColumn>? HeaderTemplate { get; set; }
    
    /// <summary>
    /// Custom cell template.
    /// </summary>
    public RenderFragment<object>? CellTemplate { get; set; }
    
    /// <summary>
    /// Format string for cell values.
    /// </summary>
    public string? Format { get; set; }
    
    /// <summary>
    /// Whether this column is frozen (sticky) on the left side.
    /// </summary>
    public bool Frozen { get; set; } = false;
    
    /// <summary>
    /// Group name for column grouping. Columns with the same group name will be grouped together.
    /// </summary>
    public string? Group { get; set; }
    
    /// <summary>
    /// Whether this column is editable inline.
    /// </summary>
    public bool Editable { get; set; } = false;
    
    /// <summary>
    /// Column span for header (for grouping).
    /// </summary>
    public int ColSpan { get; set; } = 1;
}

/// <summary>
/// Selection mode for data grid.
/// </summary>
public enum SelectionMode
{
    /// <summary>
    /// No selection.
    /// </summary>
    None,
    
    /// <summary>
    /// Single row selection.
    /// </summary>
    Single,
    
    /// <summary>
    /// Multiple row selection.
    /// </summary>
    Multiple
}

/// <summary>
/// Sort direction.
/// </summary>
public enum SortDirection
{
    /// <summary>
    /// No sorting.
    /// </summary>
    None,
    
    /// <summary>
    /// Ascending order.
    /// </summary>
    Ascending,
    
    /// <summary>
    /// Descending order.
    /// </summary>
    Descending
}
