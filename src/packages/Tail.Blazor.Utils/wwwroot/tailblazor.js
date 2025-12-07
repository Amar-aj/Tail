// Tail.Blazor Utils - Minimal JavaScript (< 5 KB)

// Copy to clipboard
window.copyToClipboard = async (text) => {
    try {
        await navigator.clipboard.writeText(text);
        return true;
    } catch (err) {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'fixed';
        textArea.style.opacity = '0';
        document.body.appendChild(textArea);
        textArea.select();
        try {
            document.execCommand('copy');
            document.body.removeChild(textArea);
            return true;
        } catch (e) {
            document.body.removeChild(textArea);
            return false;
        }
    }
};

// Focus element
window.focusElement = (elementId) => {
    const element = document.getElementById(elementId);
    if (element) {
        element.focus();
    }
};

// Scroll into view
window.scrollIntoView = (elementId, smooth = true) => {
    const element = document.getElementById(elementId);
    if (element) {
        element.scrollIntoView({ behavior: smooth ? 'smooth' : 'auto', block: 'nearest' });
    }
};

// Get element dimensions
window.getElementDimensions = (elementId) => {
    const element = document.getElementById(elementId);
    if (element) {
        const rect = element.getBoundingClientRect();
        return {
            width: rect.width,
            height: rect.height,
            top: rect.top,
            left: rect.left
        };
    }
    return { width: 0, height: 0, top: 0, left: 0 };
};

// ResizeObserver setup
window.observeResize = (elementId, dotNetRef) => {
    const element = document.getElementById(elementId);
    if (!element) return '';
    
    const observer = new ResizeObserver(entries => {
        for (let entry of entries) {
            const rect = entry.contentRect;
            dotNetRef.invokeMethodAsync('OnResize', {
                width: rect.width,
                height: rect.height,
                top: rect.top,
                left: rect.left
            });
        }
    });
    
    observer.observe(element);
    return elementId; // Return ID for cleanup
};

