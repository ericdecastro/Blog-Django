from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
import requests
from django.contrib import messages
from django.core.exceptions import ValidationError


User = get_user_model()


class CadastroForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="Nome")
    last_name = forms.CharField(max_length=30, required=True, label="Sobrenome")
    username = forms.CharField(max_length=30, required=True, label="Usuário")
    email = forms.EmailField(max_length=254, required=True, label="E-Mail")

    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LcWqYAaAAAAADUGOTCXfPxWiB4yCjdlCPNf2OO_',
                'response': recaptcha_response
            }
        )

        recaptcha_result = recaptcha_request.json()

        if not recaptcha_response:
            raise ValidationError('Por favor, marque a caixa "não sou um robô."')

        elif not recaptcha_result.get('success'):
            raise ValidationError('Você é um robô.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LcWqYAaAAAAADUGOTCXfPxWiB4yCjdlCPNf2OO_',
                'response': recaptcha_response
            }
        )

        recaptcha_result = recaptcha_request.json()

        if not recaptcha_response:
            raise ValidationError('Por favor, marque a caixa "não sou um robô."')

        elif not recaptcha_result.get('success'):
            raise ValidationError('Você é um robô.')

