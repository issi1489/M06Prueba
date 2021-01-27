
from django import forms
from django.forms import widgets
from .models import *

<<<<<<< HEAD
class UsuarioForms(forms.ModelForm):
 
=======



class FormularioUsuario(forms.ModelForm):
    
>>>>>>> cdcf2c8ecf05ed93136ff1c30dcd9edb66917202
    class Meta:
        model=Usuario
        fields='__all__'


<<<<<<< HEAD
=======
class UsuarioForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Usuario
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }


>>>>>>> cdcf2c8ecf05ed93136ff1c30dcd9edb66917202
class DiagnosticoForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Diagnostico
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
<<<<<<< HEAD
       
=======
        Widget = {
            "Fecha_Fabricacion": forms.SelectDateWidget()
        }



>>>>>>> cdcf2c8ecf05ed93136ff1c30dcd9edb66917202
class PerfilBioquimicoForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = PerfilBioquimico
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
       
class HemogramaForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Hemograma
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
       


        
class CoagulacionForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Coagulacion
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
      


class GlicemiaForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Glicemia
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
      

class OrinaForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Orina
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
     

class PerfilLipidicoForms(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = PerfilLipidico
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
    



