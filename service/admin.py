from django.contrib import admin
from .models import DirectionRegionale, ServiceCommerce, ServiceConditionnement, ServiceMetrologie

admin.site.register(DirectionRegionale)
admin.site.register(ServiceCommerce)
admin.site.register(ServiceConditionnement)
admin.site.register(ServiceMetrologie)

