# users/admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Directeur, Agent, Ordsec, Tresorier, Sg, Operateur


class OperateurAdmin(admin.ModelAdmin):
    list_display = ("user", "nif", "stat", "raisonSociale", "phone", "adresse")
    search_fields = ("nif", "raisonSociale", "user__username", "user__email", "phone")
    list_filter = ("stat",)
    ordering = ("user",)
    raw_id_fields = ("user",)  # préférable si beaucoup d'utilisateurs
    readonly_fields = ()
    fieldsets = (
        ("Utilisateur lié", {"fields": ("user",)}),
        (
            "Informations opérateur",
            {"fields": ("nif", "stat", "raisonSociale", "adresse", "phone")},
        ),
    )


class FonctionnaireAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "matricule",
        "adres_pro",
        "phone",
        "fonction",
        "role",
        "service",
    )
    search_fields = ("matricule",)
    list_filter = ("matricule",)
    ordering = ("matricule",)
    raw_id_fields = ("user",)  # préférable si beaucoup d'utilisateurs
    readonly_fields = ()


class CustomUserAdmin(BaseUserAdmin):
    # afficher les champs principaux de la table User dans la liste
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "is_superuser",
        "last_login",
        "date_joined",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_active", "is_superuser", "groups")
    ordering = ("id",)


# Déregister l'admin User par défaut et enregistrer une version personnalisée
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Directeur, FonctionnaireAdmin)
admin.site.register(Agent, FonctionnaireAdmin)
admin.site.register(Ordsec, FonctionnaireAdmin)
admin.site.register(Tresorier, FonctionnaireAdmin)
admin.site.register(Sg, FonctionnaireAdmin)
admin.site.register(Operateur, OperateurAdmin)
