// Docking Layout JavaScript for drag-and-drop

let dockingInstances = new Map();

export function initializeDocking(layoutId, dotNetRef) {
    try {
        const layout = document.getElementById(layoutId);
        if (!layout) return;

        // Handle floating panel dragging
        const floatingPanels = layout.querySelectorAll('[data-panel-id]');
        floatingPanels.forEach(panel => {
            let isDragging = false;
            let currentX;
            let currentY;
            let initialX;
            let initialY;
            let xOffset = 0;
            let yOffset = 0;

            const header = panel.querySelector('.cursor-move');
            if (!header) return;

            header.addEventListener('mousedown', dragStart);
            document.addEventListener('mousemove', drag);
            document.addEventListener('mouseup', dragEnd);

            function dragStart(e) {
                if (e.button !== 0) return; // Only left mouse button
                
                initialX = e.clientX - xOffset;
                initialY = e.clientY - yOffset;

                if (e.target === header || header.contains(e.target)) {
                    isDragging = true;
                    panel.style.cursor = 'grabbing';
                }
            }

            function drag(e) {
                if (isDragging) {
                    e.preventDefault();
                    currentX = e.clientX - initialX;
                    currentY = e.clientY - initialY;

                    xOffset = currentX;
                    yOffset = currentY;

                    setTranslate(currentX, currentY, panel);
                }
            }

            function dragEnd(e) {
                initialX = currentX;
                initialY = currentY;
                isDragging = false;
                panel.style.cursor = '';
            }

            function setTranslate(xPos, yPos, el) {
                el.style.transform = `translate(${xPos}px, ${yPos}px)`;
            }
        });

        dockingInstances.set(layoutId, {
            layout,
            dotNetRef
        });
    } catch (error) {
        console.error('Error initializing docking:', error);
    }
}

export function disposeDocking(layoutId) {
    try {
        dockingInstances.delete(layoutId);
    } catch (error) {
        console.error('Error disposing docking:', error);
    }
}

