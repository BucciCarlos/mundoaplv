document.addEventListener('DOMContentLoaded', () => {

    // --- Mobile Navigation (Hamburger Menu) ---
    const hamburger = document.querySelector('.hamburger');
    const navContainer = document.querySelector('.nav-container');
    const navLinks = document.querySelectorAll('.nav-links a');

    if (hamburger && navContainer) {
        hamburger.addEventListener('click', () => {
            navContainer.classList.toggle('active');
            // Toggle aria-expanded for accessibility
            const isExpanded = navContainer.classList.contains('active');
            hamburger.setAttribute('aria-expanded', isExpanded);
        });

        // Close menu when a link is clicked
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (navContainer.classList.contains('active')) {
                    navContainer.classList.remove('active');
                    hamburger.setAttribute('aria-expanded', 'false');
                }
            });
        });
    }

    // --- Animations on Scroll ---
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
                observer.unobserve(entry.target); // Stop observing after animation
            }
        });
    }, observerOptions);

    document.querySelectorAll('.card, .info-item, .resource-item').forEach(el => {
        el.style.animation = 'none'; // Reset animation state
        el.style.opacity = '0'; // Start as invisible
        observer.observe(el);
    });

    // --- Important Note Modal on alternativas.html ---
    const modal = document.getElementById('important-note-modal');
    if (modal) {
        const closeButton = modal.querySelector('.close-button');

        const showModal = () => {
            modal.style.display = 'block';
        };

        const hideModal = () => {
            modal.style.display = 'none';
        };

        // Show the modal as soon as the page loads
        showModal();

        // Close it when the close button is clicked
        if (closeButton) {
            closeButton.addEventListener('click', hideModal);
        }

        // Close it when the user clicks outside the modal content
        window.addEventListener('click', (event) => {
            if (event.target === modal) {
                hideModal();
            }
        });
    }

    // --- Header Scroll Effect ---
    const header = document.querySelector('header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 10) {
                header.classList.add('header-scrolled');
            } else {
                header.classList.remove('header-scrolled');
            }
        });
    }
});

function initializeDarkMode() {
    const darkModeToggle = document.querySelector('.dark-mode-toggle');
    const body = document.body;

    const applyTheme = (theme) => {
        if (theme === 'dark') {
            body.classList.add('dark-mode');
        } else {
            body.classList.remove('dark-mode');
        }
    };

    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', () => {
            const currentTheme = body.classList.contains('dark-mode') ? 'light' : 'dark';
            localStorage.setItem('theme', currentTheme);
            applyTheme(currentTheme);
        });
    }

    // Load saved theme or use system preference
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme) {
        applyTheme(savedTheme);
    } else {
        applyTheme('light');
    }
}