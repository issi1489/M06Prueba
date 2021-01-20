
from django.urls import path
from . import views

app_name = "app_med"


urlpatterns = [
    path('crear_examen/', views.CrearExamen.as_view(), name='crear_examen' )
]