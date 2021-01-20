from django.shortcuts import render
import json

#Forms
from .forms import CrearUsuario, rutPacientes

def home(request):

    return render(request,'home.html')

def admin(request):

    #-------------- Lectura de datos del usuario del .json --------------
    # Generar copia de los datos de usuarios
    with open('../proyecto_web/app_med2/data/usuarios.json', 'r') as file:
        usuarios=json.load(file)
    #Seleccionar el usuario requerido y extraer los datos asociados
    usuario=usuarios['9999999-9']
    nombre_us=usuario['nombre']+" "+usuario['apellido']
    edad_us=usuario['edad']
    direccion_us=usuario['direccion']

    #-------------- Lectura de datos de pacientes del .json --------------
    # Generar copia de los datos de pacientes
    with open('../proyecto_web/app_med2/data/usuarios.json', 'r') as file:
        pacientes=json.load(file)

    lpacientes=pacientes

    #-------------- Creación de usuario por formulario --------------
    add_user = CrearUsuario(request.POST or None)
    
    if add_user.is_valid():
        form_data = add_user.cleaned_data
        #form_data['fecha_creacion']=form_data['fecha_creacion'].strftime("%Y-%m-%d")
        
        #usuarios.append(form_data)
        with open('../proyecto_web/app_med2/data/usuarios.json', 'w') as file:
            json.dump(usuarios, file)
        #return redirect('formularios:usuario_creado')
    

    #datos a entregar al html
    context_us={'nombre_us':nombre_us,'edad_us':edad_us, 'direccion_us':direccion_us,'lpacientes':lpacientes,'form_pac': add_user}

    return render(request,'admin.html',context_us)

def paciente(request):

    # ----------- Generar copia de los datos de pacientes y exámenes -----------
    # Pacientes
    with open('../proyecto_web/app_med2/data/usuarios.json', 'r') as file:
        pacientes=json.load(file)
    # Examenes
    with open('../proyecto_web/app_med2/data/examenes.json', 'r') as file:
        examenes=json.load(file)

    # ----------- FUNCIÓN PARA CARGA DE DATOS DEL USUARIO SELECCIONADO -----------
    def info_paciente(rut,pacientes):
        '''
        Función info_paciente: extrae los datos asociados al paciente para visualización en html
        Parámetros:
            * rut: rut del paciente --> asociado a datos del usuario
            * pacientes: json de pacientes
        '''
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
    

    #Gráficos
    #Formulario Exámenes

    # --------------------- Vista del usuario --------------------- 

    form_rut = rutPacientes(request.POST or None)


    #Datos a entregar al html
    context_pac={'nombre_us':nombre_pac,'edad_us':edad_pac, 'direccion_us':direccion_pac,'rut_pacs':rut_pacs,
    'form_rut':form_rut,'img_src':img_src,'diag_rut':diag_rut,'hemo_rut':hemo_rut,'pbio_rut':pbio_rut,
    'plip_rut':plip_rut,'orin_rut':orin_rut,'coag_rut':coag_rut,'glic_rut':glic_rut,'elec_rut':elec_rut}
    return render(request,'paciente.html',context_pac)


def noticia(request):
    
    return render(request, 'noticiarios.html')

def provedor(request):
    
    return render(request, 'provedores.html')

def admin1(request):

    return render(request, 'admin.html')