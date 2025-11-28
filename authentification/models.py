from django.db import models
from django.contrib.auth.models import User


class Operateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nif = models.CharField(max_length=20)
    stat = models.CharField(max_length=20)
    raison_sociale = models.CharField(max_length=100)
    adresse_pro = models.CharField(max_length=100)
    phone_pro = models.CharField(max_length=100)
    phone_perso = models.CharField(max_length=100)
    adresse_perso = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
        
        

class Fonctionnaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=50)
    matricule = models.CharField(max_length=20)
    adresse_pro = models.CharField(max_length=100)
    adresse_perso = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    fonction = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

    class Meta:
        abstract = True

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

