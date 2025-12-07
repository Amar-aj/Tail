using Microsoft.AspNetCore.Components;

namespace Tail.Blazor.Data.Models;

/// <summary>
/// Represents a node in a tree structure.
/// </summary>
/// <typeparam name="TValue">The type of the value.</typeparam>
public class TreeNode<TValue>
{
    private bool _isExpanded;
    private bool _isSelected;
    private bool _isDisabled;
    
    /// <summary>
    /// Node value.
    /// </summary>
    public TValue? Value { get; set; }
    
    /// <summary>
    /// Display text.
    /// </summary>
    public string Text { get; set; } = string.Empty;
    
    /// <summary>
    /// Optional icon.
    /// </summary>
    public string? Icon { get; set; }
    
    /// <summary>
    /// Whether this node is expanded.
    /// </summary>
    public bool IsExpanded
    {
        get => _isExpanded;
        set => _isExpanded = value;
    }
    
    /// <summary>
    /// Alias for IsExpanded (for compatibility).
    /// </summary>
    public bool Expanded
    {
        get => _isExpanded;
        set => _isExpanded = value;
    }
    
    /// <summary>
    /// Whether this node is selected.
    /// </summary>
    public bool IsSelected
    {
        get => _isSelected;
        set => _isSelected = value;
    }
    
    /// <summary>
    /// Alias for IsSelected (for compatibility).
    /// </summary>
    public bool Selected
    {
        get => _isSelected;
        set => _isSelected = value;
    }
    
    /// <summary>
    /// Whether this node is disabled.
    /// </summary>
    public bool IsDisabled
    {
        get => _isDisabled;
        set => _isDisabled = value;
    }
    
    /// <summary>
    /// Alias for IsDisabled (for compatibility).
    /// </summary>
    public bool Disabled
    {
        get => _isDisabled;
        set => _isDisabled = value;
    }
    
    /// <summary>
    /// Child nodes.
    /// </summary>
    public List<TreeNode<TValue>> Children { get; set; } = new();
    
    /// <summary>
    /// Custom content template.
    /// </summary>
    public RenderFragment? ContentTemplate { get; set; }
    
    /// <summary>
    /// Additional metadata.
    /// </summary>
    public Dictionary<string, object>? Metadata { get; set; }
}

/// <summary>
/// Non-generic TreeNode for simpler usage.
/// </summary>
public class TreeNode : TreeNode<string>
{
    /// <summary>
    /// Child nodes (non-generic version).
    /// </summary>
    public new List<TreeNode> Children { get; set; } = new();
}
