
from .import views

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


# urlpatterns = [
#     path('inscription/', views.inscriptionPage, name='inscription'),
#     path('connexion/', views.connexionPage, name='connexion'),
#     path('deconnexion/', views.logoutUser, name='deconnexion')
# ]

urlpatterns = [

    path('profile/', views.profile, name="profile"),



    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    path('account/', views.userAccount, name="account"),
    path('update_profile/', views.updateProfile, name="update_profile"),

    path('send_email/', views.sendEmail, name="send_email"),



#1
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="compte/password_reset.html"), name="password_reset"),

    #Where can I find OR set theses paths these values
    #2
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="compte/email_sent.html"),name="password_reset_done"),
    #3
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="compte/reset.html"), name="password_reset_confirm"),
    #4
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="compte/reset_complete.html"), name="password_reset_complete"),

]