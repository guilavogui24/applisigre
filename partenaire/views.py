from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect

from compte.decorators import admin_only
from operation.filters import OperationFiltre
from operation.models import Operation
from compte.decorators import *
from .forms import PartenaireForm
from .models import Partenaire


# Create your views here.
@login_required(login_url='login')
def list_partenaire(request, pk):
    partenaire = Partenaire.objects.get(id=pk)
    operation = partenaire.operation_set.all()

    total_operation = operation.count()
    #total_operation = Operation.objects.filter(status = 'STATUS[0]').count()

    myFilter = OperationFiltre(request.GET, queryset=operation)
    operation = myFilter.qs

    sum_operation = Operation.objects.aggregate(Sum('Montant_Chiffre'))
    solde_operation = sum_operation['Montant_Chiffre__sum']

    context = {'partenaire': partenaire, 'operation': operation, 'solde_operation': solde_operation, 'total_operation' : total_operation, 'myFilter': myFilter}
    return render(request, 'partenaire/list_partenaire.html', context)


@login_required(login_url='login')
def ajouter_partenaire(request):
    form = PartenaireForm()
    if request.method == 'POST':
        form = PartenaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    context = {'form': form}
    return render(request, 'partenaire/ajouter_partenaire.html', context)

@admin_only
@login_required(login_url="acceuil")
def modifier_partenaire(request, pk):
    partenaire = Partenaire.objects.get(id=pk)
    form = PartenaireForm(instance=partenaire)

    if request.method == 'POST':
        form = PartenaireForm(request.POST, instance=partenaire)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    context = {'form': form}
    #'bonjour'

    return render(request, 'partenaire/ajouter_partenaire.html', context)


def supprimer_partenaire(request, pk):
    partenaire = Partenaire.objects.get(id=pk)
    if request.method == 'POST':
        partenaire.delete()
        return redirect('/dashboard')
    context = {'item': partenaire}
    return render(request, 'partenaire/supprimer_partenaire.html', context)

