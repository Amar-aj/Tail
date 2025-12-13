// Image Cropper JavaScript for crop, zoom, rotate functionality

let cropperInstances = {};

export function initializeCropper(cropperId, imageId, previewCanvasId, dotNetRef) {
    try {
        const cropper = document.getElementById(cropperId);
        const image = document.getElementById(imageId);
        const previewCanvas = document.getElementById(previewCanvasId);

        if (!cropper || !image) return;

        // Store instance
        cropperInstances[cropperId] = {
            image: image,
            previewCanvas: previewCanvas,
            dotNetRef: dotNetRef,
            zoom: 1.0,
            rotation: 0,
            cropX: 0,
            cropY: 0,
            cropWidth: 0,
            cropHeight: 0
        };

        // Initialize image load handler
        image.onload = () => {
            updateCropper(cropperId, imageId, 1.0, 0, 0, false, 'Fit');
        };
    } catch (error) {
        console.error('Error initializing cropper:', error);
    }
}

export function updateCropper(cropperId, imageId, zoom, rotation, aspectRatio, locked, zoomMode) {
    try {
        const instance = cropperInstances[cropperId];
        if (!instance) return;

        const image = instance.image;
        const cropper = document.getElementById(cropperId);
        if (!image || !cropper) return;

        instance.zoom = zoom;
        instance.rotation = rotation;

        // Apply zoom and rotation
        const transform = `scale(${zoom}) rotate(${rotation}deg)`;
        image.style.transform = transform;
        image.style.transformOrigin = 'center center';

        // Calculate crop area
        const cropperRect = cropper.getBoundingClientRect();
        const imageRect = image.getBoundingClientRect();

        // Simple crop area calculation (center crop)
        let cropWidth = Math.min(cropperRect.width, imageRect.width * zoom);
        let cropHeight = Math.min(cropperRect.height, imageRect.height * zoom);

        if (aspectRatio > 0 && locked) {
            if (cropWidth / cropHeight > aspectRatio) {
                cropWidth = cropHeight * aspectRatio;
            } else {
                cropHeight = cropWidth / aspectRatio;
            }
        }

        const cropX = (cropperRect.width - cropWidth) / 2;
        const cropY = (cropperRect.height - cropHeight) / 2;

        instance.cropX = cropX;
        instance.cropY = cropY;
        instance.cropWidth = cropWidth;
        instance.cropHeight = cropHeight;

        // Draw crop overlay (optional visual indicator)
        drawCropOverlay(cropper, cropX, cropY, cropWidth, cropHeight);
    } catch (error) {
        console.error('Error updating cropper:', error);
    }
}

function drawCropOverlay(cropper, x, y, width, height) {
    // Remove existing overlay
    const existing = cropper.querySelector('.crop-overlay');
    if (existing) existing.remove();

    // Create overlay
    const overlay = document.createElement('div');
    overlay.className = 'crop-overlay';
    overlay.style.cssText = `
        position: absolute;
        left: ${x}px;
        top: ${y}px;
        width: ${width}px;
        height: ${height}px;
        border: 2px dashed var(--color-primary);
        pointer-events: none;
        z-index: 10;
    `;
    cropper.appendChild(overlay);
}

export function updatePreview(cropperId, imageId, previewCanvasId, previewWidth, previewHeight) {
    try {
        const instance = cropperInstances[cropperId];
        if (!instance) return;

        const image = instance.image;
        const previewCanvas = document.getElementById(previewCanvasId);
        if (!image || !previewCanvas) return;

        const canvas = previewCanvas;
        const ctx = canvas.getContext('2d');
        canvas.width = previewWidth;
        canvas.height = previewHeight;

        // Calculate source crop area
        const sourceX = instance.cropX / instance.zoom;
        const sourceY = instance.cropY / instance.zoom;
        const sourceWidth = instance.cropWidth / instance.zoom;
        const sourceHeight = instance.cropHeight / instance.zoom;

        // Draw cropped image to canvas
        ctx.save();
        ctx.translate(previewWidth / 2, previewHeight / 2);
        ctx.rotate((instance.rotation * Math.PI) / 180);
        ctx.drawImage(
            image,
            sourceX, sourceY, sourceWidth, sourceHeight,
            -previewWidth / 2, -previewHeight / 2, previewWidth, previewHeight
        );
        ctx.restore();
    } catch (error) {
        console.error('Error updating preview:', error);
    }
}

export function getCroppedImage(cropperId, imageId) {
    try {
        const instance = cropperInstances[cropperId];
        if (!instance) return null;

        const image = instance.image;
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');

        // Set canvas size to crop dimensions
        canvas.width = instance.cropWidth;
        canvas.height = instance.cropHeight;

        // Calculate source crop area
        const sourceX = instance.cropX / instance.zoom;
        const sourceY = instance.cropY / instance.zoom;
        const sourceWidth = instance.cropWidth / instance.zoom;
        const sourceHeight = instance.cropHeight / instance.zoom;

        // Draw cropped and rotated image
        ctx.save();
        ctx.translate(canvas.width / 2, canvas.height / 2);
        ctx.rotate((instance.rotation * Math.PI) / 180);
        ctx.drawImage(
            image,
            sourceX, sourceY, sourceWidth, sourceHeight,
            -canvas.width / 2, -canvas.height / 2, canvas.width, canvas.height
        );
        ctx.restore();

        // Convert to blob and return as base64
        return new Promise((resolve) => {
            canvas.toBlob((blob) => {
                const reader = new FileReader();
                reader.onloadend = () => {
                    const base64 = reader.result.split(',')[1];
                    const bytes = atob(base64);
                    const byteArray = new Uint8Array(bytes.length);
                    for (let i = 0; i < bytes.length; i++) {
                        byteArray[i] = bytes.charCodeAt(i);
                    }
                    resolve(Array.from(byteArray));
                };
                reader.readAsDataURL(blob);
            }, 'image/png');
        });
    } catch (error) {
        console.error('Error getting cropped image:', error);
        return null;
    }
}

