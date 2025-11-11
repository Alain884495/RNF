from django.urls import path
from . import views

app_name = "Services"
urlpatterns = [
    path("accueilCommerce/", views.accueilCommerce, name="accueilCommerce"),
    path("accueildemandeamc/", views.accueildemandeamc, name="accueildemandeamc"),
    path("creerdemandeamc/", views.creerdemandeamc, name="creerdemandeamc"),
    path("modifierdemandeamc/", views.modifierdemandeamc, name="modifierdemandeamc"),
    path("supprimerdemandeamc/", views.supprimerdemandeamc, name="supprimerdemandeamc"),
    path(
        "rechercherdemandeamc/", views.rechercherdemandeamc, name="rechercherdemandeamc"
    ),
    path("cipens/", views.cipens, name="cipens"),
    path("agrement/", views.agrement, name="agrement"),
]
