from django.shortcuts import render
from .models import Usuario, PerfilLipidico, Orina, Coagulacion, Glicemia, Diagnostico, Hemograma, PerfilBioquimico
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import FormularioUsuario, UsuarioForms, DiagnosticoForms, PerfilBioquimicoForms, HemogramaForms
from .forms import CoagulacionForms, GlicemiaForms, OrinaForms, PerfilLipidicoForms, FamiliarForms, UserLoginForms
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Home
def home(request):
    '''
    Home page de el proyecto
    '''
    return render(request, 'app_med2/home.html')

# Vista admin
@login_required(login_url='accounts/login')
def admin(request):
    '''
    (No funcional aún) Debe mostrar el perfil del usuario admin que ingresó
    '''
    return render(request, 'app_med2/admin.html')

# Vista admin: Crear nuevos registros
@login_required(login_url='accounts/login')
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
            'loginUs_form':UserLoginForms(),
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
        loginUs_form = UserLoginForms(request.POST)
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

        elif loginUs_form.is_valid():
            loginUs_form.save()
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
                'loginUs_form': loginUs_form,
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
            'loginUs_form':UserLoginForms(),
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
@login_required(login_url='accounts/login')
def gestionRegistro(request):
    '''
    Función para visualizar un template intermedio que permite ingresar
    a las distintas tablas con datos de usuario, diagnostico y exámenes.
    '''
    return render(request,'../templates/app_med2/registros_gestion.html')


# Vista paciente
@login_required(login_url='accounts/login')
def paciente(request):

    datos_us = Usuario.objects.filter(rutUsuario='17684562-7')
    diagnostico_us = Diagnostico.objects.filter(rutUsuario='17684562-7')
    pBioquimico_us = PerfilBioquimico.objects.filter(rutUsuario='17684562-7')
    hemograma_us = Hemograma.objects.filter(rutUsuario='17684562-7')
    coagulacion_us = Coagulacion.objects.filter(rutUsuario='17684562-7')
    glicemia_us = Glicemia.objects.filter(rutUsuario='17684562-7')
    orina_us = Orina.objects.filter(rutUsuario='17684562-7')
    pLipidico_us = PerfilLipidico.objects.filter(rutUsuario='17684562-7')

    context = {'familiar_form': FamiliarForms(),'datos':datos_us,'diagnostico':diagnostico_us,
                'pBioquimico':pBioquimico_us, 'hemograma':hemograma_us,
                'coagulacion':coagulacion_us, 'glicemia':glicemia_us,
                'orina':orina_us, 'pLipidico':pLipidico_us}
                
    if request.method == 'POST':
        familiar_form = FamiliarForms(request.POST)
        if familiar_form.is_valid():
            familiar_form.save()
            return render(request,'../templates/app_med2/paciente.html',context) 
        else:
            context = {'familiar_form': familiar_form,'datos':datos_us,'diagnostico':diagnostico_us,
                'pBioquimico':pBioquimico_us, 'hemograma':hemograma_us,
                'coagulacion':coagulacion_us, 'glicemia':glicemia_us,
                'orina':orina_us, 'pLipidico':pLipidico_us}
    else:
        context = {'familiar_form': FamiliarForms(),'datos':datos_us,'diagnostico':diagnostico_us,
                'pBioquimico':pBioquimico_us, 'hemograma':hemograma_us,
                'coagulacion':coagulacion_us, 'glicemia':glicemia_us,
                'orina':orina_us, 'pLipidico':pLipidico_us}

    
    '''
    context = {'familiar_form': FamiliarForms(),'datos':datos_us,'diagnostico':diagnostico_us,
                'pBioquimico':pBioquimico_us, 'hemograma':hemograma_us,
                'coagulacion':coagulacion_us, 'glicemia':glicemia_us,
                'orina':orina_us, 'pLipidico':pLipidico_us}'''

    return render(request,'../templates/app_med2/paciente.html',context)
@login_required(login_url='accounts/login')
def familiar(request):

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
    return render(request,'../templates/app_med2/familiar.html',context)
    
#----------------------------------- CRUDS ---------------------------------

# CRUD USUARIO
class ListarUsuario(LoginRequiredMixin, ListView):
    model=Usuario
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_usuarios')

class UpdateUsuario(LoginRequiredMixin, UpdateView):
    model=Usuario
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_usuarios')

class EliminarUsuario(LoginRequiredMixin, DeleteView):
    model= Usuario
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_usuarios')

# CRUD DIAGNOSTICO
class ListarDiagnostico(LoginRequiredMixin, ListView):
    model=Diagnostico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_diagnosticos')
    
class UpdateDiagnostico(LoginRequiredMixin, UpdateView):
    model=Diagnostico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_diagnosticos')

class EliminarDiagnostico(LoginRequiredMixin, DeleteView):
    model=Diagnostico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_diagnosticos')

# CRUD PERFIL LIPIDICO
class ListarPerfilLipidico(LoginRequiredMixin, ListView):
    model=PerfilLipidico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfillipidico')
    
class UpdatePerfilLipidico(LoginRequiredMixin, UpdateView):
    model=PerfilLipidico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfillipidico')

class EliminarPerfilLipidico(LoginRequiredMixin, DeleteView):
    model=PerfilLipidico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfillipidico')

#CRUD GLICEMIA
class ListarGlicemia(LoginRequiredMixin, ListView):
    model=Glicemia
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_glicemia')
    
class UpdateGlicemia(LoginRequiredMixin, UpdateView):
    model=Glicemia
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_glicemia')

class EliminarGlicemia(LoginRequiredMixin, DeleteView):
    model=Glicemia
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_glicemia')

#CRUD PerfilBioquimico
class ListarPerfilBioquimico(LoginRequiredMixin, ListView):
    model=PerfilBioquimico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfilbioquimico')
    
class UpdatePerfilBioquimico(LoginRequiredMixin, UpdateView):
    model=PerfilBioquimico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfilbioquimico')

class EliminarPerfilBioquimico(LoginRequiredMixin, DeleteView):
    model=PerfilBioquimico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfilbioquimico')

#CRUD Orina
class ListarOrina(LoginRequiredMixin, ListView):
    model=Orina
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_orina')
    
class UpdateOrina(LoginRequiredMixin, UpdateView):
    model=Orina
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_orina')

class EliminarOrina(LoginRequiredMixin, DeleteView):
    model=Orina
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_orina')

#CRUD Coagulacion
class ListarCoagulacion(LoginRequiredMixin, ListView):
    model=Coagulacion
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_coagulacion')
    
class UpdateCoagulacion(LoginRequiredMixin, UpdateView):
    model=Coagulacion
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_coagulacion')

class EliminarCoagulacion(LoginRequiredMixin, DeleteView):
    model=Coagulacion
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_coagulacion')

#CRUD Hemograma
class ListarHemograma(LoginRequiredMixin, ListView):
    model=Hemograma
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_hemograma')
    
class UpdateHemograma(LoginRequiredMixin, UpdateView):
    model=Hemograma
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_hemograma')

class EliminarHemograma(LoginRequiredMixin, DeleteView):
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