from django.shortcuts import render

def accueilCommerce(request):
    return render(request, 'service/commerce/accueilCommerce.html')

def referencePage(request):
    return render(request, 'service/commerce/referencePage.html')

def accueilDemandeamc(request):
    return render(request, 'service/commerce/amc/accueilDemandeamc.html')

def creerDemandeamc(request):
    return render(request, 'service/commerce/amc/creerDemaneamc.html')

def modifierDemandeamc(request):
    return render(request, 'service/commerce/amc/modifierDemandeamc.html')

def supprimerDemandeamc(request):
    return render(request, 'service/commerce/amc/supprimerDemandeamc.html')

def rechercherDemandeamc(request):
    return render(request, 'service/commerce/amc/rechercherDemandeamc.html')





def accueilDemandeAgrement(request):
    return render(request, 'service/commerce/agrementppn/accueilDemandeAgrement.html')

def creerDemandeAgrement(request):
    return render(request, 'service/commerce/agrementppn/creerDemandeAgrement.html')

def modifierDemandeAgrement(request):
    return render(request, 'service/commerce/agrementppn/modifierDemandeAgrement.html')

def supprimerDemandeAgrement(request):
    return render(request, 'service/commerce/agrementppn/supprimerDemandeAgrement.html')

def rechercherDemandeAgrement(request):
    return render(request, 'service/commerce/agrementppn/rechercherDemandeAgrement.html')





def accueilDemandeCipens(request):
    return render(request, 'service/commerce/cipens/accueilDemandeCipens.html')

def creerDemandeCipens(request):
    return render(request, 'service/commerce/cipens/creerDemandeCipens.html')

def modifierDemandeCipens(request):
    return render(request, 'service/commerce/cipens/modifierDemandeCipens.html')

def supprimerDemandeCipens(request):
    return render(request, 'service/commerce/cipens/supprimerDemandeCipens.html')

def rechercherDemandeCipens(request):
    return render(request, 'service/commerce/cipens/rechercherDemandeCipens.html')

