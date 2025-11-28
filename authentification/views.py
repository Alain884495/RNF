from django.shortcuts import render, redirect
from .models import Operateur, Ordsec, Agent, Directeur, Tresorier, Sg
from django.contrib.auth.models import User
from django.contrib import messages 


def index(request):
    return render(request, "authentification/index.html")


def inscription_operateur(request):
    if request.method == "POST":
        # Nettoyage des champs avec strip()
        nom = request.POST.get("nom", "").strip()
        prenom = request.POST.get("prenom", "").strip()
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password")
        nif = request.POST.get("nif", "").strip()
        stat = request.POST.get("stat", "").strip()
        raison_sociale = request.POST.get("raison_sociale", "").strip()
        adresse_pro = request.POST.get("adresse_pro", "").strip()
        phone_pro = request.POST.get("phone_pro", "").strip()
        phone_perso = request.POST.get("phone_perso", "").strip()
        adresse_perso = request.POST.get("adresse_perso", "").strip()
        confirm_password = request.POST.get("confirm_password")

        if not all([
            nom, prenom, username, email, password,
            nif, stat, raison_sociale, adresse_pro,
            phone_pro, phone_perso, adresse_perso, confirm_password
        ]):
            messages.error(request, "Tous les champs doivent être remplis.")
            return render(request, "authentification/inscription_operateur.html", locals())

        # Vérifier si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            messages.error(request, f"Le nom d'utilisateur '{username}' est déjà utilisé.")
            return render(request, "authentification/inscription_operateur.html", locals())

        # Vérifier si l'email est déjà utilisé
        if User.objects.filter(email=email).exists():
            messages.error(request, f"L'adresse email '{email}' est déjà utilisée.")
            return render(request, "authentification/inscription_operateur.html", locals())

        # vérifier si les deux mot de passe sont différents
        if password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, "authentification/inscription_operateur.html", locals())

        
        try:
            user = User.objects.create_user(
                username=username,
                first_name=nom,
                last_name=prenom,
                email=email,
                password=password,
            )
            operateur = Operateur.objects.create(
                user=user,
                nif=nif,
                stat=stat,
                raison_sociale=raison_sociale,
                adresse_pro=adresse_pro,
                phone_pro=phone_pro,
                phone_perso=phone_perso,
                adresse_perso=adresse_perso,
            )
            messages.success(request, "Opérateur inscrit avec succès.")
            return redirect("authentification:inscription_operateur")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'inscription : {str(e)}")
    else:
        return render(request, "authentification/inscription_operateur.html")


def inscription_fonctionnaire(request):
    if request.method == "POST":
        nom = request.POST.get("nom", "").strip()
        prenom = request.POST.get("prenom", "").strip()
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        matricule = request.POST.get("matricule", "").strip()
        role = request.POST.get("role", "").strip()
        fonction = request.POST.get("fonction", "").strip()
        service = request.POST.get("service", "").strip()
        adresse_pro = request.POST.get("adresse_pro", "").strip()
        adresse_perso = request.POST.get("adresse_perso", "").strip()
        phone = request.POST.get("phone", "").strip()

        print(adresse_pro)
        if not all([
            nom, prenom, username, email, password, confirm_password,
            matricule, role, fonction, service, adresse_pro, adresse_perso, phone
        ]):
            messages.error(request, "Tous les champs doivent être remplis.")
            return render(request, "authentification/inscription_fonctionnaire.html", locals())

        # Vérifier si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            messages.error(request, f"Le nom d'utilisateur '{username}' est déjà utilisé.")
            return render(request, "authentification/inscription_fonctionnaire.html", locals())

        # Vérifier si l'email est déjà utilisé
        if User.objects.filter(email=email).exists():
            messages.error(request, f"L'adresse email '{email}' est déjà utilisée.")
            return render(request, "authentification/inscription_fonctionnaire.html", locals())

        # vérifier si les deux mot de passe sont différents
        if password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, "authentification/inscription_fonctionnaire.html", locals())

        try:
            role_model_map = {
                "agent": Agent,
                "ordsec": Ordsec,
                "directeur": Directeur,
                "tresorier": Tresorier,
                "sg": Sg,
            }

            model_class = role_model_map.get(role)
            if model_class is None:
                messages.error(request, "Rôle invalide sélectionné.")
                return render(request, "authentification/inscription_fonctionnaire.html", locals())

            user = User.objects.create_user(
                username=username,
                first_name=nom,
                last_name=prenom,
                email=email,
                password=password,
            )

            fonctionnaire = model_class.objects.create(
                user=user,
                matricule=matricule,
                role=role,
                fonction=fonction,
                service=service,
                adresse_pro=adresse_pro,
                adresse_perso=adresse_perso,
                phone=phone,
            )

            messages.success(request, "Fonctionnaire inscrit avec succès.")
            return redirect("authentification:inscription_fonctionnaire")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'inscription : {str(e)}")
    else:
        return render(request, "authentification/inscription_fonctionnaire.html")
