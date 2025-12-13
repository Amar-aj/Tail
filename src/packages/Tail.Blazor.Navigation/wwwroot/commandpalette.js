// Command Palette JavaScript for global keyboard shortcut handling
let commandPaletteRef = null;
let triggerKey = 'k';
let requireModifier = true;

export function registerCommandPalette(dotNetRef, key, requireMod) {
    commandPaletteRef = dotNetRef;
    triggerKey = key || 'k';
    requireModifier = requireMod !== false;
    
    document.addEventListener('keydown', handleKeyDown);
}

export function unregisterCommandPalette() {
    document.removeEventListener('keydown', handleKeyDown);
    commandPaletteRef = null;
}

function handleKeyDown(event) {
    // Check if the trigger key combination is pressed
    const isModifierPressed = event.metaKey || event.ctrlKey;
    const isTriggerKey = event.key.toLowerCase() === triggerKey.toLowerCase();
    
    // Ignore if typing in input, textarea, or contenteditable
    const target = event.target;
    const isInputElement = target.tagName === 'INPUT' || 
                          target.tagName === 'TEXTAREA' || 
                          target.isContentEditable;
    
    if (isInputElement && !event.ctrlKey && !event.metaKey) {
        return; // Allow normal typing
    }
    
    // Check if the command palette should open
    if (requireModifier && isModifierPressed && isTriggerKey) {
        event.preventDefault();
        if (commandPaletteRef) {
            commandPaletteRef.invokeMethodAsync('OpenCommandPalette');
        }
    } else if (!requireModifier && isTriggerKey) {
        event.preventDefault();
        if (commandPaletteRef) {
            commandPaletteRef.invokeMethodAsync('OpenCommandPalette');
        }
    }
}

