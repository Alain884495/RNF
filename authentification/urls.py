from django.urls import path
from . import views
app_name = 'authentification'

urlpatterns = [
    path('', views.index, name='index'),
    path('inscription/', views.inscription, name='inscription'),
    path('accueilOrdsec/', views.accueilOrdsec, name='accueilOrdsec'),
    path('accueilCommerce', views.accueilCommerce, name='accueilCommerce'),
]
