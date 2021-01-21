from django.urls import path
from . import views

app_name = 'app_med2'
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.admin, name='admin'),
    path('paciente/', views.paciente, name= 'paciente'),
    path('ver_usuarios', views.VerUsuarios.as_view(), name="ver_usuarios"),

]