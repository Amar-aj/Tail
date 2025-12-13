// Tour JavaScript for element positioning and highlighting

export function getElementDimensions(selector) {
    try {
        const element = document.querySelector(selector);
        if (!element) {
            return { width: 0, height: 0, top: 0, left: 0 };
        }
        
        const rect = element.getBoundingClientRect();
        return {
            width: rect.width,
            height: rect.height,
            top: rect.top + window.scrollY,
            left: rect.left + window.scrollX
        };
    } catch (error) {
        return { width: 0, height: 0, top: 0, left: 0 };
    }
}

export function scrollIntoView(selector, smooth = true) {
    try {
        const element = document.querySelector(selector);
        if (element) {
            element.scrollIntoView({ behavior: smooth ? 'smooth' : 'auto', block: 'center', inline: 'center' });
        }
    } catch (error) {
        console.error('Error scrolling to element:', error);
    }
}

export function updateHighlight(highlightId, dimensions) {
    try {
        const highlight = document.getElementById(highlightId);
        if (highlight && dimensions) {
            highlight.style.left = `${dimensions.left}px`;
            highlight.style.top = `${dimensions.top}px`;
            highlight.style.width = `${dimensions.width}px`;
            highlight.style.height = `${dimensions.height}px`;
        }
    } catch (error) {
        console.error('Error updating highlight:', error);
    }
}

export function updateTooltipPosition(tooltipId, targetSelector, placement, dimensions) {
    try {
        const tooltip = document.getElementById(tooltipId);
        const target = document.querySelector(targetSelector);
        
        if (!tooltip || !target || !dimensions) return;
        
        const tooltipRect = tooltip.getBoundingClientRect();
        const spacing = 16;
        let top = 0;
        let left = 0;
        
        // Calculate position based on placement
        switch (placement.toLowerCase()) {
            case 'top':
                top = dimensions.top - tooltipRect.height - spacing;
                left = dimensions.left + (dimensions.width / 2) - (tooltipRect.width / 2);
                break;
            case 'bottom':
                top = dimensions.top + dimensions.height + spacing;
                left = dimensions.left + (dimensions.width / 2) - (tooltipRect.width / 2);
                break;
            case 'left':
                top = dimensions.top + (dimensions.height / 2) - (tooltipRect.height / 2);
                left = dimensions.left - tooltipRect.width - spacing;
                break;
            case 'right':
                top = dimensions.top + (dimensions.height / 2) - (tooltipRect.height / 2);
                left = dimensions.left + dimensions.width + spacing;
                break;
            case 'topleft':
                top = dimensions.top - tooltipRect.height - spacing;
                left = dimensions.left;
                break;
            case 'topright':
                top = dimensions.top - tooltipRect.height - spacing;
                left = dimensions.left + dimensions.width - tooltipRect.width;
                break;
            case 'bottomleft':
                top = dimensions.top + dimensions.height + spacing;
                left = dimensions.left;
                break;
            case 'bottomright':
                top = dimensions.top + dimensions.height + spacing;
                left = dimensions.left + dimensions.width - tooltipRect.width;
                break;
            default: // auto or bottom
                top = dimensions.top + dimensions.height + spacing;
                left = dimensions.left + (dimensions.width / 2) - (tooltipRect.width / 2);
                break;
        }
        
        // Keep tooltip within viewport
        const viewportWidth = window.innerWidth;
        const viewportHeight = window.innerHeight;
        
        if (left < spacing) left = spacing;
        if (left + tooltipRect.width > viewportWidth - spacing) {
            left = viewportWidth - tooltipRect.width - spacing;
        }
        
        if (top < spacing) top = spacing;
        if (top + tooltipRect.height > viewportHeight - spacing) {
            top = viewportHeight - tooltipRect.height - spacing;
        }
        
        tooltip.style.position = 'fixed';
        tooltip.style.top = `${top}px`;
        tooltip.style.left = `${left}px`;
    } catch (error) {
        console.error('Error updating tooltip position:', error);
    }
}

