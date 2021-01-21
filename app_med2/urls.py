from django.urls import path
from . import views

app_name = 'app_med2'
urlpatterns = [
    path('', views.home, name='home'),
    path('admin', views.admin, name='admin'),
    path('paciente/', views.paciente, name= 'paciente'),
    path('provedores', views.provedor, name= 'provedores'),
    path('noticiario', views.noticia, name= 'noticiario'),

    path('lista_usuario', views.ListaUsuario.as_view(), name= 'lista_usuario'),
    path('crear_usuario/', views.CrearUsuario.as_view(), name= 'crear_usuario'),
    path('<pk>/editar_usuario', views.EditarUsuario.as_view(), name= 'editar_usuario'),
    path('<pk>/eliminar_usuario', views.EliminarUsuario.as_view(), name= 'eliminar_usuario'),

]