from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Profils
#from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST.get("username","").strip()
        password = request.POST.get("password","").strip()
        if not username or not password:
            return redirect("authentification:index")
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.profils.service == "ordsec":
                    return render(request, 'authentification/accueilOrdsec.html')
                elif user.profils.service == "commerce":
                    return render(request, 'authentification/accueilCommerce.html')
                elif user.profils.service == "directeur":
                    return render(request, 'authentification/accueilDirecteur.html')
                elif user.profils.service == "ministre":
                    return render(request, 'authentification/accueilMinistre.html')
            else:
                return redirect("authentification:index")           
    else:
        return render(request, 'authentification/index.html')


def inscription(request):
    if request.method == "POST":
        username = request.POST.get("username","").strip()
        password = request.POST.get("password","").strip()
        email = request.POST.get("email","").strip()
        fonction = request.POST.get("fonction","").strip()
        service = request.POST.get("service","").strip()
        if not username or not password or not email or not fonction or not service:
            return redirect("authentification:inscription")
        else:
            #CREATION USER
            try:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                #CREATION PROFIL LIE A L'USER
                profil = Profils(user=user, fonction=fonction, service=service)
                profil.save()
                return redirect("authentification:accueilOrdsec")
            except: 
                return redirect("authentification:inscription")
    else:    
        referer = request.META.get("HTTP_REFERER")
        if referer:
            # La requête vient d'un lien (ou d'une autre page)
            return render(request, 'authentification/inscription.html')
        else:
            # L'utilisateur a probablement tapé l'URL directement
            return render(request, 'authentification/index.html')


def accueilOrdsec(request):
    return render(request, 'authentification/accueilOrdsec.html')

def accueilCommerce(request):
    return render(request, 'authentification/accueilCommerce.html')