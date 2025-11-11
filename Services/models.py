from django.db import models


# Create your models here.
class Service(models.Model):
    nomService = models.CharField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.nomService)


class ServiceCommerce(Service):
    pass


class ServiceConditionnement(Service):
    pass


class ServiceMetrologie(Service):
    pass
