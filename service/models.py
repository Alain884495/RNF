from django.db import models

class Service(models.Model):
    nom_service = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom_service

    class Meta:
        abstract = True

class ServiceCommerce(Service):
    pass

class ServiceConditionnement(Service):
    pass

class ServiceMetrologie(Service):
    pass