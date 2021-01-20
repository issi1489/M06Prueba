from django import forms
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
    
    nombre = forms.CharField(widget = forms.TextInput(
                attrs = {'style': 'background-color: green;'}),
                validators=[validators.MinLengthValidator(10, "El nombre debe tener minimo 10 caracteres"), 
                validators.MaxLengthValidator(30, "El nombre puede tener hasta 30 caracteres")])

    email = forms.EmailField(widget = forms.TextInput(
                attrs = {'style': 'background-color: pink;'}))

    mensaje_email = forms.CharField(widget = forms.TextInput(
                attrs = {'style': 'background-color: yellow;'}),
                validators=[ validators.MaxLengthValidator(100, "El nombre puede tener hasta 30 caracteres")])

class rutPacientes(forms.Form):

     # Generar copia de los datos de usuarios
    with open('../proyecto_web/app_med2/data/usuarios.json', 'r') as file:
        pacientes=json.load(file)

    #Extraer ruts para lista desplegable de cambio de usuario
    rut_pacs=[]
    for p in pacientes:
        rut_pacs.append((p,p))

    rut_pac= forms.ChoiceField(choices=(rut_pacs))