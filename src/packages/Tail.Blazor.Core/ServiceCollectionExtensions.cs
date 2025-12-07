using Microsoft.Extensions.DependencyInjection;

namespace Tail.Blazor.Core;

/// <summary>
/// Extension methods for configuring Tail.Blazor services.
/// </summary>
public static class ServiceCollectionExtensions
{
    /// <summary>
    /// Adds Tail.Blazor services to the service collection.
    /// </summary>
    /// <param name="services">The service collection.</param>
    /// <param name="configure">Optional configuration action.</param>
    /// <returns>The service collection for chaining.</returns>
    public static IServiceCollection AddTailBlazor(
        this IServiceCollection services,
        Action<TailBlazorConfig>? configure = null)
    {
        var config = new TailBlazorConfig();
        configure?.Invoke(config);
        
        services.AddSingleton(config);
        
        return services;
    }
}

