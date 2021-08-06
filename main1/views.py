from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template.loader import render_to_string

from operation.models import Operation
from partenaire.models import Partenaire
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here



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

def payement(request):
    return render(request, 'main1/mode_de_payement.html')

def cgu(request):
    return render(request, 'main1/cgu.html')

def procedure_deconsignation(request):
    return render(request, 'main1/procedure_de_deconsignation.html')

def aides_securite(request):
    return render(request, 'main1/aides_securite.html')

def contact(request):
    return render(request, 'main1/contact.html')





