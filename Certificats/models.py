from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from Authentification.models import (
    Agent,
    Directeur,
    Ordsec,
    Tresorier,
    Operateur,
)


class Certificat(models.Model):
    numero = models.CharField(max_length=20, unique=True, blank=True, null=True)
    reference = models.CharField(max_length=20, blank=True, null=True)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    service = GenericForeignKey("content_type", "object_id")
    operateur = models.ForeignKey(
        Operateur, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, blank=True, null=True)
    ordsec = models.ForeignKey(
        Ordsec, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    directeur = models.ForeignKey(
        Directeur, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    tresorier = models.ForeignKey(
        Tresorier, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    etat = models.CharField(max_length=25, blank=True, null=True)
    dateDemande = models.DateField(blank=True, null=True)
    dateEtatVersement = models.DateField(blank=True, null=True)
    dateQuittance = models.DateField(blank=True, null=True)
    dateCertificat = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.service

    class Meta:
        abstract = True

    @classmethod
    def creerCertificat(cls, **kwargs):
        certificat = cls(**kwargs)
        certificat.save()
        return certificat

    @classmethod
    def modifierCertificat(cls, **kwargs):
        certificat = cls(**kwargs)
        certificat.save()
        return certificat

    @classmethod
    def supprimerCertificat(cls, **kwargs):
        certificat = cls(**kwargs)
        certificat.delete()
        return certificat

    @classmethod
    def chercherCertificat(cls, **kwargs):
        certificat = cls(**kwargs)
        return certificat


class CertificatAMC(Certificat):
    nomMarchandise = models.CharField(max_length=40, blank=True, null=True)
    paysOrigine = models.CharField(max_length=25, blank=True, null=True)
    quantite = models.FloatField(blank=True, null=True)
    unite = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        if self.numero:
            return f"AMC {self.numero} - {self.nomMarchandise or 'Sans nom'}"
        return f"AMC (ID: {self.id}) - {self.nomMarchandise or 'Sans nom'}"
