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
    
    #path crud usuario
    path('crear_usuario/', views.CrearUsuario.as_view(), name="crear_usuario"),
    path('listar_usuarios/', views.ListarUsuario.as_view(), name="listar_usuarios"),
    path('<pk>/editar_usuario', views.UpdateUsuario.as_view(), name="editar_usuario"),
    path('<pk>/eliminar_usuario', views.EliminarUsuario.as_view(), name="eliminar_usuario")
]