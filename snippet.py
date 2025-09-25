
#AFFICHER LES CHAMPS DU MODEL DANS L'ADMIN ----> admin.py
from django.contrib import admin
from .models import Produit

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Produit._meta.get_fields()]


            # ou

from django.contrib import admin
from .models import Produit

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "prix", "date_creation")


#AFFICHER LES CHAMPS DU USER DANS L'ADMIN ----> admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models import ManyToManyField

# Désenregistrer le User existant
admin.site.unregister(User)

# Créer un nouveau UserAdmin
class UserAdmin(BaseUserAdmin):
    # afficher tous les champs sauf ManyToMany pour éviter les erreurs
    list_display = [f.name for f in User._meta.get_fields() if not isinstance(f, ManyToManyField)]

# Réenregistrer le User avec le nouvel admin
admin.site.register(User, UserAdmin)