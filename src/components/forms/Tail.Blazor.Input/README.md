# Tail.Blazor.Input

Independent NuGet package for the TailInput component.

## Installation

```bash
dotnet add package Tail.Blazor.Input
```

## Usage

```razor
@using Tail.Blazor.Input

<TailInput @bind-Value="name" Label="Name" Placeholder="Enter your name" Required="true" />

<TailInput @bind-Value="email" Type="InputType.Email" Label="Email" />

<TailInput @bind-Value="password" Type="InputType.Password" Label="Password" ShowClearButton="true" />
```

## Features

- Multiple input types (Text, Password, Email, Number, Tel, Url, Search, Date, etc.)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label and help text support
- Icon support (start/end)
- Clear button
- Character count
- Validation error display
- Required field indicator
- Disabled and readonly states
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~4 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)
