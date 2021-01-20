from django.db import models

class Usuario(models.Model):
    #pk
    rutUsuario = models.CharField(max_length=10, primary_key=True, required=True, default=None,label='Rut')
    #atributos
    nombre = models.CharField(required=True, max_length=45)
    edad = models.IntegerField(required=True )
    direccion = models.CharField(required=True, max_length=45)
    staff = models.BooleanField(required=True)
    usuario = models.CharField(required=True, max_length=10)
    password = models.CharField(required=True, max_length=10)


class Diagnostico(models.Model):
    #pk
    fecha_diagnostico = models.DateTimeField(label='Fecha', primary_key=True, required=True, default=None)
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario,required=True, on_delete=models.CASCADE, default=None,label='Rut')
    #atributos
    diagnostico = models.CharField(max_length=100, required=True )


class PerfilBioquimico(models.Model):

    #pk
    id_pbioquimico = models.AutoField(primary_key=True,default=None, label="Id")
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario,required=True, on_delete=models.CASCADE, default=None,label='Rut')
    #atributos
    fecha_pbioquimico = models.DateTimeField(label='Fecha', required=True)
    nombre_pbioquimico = models.CharField(default='Examen de Perfil Bioquimico')
    glucosa = models.DecimalField(decimal_places=1, required=True)
    nitrogeno_ureico = models.DecimalField(label='Nitrogeno ureico', decimal_places=1, required=True)
    calcio = models.DecimalField(decimal_places=1, required=True)
    fosforo = models.DecimalField(decimal_places=1, required=True)
    proteinas_totales = models.DecimalField(label='Proteinas Totales', decimal_places=1, required=True)
    albumina = models.DecimalField(decimal_places=1, required=True)
    colesterol_total = models.DecimalField(label='Colesterol Total', decimal_places=1, required=True)
    acido_urico = models.DecimalField(label='Acido urico', decimal_places=1, required=True)
    fosfatas_alcalinas = models.DecimalField(label='Fosfatas alcalinas', decimal_places=1, required=True)
    bilirrubina_total = models.DecimalField(label='Bilirrubina Total', decimal_places=1, required=True)
    ldh = models.DecimalField(label='LDH',decimal_places=1, required=True)
    got_ast = models.DecimalField(label='GOT/AST',decimal_places=1, required=True)
    creatinina = models.DecimalField(decimal_places=1, required=True)
    observaciones_pbioquimico = models.CharField(label='Observaciones', max_length=100, required=True, default="Parametros normales")


class Hemograma(models.Model):

    #pk
    id_hemograma = models.AutoField(primary_key=True,default=None, label="Id")
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario,required=True, on_delete=models.CASCADE, default=None,label='Rut')
    #atributos
    fecha_hemograma = models.DateTimeField(label='Fecha', required=True)
    nombre_hemograma = models.CharField(default='Examen de Hemograma')
    eritrocito = models.DecimalField(decimal_places=1, required=True)
    leucocitos = models.DecimalField(decimal_places=1, required=True)
    hemoglobina = models.DecimalField(decimal_places=1, required=True)
    hematocrito = models.DecimalField(decimal_places=1, required=True)
    vcm = models.DecimalField(label='VCM', decimal_places=1, required=True)
    chcm = models.DecimalField(label='CHCM', decimal_places=1, required=True)
    plaquetas = models.DecimalField(decimal_places=1, required=True)
    observaciones_hemograma = models.CharField(label='Observaciones', max_length=100, required=True, default="Parametros normales")


class Coagulacion(models.Model):

    #pk
    id_coagulacion = models.AutoField(primary_key=True,default=None, label="Id")
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario,required=True, on_delete=models.CASCADE, default=None,label='Rut')
    #atributos
    fecha_coagulacion = models.DateTimeField(label='Fecha', required=True)
    nombre_coagulacion = models.CharField(default='Examen de Coagulacion')
    tiempo_protrombina = models.DecimalField(label='Tiempo Protrombina', decimal_places=1, required=True)
    porc_protrombina = models.DecimalField(label='Protrombina(%)', decimal_places=1, required=True)
    observaciones_coagulacion = models.CharField(label='Observaciones', max_length=100, required=True, default="Parametros normales")


class Glicemia(models.Model):

    #pk
    id_glicemia = models.AutoField(primary_key=True,default=None, label="Id")
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario,required=True, on_delete=models.CASCADE, default=None,label='Rut')
    #atributos
    fecha_glicemia = models.DateTimeField(label='Fecha', required=True)
    nombre_glicemia = models.CharField(default='Examen de Glicemia')
    glicemia_basal = models.DecimalField(label='Glicemia basal', decimal_places=1, required=True)
    glicemia_120min= models.DecimalField(label='Glicemia 120min', decimal_places=1, required=True)
    observaciones_glicemia = models.CharField(label='Observaciones', max_length=100, required=True, default="Parametros normales")


class Orina(models.Model):

    #pk
    id_orina = models.AutoField(primary_key=True,default=None, label="Id")
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario,required=True, on_delete=models.CASCADE, default=None,label='Rut')
    #atributos
    fecha_orina = models.DateTimeField(label='Fecha', required=True)
    nombre_orina = models.CharField(default="Examen de Orina")
    color = models.CharField(max_length=25, required=True)
    densidad = models.DecimalField(decimal_places=1, required=True)
    glucosa = models.DecimalField(decimal_places=1, required=True)
    cetonas = models.DecimalField(decimal_places=1, required=True)
    urobilinogeno = models.DecimalField(decimal_places=1, required=True)
    billirubina = models.DecimalField(decimal_places=1, required=True)
    observaciones_orina = models.CharField(label='Observaciones', max_length=100, required=True, default="Parametros normales")


class PerfilLipidico(models.Model):

    #pk
    id_plipidico = models.AutoField(primary_key=True,default=None, label="Id")
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario,required=True, on_delete=models.CASCADE, default=None,label='Rut')
    #atributos
    fecha_plipidico = models.DateTimeField(label='Fecha', required=True)
    nombre_plipidico = models.CharField(default="Examen de Perfil Lipidico")
    colesterol = models.DecimalField(decimal_places=1, required=True)
    colesterol_ldl = models.DecimalField(label='LDL', decimal_places=1, required=True)
    colesterol_hdl = models.DecimalField(label='HDL', decimal_places=1, required=True)
    trigliceridos = models.DecimalField(decimal_places=1, required=True)
    observacion_plipidico = models.CharField(label='Observaciones', max_length=100, required=True, default="Parametros normales")





