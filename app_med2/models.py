from django.db import models

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





