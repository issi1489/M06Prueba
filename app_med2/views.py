from django.shortcuts import render
from .models import Usuario, PerfilLipidico, Orina, Coagulacion, Glicemia, Diagnostico, Hemograma, PerfilBioquimico
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import FormularioUsuario, UsuarioForms, DiagnosticoForms, PerfilBioquimicoForms, HemogramaForms
from .forms import CoagulacionForms, GlicemiaForms, OrinaForms, PerfilLipidicoForms
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

# Home 
def home(request):
    '''
    Home page de el proyecto
    '''
    return render(request, 'app_med2/home.html')

# Vista admin
def admin(request):     
    return render(request, 'app_med2/admin.html')
 
# Vista admin
def cuidador(request):
    pass
# Vista admin: Crear nuevos registros

def nuevoRegistro(request):
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
            return render(request,'app_med2/registros_nuevos.html',context) 

        elif diagnostico_form.is_valid():
            diagnostico_form.save()
            return render(request,'app_med2/registros_nuevos.html',context)     

        elif lipidico_form.is_valid():
            lipidico_form.save()
            return render(request,'app_med2/registros_nuevos.html',context)

        elif glicemia_form.is_valid():
            glicemia_form.save()
            return render(request,'app_med2/registros_nuevos.html',context)

        elif coagulacion_form.is_valid():
            coagulacion_form.save()
            return render(request,'app_med2/registros_nuevos.html',context)

        elif bioquimico_form.is_valid():
            bioquimico_form.save()
            return render(request,'app_med2/registros_nuevos.html',context)

        elif orina_form.is_valid():
            orina_form.save()
            return render(request,'app_med2/registros_nuevos.html',context)

        elif hemograma_form.is_valid():
            hemograma_form.save()
            return render(request,'app_med2/registros_nuevos.html',context)   

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

# Vista admin: Template intermedio con links a listas
def gestionRegistro(request):
    '''
    Función para visualizar un template intermedio que permite ingresar
    a las distintas tablas con datos de usuario, diagnostico y exámenes.
    '''
    return render(request,'../templates/app_med2/registros_gestion.html')


# Vista paciente
@login_required(login_url='/accounts/login/')
def paciente(request):

    datos_us = Usuario.objects.filter(rutUsuario='17684562-7')
    diagnostico_us = Diagnostico.objects.filter(rutUsuario='17684562-7')
    pBioquimico_us = PerfilBioquimico.objects.filter(rutUsuario='17684562-7')
    hemograma_us = Hemograma.objects.filter(rutUsuario='17684562-7')
    coagulacion_us = Coagulacion.objects.filter(rutUsuario='17684562-7')
    glicemia_us = Glicemia.objects.filter(rutUsuario='17684562-7')
    orina_us = Orina.objects.filter(rutUsuario='17684562-7')
    pLipidico_us = PerfilLipidico.objects.filter(rutUsuario='17684562-7')

    context = {'datos':datos_us,'diagnostico':diagnostico_us,
                'pBioquimico':pBioquimico_us, 'hemograma':hemograma_us,
                'coagulacion':coagulacion_us, 'glicemia':glicemia_us,
                'orina':orina_us, 'pLipidico':pLipidico_us}

    return render(request,'../templates/app_med2/paciente.html',context)

#----------------------------------- CRUDS ---------------------------------

# CRUD USUARIO
class ListarUsuario(ListView):
    model=Usuario
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

# CRUD DIAGNOSTICO
class ListarDiagnostico(ListView):
    model=Diagnostico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_diagnosticos')
    
class UpdateDiagnostico(UpdateView):
    model=Diagnostico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_diagnosticos')

class EliminarDiagnostico(DeleteView):
    model=Diagnostico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_diagnosticos')

# CRUD PERFIL LIPIDICO
class ListarPerfilLipidico(ListView):
    model=PerfilLipidico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfillipidico')
    
class UpdatePerfilLipidico(UpdateView):
    model=PerfilLipidico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfillipidico')

class EliminarPerfilLipidico(DeleteView):
    model=PerfilLipidico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfillipidico')

#CRUD GLICEMIA
class ListarGlicemia(ListView):
    model=Glicemia
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_glicemia')
    
class UpdateGlicemia(UpdateView):
    model=Glicemia
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_glicemia')

class EliminarGlicemia(DeleteView):
    model=Glicemia
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_glicemia')

#CRUD PerfilBioquimico
class ListarPerfilBioquimico(ListView):
    model=PerfilBioquimico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfilbioquimico')
    
class UpdatePerfilBioquimico(UpdateView):
    model=PerfilBioquimico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfilbioquimico')

class EliminarPerfilBioquimico(DeleteView):
    model=PerfilBioquimico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfilbioquimico')

#CRUD Orina
class ListarOrina(ListView):
    model=Orina
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_orina')
    
class UpdateOrina(UpdateView):
    model=Orina
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_orina')

class EliminarOrina(DeleteView):
    model=Orina
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_orina')

#CRUD Coagulacion
class ListarCoagulacion(ListView):
    model=Coagulacion
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_coagulacion')
    
class UpdateCoagulacion(UpdateView):
    model=Coagulacion
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_coagulacion')

class EliminarCoagulacion(DeleteView):
    model=Coagulacion
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_coagulacion')

#CRUD Hemograma
class ListarHemograma(ListView):
    model=Hemograma
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_hemograma')
    
class UpdateHemograma(UpdateView):
    model=Hemograma
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_hemograma')

class EliminarHemograma(DeleteView):
    model=Hemograma
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_hemograma')


# ----------- CODIGO QUE DEBE ELIMINARSE AL CONFIRMAR QUE NO SE USARÁ -------------
'''
CRUD: CREAR USUARIO Y DIAGNOSTICO
class CrearUsuario(CreateView):
    model=Usuario
    template_name='app_med2/usuario_form.html'
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_usuarios')


class CrearDiagnostico(CreateView):
    model=Diagnostico
    fields='_all_'
    success_url=reverse_lazy('app_med2:listar_diagnosticos')


'''