from django.shortcuts import render
from .models import Usuario, PerfilLipidico, Orina, Coagulacion, Glicemia, Diagnostico, Hemograma, PerfilBioquimico
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import FormularioUsuario, UsuarioForms, DiagnosticoForms, PerfilBioquimicoForms, HemogramaForms
from .forms import CoagulacionForms, GlicemiaForms, OrinaForms, PerfilLipidicoForms
from django.template.response import TemplateResponse

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


def paciente(request):
    return render(request,'../templates/app_med2/paciente.html')


def registroExamen(request):
    '''
    Función registroExamen:
        * Carga los formularios en el template reg_examen.html es este orden:
            | usuario | diagnostico |
            |perfil lipidico| glicemia | coagulacion |
            |perfil bioquimico | orina | hemograma |

        * Permite insertar datos de los formularios a la BD en PostgreSQL
    '''
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

    return TemplateResponse(request, 'app_med2/registros_nuevos.html', context)
