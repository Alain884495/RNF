from django.contrib import admin
from .models import Operateur, Directeur, Agent, Ordsec, Tresorier, Sg

class OperateurAdmin(admin.ModelAdmin):
    list_display = ('user', 'nif', 'stat', 'raison_sociale', 'adresse_pro', 'phone_pro', 'phone_perso', 'adresse_perso')
    list_filter = ('user', 'nif', 'stat', 'raison_sociale', 'adresse_pro', 'phone_pro', 'phone_perso', 'adresse_perso')
    search_fields = ('user', 'nif', 'stat', 'raison_sociale', 'adresse_pro', 'phone_pro', 'phone_perso', 'adresse_perso')
    list_per_page = 25

class FonctionnaireAdmin(admin.ModelAdmin):
    list_display = ('user', 'matricule', 'role', 'fonction', 'service', 'adresse_pro', 'adresse_perso', 'phone')
    list_filter = ('user', 'matricule', 'role', 'fonction', 'service', 'adresse_pro', 'adresse_perso', 'phone')
    search_fields = ('user', 'matricule', 'role', 'fonction', 'service', 'adresse_pro', 'adresse_perso', 'phone')
    list_per_page = 25


admin.site.register(Operateur, OperateurAdmin)
admin.site.register(Directeur, FonctionnaireAdmin)
admin.site.register(Agent, FonctionnaireAdmin)
admin.site.register(Ordsec, FonctionnaireAdmin)
admin.site.register(Tresorier, FonctionnaireAdmin)
admin.site.register(Sg, FonctionnaireAdmin)