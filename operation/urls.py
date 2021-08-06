from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.list_operation),
    path('ajout_operation/', views.ajouter_operation, name='ajout_operation'),
    path('modifier_operation/<str:pk>', views.modifier_operation, name='modifier_operation'),
    path('supprimer_operation/<str:pk>', views.supprimer_operation, name='supprimer_operation')
]