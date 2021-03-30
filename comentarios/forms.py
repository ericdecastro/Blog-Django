from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Comentario
import requests
from decouple import config


class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': config('RECAPTCHA'),
                'response': recaptcha_response
            }
        )

        recaptcha_result = recaptcha_request.json()

        if not recaptcha_response:
            raise ValidationError('Por favor, marque a caixa "não sou um robô."')

        elif not recaptcha_result.get('success'):
            raise ValidationError('Você é um robô.')

    class Meta:
        model = Comentario
        fields = ('comentario',)
