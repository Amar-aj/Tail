// Image Zoom and Lightbox JavaScript

let imageZoomInstances = {};

export function initializeImageZoom(imageId, dotNetRef) {
    try {
        const image = document.getElementById(imageId);
        if (!image) return;

        imageZoomInstances[imageId] = {
            image: image,
            dotNetRef: dotNetRef,
            zoom: 1.0,
            panX: 0,
            panY: 0
        };
    } catch (error) {
        console.error('Error initializing image zoom:', error);
    }
}

export function zoomImage(imageId, factor) {
    try {
        const instance = imageZoomInstances[imageId];
        if (!instance) return;

        instance.zoom = Math.max(1.0, Math.min(5.0, instance.zoom * factor));
        updateImageTransform(instance);
    } catch (error) {
        console.error('Error zooming image:', error);
    }
}

export function panImage(imageId, deltaX, deltaY) {
    try {
        const instance = imageZoomInstances[imageId];
        if (!instance) return;

        instance.panX += deltaX;
        instance.panY += deltaY;
        updateImageTransform(instance);
    } catch (error) {
        console.error('Error panning image:', error);
    }
}

export function resetImageZoom(imageId) {
    try {
        const instance = imageZoomInstances[imageId];
        if (!instance) return;

        instance.zoom = 1.0;
        instance.panX = 0;
        instance.panY = 0;
        updateImageTransform(instance);
    } catch (error) {
        console.error('Error resetting image zoom:', error);
    }
}

function updateImageTransform(instance) {
    if (instance.image) {
        instance.image.style.transform = `scale(${instance.zoom}) translate(${instance.panX}px, ${instance.panY}px)`;
    }
}

export function enableLightboxKeyboardNavigation() {
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            // Close lightbox - handled by Blazor
        } else if (e.key === 'ArrowLeft') {
            // Previous image - handled by Blazor
        } else if (e.key === 'ArrowRight') {
            // Next image - handled by Blazor
        }
    });
}

export function disableLightboxKeyboardNavigation() {
    // Cleanup if needed
}

