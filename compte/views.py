from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from projet import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .decorators import *

from .forms import CustomUserCreationForm, ProfileForm, UserForm

from .models import *


# Create your views here.

def profile(request):
    return render(request, 'compte/profile.html')


# CRUD VIEWS
def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('main1/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['guilavoguijoseph@gmail.com']
        )

        email.fail_silently = False
        email.send()

    return render(request, 'main1/email_sent.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('acceuil')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Little Hack to work around re-building the usermodel
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except:
            messages.error(request, "L'utilisateur avec cet e-mail n'existe pas")
            return redirect('login')

        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.error(request, 'E-mail ou mot de passe incorrect')

    context = {}
    return render(request, 'compte/login.html', context)


def registerPage(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Compte créé avec succès!')

            user = authenticate(request, username=user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)

            next_url = request.GET.get('next')
            if next_url == '' or next_url == None:
                next_url = 'acceuil'
            return redirect(next_url)
        else:
            messages.error(request, "Une erreur s'est produite lors de l'enregistrement")
    context = {'form': form}
    return render(request, 'compte/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('acceuil')


@login_required(login_url="acceuil")
def userAccount(request):
    profile = request.user.profile

    context = {'profile': profile}
    return render(request, 'compte/account.html', context)


@login_required(login_url="acceuil")
def updateProfile(request):
    user = request.user
    profile = user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()

        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'compte/profile_form.html', context)
