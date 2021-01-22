from app_med2.models import PerfilLipidico

def obtener_examenes_usuario(request):
    perfil_usuario = PerfilLipidico.objects.all().values()
    print(perfil_usuario)

obtener_examenes_usuario()