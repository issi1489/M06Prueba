from django.shortcuts import render
from .models import Usuario, PerfilLipidico, Orina, Coagulacion, Glicemia, Diagnostico, Hemograma, PerfilBioquimico
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
<<<<<<< HEAD
from .forms import *

=======
from .forms import FormularioUsuario, UsuarioForms, DiagnosticoForms, PerfilBioquimicoForms, HemogramaForms
from .forms import CoagulacionForms, GlicemiaForms, OrinaForms, PerfilLipidicoForms
>>>>>>> ffdfb6d1889422f4adbbe25c9858f2ab1e059a94

class ListarUsuario(ListView):
    model=Usuario
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_usuarios')

class CrearUsuario(CreateView):
    model=Usuario
    template_name='app_med2/usuario_form.html'
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_usuarios')

class UpdateUsuario(UpdateView):
    model=Usuario
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_usuarios')

class EliminarUsuario(DeleteView):
    model= Usuario
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_usuarios')






def base(request):

    return render(request, 'app_med2/agregar/base.html')

def admin(request):

    return render(request, 'app_med2/admin.html')


def home(request):

    return render(request, 'app_med2/home.html')


'''def usuario(request):
    data = {
        'usuario': UsuarioForms()
    }
    

    if request.method == 'POST':
        formulario = UsuarioForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["usuario"] = formulario
			

    return render(request, 'app_med2/agregar/formulario1.html', data)'''

class Diagnostico(CreateView):
    model= Diagnostico
    fields='__all__'
    success_url=reverse_lazy('app_med2:formulario_form')


'''def diagnostico(request):
    data = {
        'diagnostico': DiagnosticoForms()
    }
    

    if request.method == 'POST':
        formulario = DiagnosticoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["diagnostico"] = formulario
			

    return render(request, 'app_med2/agregar/formulario2.html', data)'''

class Perfilbioquimico(CreateView):
    model= PerfilBioquimico
    fields='__all__'
    success_url=reverse_lazy('app_med2:formulario3.html')

'''def PerBioquimico(request):
    data = {
        'perfil':PerfilBioquimicoForms()
    }
    

    if request.method == 'POST':
        formulario = PerfilBioquimicoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["perfil"] = formulario
			

    return render(request, 'app_med2/agregar/formulario3.html', data)'''

class Hemograma(CreateView):
    model= Hemograma
    fields='__all__'
    success_url=reverse_lazy('app_med2:hemograma_form')
    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
'''def hemograma(request):
    data = {
        'hemograma': HemogramaForms()
    }
    

    if request.method == 'POST':
        formulario = HemogramaForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["hemograma"] = "contacto guardado"
        else:
            data["hemogram"] = formulario
			

    return render(request, 'app_med2/agregar/formulario4.html', data)'''

class Coagulacion(CreateView):
    model= Coagulacion
    fields='__all__'
    success_url=reverse_lazy('app_med2:formulario5.html')

'''def coagulacion(request):
    data = {
        'coagulacion': CoagulacionForms()
    }
    

    if request.method == 'POST':
        formulario = CoagulacionForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["coagulacion"] = formulario
			

    return render(request, 'app_med2/agregar/formulario5.html', data)'''

class Glicemia(CreateView):
    model= Glicemia
    fields='__all__'
    success_url=reverse_lazy('app_med2:formulario6.html')

'''def glicemia(request):
    data = {
        'glicemia': GlicemiaForms()
    }

    if request.method == 'POST':
        formulario = GlicemiaForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["glicemia"] = formulario

    return render(request, 'app_med2/agregar/formulario6.html', data)'''

class Orina(CreateView):
    model= Orina
    fields='__all__'
    success_url=reverse_lazy('app_med2:formulario7.html')

'''def orina(request):
    data = {
        'orina': OrinaForms()
    }
    

    if request.method == 'POST':
        formulario = OrinaForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["orina"] = formulario
			

    return render(request, 'app_med2/agregar/formulario7.html', data)'''

class PerfilLipidico(CreateView):
    model= PerfilLipidico
    fields='__all__'
    success_url=reverse_lazy('app_med2:formulario8.html')

'''def perfilLipidico(request):
    data = {
        'plipidico':PerfilLipidicoForms()
    }
    

    if request.method == 'POST':
        formulario = PerfilLipidicoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["plipidico"] = formulario
			

    return render(request, 'app_med2/agregar/formulario8.html', data)'''


def paciente(request):
    return render(request,'../templates/app_med2/paciente.html')


# NO TOCAR DE AQUI EN ADELANTE!

def registroExamen(request, template="pruebas_forms.html"):
    """
    Handle Multiple <form></form> elements
    """
    data = {'plipidico':PerfilLipidicoForms(), 'orina': OrinaForms(),
            'glicemia':GlicemiaForms(), 'coagulacion':CoagulacionForms(),
            'hemograma':HemogramaForms(), 'bioquimico': PerfilBioquimicoForms(),
            'diagnostico': DiagnosticoForms(), 'usuario':UsuarioForms()}


    if request.method == 'POST':
        if request.POST.get("form_type") == 'formLip':
            #Perfil lipidico
            formulario = PerfilLipidicoForms(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "contacto guardado"
            else:
                data["plipidico"] = formulario
        elif request.POST.get("form_type") == 'formOrin':
            # Orina
            formulario = OrinaForms(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "contacto guardado"
            else:
                data["orina"] = formulario
        elif request.POST.get("form_type") == 'formOrin':
            # Glicemia
            formulario = GlicemiaForms(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "contacto guardado"
            else:
                data["glicemia"] = formulario
        elif request.POST.get("form_type") == 'formOrin':
            # coagulacion
            formulario = CoagulacionForms(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "contacto guardado"
            else:
                data["coagulacion"] = formulario
        elif request.POST.get("form_type") == 'formOrin':
            # Hemograma
            formulario = HemogramaForms(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "contacto guardado"
            else:
                data["hemograma"] = formulario
        elif request.POST.get("form_type") == 'formOrin':
            # Bioquimico
            formulario = PerfilBioquimicoForms(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "contacto guardado"
            else:
                data["bioquimico"] = formulario
        elif request.POST.get("form_type") == 'formOrin':
            # diagnostico
            formulario = DiagnosticoForms(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "contacto guardado"
            else:
                data["diagnostico"] = formulario
        elif request.POST.get("form_type") == 'formOrin':
            # Glicemia
            formulario = UsuarioForms(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "contacto guardado"
            else:
                data["usuario"] = formulario    

    return render(request, 'app_med2/agregar/reg_examen.html', data)
