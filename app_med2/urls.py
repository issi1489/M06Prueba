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
    path('crear_usuario/',views.CrearUsuario.as_view(),  name="crear_usuario"),
    path('listar_usuarios/', views.ListarUsuario.as_view(), name="listar_usuarios"),
    path('<pk>/editar_usuario', views.UpdateUsuario.as_view(), name="editar_usuario"),
    path('<pk>/eliminar_usuario', views.EliminarUsuario.as_view(), name="eliminar_usuario"),

    #path crud diagnostico
    path('crear_diagnostico/',views.CrearDiagnostico.as_view(),  name="crear_diagnostico"),
    path('listar_diagnosticos/', views.ListarDiagnostico.as_view(), name="listar_diagnosticos"),
    path('<pk>/editar_diagnostico', views.UpdateDiagnostico.as_view(), name="editar_diagnostico"),
    path('<pk>/eliminar_diagnostico', views.EliminarDiagnostico.as_view(), name="eliminar_diagnostico"),


    #path crud hemograma
    path('crear_hemograma/',views.CrearHemograma.as_view(),  name="crear_hemograma"),
    path('listar_hemograma/', views.ListarHemograma.as_view(), name="listar_hemograma"),
    path('<pk>/editar_hemograma', views.UpdateHemograma.as_view(), name="editar_hemograma"),
    path('<pk>/eliminar_hemograma', views.EliminarHemograma.as_view(), name="eliminar_hemograma"),


    #path crud coagulacion
    path('crear_coagulacion/',views.CrearCoagulacion.as_view(),  name="crear_coagulacion"),
    path('listar_coagulacion/', views.ListarCoagulacion.as_view(), name="listar_coagulacion"),
    path('<pk>/editar_coagulacion', views.UpdateCoagulacion.as_view(), name="editar_coagulacion"),
    path('<pk>/eliminar_coagulacion', views.EliminarCoagulacion.as_view(), name="eliminar_coagulacion"),

]