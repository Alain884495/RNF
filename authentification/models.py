from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profils(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fonction = models.CharField(max_length=25, blank=True, null=True)
    service = models.CharField(max_length=25, blank=True, null=True)
    def __str__(self):
        return str(self.user)