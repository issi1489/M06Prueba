from django.shortcuts import render
from .models import Usuario, PerfilLipidico, Orina, Coagulacion, Glicemia, Diagnostico, Hemograma, PerfilBioquimico
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import FormularioUsuario, UsuarioForms, DiagnosticoForms, PerfilBioquimicoForms, HemogramaForms
from .forms import CoagulacionForms, GlicemiaForms, OrinaForms, PerfilLipidicoForms

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
        'plipidico':PerfilLipidicoForms()
    }
    

    if request.method == 'POST':
        formulario = PerfilLipidicoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["plipidico"] = formulario
			

    return render(request, 'app_med2/agregar/formulario8.html', data)


def paciente(request):
    return render(request,'../templates/app_med2/paciente.html')

# CODIGO PRUEBA 1

from django.template.response import TemplateResponse

def registroExamen(request):
    context = {
            'usuario_form': UsuarioForms(),
            'diagnostico_form': DiagnosticoForms(),
            'lipidico_form': PerfilLipidicoForms(),
            'glicemia_form': GlicemiaForms(),
            'coagulacion_form': CoagulacionForms(),
            'bioquimico_form': PerfilBioquimicoForms(),
            'orina_form': OrinaForms(),
            'hemograma_form': HemogramaForms()
        }
    
        
    if request.method == 'POST':
        

        usuario_form = UsuarioForms(request.POST)
        diagnostico_form = DiagnosticoForms(request.POST)
        lipidico_form = PerfilLipidicoForms(request.POST)
        glicemia_form = GlicemiaForms(request.POST)
        coagulacion_form = CoagulacionForms(request.POST)
        bioquimico_form = PerfilBioquimicoForms(request.POST)
        orina_form = OrinaForms(request.POST)
        hemograma_form = HemogramaForms(request.POST)


        if usuario_form.is_valid():
            usuario_form.save()
            return render(request,'app_med2/agregar/reg_examen.html',context) 

        elif diagnostico_form.is_valid():
            diagnostico_form.save()
            return render(request,'app_med2/agregar/reg_examen.html',context)     

        elif lipidico_form.is_valid():
            lipidico_form.save()
            return render(request,'app_med2/agregar/reg_examen.html',context)

        elif glicemia_form.is_valid():
            glicemia_form.save()
            return render(request,'app_med2/agregar/reg_examen.html',context)

        elif coagulacion_form.is_valid():
            coagulacion_form.save()
            return render(request,'app_med2/agregar/reg_examen.html',context)

        elif bioquimico_form.is_valid():
            bioquimico_form.save()
            return render(request,'app_med2/agregar/reg_examen.html',context)

        elif orina_form.is_valid():
            orina_form.save()
            return render(request,'app_med2/agregar/reg_examen.html',context)

        elif hemograma_form.is_valid():
            hemograma_form.save()
            return render(request,'app_med2/agregar/reg_examen.html',context)   

        else:
            context = {
                'usuario_form': usuario_form,
                'diagnostico_form': diagnostico_form,
                'lipidico_form': lipidico_form,
                'glicemia_form': glicemia_form,
                'coagulacion_form': coagulacion_form,
                'bioquimico_form': bioquimico_form,
                'orina_form': orina_form,
                'hemograma_form': hemograma_form

            }

    else:
        context = {
            'usuario_form': UsuarioForms(),
            'diagnostico_form': DiagnosticoForms(),
            'lipidico_form': PerfilLipidicoForms(),
            'glicemia_form': GlicemiaForms(),
            'coagulacion_form': CoagulacionForms(),
            'bioquimico_form': PerfilBioquimicoForms(),
            'orina_form': OrinaForms(),
            'hemograma_form': HemogramaForms()
        }

    return TemplateResponse(request, 'app_med2/agregar/reg_examen.html', context)
    '''
    if request.method == 'POST':

        usuario_form = UsuarioForms(request.POST)
        diagnostico_form = DiagnosticoForms(request.POST)
        lipidico_form = PerfilLipidicoForms(request.POST)
        glicemia_form = GlicemiaForms(request.POST)
        coagulacion_form = CoagulacionForms(request.POST)
        bioquimico_form = PerfilBioquimicoForms(request.POST)
        orina_form = OrinaForms(request.POST)
        hemograma_form = HemogramaForms(request.POST)


        if usuario_form.is_valid() or diagnostico_form.is_valid() or lipidico_form.is_valid() or glicemia_form.is_valid() or coagulacion_form.is_valid() or bioquimico_form.is_valid() or orina_form.is_valid() or hemograma_form.is_valid():

            usuario_form.save()
            diagnostico_form.save()
            lipidico_form.save()
            glicemia_form.save()
            coagulacion_form.save()
            bioquimico_form.save()
            orina_form.save()
            hemograma_form.save()
            #return HttpResponseRedirect('/success')        

        else:
            context = {
                'usuario_form': usuario_form,
                'diagnostico_form': diagnostico_form,
                'lipidico_form': lipidico_form,
                'glicemia_form': glicemia_form,
                'coagulacion_form': coagulacion_form,
                'bioquimico_form': bioquimico_form,
                'orina_form': orina_form,
                'hemograma_form': hemograma_form

            }

    else:
        context = {
            'usuario_form': UsuarioForms(),
            'diagnostico_form': DiagnosticoForms(),
            'lipidico_form': PerfilLipidicoForms(),
            'glicemia_form': GlicemiaForms(),
            'coagulacion_form': CoagulacionForms(),
            'bioquimico_form': PerfilBioquimicoForms(),
            'orina_form': OrinaForms(),
            'hemograma_form': HemogramaForms()
        }
    '''
    


