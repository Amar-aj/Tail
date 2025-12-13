// Gantt Chart JavaScript for enhanced interactions

export function initializeGantt(ganttId) {
    try {
        const gantt = document.getElementById(ganttId);
        if (!gantt) return;

        // Sync scroll between header and content
        const header = gantt.querySelector('.overflow-x-auto');
        const content = gantt.querySelector('.overflow-auto');
        
        if (header && content) {
            header.addEventListener('scroll', () => {
                content.scrollLeft = header.scrollLeft;
            });
            
            content.addEventListener('scroll', () => {
                header.scrollLeft = content.scrollLeft;
            });
        }
    } catch (error) {
        console.error('Error initializing gantt:', error);
    }
}

