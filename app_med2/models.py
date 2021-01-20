from django.db import models

# Create your models here.

class coagulacion(models.Model):

    paciente_rut = models.IntegerField()
    id_coagulacion = models.AutoField(primary_key=True,default=None)
    fecha = models.DateField()
    nombre_coagulacion = models.CharField(max_length=50)
    tiempo_protrombina = models.DecimalField(decimal_places=3)
    porc_protrombina = models.DecimalField(decimal_places=3)
    observaciones_coagulacion = models.CharField(max_length=50)
   
   
   
class glicemia(models.Model):

    paciente_rut = models.IntegerField()
    id_glicemia = models.AutoField(primary_key=True,default=None)
    fecha_glicemia = models.DateField()
    nombre_glicemia = models.CharField(max_length=50)
    glicemia_basal = models.DecimalField(decimal_places=3)
    glicemia_120min= models.DecimalField(decimal_places=3)
    observaciones_glicemia = models.CharField(max_length=50)

