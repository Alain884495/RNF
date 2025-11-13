const trs = document.querySelectorAll(".table-content");
const valider = document.querySelector(".popup-valider");
const annuler = document.querySelector(".popup-annuler");
const inf_operateur = document.querySelectorAll(".amc-cell-operator input");
const popup = document.getElementById("popup");
const raison_sociale = document.getElementById("raison-sociale");

trs.forEach(tr => {
    tr.addEventListener('click', function() {
        // Si la ligne cliquée est déjà sélectionnée, on la désélectionne
        if (this.classList.contains("selected")) {
            this.classList.remove("selected");
        } else {
            // Sinon, on retire "selected" de toutes les autres lignes
            trs.forEach(t => t.classList.remove("selected"));
            // Et on ajoute "selected" à la ligne cliquée
            this.classList.add("selected");
        }
    });
});


valider.addEventListener('click', function(e) {
    trs.forEach(tr => {
        if (tr.classList.contains("selected")) {
            for(var i=0; i < inf_operateur.length; i++){
                inf_operateur[i].value = tr.cells[i+1].innerText;
            }
            popup.classList.remove('active');
        }
    });
});

raison_sociale.addEventListener('click', function(e) {
    popup.classList.add('active');
});

annuler.addEventListener('click', function(e){
    popup.classList.remove('active');
});



 // Fonction Alert
function customAlert(msg, type = 'info', seconds = 4) {
    const box = document.getElementById('customAlert');
    const msgEl = document.getElementById('customAlertMsg');
    const close = document.getElementById('customAlertClose');

    msgEl.textContent = msg;
    box.classList.remove('hidden', 'error', 'success');
    box.classList.add(type);          // type = 'info' | 'error' | 'success'

    // Fermeture auto après X secondes
    const timer = setTimeout(() => box.classList.add('hidden'), seconds * 1000);

    // Fermeture manuelle
    close.onclick = () => {
        clearTimeout(timer);
        box.classList.add('hidden');
    };
}