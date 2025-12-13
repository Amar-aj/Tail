// Organization Chart JavaScript for zoom and export

export function initializeOrgChart(chartId, dotNetRef) {
    try {
        const chart = document.getElementById(chartId);
        if (!chart) return;

        // Additional initialization if needed
    } catch (error) {
        console.error('Error initializing org chart:', error);
    }
}

export function exportOrgChart(chartId) {
    try {
        const chart = document.getElementById(chartId);
        if (!chart) return;

        // Use html2canvas or similar library for export
        // For now, we'll use a simple SVG export approach
        const svg = chart.querySelector('svg');
        if (svg) {
            const svgData = new XMLSerializer().serializeToString(svg);
            const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
            const svgUrl = URL.createObjectURL(svgBlob);
            const downloadLink = document.createElement('a');
            downloadLink.href = svgUrl;
            downloadLink.download = 'orgchart.svg';
            document.body.appendChild(downloadLink);
            downloadLink.click();
            document.body.removeChild(downloadLink);
        } else {
            // Fallback: export as PNG using canvas
            html2canvas(chart).then(canvas => {
                canvas.toBlob(blob => {
                    const url = URL.createObjectURL(blob);
                    const link = document.createElement('a');
                    link.href = url;
                    link.download = 'orgchart.png';
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                    URL.revokeObjectURL(url);
                });
            });
        }
    } catch (error) {
        console.error('Error exporting org chart:', error);
    }
}

