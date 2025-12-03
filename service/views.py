from django.shortcuts import render, redirect 
from authentification.models import Operateur
import certificat
from certificat.models import Sigle, CertificatAMC
from django.contrib import messages

def accueilCommerce(request):
    return render(request, 'service/commerce/accueilCommerce.html')

def referencePage(request):
    return render(request, 'service/commerce/referencePage.html')

def accueilDemandeamc(request):
    
    return render(request, 'service/commerce/amc/accueilDemandeamc.html')

def creerDemandeamc(request):
    operateurs = Operateur.objects.all().order_by('raison_sociale')
    sigle = Sigle.objects.first()
    numeroCertificat = str(CertificatAMC.objects.count() + 1).zfill(3)
    context = {
        'operateurs': operateurs,
        'sigle': sigle,
        'numeroCertificat': numeroCertificat,
    }
    if request.method == 'POST':
        raisonSociale = request.POST.get("raisonSociale")
        nif = request.POST.get("nif", "").strip()
        adresse = request.POST.get("adresse", "").strip()
        produit = request.POST.get("produit", "").strip()
        pays = request.POST.get("pays", "").strip()
        quantite = request.POST.get("quantite", "").strip()
        unite = request.POST.get("unite", "").strip()
        reference = request.POST.get("reference")
        demandeN = request.POST.get("demandeN")
        
        CertificatAMC.objects.create(
            operateur=Operateur.objects.get(raison_sociale=raisonSociale),
            nom_marchandise=produit,
            pays_origine=pays,
            quantite=quantite,
            etat="demande",
            unite=unite,
            reference=reference,
            numero=demandeN,
        )
        messages.success(request, 'Demande AMC créée avec succès.')
        return redirect('service:creerDemandeamc')
    return render(request, 'service/commerce/amc/creerDemaneamc.html', context)

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

