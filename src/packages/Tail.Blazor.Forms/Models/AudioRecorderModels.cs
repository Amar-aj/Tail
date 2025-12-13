namespace Tail.Blazor.Forms.Models;

/// <summary>
/// Audio recorder state.
/// </summary>
public enum AudioRecorderState
{
    Idle,
    Recording,
    Paused,
    Playing,
    Stopped
}

/// <summary>
/// Audio recorder format.
/// </summary>
public enum AudioRecorderFormat
{
    WebM,
    Ogg,
    Wav,
    Mp3
}

/// <summary>
/// Audio recorder quality.
/// </summary>
public enum AudioRecorderQuality
{
    Low,
    Medium,
    High
}

