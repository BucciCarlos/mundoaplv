(function() {
    // Determinar la ruta base para ajustar las rutas de los enlaces y scripts
    const base_path = window.location.pathname.includes("/pages/") ? "../" : "./";

    // Cargar el encabezado
    fetch(base_path + 'components/header.html')
        .then(response => response.text())
        .then(data => {
            const headerPlaceholder = document.getElementById("header-placeholder");
            if (headerPlaceholder) {
                headerPlaceholder.innerHTML = data.replace(/{{BASE_PATH}}/g, base_path);
            }
        });

    // Cargar el pie de página
    fetch(base_path + 'components/footer.html')
        .then(response => response.text())
        .then(data => {
            const footerPlaceholder = document.getElementById("footer-placeholder");
            if (footerPlaceholder) {
                footerPlaceholder.innerHTML = data;
            }
        });
})();