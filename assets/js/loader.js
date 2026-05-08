document.addEventListener('DOMContentLoaded', function() {
    const loadComponent = (id, url, basePath) => {
        fetch(url)
            .then(response => response.text())
            .then(data => {
                const processedData = data.replace(/\{\{BASE_PATH\}\}/g, basePath);
                document.getElementById(id).innerHTML = processedData;
                if (id === 'header-placeholder') {
                    initializeDarkMode();
                }
            })
            .catch(error => console.error(`Error loading component from ${url}:`, error));
    };

    // Determine the base path based on the current page's location
    const path = window.location.pathname;
    const isIndex = path.endsWith('/') || path.endsWith('index.html');
    const basePath = isIndex ? '' : '../';

    // Load header and footer
    loadComponent('header-placeholder', `${basePath}components/header.html`, basePath);
    loadComponent('footer-placeholder', `${basePath}components/footer.html`, basePath);
});
