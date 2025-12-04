function formatNom(e){
    e.value = e.value.toUpperCase();
}

function formatPrenoms(e) {
    e.value = e.value.replace(/\b\w+/g, function(mot) {
        return mot.charAt(0).toUpperCase() + mot.slice(1).toLowerCase();
    });
}

function formatNIF(e) {
    // Retirer tout sauf les chiffres
    let v = e.value.replace(/\D/g, "");

    // Limite à 10 chiffres
    if (v.length > 10) v = v.slice(0, 10);

    // Reconstruction groupée progressive
    let groupe = [];
    if (v.length > 0) groupe.push(v.substring(0, 1));
    if (v.length > 1) groupe.push(v.substring(1, 4));
    if (v.length > 4) groupe.push(v.substring(4, 7));
    if (v.length > 7) groupe.push(v.substring(7, 10));

    e.value = groupe.join(" ");
}