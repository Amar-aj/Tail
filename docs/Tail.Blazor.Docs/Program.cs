using Tail.Blazor.Core;
using Tail.Blazor.Core.Theme;

var builder = WebApplication.CreateBuilder(args);

// Add services
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();
builder.Services.AddTailBlazor();

// Register ThemeEngine as Singleton (required for ThemeProvider)
builder.Services.AddSingleton<ThemeEngine>();

// Add Theme Service with localStorage support
builder.Services.AddScoped<ThemeService>();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();

app.MapRazorPages();
app.MapBlazorHub();
app.MapFallbackToPage("/_Host");

app.Run();
