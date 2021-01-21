from django.urls import path
from . import views

app_name = 'app_med2'
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.admin, name='admin'),
    path('paciente/', views.paciente, name= 'paciente'),
    path('admin', views.admin, name='admin'),
    path('base', views.base, name='base'),
    path('registroExamen',views.registroExamen, name='registroExamen'),

]