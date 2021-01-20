from django.db import models

# Create your models here.


class Usuario(models.Model):

    rut = models.AutoField(primary_key=True, default=None, max_length=10)
    nombre_paciente = models.CharField(max_length=45)
    edad_paciente = models.IntegerField()
    direccion_paciente = models.CharField(max_length=45)
    staff = models.BooleanField()
    usuario = models.CharField(max_length=10)
    password = models.CharField(max_length=10)


class Hemograma(models.Model):

    id_hemograma = models.AutoField(primary_key=True, default=None, max_length=10)
    paciente_rut = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    fecha_hemograma = models.DateField()
    nombre_hemograma = models.CharField(default='Hemograma')
    eritrocito = models.DecimalField(decimal_places=1)
    leucocitos = models.DecimalField(decimal_places=1)
    hemoglobina = models.DecimalField(decimal_places=1)
    hematocrito = models.DecimalField(decimal_places=1)
    vcm = models.DecimalField(label='VCM', decimal_places=1)
    chcm = models.DecimalField(label='CHCM', decimal_places=1)
    plaquetas = models.DecimalField(decimal_places=1)
    observaciones_hemograma = models.CharField(max_length=100)


