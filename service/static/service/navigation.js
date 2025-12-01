document.addEventListener('DOMContentLoaded', function() {
    // Sélectionne tous les liens de navigation
    const navLinks = document.querySelectorAll('.navbar .nav-link');
    
    // Ajoute un gestionnaire d'événement à chaque lien
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Supprime la classe 'active' de tous les liens
            navLinks.forEach(l => l.classList.remove('active'));
            // Ajoute la classe 'active' au lien cliqué
            this.classList.add('active');
            // Ajoute l'attribut aria-current pour l'accessibilité
            this.setAttribute('aria-current', 'page');
            // Supprime l'attribut des autres liens
            navLinks.forEach(l => {
                if (l !== this) l.removeAttribute('aria-current');
            });
        });
    });

    // Met à jour l'état actif au chargement de la page
    const currentLocation = window.location.pathname;
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentLocation) {
            link.classList.add('active');
            link.setAttribute('aria-current', 'page');
        } else {
            link.classList.remove('active');
            link.removeAttribute('aria-current');
        }
    });
});
