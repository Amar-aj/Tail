// Audio Recorder JavaScript for recording, playback, and waveform visualization

let recorderInstances = {};

export function initializeRecorder(recorderId, waveformCanvasId, audioPlayerId, dotNetRef, format, quality) {
    try {
        const waveformCanvas = document.getElementById(waveformCanvasId);
        const audioPlayer = document.getElementById(audioPlayerId);

        recorderInstances[recorderId] = {
            mediaRecorder: null,
            audioChunks: [],
            stream: null,
            waveformCanvas: waveformCanvas,
            audioPlayer: audioPlayer,
            dotNetRef: dotNetRef,
            format: format,
            quality: quality,
            animationFrame: null
        };

        // Setup audio player event listeners
        if (audioPlayer) {
            audioPlayer.addEventListener('timeupdate', () => {
                if (dotNetRef) {
                    dotNetRef.invokeMethodAsync('OnPlaybackTimeUpdate', audioPlayer.currentTime, audioPlayer.duration || 0);
                }
            });

            audioPlayer.addEventListener('ended', () => {
                if (dotNetRef) {
                    dotNetRef.invokeMethodAsync('OnPlaybackEnded');
                }
            });
        }
    } catch (error) {
        console.error('Error initializing recorder:', error);
    }
}

export async function startRecording(recorderId) {
    try {
        const instance = recorderInstances[recorderId];
        if (!instance) return;

        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        instance.stream = stream;
        instance.audioChunks = [];

        const mimeType = getMimeType(instance.format);
        const options = {
            mimeType: mimeType,
            audioBitsPerSecond: getBitrate(instance.quality)
        };

        instance.mediaRecorder = new MediaRecorder(stream, options);

        instance.mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                instance.audioChunks.push(event.data);
            }
        };

        instance.mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(instance.audioChunks, { type: mimeType });
            const arrayBuffer = await audioBlob.arrayBuffer();
            const bytes = new Uint8Array(arrayBuffer);
            
            if (instance.dotNetRef) {
                instance.dotNetRef.invokeMethodAsync('OnRecordingTimeUpdate', 0);
            }

            // Convert to byte array for C#
            return Array.from(bytes);
        };

        // Start recording
        instance.mediaRecorder.start();

        // Start waveform visualization
        startWaveformVisualization(recorderId, stream);

        // Start time tracking
        let startTime = Date.now();
        const timeInterval = setInterval(() => {
            if (instance.mediaRecorder && instance.mediaRecorder.state === 'recording') {
                const elapsed = (Date.now() - startTime) / 1000;
                if (instance.dotNetRef) {
                    instance.dotNetRef.invokeMethodAsync('OnRecordingTimeUpdate', elapsed);
                }
            } else {
                clearInterval(timeInterval);
            }
        }, 100);
    } catch (error) {
        console.error('Error starting recording:', error);
    }
}

export async function stopRecording(recorderId) {
    try {
        const instance = recorderInstances[recorderId];
        if (!instance || !instance.mediaRecorder) return null;

        instance.mediaRecorder.stop();
        instance.stream.getTracks().forEach(track => track.stop());

        // Stop waveform visualization
        if (instance.animationFrame) {
            cancelAnimationFrame(instance.animationFrame);
        }

        // Wait for recording to stop and get the blob
        return new Promise((resolve) => {
            instance.mediaRecorder.onstop = async () => {
                const mimeType = getMimeType(instance.format);
                const audioBlob = new Blob(instance.audioChunks, { type: mimeType });
                const arrayBuffer = await audioBlob.arrayBuffer();
                const bytes = new Uint8Array(arrayBuffer);
                resolve(Array.from(bytes));
            };
        });
    } catch (error) {
        console.error('Error stopping recording:', error);
        return null;
    }
}

export function resumeRecording(recorderId) {
    try {
        const instance = recorderInstances[recorderId];
        if (!instance || !instance.mediaRecorder) return;

        if (instance.mediaRecorder.state === 'paused') {
            instance.mediaRecorder.resume();
        }
    } catch (error) {
        console.error('Error resuming recording:', error);
    }
}

export function startPlayback(audioPlayerId) {
    try {
        const audioPlayer = document.getElementById(audioPlayerId);
        if (audioPlayer) {
            audioPlayer.play();
        }
    } catch (error) {
        console.error('Error starting playback:', error);
    }
}

export function pausePlayback(audioPlayerId) {
    try {
        const audioPlayer = document.getElementById(audioPlayerId);
        if (audioPlayer) {
            audioPlayer.pause();
        }
    } catch (error) {
        console.error('Error pausing playback:', error);
    }
}

export function stopPlayback(audioPlayerId) {
    try {
        const audioPlayer = document.getElementById(audioPlayerId);
        if (audioPlayer) {
            audioPlayer.pause();
            audioPlayer.currentTime = 0;
        }
    } catch (error) {
        console.error('Error stopping playback:', error);
    }
}

export function clearRecording(recorderId) {
    try {
        const instance = recorderInstances[recorderId];
        if (instance) {
            if (instance.stream) {
                instance.stream.getTracks().forEach(track => track.stop());
            }
            if (instance.animationFrame) {
                cancelAnimationFrame(instance.animationFrame);
            }
            instance.audioChunks = [];
            instance.mediaRecorder = null;
            instance.stream = null;
        }
    } catch (error) {
        console.error('Error clearing recording:', error);
    }
}

export function downloadRecording(audioData, filename) {
    try {
        const blob = new Blob([new Uint8Array(audioData)], { type: 'audio/webm' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    } catch (error) {
        console.error('Error downloading recording:', error);
    }
}

export function createBlobUrl(audioData, mimeType) {
    try {
        const blob = new Blob([new Uint8Array(audioData)], { type: mimeType });
        return URL.createObjectURL(blob);
    } catch (error) {
        console.error('Error creating blob URL:', error);
        return '';
    }
}

function startWaveformVisualization(recorderId, stream) {
    try {
        const instance = recorderInstances[recorderId];
        if (!instance || !instance.waveformCanvas) return;

        const canvas = instance.waveformCanvas;
        const ctx = canvas.getContext('2d');
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const analyser = audioContext.createAnalyser();
        const source = audioContext.createMediaStreamSource(stream);

        analyser.fftSize = 256;
        source.connect(analyser);

        const bufferLength = analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);

        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;

        function draw() {
            if (instance.mediaRecorder && instance.mediaRecorder.state === 'recording') {
                instance.animationFrame = requestAnimationFrame(draw);

                analyser.getByteFrequencyData(dataArray);

                ctx.fillStyle = 'var(--color-surface)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                const barWidth = (canvas.width / bufferLength) * 2.5;
                let barHeight;
                let x = 0;

                for (let i = 0; i < bufferLength; i++) {
                    barHeight = (dataArray[i] / 255) * canvas.height;

                    ctx.fillStyle = 'var(--color-primary)';
                    ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);

                    x += barWidth + 1;
                }
            }
        }

        draw();
    } catch (error) {
        console.error('Error starting waveform visualization:', error);
    }
}

function getMimeType(format) {
    switch (format) {
        case 'WebM': return 'audio/webm';
        case 'Ogg': return 'audio/ogg';
        case 'Wav': return 'audio/wav';
        case 'Mp3': return 'audio/mpeg';
        default: return 'audio/webm';
    }
}

function getBitrate(quality) {
    switch (quality) {
        case 'Low': return 32000;
        case 'Medium': return 64000;
        case 'High': return 128000;
        default: return 64000;
    }
}

