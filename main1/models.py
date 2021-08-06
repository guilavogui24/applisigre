from django.db import models

# Create your models here.
from django.shortcuts import render
from operation.models import Operation
from partenaire.models import Partenaire
from django.contrib.auth.decorators import login_required
# Create your views here


@login_required(login_url='login')
def home(request):
    operations = Operation.objects.all()
    partenaires = Partenaire.objects.all()
    context = {'operations': operations, 'partenaires': partenaires}
#   return render(request, 'main1/acceuil.html', context)
    return render(request, 'main1/home.html', context)

@login_required(login_url='login')
def dashboard(request):
        operations = Operation.objects.all()
        partenaires = Partenaire.objects.all()
        context = {'operations': operations, 'partenaires': partenaires}
        return render(request, 'main1/dashboard.html', context)


def ouverture_compte(request):
    return render(request, 'main1/ouverture_de_compte.html')


def cgu(request):
    return render(request, 'main1/cgu.html')


def payement(request):
    return render(request, 'main1/mode_de_payement.html')


def nous_contacter(request):
    return render(request, 'main1/nous_contacter.html')


def procedure_deconsignation(request):
    return render(request, 'main1/procedure_de_deconsignation.html')
