from django.db import models

class Orina(models.Model):
    id_orina = models.AutoField(primary_key=True,default=None)
    fk_rutUsuario = models.ForeignKey(Usuario,required=True, on_delete=models.CASCADE)
    fecha_orina = models.DateField()
    nombre_examen = models.CharField(max_length=50, default="Examen de Orina")
    color = models.CharField(max_length=25)
    densidad = models.DecimalField(decimal_places=3)
    glucosa = densidad = models.DecimalField(decimal_places=3)
    cetonas = densidad = models.DecimalField(decimal_places=3)
    urobilinogeno = densidad = models.DecimalField(decimal_places=3)
    billirubina = models.DecimalField(decimal_places=3)
    observaciones_orina = models.CharField(max_length=100)

class PerfilLipidico(models.Model):
    id_plipidico = models.AutoField(primary_key=True,default=None)
    fk_rutUsuario = models.ForeignKey(Usuario,required=True, on_delete=models.CASCADE)
    fecha_orina = models.DateField()
    nombre_examen = models.CharField(max_length=50, default="Examen de Perfil Lipidico")
    colesterol = models.DecimalField(decimal_places=3)
    colesterol_ldl = models.DecimalField(decimal_places=3)
    colesterol_hdl = models.DecimalField(decimal_places=3)
    trigliceridos = models.DecimalField(decimal_places=3)
    observacion_plipidico = models.CharField(max_length=100)





