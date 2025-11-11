from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Operateur, Fonctionnaire, Ordsec, Agent, Tresorier, Sg, Directeur
from Services.models import ServiceCommerce, ServiceConditionnement, ServiceMetrologie
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    if request.method == "POST":
        username = request.POST.get("login", "").strip()
        password = request.POST.get("password", "")
        if username and password:
            if Ordsec.seConnecter(request, username, password):
                print("Ordsec")
            elif Agent.seConnecter(request, username, password):
                service = Agent.seConnecter(request, username, password).service
                match service.nomService:
                    case "commerce":
                        print(service)
                        return render(request, "Services/commerce/accueilCommerce.html")
                    case "conditionnement":
                        print("conditionnement")
                    case "metrologie":
                        print("metrologie")

            elif Tresorier.seConnecter(request, username, password):
                print("Tresorier")
            elif Sg.seConnecter(request, username, password):
                print("Sg")
            elif Directeur.seConnecter(request, username, password):
                print("Directeur")
            elif Operateur.seConnecter(request, username, password):
                print("Operateur")
            else:
                print("Alert")
                messages.error(request, "Login ou mot de passe incorrect.")
                return render(request, "Authentification/index.html")
    return render(request, "Authentification/index.html")


def inscription_operateur(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        nif = request.POST.get("nif", "").strip()
        stat = request.POST.get("stat", "").strip()
        raisonSociale = request.POST.get("raisonSociale", "").strip()
        adresse = request.POST.get("adresse", "").strip()
        phone = request.POST.get("phone", "").strip()

        if all(
            [
                username,
                first_name,
                last_name,
                email,
                password,
                nif,
                stat,
                raisonSociale,
                adresse,
                phone,
            ]
        ):
            user = User.objects.filter(username=username).first()
            if user:
                messages.error(request, "Nom d'utilisateur déjà pris.")
                return render(request, "Authentification/inscriptionOperateur.html")
            else:
                operateur = Operateur.inscription(
                    nif,
                    stat,
                    raisonSociale,
                    adresse,
                    phone,
                    username,
                    first_name,
                    last_name,
                    email,
                    password,
                )
                if operateur:
                    messages.success(request, "Inscription succès !")
                    return redirect("Authentification:inscription_operateur")
                else:
                    messages.error(request, "Inscription echouée !")
                    return redirect("Authentification:inscription_operateur")

        else:
            messages.error(request, "Les champs sont vides !")
        return render(request, "Authentification/inscriptionOperateur.html")
    else:
        print("get")
        return render(request, "Authentification/inscriptionOperateur.html")


def inscription_fonctionnaire(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        matricule = request.POST.get("matricule", "").strip()
        adres_pro = request.POST.get("adres_pro", "").strip()
        phone = request.POST.get("phone", "").strip()
        fonction = request.POST.get("fonction", "").strip()
        role = request.POST.get("role", "").strip()
        service = request.POST.get("service", "").strip()

        if all(
            [
                username,
                first_name,
                last_name,
                email,
                password,
                matricule,
                adres_pro,
                phone,
                fonction,
                role,
                service,
            ]
        ):
            user = User.objects.filter(username=username).first()
            if user:
                messages.error(request, "Nom d'utilisateur déjà pris.")
                return render(request, "Authentification/inscriptionFonctionnaire.html")
            else:
                match role:
                    case "ordsec":
                        fonctionnaire = Ordsec.inscription(
                            matricule,
                            adres_pro,
                            phone,
                            fonction,
                            role,
                            service,
                            username,
                            first_name,
                            last_name,
                            email,
                            password,
                        )
                    case "agent":
                        if service == "commerce":
                            sc = ServiceCommerce.objects.get_or_create(
                                nomService="commerce"
                            )[0]
                        elif service == "conditionnement":
                            sc = ServiceConditionnement.objects.get_or_create(
                                nomService="conditionnement"
                            )[0]
                        elif service == "metrologie":
                            sc = ServiceMetrologie.objects.get_or_create(
                                nomService="metrologie"
                            )[0]
                        fonctionnaire = Agent.inscription(
                            matricule,
                            adres_pro,
                            phone,
                            fonction,
                            role,
                            sc,
                            username,
                            first_name,
                            last_name,
                            email,
                            password,
                        )
                    case "tresorier":
                        fonctionnaire = Tresorier.inscription(
                            matricule,
                            adres_pro,
                            phone,
                            fonction,
                            role,
                            service,
                            username,
                            first_name,
                            last_name,
                            email,
                            password,
                        )
                    case "sg":
                        fonctionnaire = Sg.inscription(
                            matricule,
                            adres_pro,
                            phone,
                            fonction,
                            role,
                            service,
                            username,
                            first_name,
                            last_name,
                            email,
                            password,
                        )
                    case "directeur":
                        fonctionnaire = Directeur.inscription(
                            matricule,
                            adres_pro,
                            phone,
                            fonction,
                            role,
                            service,
                            username,
                            first_name,
                            last_name,
                            email,
                            password,
                        )

                if fonctionnaire:
                    messages.success(request, "Inscription succès !")
                    return redirect("Authentification:inscription_fonctionnaire")
                else:
                    messages.error(request, "Inscription echouée !")
                    return render(
                        request, "Authentification/inscriptionFonctionnaire.html"
                    )

        else:
            messages.error(request, "Les champs sont vides !")
            return render(request, "Authentification/inscriptionFonctionnaire.html")
    else:
        return render(request, "Authentification/inscriptionFonctionnaire.html")


def deconnexion(request):
    logout(request)
    return render(request, "Authentification/index.html")
