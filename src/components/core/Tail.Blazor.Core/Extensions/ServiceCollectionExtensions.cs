using Microsoft.Extensions.DependencyInjection;
using Tail.Blazor.Core.Theme;

namespace Tail.Blazor.Core.Extensions;

/// <summary>
/// Extension methods for configuring Tail.Blazor services
/// </summary>
public static class ServiceCollectionExtensions
{
    /// <summary>
    /// Adds Tail.Blazor theme services to the service collection
    /// </summary>
    public static IServiceCollection AddTailBlazorTheme(this IServiceCollection services)
    {
        // Register ThemeEngine as Singleton
        services.AddSingleton<ThemeEngine>();
        services.AddScoped<ThemeService>();
        return services;
    }
}
