from django.contrib import admin
from .models import Profils
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(Profils)
class ProfilsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profils._meta.get_fields()]


# D'abord désenregistrer le User par défaut
admin.site.unregister(User)

# Puis le réenregistrer avec ton admin personnalisé
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # exemple : afficher d’autres champs
    list_display = ("username", "email", "is_staff", "is_active", "date_joined")
