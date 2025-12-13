// Scroll Spy JavaScript for tracking scroll position and highlighting active sections

let scrollSpyInstances = {};

export function initializeScrollSpy(scrollSpyId, dotNetRef, targetIds, scrollOffset, threshold) {
    try {
        const observerOptions = {
            root: null, // viewport
            rootMargin: `-${scrollOffset}px 0px -50% 0px`,
            threshold: threshold / 100
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const targetId = entry.target.id;
                    dotNetRef.invokeMethodAsync('OnSectionActivated', targetId);
                }
            });
        }, observerOptions);

        // Observe all target elements
        targetIds.forEach(targetId => {
            const element = document.getElementById(targetId);
            if (element) {
                observer.observe(element);
            }
        });

        scrollSpyInstances[scrollSpyId] = {
            observer: observer,
            targetIds: targetIds,
            dotNetRef: dotNetRef
        };
    } catch (error) {
        console.error('Error initializing scroll spy:', error);
    }
}

export function scrollToElement(targetId, offset, mode) {
    try {
        const element = document.getElementById(targetId);
        if (!element) return;

        const elementPosition = element.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - offset;

        const scrollOptions = {
            top: offsetPosition,
            behavior: mode === 'Smooth' ? 'smooth' : 'auto'
        };

        window.scrollTo(scrollOptions);
    } catch (error) {
        console.error('Error scrolling to element:', error);
    }
}

export function disposeScrollSpy(scrollSpyId) {
    try {
        const instance = scrollSpyInstances[scrollSpyId];
        if (instance && instance.observer) {
            instance.observer.disconnect();
            delete scrollSpyInstances[scrollSpyId];
        }
    } catch (error) {
        console.error('Error disposing scroll spy:', error);
    }
}

