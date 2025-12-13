// Kanban Board JavaScript for enhanced drag-and-drop

let kanbanInstances = new Map();

export function initializeKanban(boardId, dotNetRef) {
    try {
        const board = document.getElementById(boardId);
        if (!board) return;

        // Enhanced drag-and-drop handling
        const cards = board.querySelectorAll('[draggable="true"]');
        cards.forEach(card => {
            card.addEventListener('dragstart', handleDragStart);
            card.addEventListener('dragend', handleDragEnd);
        });

        // Handle column drop zones
        const columns = board.querySelectorAll('[data-column-id]');
        columns.forEach(column => {
            column.addEventListener('dragover', handleDragOver);
            column.addEventListener('drop', handleDrop);
            column.addEventListener('dragleave', handleDragLeave);
        });

        kanbanInstances.set(boardId, {
            board,
            dotNetRef,
            cards,
            columns
        });
    } catch (error) {
        console.error('Error initializing kanban:', error);
    }
}

function handleDragStart(e) {
    const card = e.target;
    card.classList.add('opacity-50');
    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('text/html', card.outerHTML);
    e.dataTransfer.setData('text/plain', card.dataset.cardId);
}

function handleDragEnd(e) {
    const card = e.target;
    card.classList.remove('opacity-50');
}

function handleDragOver(e) {
    if (e.preventDefault) {
        e.preventDefault();
    }
    e.dataTransfer.dropEffect = 'move';
    e.currentTarget.classList.add('drag-over');
    return false;
}

function handleDragLeave(e) {
    e.currentTarget.classList.remove('drag-over');
}

function handleDrop(e) {
    if (e.stopPropagation) {
        e.stopPropagation();
    }
    e.currentTarget.classList.remove('drag-over');
    return false;
}

export function disposeKanban(boardId) {
    try {
        const instance = kanbanInstances.get(boardId);
        if (instance) {
            // Remove event listeners if needed
            kanbanInstances.delete(boardId);
        }
    } catch (error) {
        console.error('Error disposing kanban:', error);
    }
}

