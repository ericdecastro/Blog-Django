from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from accounts.forms import CadastroForm


class RegisterView(CreateView):
    template_name = 'accounts/accounts_cadastro.html'
    success_url = reverse_lazy('login')
    form_class = CadastroForm
    success_message = "Your profile was created successfully"


class Login(LoginView):
    template_name = 'accounts/accounts_login.html'


class Logout(LogoutView):
    template_name = 'accounts/accounts_logout.html'
