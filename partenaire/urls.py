from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('/<str:pk>', views.list_partenaire, name='partenaire'),
    path('ajout_partenaire/', views.ajouter_partenaire, name='ajout_partenaire'),
    path('modifier_partenaire/<str:pk>', views.modifier_partenaire, name='modifier_partenaire'),
    path('supprimer_partenaire/<str:pk>', views.supprimer_partenaire, name='supprimer_partenaire')
]