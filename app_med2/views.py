from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#import json
#Forms
#from .forms import CrearUsuario , rutPacientes
=======
from .models import Usuario, PerfilLipidico, Orina, Coagulacion, Glicemia, Diagnostico, Hemograma, PerfilBioquimico
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

>>>>>>> 117f807af2810a14463d52f2f6385cfc93a1d497


<<<<<<< HEAD
    return render(request,'../templates/app_med2/home.html')
=======
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
>>>>>>> 117f807af2810a14463d52f2f6385cfc93a1d497

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
    

<<<<<<< HEAD
    #datos a entregar al html
    context_us={'nombre_us':nombre_us,'edad_us':edad_us, 'direccion_us':direccion_us,'lpacientes':lpacientes,'form_pac': add_user}

    return render(request,'../templates/app_med2/admin.html',context_us)


from django.shortcuts import render
from .models import Usuario, Diagnostico, PerfilBioquimico, Hemograma, Coagulacion, Glicemia, Orina,PerfilLipidico
 
def paciente(request):
    diagnostico = Diagnostico.objects
    
    context={ 'diagnostico':diagnostico } 
    return render(request, '../templates/app_med2/paciente.html',context )


#def paciente(request):

#    return render(request,'../templates/app_med2/paciente.html')
    '''
    # ----------- Generar copia de los datos de pacientes y exámenes -----------
    # Pacientes
    with open('../proyecto_web/app_med2/data/usuarios.json', 'r') as file:
        pacientes=json.load(file)
    # Examenes
    with open('../proyecto_web/app_med2/data/examenes.json', 'r') as file:
        examenes=json.load(file)

    # ----------- FUNCIÓN PARA CARGA DE DATOS DEL USUARIO SELECCIONADO -----------
    def info_paciente(rut,pacientes):
        
        Función info_paciente: extrae los datos asociados al paciente para visualización en html
        Parámetros:
            * rut: rut del paciente --> asociado a datos del usuario
            * pacientes: json de pacientes
        
        # Extracción de los datos del paciente
        data_pac=pacientes[rut]
        
        #Datos paciente
        rut=data_pac['rut']
        nombre=data_pac['nombre']+" "+data_pac['apellido']
        edad=data_pac['edad']
        direccion=data_pac['direccion'] 
        img_src=data_pac['foto_src']
 
        return nombre, edad, direccion,img_src


    #Extraer ruts para lista desplegable de cambio de usuario
    rut_pacs=[]
    for p in pacientes:
        rut_pacs.append(p)
        break

    #Extraer primer rut
    f_pac=rut_pacs[0]
    nombre_pac,edad_pac,direccion_pac,img_src =info_paciente(f_pac,pacientes)

    # --------------------- Datos de vista por defecto --------------------- 

    #Examenes por el rut 
    diag_rut= examenes[f_pac]['diagnosticos']
    hemo_rut=examenes[f_pac]['hemograma']
    pbio_rut=examenes[f_pac]['perfil_bioquimico']
    plip_rut=examenes[f_pac]['perfil_lipidico']
    orin_rut=examenes[f_pac]['orina']
    coag_rut=examenes[f_pac]['coagulacion']
    glic_rut=examenes[f_pac]['glicemia']
    elec_rut=examenes[f_pac]['electrocardiograma']
=======
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
>>>>>>> 117f807af2810a14463d52f2f6385cfc93a1d497
    

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
    

<<<<<<< HEAD
    #Datos a entregar al html
    context_pac={'nombre_us':nombre_pac,'edad_us':edad_pac, 'direccion_us':direccion_pac,'rut_pacs':rut_pacs,
    'form_rut':form_rut,'img_src':img_src,'diag_rut':diag_rut,'hemo_rut':hemo_rut,'pbio_rut':pbio_rut,
    'plip_rut':plip_rut,'orin_rut':orin_rut,'coag_rut':coag_rut,'glic_rut':glic_rut,'elec_rut':elec_rut}'''
    
    
    #,context_pac
=======
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


>>>>>>> 117f807af2810a14463d52f2f6385cfc93a1d497
