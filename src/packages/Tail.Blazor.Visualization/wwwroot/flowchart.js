// Flowchart JavaScript for drag-and-drop, auto-routing, and export

let flowchartInstances = {};

export function initializeFlowchart(flowchartId, svgId, dotNetRef, allowDragDrop) {
    try {
        const svg = document.getElementById(svgId);
        if (!svg) return;

        flowchartInstances[svgId] = {
            svg: svg,
            dotNetRef: dotNetRef,
            allowDragDrop: allowDragDrop,
            draggedNode: null
        };

        if (allowDragDrop) {
            setupDragAndDrop(svgId);
        }
    } catch (error) {
        console.error('Error initializing flowchart:', error);
    }
}

function setupDragAndDrop(svgId) {
    const instance = flowchartInstances[svgId];
    if (!instance) return;

    const svg = instance.svg;
    const nodes = svg.querySelectorAll('.flowchart-node');

    nodes.forEach(node => {
        node.addEventListener('mousedown', (e) => {
            instance.draggedNode = node;
            const nodeId = node.getAttribute('data-node-id');
            const transform = node.getAttribute('transform');
            const match = transform.match(/translate\(([\d.]+),\s*([\d.]+)\)/);
            if (match) {
                instance.startX = parseFloat(match[1]);
                instance.startY = parseFloat(match[2]);
            }
            instance.mouseX = e.clientX;
            instance.mouseY = e.clientY;
            node.style.cursor = 'grabbing';
        });
    });

    document.addEventListener('mousemove', (e) => {
        if (instance.draggedNode) {
            const deltaX = e.clientX - instance.mouseX;
            const deltaY = e.clientY - instance.mouseY;
            const newX = instance.startX + deltaX;
            const newY = instance.startY + deltaY;
            instance.draggedNode.setAttribute('transform', `translate(${newX}, ${newY})`);
            
            // Update edge routing
            updateEdgeRouting(svgId, null, null);
        }
    });

    document.addEventListener('mouseup', () => {
        if (instance.draggedNode) {
            instance.draggedNode.style.cursor = 'pointer';
            instance.draggedNode = null;
        }
    });
}

export function updateEdgeRouting(svgId, nodes, edges) {
    try {
        const instance = flowchartInstances[svgId];
        if (!instance) return;

        const svg = instance.svg;
        const edgeElements = svg.querySelectorAll('.flowchart-edge line');

        edgeElements.forEach(edgeElement => {
            const edgeId = edgeElement.closest('.flowchart-edge')?.getAttribute('data-edge-id');
            if (!edgeId) return;

            // Find corresponding edge and nodes
            const edge = edges?.find(e => e.Id === edgeId);
            if (!edge) return;

            const sourceNode = nodes?.find(n => n.Id === edge.SourceNodeId);
            const targetNode = nodes?.find(n => n.Id === edge.TargetNodeId);
            if (!sourceNode || !targetNode) return;

            // Get node positions from SVG
            const sourceNodeElement = svg.querySelector(`[data-node-id="${edge.SourceNodeId}"]`);
            const targetNodeElement = svg.querySelector(`[data-node-id="${edge.TargetNodeId}"]`);
            
            if (sourceNodeElement && targetNodeElement) {
                const sourceTransform = sourceNodeElement.getAttribute('transform');
                const targetTransform = targetNodeElement.getAttribute('transform');
                
                const sourceMatch = sourceTransform.match(/translate\(([\d.]+),\s*([\d.]+)\)/);
                const targetMatch = targetTransform.match(/translate\(([\d.]+),\s*([\d.]+)\)/);
                
                if (sourceMatch && targetMatch) {
                    const sourceX = parseFloat(sourceMatch[1]) + sourceNode.Width / 2;
                    const sourceY = parseFloat(sourceMatch[2]) + sourceNode.Height / 2;
                    const targetX = parseFloat(targetMatch[1]) + targetNode.Width / 2;
                    const targetY = parseFloat(targetMatch[2]) + targetNode.Height / 2;

                    edgeElement.setAttribute('x1', sourceX);
                    edgeElement.setAttribute('y1', sourceY);
                    edgeElement.setAttribute('x2', targetX);
                    edgeElement.setAttribute('y2', targetY);
                }
            }
        });
    } catch (error) {
        console.error('Error updating edge routing:', error);
    }
}

export function applyAutoLayout(svgId, nodes, layoutType) {
    try {
        const instance = flowchartInstances[svgId];
        if (!instance) return;

        const svg = instance.svg;

        if (layoutType === 'Hierarchical') {
            // Simple hierarchical layout
            const levels = new Map();
            nodes.forEach((node, index) => {
                const level = Math.floor(index / 3);
                if (!levels.has(level)) {
                    levels.set(level, []);
                }
                levels.get(level).push(node);
            });

            let y = 50;
            levels.forEach((levelNodes, level) => {
                const nodeWidth = 150;
                const totalWidth = levelNodes.length * nodeWidth;
                const startX = (svg.clientWidth - totalWidth) / 2;

                levelNodes.forEach((node, index) => {
                    node.X = startX + (index * nodeWidth);
                    node.Y = y;
                });

                y += 150;
            });
        } else if (layoutType === 'Grid') {
            // Grid layout
            const cols = Math.ceil(Math.sqrt(nodes.length));
            const nodeWidth = 150;
            const nodeHeight = 80;
            const spacing = 50;

            nodes.forEach((node, index) => {
                const row = Math.floor(index / cols);
                const col = index % cols;
                node.X = col * (nodeWidth + spacing) + spacing;
                node.Y = row * (nodeHeight + spacing) + spacing;
            });
        }

        // Update SVG node positions
        nodes.forEach(node => {
            const nodeElement = svg.querySelector(`[data-node-id="${node.Id}"]`);
            if (nodeElement) {
                nodeElement.setAttribute('transform', `translate(${node.X}, ${node.Y})`);
            }
        });

        // Update edges
        updateEdgeRouting(svgId, nodes, null);
    } catch (error) {
        console.error('Error applying auto layout:', error);
    }
}

export function exportFlowchart(svgId) {
    try {
        const svg = document.getElementById(svgId);
        if (!svg) return;

        const svgData = new XMLSerializer().serializeToString(svg);
        const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
        const svgUrl = URL.createObjectURL(svgBlob);
        const downloadLink = document.createElement('a');
        downloadLink.href = svgUrl;
        downloadLink.download = 'flowchart.svg';
        document.body.appendChild(downloadLink);
        downloadLink.click();
        document.body.removeChild(downloadLink);
        URL.revokeObjectURL(svgUrl);
    } catch (error) {
        console.error('Error exporting flowchart:', error);
    }
}

