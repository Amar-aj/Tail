export function attachDropHandler(dropZoneId, inputId) {
    const dz = document.getElementById(dropZoneId);
    const input = document.getElementById(inputId);
    if (!dz || !input) return;

    const prevent = (e) => { e.preventDefault(); e.stopPropagation(); };
    const onDrop = (e) => {
        prevent(e);
        const dt = e.dataTransfer;
        if (dt && dt.files && dt.files.length) {
            try {
                // Assign files to input and dispatch change
                input.files = dt.files;
                const ev = new Event('change', { bubbles: true });
                input.dispatchEvent(ev);
            }
            catch (err) {
                console.warn('Unable to assign dropped files to input:', err);
            }
        }
    };

    dz.addEventListener('drop', onDrop);
    dz.addEventListener('dragover', prevent);
    dz.addEventListener('dragenter', prevent);
    dz.addEventListener('dragleave', prevent);

    // store handlers for cleanup
    dz.__tailFileUpload = { onDrop, prevent };
}

export function detachDropHandler(dropZoneId) {
    const dz = document.getElementById(dropZoneId);
    if (!dz || !dz.__tailFileUpload) return;
    const { onDrop, prevent } = dz.__tailFileUpload;
    dz.removeEventListener('drop', onDrop);
    dz.removeEventListener('dragover', prevent);
    dz.removeEventListener('dragenter', prevent);
    dz.removeEventListener('dragleave', prevent);
    delete dz.__tailFileUpload;
}
