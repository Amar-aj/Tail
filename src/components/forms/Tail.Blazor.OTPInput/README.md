# Tail.Blazor.OTPInput

Independent NuGet package for the TailOTPInput component.

## Installation

```bash
dotnet add package Tail.Blazor.OTPInput
```

## Usage

```razor
@using Tail.Blazor.OTPInput

<TailOTPInput @bind-Value="otpCode" Length="6" Label="Enter OTP Code" />
```

## Features

- One-time password input
- Multiple digit inputs
- Customizable length (default 6)
- 5 sizes (Xs, Sm, Md, Lg, Xl)
- Label support
- Help text
- Auto-focus next input
- Paste support
- Disabled state
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Package Size

~3 KB (ultra-lightweight)

## Dependencies

- Tail.Blazor.Core (required)

