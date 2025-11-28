from django.urls import path
from . import views

app_name = "authentification"

urlpatterns = [
    path('', views.index, name="index"),
    path('inscription_operateur/', views.inscription_operateur, name="inscription_operateur"),
    path('inscription_fonctionnaire/', views.inscription_fonctionnaire, name="inscription_fonctionnaire"),
]