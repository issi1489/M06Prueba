from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class VerUsuarios(ListView):
    model = Usuario
    template_name = "app_med2/ver_usuarios.html"
    context_object_name = "usuarios"


def base(request):

    return render(request, 'app_med2/agregar/base.html')


def admin(request):

    return render(request, 'app_med2/admin.html')


def home(request):

    return render(request, 'app_med2/home.html')


def paciente(request):
    return render(request,'../templates/app_med2/paciente.html')