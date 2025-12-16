// Theme toggle JavaScript module for Tail.Blazor
export function saveTheme(key, value) {
    try {
        localStorage.setItem(key, value);
    } catch (e) {
        console.error('Failed to save theme to localStorage:', e);
    }
}

export function getTheme(key) {
    try {
        return localStorage.getItem(key);
    } catch (e) {
        console.error('Failed to get theme from localStorage:', e);
        return null;
    }
}

export function applyTheme(isDark) {
    const html = document.documentElement;
    if (isDark) {
        html.classList.add('dark');
    } else {
        html.classList.remove('dark');
    }
}

export function prefersDarkMode() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
}

// Listen for system theme changes
export function watchSystemTheme(dotnetHelper, methodName) {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    
    const handler = (e) => {
        dotnetHelper.invokeMethodAsync(methodName, e.matches);
    };
    
    mediaQuery.addEventListener('change', handler);
    
    // Return cleanup function
    return () => {
        mediaQuery.removeEventListener('change', handler);
    };
}
