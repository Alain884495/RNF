from django.contrib import admin
from .models import ServiceCommerce, ServiceConditionnement, ServiceMetrologie

admin.site.register(ServiceCommerce)
admin.site.register(ServiceConditionnement)
admin.site.register(ServiceMetrologie)

