from django.contrib import admin
from .models import CertificatAMC, Sigle


class CertificatAdmin(admin.ModelAdmin):
    list_display = (
        "numero",
        "reference",
        "operateur",
        "date_demande",
        "date_etat_versement",
        "date_quittance",
        "date_certificat",
        "nom_marchandise",
        "pays_origine",
        "quantite",
        "unite",
    )
    list_filter = (
        "date_demande",
        "date_etat_versement",
        "date_quittance",
        "date_certificat",
    )
    search_fields = ("numero", "reference")
    list_per_page = 25

class SigleAdmin(admin.ModelAdmin):
    list_display = (
        "sigle_amc",
        "sigle_agrement",
        "sigle_cipens",
    )
    search_fields = ("sigle_amc", "sigle_agrement", "sigle_cipens")
    list_per_page = 25

admin.site.register(CertificatAMC, CertificatAdmin)
admin.site.register(Sigle, SigleAdmin)
