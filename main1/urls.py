from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='acceuil'),
    path('ouverture_compte/', views.ouverture_compte, name='ouvrir_compte'),
    path('mode_payement/', views.payement, name='payement'),
    path('procedure_deconsignation/', views.procedure_deconsignation, name='procedure_deconsignation'),
    path('cgu/', views.cgu, name='cgu'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('aides_securite/', views.aides_securite, name='aides_securite'),
    path('contact/', views.contact, name='contact'),

]
