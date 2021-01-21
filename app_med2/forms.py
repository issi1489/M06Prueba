
from django import forms
<<<<<<< HEAD
'''
from django.core import validators
from django.core.exceptions import ValidationError
import datetime
import json 

def validar_fecha(fecha):
    fecha_mayor = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d").date()
    if fecha <= fecha_mayor:
        return fecha
    else:
        raise ValidationError("Sólo fechas de diciembre 2020")

class CrearUsuario(forms.Form):
    dni = forms.CharField(widget = forms.TextInput(
                                attrs = {'style': 'background-color: pink;'}),
                                    validators=[validators.MinLengthValidator(9, "Ingresar dni en el siguiente formato 77111666-5"), 
                                        validators.MaxLengthValidator(11, "Ingresar dni en el siguiente formato 77111666-5")])

    nombre = forms.CharField(widget = forms.TextInput(
                                attrs = {'style': 'background-color: green;'}),
                                    validators=[validators.MinLengthValidator(10, "El nombre debe tener minimo 10 caracteres"), 
                                        validators.MaxLengthValidator(30, "El nombre puede tener hasta 30 caracteres")])

    edad =  forms.IntegerField(widget = forms.TextInput( 
                                attrs = {'style': 'background-color: yellow;'}),
                                    validators=[validators.MinValueValidator(1, "Error, la edad no puede ser menor a 1 "),
                                        validators.MaxValueValidator(99, "Error, la edad no puede tener menos más de 3 numero")])

    direccion = forms.CharField(widget = forms.TextInput(
                                attrs = {'style': 'background-color: red;'}),
                                    validators=[validators.MinLengthValidator(10, "Error, la dirección debe contener más de 10 caracteres"),
                                                validators.MaxLengthValidator(50, "Error, la dirección puede contener hasta 30 caracteres ")])                                                
    tipo_usuario = forms.CharField(widget = forms.TextInput(
                                attrs = {'style': 'background-color: orange;'}),
                                    validators=[validators.MinLengthValidator(1, "El tipo de usuario puede ser A o U"),
                                                validators.MaxLengthValidator(1, "El tipo de usuario puede ser A o U")])
                                                        
    #fecha_creacion = forms.DateField(validators=[validar_fecha])

class Contacto(forms.Form):
=======
from django.forms import widgets
from .models import *


class FormularioUsuario(forms.ModelForm):
>>>>>>> 117f807af2810a14463d52f2f6385cfc93a1d497
    
    class Meta:
        model=Usuario
        fields='__all__'



"""
class UsuarioForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Usuario
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }
class DiagnosticoForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Diagnostico
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }
class PerfilBioquimicoForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = PerfilBioquimico
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()

        }
class HemogramaForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Hemograma
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }


        
class CoagulacionForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Coagulacion
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }


class GlicemiaForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Glicemia
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }

class OrinaForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Orina
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }

<<<<<<< HEAD

class rutPacientes(forms.Form):
=======
class PerfilLipidicoForms(forms.ModelForm):
>>>>>>> 117f807af2810a14463d52f2f6385cfc93a1d497

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = PerfilLipidico
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }

<<<<<<< HEAD
    rut_pac= forms.ChoiceField(choices=(rut_pacs))
    '''
=======
"""
>>>>>>> 117f807af2810a14463d52f2f6385cfc93a1d497
