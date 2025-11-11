from django.contrib import admin
from .models import CertificatAMC


class CertificatAdmin(admin.ModelAdmin):
    list_display = (
        "numero",
        "reference",
        "etat",
        "operateur",
        "agent",
        "ordsec",
        "tresorier",
        "directeur",
        "dateDemande",
    )
    search_fields = ("numero",)
    list_filter = ("etat",)
    ordering = ("numero",)
    raw_id_fields = ("agent",)  # préférable si beaucoup d'utilisateurs
    readonly_fields = ()


admin.site.register(CertificatAMC, CertificatAdmin)
