using Tail.Blazor.Core;
using System.Text.Json;
using System.Text.Json.Serialization;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();
builder.Services.AddTailBlazor();

// Configure JSON serialization to work with trimming
builder.Services.Configure<JsonSerializerOptions>(options =>
{
    options.TypeInfoResolverChain.Add(AppJsonSerializerContext.Default);
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();

app.MapBlazorHub();
app.MapFallbackToPage("/_Host");

app.Run();

// JSON serialization context for source generation
[JsonSerializable(typeof(Dictionary<string, object>))]
[JsonSerializable(typeof(string))]
internal partial class AppJsonSerializerContext : JsonSerializerContext
{
}
