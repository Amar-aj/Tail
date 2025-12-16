namespace Tail.Blazor.Docs.Shared;

/// <summary>
/// Represents a navigation menu item.
/// </summary>
public class NavMenuItem
{
    public string? Href { get; set; }
    public string? Text { get; set; }
    public string? Icon { get; set; }
    public string? Description { get; set; }
    public bool ExactMatch { get; set; }
    public bool IsDivider { get; set; }
    public List<NavMenuItem>? Children { get; set; }
}

