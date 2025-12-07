using Tail.Blazor.Core;
using Tail.Blazor.Core.Theme;

var builder = WebApplication.CreateBuilder(args);

// Add services
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();
builder.Services.AddTailBlazor(config =>
{
    config.ThemeMode = ThemeMode.Light;
    config.ThemePalette = ThemePalette.Blue;
    config.UseGradients = true;
});

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
