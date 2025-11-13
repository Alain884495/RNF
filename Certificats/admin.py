from django.contrib import admin
from .models import CertificatAMC, Sigle


class CertificatAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "numero",
        "reference",
        "service",
        "etat",
        "operateur",
        "agent",
        "ordsec",
        "tresorier",
        "directeur",
        "dateDemande",
        "nomMarchandise",
        "paysOrigine",
        "quantite",
        "unite",
    )
    search_fields = ("numero",)
    list_filter = ("etat",)
    ordering = ("numero",)
    raw_id_fields = ("agent",)  # préférable si beaucoup d'utilisateurs
    readonly_fields = ()


class SigleAdmin(admin.ModelAdmin):
    list_display = ("id", "sigleCertificatamc", "sigleAgrementppn")


admin.site.register(CertificatAMC, CertificatAdmin)
admin.site.register(Sigle, SigleAdmin)
