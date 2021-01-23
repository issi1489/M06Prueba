from django.shortcuts import render
from .forms import *
from .models import *





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

