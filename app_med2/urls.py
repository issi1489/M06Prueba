from django.urls import path
from . import views

app_name = 'app_med2'
urlpatterns = [
    path('', views.home, name='home'),
    path('admin', views.admin, name='admin'),
    path('usuario', views.usuario, name= 'usuario'),
    path('diagnostico', views.diagnostico, name= 'diagnostico'),
    path('perfil', views.PerBioquimico, name= 'perfil'),
    path('hemograma', views.hemograma, name= 'hemograma'),
    path('coagulacion', views.coagulacion, name= 'coagolacion'),
    path('glicemia', views.glicemia, name= 'glicemia'),
    path('orina', views.orina, name= 'orina'),
    path('perfilLipidico', views.perfilLipidico, name= 'perfilLipidico'),
    path('base', views.base, name='base'),
    path('CrearUsuario', views.CrearUsuario.as_view(), name="CrearUsuario"),
]