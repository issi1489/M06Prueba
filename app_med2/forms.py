
from django import forms
from django.forms import widgets
from .models import *




class FormularioUsuario(forms.ModelForm):
    
    class Meta:
        model=Usuario
        fields='__all__'

class UserLoginForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }

class UsuarioForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Usuario
        #user django : ['first_name','last_name','username','password']
        # user proyecto 
        #fields = ['id','first_name','last_name','username','password','email']
        fields = '__all__'
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }

class FamiliarForms(forms.ModelForm):
    
    class Meta:
        model = Familiar
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

class PerfilLipidicoForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = PerfilLipidico
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }


