namespace Tail.Blazor.DateRangePicker;

/// <summary>
/// DateRangePicker size options.
/// </summary>
public enum DateRangePickerSize
{
    Xs,
    Sm,
    Md,
    Lg,
    Xl
}

/// <summary>
/// Hour format options for time selection.
/// </summary>
public enum HourFormat
{
    /// <summary>
    /// 12-hour format (1-12 with AM/PM)
    /// </summary>
    TwelveHour,
    /// <summary>
    /// 24-hour format (0-23)
    /// </summary>
    TwentyFourHour
}

/// <summary>
/// View mode for the date picker calendar.
/// </summary>
public enum DatePickerViewMode
{
    /// <summary>
    /// Calendar view showing days
    /// </summary>
    Days,
    /// <summary>
    /// Month selection view
    /// </summary>
    Months,
    /// <summary>
    /// Year selection view
    /// </summary>
    Years
}

/// <summary>
/// Selection mode for date picking.
/// </summary>
public enum DateSelectionMode
{
    /// <summary>
    /// Single date range selection
    /// </summary>
    SingleRange,
    /// <summary>
    /// Multiple date ranges selection
    /// </summary>
    MultipleRanges
}

/// <summary>
/// Display mode for the date picker.
/// </summary>
public enum DatePickerDisplayMode
{
    /// <summary>
    /// Show both input and calendar popup
    /// </summary>
    InputAndPopup,
    /// <summary>
    /// Show only input (no popup button)
    /// </summary>
    InputOnly,
    /// <summary>
    /// Show only calendar popup (no input box)
    /// </summary>
    PopupOnly
}

/// <summary>
/// Animation type for calendar popup.
/// </summary>
public enum CalendarAnimation
{
    /// <summary>
    /// No animation
    /// </summary>
    None,
    /// <summary>
    /// Fade animation
    /// </summary>
    Fade,
    /// <summary>
    /// Slide down animation
    /// </summary>
    SlideDown,
    /// <summary>
    /// Scale animation
    /// </summary>
    Scale
}

