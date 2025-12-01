
from django.urls import path
from . import views

app_name = "service"

urlpatterns = [
    path('commerce', views.accueilCommerce, name="accueilCommerce"),
    path('referencePage', views.referencePage, name="referencePage"),



    path('accueilDemandeamc', views.accueilDemandeamc, name="accueilDemandeamc"),
    path('creerDemandeamc', views.creerDemandeamc, name="creerDemandeamc"),
    path('modifierDemandeamc', views.modifierDemandeamc, name="modifierDemandeamc"),
    path('supprimerDemandeamc', views.supprimerDemandeamc, name="supprimerDemandeamc"),
    path('rechercherDemandeamc', views.rechercherDemandeamc, name="rechercherDemandeamc"),

    
    
    path('accueilDemandeAgrement', views.accueilDemandeAgrement, name="accueilDemandeAgrement"),
    path('creerDemandeAgrement', views.creerDemandeAgrement, name="creerDemandeAgrement"),
    path('modifierDemandeAgrement', views.modifierDemandeAgrement, name="modifierDemandeAgrement"),
    path('supprimerDemandeAgrement', views.supprimerDemandeAgrement, name="supprimerDemandeAgrement"),
    path('rechercherDemandeAgrement', views.rechercherDemandeAgrement, name="rechercherDemandeAgrement"),



    path('accueilDemandeCipens', views.accueilDemandeCipens, name="accueilDemandeCipens"),
    path('creerDemandeCipens', views.creerDemandeCipens, name="creerDemandeCipens"),
    path('modifierDemandeCipens', views.modifierDemandeCipens, name="modifierDemandeCipens"),
    path('supprimerDemandeCipens', views.supprimerDemandeCipens, name="supprimerDemandeCipens"),
    path('rechercherDemandeCipens', views.rechercherDemandeCipens, name="rechercherDemandeCipens"),
]
