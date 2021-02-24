from django.urls import path
from .views import *


urlpatterns = [
    path('cadastro/', RegisterView.as_view(), name='cadastro'),
    path('entrar/', LoginView.as_view(template_name='accounts/accounts_login.html'), name='entrar'),
    path('sair/', LogoutView.as_view(template_name='accounts/accounts_logout.html'), name='sair'),
]