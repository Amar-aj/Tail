using System.Collections.Concurrent;

namespace Tail.Blazor.Icons;

/// <summary>
/// Registry for custom SVG icons.
/// </summary>
public class IconRegistry
{
    private static readonly ConcurrentDictionary<string, string> _icons = new();

    /// <summary>
    /// Registers a custom icon.
    /// </summary>
    public static void Register(string name, string svgPath)
    {
        _icons[name] = svgPath;
    }

    /// <summary>
    /// Gets a registered icon path.
    /// </summary>
    public static string? Get(string name)
    {
        return _icons.TryGetValue(name, out var path) ? path : null;
    }

    /// <summary>
    /// Checks if an icon is registered.
    /// </summary>
    public static bool IsRegistered(string name)
    {
        return _icons.ContainsKey(name);
    }

    /// <summary>
    /// Removes an icon from the registry.
    /// </summary>
    public static bool Unregister(string name)
    {
        return _icons.TryRemove(name, out _);
    }

    /// <summary>
    /// Clears all registered icons.
    /// </summary>
    public static void Clear()
    {
        _icons.Clear();
    }
}

