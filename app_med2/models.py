from django.db import models


# Vale

class PerfilBioquimico(models.Model):
    id_pbioquimico = models.AutoField(primary_key=True,default=None)
    fk_rutUsuario = models.ForeignKey(Usuario,required=True, on_delete=models.CASCADE)
    fecha_pbioquimico = models.DateTimeField(required=True)
    nombre_pbioquimico = models.CharField(default="Perfil Bioquimico")
    glucosa = models.DecimalField(decimal_places=3,required=True)
    nitrogeno_ureico =models.DecimalField(decimal_places=3,required=True)
    calcio = models.DecimalField(decimal_places=3,required=True)
    fosforo = models.DecimalField(decimal_places=3,required=True)
    proteinas_totales = models.DecimalField(decimal_places=3,required=True)
    albumina =models.DecimalField(decimal_places=3,required=True)
    colesterol_total = models.DecimalField(decimal_places=3,required=True)
    acido_urico = models.DecimalField(decimal_places=3,required=True)
    fosfatas_alcalinas = models.DecimalField(decimal_places=3,required=True)
    bilirrubina_total = models.DecimalField(decimal_places=3,required=True)
    ldh = models.DecimalField(decimal_places=3,required=True)
    got_ast = models.DecimalField(decimal_places=3,required=True)
    creatinina = models.DecimalField(decimal_places=3,required=True)
    observaciones_pbioquimico = models.CharField(max_length=100, required=True, default="Parametros normales")

class Diagnostico(models.Model):
    fecha_diagnostico = models.DateTimeField(required=True)
    fk_rutUsuario = models.ForeignKey(Usuario, required=True, on_delete=models.CASCADE)
    diagnostico = models.CharField(max_length=100, required=True )