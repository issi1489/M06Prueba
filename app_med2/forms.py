
from django import forms
from .model import UsuarioCBV

from django.core import validators
from django.core.exceptions import ValidationError
import datetime


# form para vistas basadas en clases

class UsuarioFormularioCBV(forms.ModelForm):

    class Meta:
        model = UsuarioCBV
        fields = '__all__'


