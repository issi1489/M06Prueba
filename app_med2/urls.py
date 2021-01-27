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

    #crud diagnostico
    path('listar_diagnosticos/', views.ListarDiagnostico.as_view(), name="listar_diagnosticos"),
    path('<pk>/editar_diagnostico', views.UpdateDiagnostico.as_view(), name="editar_diagnosticos"),
    path('<pk>/eliminar_diagnostico', views.EliminarDiagnostico.as_view(), name="eliminar_diagnosticos"),
    #crud usuarios
    path('listar_usuarios/', views.ListarUsuario.as_view(), name="listar_usuarios"),
    path('<pk>/editar_usuario', views.UpdateUsuario.as_view(), name="editar_usuario"),
    path('<pk>/eliminar_usuario', views.EliminarUsuario.as_view(), name="eliminar_usuario"),
    #crud perfil lipidico
    path('listar_perfillipidico/', views.ListarPerfilLipidico.as_view(), name="listar_perfillipidico"),
    path('<pk>/editar_perfillipidico', views.UpdatePerfilLipidico.as_view(), name="editar_perfillipidico"),
    path('<pk>/eliminar_perfillipidico', views.EliminarPerfilLipidico.as_view(), name="eliminar_perfillipidico"),
    #crud glicemia
    path('listar_glicemia/', views.ListarGlicemia.as_view(), name="listar_glicemia"),
    path('<pk>/editar_glicemia', views.UpdateGlicemia.as_view(), name="editar_glicemia"),
    path('<pk>/eliminar_glicemia', views.EliminarGlicemia.as_view(), name="eliminar_glicemia"),
    #crud perfil bioquimico
    path('listar_perfilbioquimico/', views.ListarPerfilBioquimico.as_view(), name="listar_perfilbioquimico"),
    path('<pk>/editar_perfilbioquimico', views.UpdatePerfilBioquimico.as_view(), name="editar_perfilbioquimico"),
    path('<pk>/eliminar_perfilbioquimico', views.EliminarPerfilBioquimico.as_view(), name="eliminar_perfilbioquimico"),
    #crud orina
    path('listar_orina/', views.ListarOrina.as_view(), name="listar_orina"),
    path('<pk>/editar_orina', views.UpdateOrina.as_view(), name="editar_orina"),
    path('<pk>/eliminar_orina', views.EliminarOrina.as_view(), name="eliminar_orina"),
    #crud coagulacion
    path('listar_coagulacion/', views.ListarCoagulacion.as_view(), name="listar_coagulacion"),
    path('<pk>/editar_coagulacion', views.UpdateCoagulacion.as_view(), name="editar_coagulacion"),
    path('<pk>/eliminar_coagulacion', views.EliminarCoagulacion.as_view(), name="eliminar_coagulacion"),
    #crud hemograma
    path('listar_hemograma/', views.ListarHemograma.as_view(), name="listar_hemograma"),
    path('<pk>/editar_hemograma', views.UpdateHemograma.as_view(), name="editar_hemograma"),
    path('<pk>/eliminar_hemograma', views.EliminarHemograma.as_view(), name="eliminar_hemograma"),
    
    # CLAUDIO Vista medico
    path('vista_medico/', views.vista_medico, name="vista_medico"),




]

'''
Paths en desuso por funcion nuevoRegistro
path('crear_usuario/', views.CrearUsuario.as_view(), name="crear_usuario"),
path('crear_diagnostico/',views.CrearDiagnostico.as_view(),  name="crear_diagnostico"),
'''