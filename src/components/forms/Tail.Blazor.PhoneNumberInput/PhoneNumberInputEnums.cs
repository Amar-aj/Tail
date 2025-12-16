namespace Tail.Blazor.PhoneNumberInput;

/// <summary>
/// PhoneNumberInput size options.
/// </summary>
public enum PhoneNumberInputSize
{
    Xs,
    Sm,
    Md,
    Lg,
    Xl
}

/// <summary>
/// Country code information.
/// </summary>
public class CountryCode
{
    public string Code { get; set; } = string.Empty;
    public string Flag { get; set; } = string.Empty;
    public string Country { get; set; } = string.Empty;
}

