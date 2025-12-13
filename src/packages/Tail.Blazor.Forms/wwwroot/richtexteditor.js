// Rich Text Editor JavaScript for formatting commands

export function execCommand(editorId, command, showUI, value, argument) {
    try {
        const editor = document.getElementById(editorId);
        if (!editor) return false;
        
        editor.focus();
        
        // Handle special commands
        if (command === "createLink" && argument) {
            document.execCommand(command, showUI, argument);
            return true;
        }
        
        if (command === "insertImage" && argument) {
            document.execCommand(command, showUI, argument);
            return true;
        }
        
        if (command === "formatBlock" && argument) {
            document.execCommand(command, showUI, argument);
            return true;
        }
        
        // Standard execCommand
        if (value !== null && value !== undefined) {
            document.execCommand(command, showUI, value);
        } else {
            document.execCommand(command, showUI);
        }
        
        return true;
    } catch (error) {
        console.error('Error executing command:', error);
        return false;
    }
}

export function getEditorContent(editorId) {
    try {
        const editor = document.getElementById(editorId);
        if (!editor) return '';
        
        return editor.innerHTML || '';
    } catch (error) {
        console.error('Error getting editor content:', error);
        return '';
    }
}

export function setPlaceholder(editorId, placeholder) {
    try {
        const editor = document.getElementById(editorId);
        if (!editor) return;
        
        // Set data-placeholder attribute for CSS styling
        editor.setAttribute('data-placeholder', placeholder);
        
        // Add placeholder styling via inline style
        const style = document.createElement('style');
        style.textContent = `
            #${editorId}[data-placeholder]:empty:before {
                content: attr(data-placeholder);
                color: #9ca3af;
                pointer-events: none;
            }
            #${editorId}[data-placeholder]:empty:focus:before {
                color: #6b7280;
            }
        `;
        if (!document.head.querySelector(`style[data-rte="${editorId}"]`)) {
            style.setAttribute('data-rte', editorId);
            document.head.appendChild(style);
        }
    } catch (error) {
        console.error('Error setting placeholder:', error);
    }
}

