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



// Script pour le pop up
function openPopup() {
    const bg = document.getElementById("popup");
    const box = document.getElementById("popupBox");

    bg.classList.remove("closing");
    box.classList.remove("closing");

    bg.classList.add("active");
}

function closePopup() {
    const bg = document.getElementById("popup");
    const box = document.getElementById("popupBox");

    box.classList.add("closing");
    bg.classList.add("closing");

    // Attendre la fin de l'animation
    setTimeout(() => {
        bg.classList.remove("active");
        bg.classList.remove("closing");
        box.classList.remove("closing");
    }, 250);
}

/**
 * Gère la sélection d'un opérateur dans la liste de popup
 * @param {number} id - L'identifiant de l'opérateur
 * @param {string} entreprise - Le nom de l'entreprise
 * @param {string} nif - Le numéro NIF de l'entreprise
 * @param {string} ville - La ville de l'entreprise
 */
function selectOperator(id, entreprise, nif, ville) {
    try {
        // Mise à jour des champs du formulaire principal
        const raisonSociale = document.getElementById('raisonSociale');
        const nifField = document.getElementById('nif');
        const adresse = document.getElementById('adresse');

        if (raisonSociale) raisonSociale.value = entreprise;
        if (nifField) nifField.value = nif;
        if (adresse) adresse.value = ville;
        
        // Mise en surbrillance de la ligne sélectionnée
        const rows = document.querySelectorAll('tbody tr');
        rows.forEach(row => {
            row.classList.remove('table-active');
            row.style.backgroundColor = '';
        });
        
        // Ajout de la classe active à la ligne sélectionnée
        if (event && event.currentTarget) {
            event.currentTarget.classList.add('table-active');
            event.currentTarget.style.backgroundColor = '#9ea4aaff';
        }

        // Fermeture automatique du popup après sélection
        closePopup();
        
    } catch (error) {
        console.error('Erreur lors de la sélection de l\'opérateur :', error);
    }
}

/**
 * Filtre les lignes du tableau en fonction de la recherche dans la popup
 * La recherche s'effectue sur la colonne "Raison Sociale" (index 1)
 */
function filterTable() {
    try {
        const input = document.getElementById('raison');
        if (!input) return;

        const filter = input.value.toLowerCase();
        const table = document.querySelector('table');
        if (!table) return;

        const rows = table.getElementsByTagName('tr');
        let hasResults = false;

        // Commencer à 1 pour ignorer l'en-tête du tableau
        for (let i = 1; i < rows.length; i++) {
            const cells = rows[i].getElementsByTagName('td');
            if (cells.length < 2) continue;

            // Recherche dans la colonne "Raison Sociale" (index 1)
            const text = cells[1].textContent || cells[1].innerText;
            const isVisible = text.toLowerCase().includes(filter);
            
            rows[i].style.display = isVisible ? '' : 'none';
            if (isVisible) hasResults = true;
        }

        // Optionnel : Afficher un message si aucun résultat
        const noResults = document.getElementById('noResults');
        if (noResults) {
            noResults.style.display = hasResults ? 'none' : 'block';
        }

    } catch (error) {
        console.error('Erreur lors du filtrage du tableau :', error);
    }
}