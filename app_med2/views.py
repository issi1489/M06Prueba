from django.shortcuts import render
<<<<<<< HEAD
from .forms import *
from .models import *


=======
from .models import Usuario, PerfilLipidico, Orina, Coagulacion, Glicemia, Diagnostico, Hemograma, PerfilBioquimico
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import FormularioUsuario, UsuarioForms, DiagnosticoForms, PerfilBioquimicoForms, HemogramaForms
from .forms import CoagulacionForms, GlicemiaForms, OrinaForms, PerfilLipidicoForms
from django.template.response import TemplateResponse

# Home 
def home(request):
    '''
    Home page de el proyecto
    '''
    return render(request, 'app_med2/home.html')

# Vista admin
def admin(request):
    '''
    (No funcional aún) Debe mostrar el perfil del usuario admin que ingresó
    '''
    return render(request, 'app_med2/admin.html')

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
>>>>>>> cdcf2c8ecf05ed93136ff1c30dcd9edb66917202


<<<<<<< HEAD

def admin(request):

    return render(request, 'app_med2/admin.html')


def home(request):

    return render(request, 'app_med2/home.html')


'''def usuario(request):
    data = {
        'usuario': UsuarioForms()
    }
=======
class EliminarUsuario(DeleteView):
    model= Usuario
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_usuarios')

# CRUD DIAGNOSTICO
class ListarDiagnostico(ListView):
    model=Diagnostico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_diagnosticos')
>>>>>>> cdcf2c8ecf05ed93136ff1c30dcd9edb66917202
    
class UpdateDiagnostico(UpdateView):
    model=Diagnostico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_diagnosticos')

<<<<<<< HEAD
    if request.method == 'POST':
        formulario = UsuarioForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["usuario"] = formulario
			

    return render(request, 'app_med2/agregar/formulario1.html', data)'''


'''def diagnostico(request):
    data = {
        'diagnostico': DiagnosticoForms()
    }
=======
class EliminarDiagnostico(DeleteView):
    model=Diagnostico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_diagnosticos')

# CRUD PERFIL LIPIDICO
class ListarPerfilLipidico(ListView):
    model=PerfilLipidico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfillipidico')
>>>>>>> cdcf2c8ecf05ed93136ff1c30dcd9edb66917202
    
class UpdatePerfilLipidico(UpdateView):
    model=PerfilLipidico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfillipidico')

<<<<<<< HEAD
    if request.method == 'POST':
        formulario = DiagnosticoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["diagnostico"] = formulario
			

    return render(request, 'app_med2/agregar/formulario2.html', data)'''



'''def PerBioquimico(request):
    data = {
        'perfil':PerfilBioquimicoForms()
    }
=======
class EliminarPerfilLipidico(DeleteView):
    model=PerfilLipidico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfillipidico')

#CRUD GLICEMIA
class ListarGlicemia(ListView):
    model=Glicemia
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_glicemia')
>>>>>>> cdcf2c8ecf05ed93136ff1c30dcd9edb66917202
    
class UpdateGlicemia(UpdateView):
    model=Glicemia
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_glicemia')

<<<<<<< HEAD
    if request.method == 'POST':
        formulario = PerfilBioquimicoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["perfil"] = formulario
			

    return render(request, 'app_med2/agregar/formulario3.html', data)'''


'''def hemograma(request):
    data = {
        'hemograma': HemogramaForms()
    }
=======
class EliminarGlicemia(DeleteView):
    model=Glicemia
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_glicemia')

#CRUD PerfilBioquimico
class ListarPerfilBioquimico(ListView):
    model=PerfilBioquimico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfilbioquimico')
>>>>>>> cdcf2c8ecf05ed93136ff1c30dcd9edb66917202
    
class UpdatePerfilBioquimico(UpdateView):
    model=PerfilBioquimico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfilbioquimico')

<<<<<<< HEAD
    if request.method == 'POST':
        formulario = HemogramaForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["hemograma"] = "contacto guardado"
        else:
            data["hemogram"] = formulario
			

    return render(request, 'app_med2/agregar/formulario4.html', data)'''



'''def coagulacion(request):
    data = {
        'coagulacion': CoagulacionForms()
    }
=======
class EliminarPerfilBioquimico(DeleteView):
    model=PerfilBioquimico
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_perfilbioquimico')

#CRUD Orina
class ListarOrina(ListView):
    model=Orina
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_orina')
>>>>>>> cdcf2c8ecf05ed93136ff1c30dcd9edb66917202
    
class UpdateOrina(UpdateView):
    model=Orina
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_orina')

<<<<<<< HEAD
    if request.method == 'POST':
        formulario = CoagulacionForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["coagulacion"] = formulario
			

    return render(request, 'app_med2/agregar/formulario5.html', data)'''



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


'''def orina(request):
    data = {
        'orina': OrinaForms()
    }
=======
class EliminarOrina(DeleteView):
    model=Orina
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_orina')

#CRUD Coagulacion
class ListarCoagulacion(ListView):
    model=Coagulacion
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_coagulacion')
>>>>>>> cdcf2c8ecf05ed93136ff1c30dcd9edb66917202
    
class UpdateCoagulacion(UpdateView):
    model=Coagulacion
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_coagulacion')

<<<<<<< HEAD
    if request.method == 'POST':
        formulario = OrinaForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["orina"] = formulario
			

    return render(request, 'app_med2/agregar/formulario7.html', data)'''



'''def perfilLipidico(request):
    data = {
        'plipidico':PerfilLipidicoForms()
    }
=======
class EliminarCoagulacion(DeleteView):
    model=Coagulacion
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_coagulacion')

#CRUD Hemograma
class ListarHemograma(ListView):
    model=Hemograma
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_hemograma')
>>>>>>> cdcf2c8ecf05ed93136ff1c30dcd9edb66917202
    
class UpdateHemograma(UpdateView):
    model=Hemograma
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_hemograma')

<<<<<<< HEAD
    if request.method == 'POST':
        formulario = PerfilLipidicoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["plipidico"] = formulario
			

    return render(request, 'app_med2/agregar/formulario8.html', data)'''

=======
class EliminarHemograma(DeleteView):
    model=Hemograma
    fields='__all__'
    success_url=reverse_lazy('app_med2:listar_hemograma')
>>>>>>> cdcf2c8ecf05ed93136ff1c30dcd9edb66917202


<<<<<<< HEAD
def informacion(request):
    data ={
            
            'diagnostico': DiagnosticoForms(), 'usuario':UsuarioForms()
    }
    if request.method == 'POST':
        formulario =  UsuarioForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "info guardada"
        else:
            data["usuario"] = formulario
    
    if request.method == 'POST':
        formulario =  DiagnosticoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "info guardada"
        else:
            data["diagnostico"] = formulario

    return render(request, 'app_med2/agregar/reg_examen.html', data)
# NO TOCAR DE AQUI EN ADELANTE!
'''
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
        
                
    return render(request, 'app_med2/agregar/reg_examen.html', data)'''


def producto(request):
    nombres = Usuario.objects.all()  
    diagnostico = Diagnostico.objects.all()

    data ={
        "nombres" : nombres,
        "diagnostico": diagnostico
    }
    return render(request, 'app_med2/agregar/hemograma_form.html', data)

=======
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
>>>>>>> cdcf2c8ecf05ed93136ff1c30dcd9edb66917202
