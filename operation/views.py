from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OperationForm
from .models import Operation
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def list_operation(request):
    return render(request, 'operation/list_operation.html')

@login_required(login_url='login')
def ajouter_operation(request):
    form = OperationForm()
    if request.method == 'POST':
        form = OperationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    context = {'form': form}
    return render(request, 'operation/ajouter_operation.html', context)

@login_required(login_url='login')
def modifier_operation(request, pk):
    operation = Operation.objects.get(id=pk)
    form = OperationForm(instance=operation)

    if request.method == 'POST':
        form = OperationForm(request.POST, instance=operation)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    context = {'form': form}
    #'bonjour'

    return render(request, 'operation/ajouter_operation.html', context)


def supprimer_operation(request, pk):
    operation = Operation.objects.get(id=pk)
    if request.method == 'POST':
        operation.delete()
        return redirect('/dashboard')
    context = {'item': operation}
    return render(request, 'operation/supprimer_operation.html', context)
