using Microsoft.JSInterop;

namespace Tail.Blazor.Utils;

/// <summary>
/// JavaScript interop helpers for Tail.Blazor components.
/// </summary>
public class JsInterop : IAsyncDisposable
{
    private readonly Lazy<Task<IJSObjectReference>> _moduleTask;
    private readonly IJSRuntime _jsRuntime;

    public JsInterop(IJSRuntime jsRuntime)
    {
        _jsRuntime = jsRuntime;
        _moduleTask = new Lazy<Task<IJSObjectReference>>(() =>
            jsRuntime.InvokeAsync<IJSObjectReference>("import", "./_content/Tail.Blazor.Utils/tailblazor.js").AsTask());
    }

    /// <summary>
    /// Copies text to clipboard.
    /// </summary>
    public async ValueTask<bool> CopyToClipboardAsync(string text)
    {
        try
        {
            var module = await _moduleTask.Value;
            return await module.InvokeAsync<bool>("copyToClipboard", text);
        }
        catch
        {
            return false;
        }
    }

    /// <summary>
    /// Focuses an element by ID.
    /// </summary>
    public async ValueTask FocusElementAsync(string elementId)
    {
        try
        {
            var module = await _moduleTask.Value;
            await module.InvokeVoidAsync("focusElement", elementId);
        }
        catch
        {
            // Ignore errors
        }
    }

    /// <summary>
    /// Scrolls an element into view.
    /// </summary>
    public async ValueTask ScrollIntoViewAsync(string elementId, bool smooth = true)
    {
        try
        {
            var module = await _moduleTask.Value;
            await module.InvokeVoidAsync("scrollIntoView", elementId, smooth);
        }
        catch
        {
            // Ignore errors
        }
    }

    /// <summary>
    /// Gets element dimensions.
    /// </summary>
    public async ValueTask<ElementDimensions> GetElementDimensionsAsync(string elementId)
    {
        try
        {
            var module = await _moduleTask.Value;
            return await module.InvokeAsync<ElementDimensions>("getElementDimensions", elementId);
        }
        catch
        {
            return new ElementDimensions();
        }
    }

    /// <summary>
    /// Sets up ResizeObserver for an element.
    /// </summary>
    public async ValueTask<string> ObserveResizeAsync(string elementId, DotNetObjectReference<ResizeObserver> observer)
    {
        try
        {
            var module = await _moduleTask.Value;
            return await module.InvokeAsync<string>("observeResize", elementId, observer);
        }
        catch
        {
            return string.Empty;
        }
    }

    /// <summary>
    /// Disposes the JS module.
    /// </summary>
    public async ValueTask DisposeAsync()
    {
        if (_moduleTask.IsValueCreated)
        {
            var module = await _moduleTask.Value;
            await module.DisposeAsync();
        }
    }
}

public class ElementDimensions
{
    public double Width { get; set; }
    public double Height { get; set; }
    public double Top { get; set; }
    public double Left { get; set; }
}

public class ResizeObserver
{
    [JSInvokable]
    public void OnResize(ElementDimensions dimensions)
    {
        OnResizeCallback?.Invoke(dimensions);
    }

    public Action<ElementDimensions>? OnResizeCallback { get; set; }
}

