from django.shortcuts import render
from Authentification.models import Operateur


def accueilCommerce(request):
    return render(request, "Services/commerce/accueilCommerce.html")


def accueildemandeamc(request):
    return render(request, "Services/commerce/amc/accueildemandeamc.html")


def creerdemandeamc(request):
    operateurs = Operateur.objects.all()
    if operateurs.exists():
        print(operateurs[0].raisonSociale)
    else:
        print("Aucun opérateur trouvé.")
    return render(
        request,
        "Services/commerce/amc/creerdemandeamc.html",
        {"operateurs": operateurs},
    )


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
