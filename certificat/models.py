from django.db import models
from authentification.models import Agent, Ordsec, Tresorier, Directeur, Operateur

class Certificat(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, null=True, blank=True)
    ordsec = models.ForeignKey(Ordsec, on_delete=models.DO_NOTHING, null=True, blank=True)
    tresorier = models.ForeignKey(Tresorier, on_delete=models.DO_NOTHING, null=True, blank=True)
    directeur = models.ForeignKey(Directeur, on_delete=models.DO_NOTHING, null=True, blank=True)
    operateur = models.ForeignKey(Operateur, on_delete=models.DO_NOTHING, null=True, blank=True)
    numero = models.CharField(max_length=50, null=True, blank=True)
    reference = models.CharField(max_length=50, null=True, blank=True)
    etat = models.CharField(max_length=25, null=True, blank=True)
    date_demande = models.DateField(auto_now_add=True)
    date_etat_versement = models.DateField(null=True, blank=True)
    date_quittance = models.DateField(null=True, blank=True)
    date_certificat = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.numero or "Certificat sans numéro"
    
    class Meta:
        abstract = True

class CertificatAMC(Certificat):
    nom_marchandise = models.CharField(max_length=100)
    pays_origine = models.CharField(max_length=100)
    quantite = models.IntegerField()
    unite = models.CharField(max_length=10)


class Sigle(models.Model):
    sigle_amc = models.CharField(max_length=25, blank=True, null=True)
    sigle_agrement = models.CharField(max_length=25, blank=True, null=True)
    sigle_cipens = models.CharField(max_length=25, blank=True, null=True)
    