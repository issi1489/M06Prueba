from django import forms
from django.forms import widgets
from .models import *
#from .models import Usuario,Diagnostico,PerfilBioquimico,Hemograma,Orina, Coagulacion, Glicemia,


class UsuarioForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Usuario
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }
class DiasnosticoForms(forms.ModelForm):

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


class glicemiaForms(forms.ModelForm):

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

class PerfilLipidicoForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = PerfilLipidico
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }