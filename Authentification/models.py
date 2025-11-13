from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.db.models import Q
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# ..........begin Fonctionnaire..............................
class Fonctionnaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=15, blank=True, null=True)
    adres_pro = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    fonction = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    service_content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True
    )
    service_object_id = models.PositiveIntegerField()
    service = GenericForeignKey("service_content_type", "service_object_id")

    class Meta:
        abstract = True

    def __str__(self):
        return self.user.username

    @classmethod
    def inscription(
        cls,
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
    ):

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        instance, created = cls.objects.get_or_create(
            user=user,
            defaults={
                "matricule": matricule,
                "adres_pro": adres_pro,
                "phone": phone,
                "fonction": fonction,
                "role": role,
                "service": service,
            },
        )
        if created:
            user.is_active = True
            user.save()
        return instance

    @classmethod
    def seConnecter(cls, request, username, password):
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                fonctionnaire = cls.objects.get(user=user)
                return fonctionnaire
            else:
                return None
        except (User.DoesNotExist, cls.DoesNotExist):
            return None

    @classmethod
    def seDeconnecter(cls, request):
        logout(request)
        return render(request, "Authentification/index.html")


# ..........end Fonctionnaire.................................


# ...... begin Operateur.....................................
class Operateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nif = models.CharField(max_length=15, blank=True, null=True)
    stat = models.CharField(max_length=15, blank=True, null=True)
    raisonSociale = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        abstract = False

    def __str__(self):
        return self.raisonSociale

    @classmethod
    def inscription(
        cls,
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
    ):

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        instance, created = cls.objects.get_or_create(
            user=user,
            defaults={
                "nif": nif,
                "stat": stat,
                "raisonSociale": raisonSociale,
                "adresse": adresse,
                "phone": phone,
            },
        )
        if created:
            user.is_active = True
            user.save()
        return instance

    @classmethod
    def seConnecter(cls, request, username, password):
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                operateur = cls.objects.get(user=user)
                return operateur
            else:
                return None
        except (User.DoesNotExist, cls.DoesNotExist):
            return None

    @classmethod
    def seDeconnecter(cls, request):
        logout(request)
        return render(request, "Authentification/index.html")


# ....... end Operateur .....................................


class Directeur(Fonctionnaire):
    pass


class Agent(Fonctionnaire):
    pass


class Ordsec(Fonctionnaire):
    pass


class Tresorier(Fonctionnaire):
    pass


class Sg(Fonctionnaire):
    pass
