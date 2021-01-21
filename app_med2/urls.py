from django.urls import path
from . import views

app_name = 'app_med2'
urlpatterns = [
    path('', views.home, name='home'),
    path('admin', views.admin, name='admin'),
    path('paciente/', views.paciente, name= 'paciente'),
    path('provedores', views.provedor, name= 'provedores'),
    path('noticiario', views.noticia, name= 'noticiario')
]