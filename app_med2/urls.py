from django.urls import path
from . import views

app_name = 'app_med2'
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.admin, name='admin'),
    path('paciente/', views.paciente, name= 'paciente'),

    
    path('admin', views.admin, name='admin'),
   
   
    path('perfil', views.Perfilbioquimico.as_view(), name= 'perfil'),


    path('hemograma_form', views.Hemograma.as_view(), name= 'hemograma_form'),

    path('coagulacion/', views.Coagulacion.as_view(), name= 'coagolacion'),

    path('glicemia/', views.Glicemia.as_view(), name= 'glicemia'),

    path('orina/', views.Orina.as_view(), name= 'orina'),

    path('perfilLipidico/', views.PerfilLipidico.as_view(), name= 'perfilLipidico'),


    path('base', views.base, name='base'),
    path('registroExamen',views.registroExamen, name='registroExamen'),
    path('crear_usuario/', views.CrearUsuario.as_view(), name="crear_usuario"),
    path('listar_usuarios/', views.ListarUsuario.as_view(), name="listar_usuarios"),
    path('<pk>/editar_usuario', views.UpdateUsuario.as_view(), name="editar_usuario"),
    path('<pk>/eliminar_usuario', views.EliminarUsuario.as_view(), name="eliminar_usuario")
]