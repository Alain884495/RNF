from django.shortcuts import render, redirect
from django.contrib import messages
from Authentification.models import Operateur
from Certificats.models import CertificatAMC, Sigle
from Services.models import ServiceCommerce
from django.contrib.auth import authenticate, login, logout
from Authentification.models import Agent
from django.utils import timezone
from django.db.models import Max


def accueilCommerce(request):
    return render(request, "Services/commerce/accueilCommerce.html")


def accueildemandeamc(request):
    return render(request, "Services/commerce/amc/accueildemandeamc.html")


def creerdemandeamc(request):
    operateurs = Operateur.objects.all()
    sigle = Sigle.objects.get(id=1)
    numeroamc = CertificatAMC.objects.count() + 1
    sigleamc = str(numeroamc).zfill(2)
    sigleamc = f"{sigleamc}{sigle.sigleCertificatamc}"

    # Contexte de base
    context = {"operateurs": operateurs, "sigle": sigle, "sigleamc": sigleamc}

    if request.method == "POST":
        # Récupération des données
        ref = request.POST.get("ref", "").strip()
        raisonSociale = request.POST.get("raison-sociale", "").strip()
        nif = request.POST.get("nif", "").strip()
        stat = request.POST.get("stat", "").strip()
        adresse = request.POST.get("adresse", "").strip()
        telephone = request.POST.get("telephone", "").strip()
        marchandise = request.POST.get("marchandise", "").strip()
        paysOrigine = request.POST.get("pays-origine", "").strip()
        quantite = request.POST.get("quantite", "").strip()
        unite = request.POST.get("unite", "").strip()

        # Ajout des données au contexte pour les conserver
        context["form_data"] = {
            "ref": ref,
            "raison_sociale": raisonSociale,
            "nif": nif,
            "stat": stat,
            "adresse": adresse,
            "telephone": telephone,
            "marchandise": marchandise,
            "pays_origine": paysOrigine,
            "quantite": quantite,
            "unite": unite,
        }

        # Validation
        if all(
            [
                ref,
                raisonSociale,
                nif,
                stat,
                adresse,
                telephone,
                marchandise,
                paysOrigine,
                quantite,
                unite,
            ]
        ):
            # Traitement réussi
            CertificatAMC.creerCertificat(
                reference=ref,
                numero=sigleamc,
                service=ServiceCommerce.objects.get(nomService="commerce"),
                operateur=Operateur.objects.get(raisonSociale=raisonSociale),
                agent=Agent.objects.get(user=request.user),
                etat="demande",
                dateDemande=timezone.now().date(),
                nomMarchandise=marchandise,
                paysOrigine=paysOrigine,
                quantite=quantite,
                unite=unite,
            )
            messages.success(request, "Demande AMC créée avec succès.")
            # Redirection après succès pour éviter la resoumission
            return redirect("Services:creerdemandeamc")  # Adapter selon votre URL
        else:
            # Identification des champs vides
            champs_vides = []
            if not ref:
                champs_vides.append("Ref")
            if not raisonSociale:
                champs_vides.append("Raison Sociale")
            if not nif:
                champs_vides.append("NIF")
            if not stat:
                champs_vides.append("STAT")
            if not adresse:
                champs_vides.append("Adresse")
            if not telephone:
                champs_vides.append("Téléphone")
            if not marchandise:
                champs_vides.append("Marchandise")
            if not paysOrigine:
                champs_vides.append("Pays d'origine")
            if not quantite:
                champs_vides.append("Quantité")
            if not unite:
                champs_vides.append("Unité")

            messages.error(
                request,
                f"Les champs suivants sont obligatoires : {', '.join(champs_vides)}",
            )

        return render(request, "Services/commerce/amc/creerdemandeamc.html", context)

    # GET request
    return render(request, "Services/commerce/amc/creerdemandeamc.html", context)


def modifierdemandeamc(request):
    return render(request, "Services/commerce/amc/modifierdemandeamc.html")


def supprimerdemandeamc(request):
    return render(request, "Services/commerce/amc/supprimerdemandeamc.html")


def rechercherdemandeamc(request):
    return render(request, "Services/commerce/amc/rechercherdemandeamc.html")


def cipens(request):
    return render(request, "Services/commerce/cipens/cipens.html")


def agrement(request):
    return render(request, "Services/commerce/agrement/agrement.html")
