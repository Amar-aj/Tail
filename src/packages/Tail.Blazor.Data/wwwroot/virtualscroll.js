// Virtual Scroll JavaScript for viewport-based rendering

let scrollObservers = new Map();

export function initializeVirtualScroll(containerId, dotNetRef) {
    try {
        const container = document.getElementById(containerId);
        if (!container) return;
        
        // Throttled scroll handler
        let scrollTimeout;
        const handleScroll = () => {
            if (scrollTimeout) {
                clearTimeout(scrollTimeout);
            }
            
            scrollTimeout = setTimeout(() => {
                const scrollTop = container.scrollTop;
                if (dotNetRef) {
                    dotNetRef.invokeMethodAsync('OnScroll', scrollTop);
                }
            }, 10); // Throttle to ~100fps
        };
        
        container.addEventListener('scroll', handleScroll, { passive: true });
        
        // Store observer info
        scrollObservers.set(containerId, {
            container,
            dotNetRef,
            handler: handleScroll
        });
        
        // Initial scroll position
        const scrollTop = container.scrollTop;
        if (dotNetRef) {
            dotNetRef.invokeMethodAsync('OnScroll', scrollTop);
        }
    } catch (error) {
        console.error('Error initializing virtual scroll:', error);
    }
}

export function getScrollTop(containerId) {
    try {
        const container = document.getElementById(containerId);
        if (!container) return 0;
        return container.scrollTop;
    } catch (error) {
        console.error('Error getting scroll top:', error);
        return 0;
    }
}

export function disposeVirtualScroll(containerId) {
    try {
        const observer = scrollObservers.get(containerId);
        if (observer) {
            observer.container.removeEventListener('scroll', observer.handler);
            scrollObservers.delete(containerId);
        }
    } catch (error) {
        console.error('Error disposing virtual scroll:', error);
    }
}

