from django.urls import path
from . import views

app_name = 'app_med2'
urlpatterns = [
    path('', views.home, name='home'),
    #path('admin/', views.admin, name='admin'),
    path('paciente/', views.paciente, name= 'paciente'),
    # Vista admin
    path('nuevosRegistros',views.nuevoRegistro, name='registroExamen'),
    path('gestionarRegistros',views.gestionRegistro, name='registroExamen'),

    #path crud diagnostico
    path('listar_diagnosticos/', views.ListarDiagnostico.as_view(), name="listar_diagnosticos"),
    path('<pk>/editar_diagnostico', views.UpdateDiagnostico.as_view(), name="editar_diagnostico"),
    path('<pk>/eliminar_diagnostico', views.EliminarDiagnostico.as_view(), name="eliminar_diagnostico"),
    
    path('listar_usuarios/', views.ListarUsuario.as_view(), name="listar_usuarios"),
    path('<pk>/editar_usuario', views.UpdateUsuario.as_view(), name="editar_usuario"),
    path('<pk>/eliminar_usuario', views.EliminarUsuario.as_view(), name="eliminar_usuario"),
    #crud perfil lipidico
    path('listar_perfillipidico/', views.ListarPerfilLipidico.as_view(), name="listar_usuarios"),
]

'''
Paths en desuso por funcion nuevoRegistro
path('crear_usuario/', views.CrearUsuario.as_view(), name="crear_usuario"),
path('crear_diagnostico/',views.CrearDiagnostico.as_view(),  name="crear_diagnostico"),
'''