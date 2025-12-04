// Exemple de validation JavaScript personnalisée, 
// met en rouge les champs vide et empêche la soumission de formulaire
//mode d'emploie: en crée une class="needs-validation" sur
// <form ... class="needs-validation" novalidate>
// et ajoute atribut "required" sur les inputs
(function () {
  'use strict'
  var forms = document.querySelectorAll('.needs-validation')
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
        form.classList.add('was-validated')
      }, false)
    })
})()