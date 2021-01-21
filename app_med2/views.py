from django.shortcuts import render
from .models import Usuario, PerfilLipidico, Orina, Coagulacion, Glicemia, Diagnostico, Hemograma, PerfilBioquimico
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView



class ListarUsuario(ListView):
    model=Usuario
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_usuarios')

class CrearUsuario(CreateView):
    model=Usuario
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_usuarios')

class UpdateUsuario(UpdateView):
    model=Usuario
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_usuarios')

class EliminarUsuario(DeleteView):
    model=Usuario
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_usuarios')






def base(request):

    return render(request, 'app_med2/agregar/base.html')

def admin(request):

    return render(request, 'app_med2/admin.html')


def home(request):

    return render(request, 'app_med2/home.html')



def usuario(request):
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
			

    return render(request, 'app_med2/agregar/formulario1.html', data)


def diagnostico(request):
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
			

    return render(request, 'app_med2/agregar/formulario2.html', data)


def PerBioquimico(request):
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
			

    return render(request, 'app_med2/agregar/formulario3.html', data)


    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
def hemograma(request):
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
			

    return render(request, 'app_med2/agregar/formulario4.html', data)


def coagulacion(request):
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
			

    return render(request, 'app_med2/agregar/formulario5.html', data)



def glicemia(request):
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

    return render(request, 'app_med2/agregar/formulario6.html', data)
        
def orina(request):
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
			

    return render(request, 'app_med2/agregar/formulario7.html', data)


def perfilLipidico(request):
    data = {
        'perfil1':PerfilLipidicoForms()
    }
    

    if request.method == 'POST':
        formulario = PerfilLipidicoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["perfil1"] = formulario
			

    return render(request, 'app_med2/agregar/formulario8.html', data)


def paciente(request):
    return render(request,'../templates/app_med2/paciente.html')

    
class VerUsuarios(ListView):
    model = Usuario
    template_name = "app_med2/ver_usuarios.html"
    context_object_name = "usuarios"