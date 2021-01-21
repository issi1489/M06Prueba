from django.db import models
from django.db.models.fields import BooleanField, CharField
from django.core import validators
from django.forms.formsets import ORDERING_FIELD_NAME



"""
class Usuario(models.Model):
    #pk
    rutUsuario = models.CharField(max_length=10, primary_key=True, default=None)
    #atributos
    nombre = models.CharField(max_length=45)
    edad = models.IntegerField( )
    direccion = models.CharField( max_length=45)
    staff = models.BooleanField( )
    usuario = models.CharField( max_length=10)
    password = models.CharField(max_length=10)
"""




class Usuario(models.Model):
    #pk
    rutUsuario = models.CharField(max_length =10, primary_key=True, default=None,
                    validators=[validators.MinLengthValidator(9, "Ingresar dni en el siguiente formato 77111666-5"), 
                                validators.MaxLengthValidator(10, "Ingresar dni en el siguiente formato 77111666-5")]
                    )

    #atributos
    nombre = models.CharField(max_length =15,
                    validators=[validators.MinLengthValidator(15, "El nombre debe tener minimo 10 caracteres"), 
                                validators.MaxLengthValidator(45, "El nombre puede tener hasta 30 caracteres")]
                    )

    edad = models.IntegerField(
                    validators=[validators.MinValueValidator(1, "Error, la edad no puede ser menor a 1 "),
                                validators.MaxValueValidator(99, "Error, la edad no puede tener menos más de 3 numero")]
                    )

    direccion = models.CharField(max_length =15,
                    validators=[validators.MinLengthValidator(10, "Error, la dirección debe contener más de 10 caracteres"),
                                validators.MaxLengthValidator(45, "Error, la dirección puede contener hasta 30 caracteres ")]
                    )
    staff = models.BooleanField()
    
    usuario = models.CharField(max_length =30,
                    validators=[validators.MinLengthValidator(3, "Error, la dirección debe contener más de 10 caracteres"),
                    validators.MaxLengthValidator(30, "Error, la dirección puede contener hasta 30 caracteres ")]
                    )
    password = models.CharField(max_length =30,
                    validators=[validators.MinLengthValidator(6, "Error, la dirección debe contener más de 10 caracteres"),
                    validators.MaxLengthValidator(30, "Error, la dirección puede contener hasta 30 caracteres ")]
                    )



class Diagnostico(models.Model):
    #pk
    fecha_diagnostico = models.DateTimeField(primary_key=True, default=None)
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None,)
    #atributos
    diagnostico = models.CharField(max_length=100,  )


class PerfilBioquimico(models.Model):

    #pk
    id_pbioquimico = models.AutoField(primary_key=True,default=None, )
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None,)
    #atributos
    fecha_pbioquimico = models.DateTimeField( )
    nombre_pbioquimico = models.CharField(max_length =15, default='Examen de Perfil Bioquimico')
    glucosa = models.DecimalField(max_digits= 2,decimal_places=1, )
    nitrogeno_ureico = models.DecimalField(max_digits= 2, decimal_places=1, )
    calcio = models.DecimalField(max_digits= 2,decimal_places=1, )
    fosforo = models.DecimalField(max_digits= 2,decimal_places=1, )
    proteinas_totales = models.DecimalField( max_digits= 2,decimal_places=1, )
    albumina = models.DecimalField(max_digits= 2,decimal_places=1, )
    colesterol_total = models.DecimalField( max_digits= 2,decimal_places=1, )
    acido_urico = models.DecimalField( max_digits= 2,decimal_places=1, )
    fosfatas_alcalinas = models.DecimalField(max_digits= 2, decimal_places=1, )
    bilirrubina_total = models.DecimalField( max_digits= 2,decimal_places=1, )
    ldh = models.DecimalField(max_digits= 2,decimal_places=1, )
    got_ast = models.DecimalField(max_digits= 2,decimal_places=1, )
    creatinina = models.DecimalField(max_digits= 2,decimal_places=1, )
    observaciones_pbioquimico = models.CharField( max_length=100,  default="Parametros normales")


class Hemograma(models.Model):

    #pk
    id_hemograma = models.AutoField(primary_key=True,default=None, )
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None,)
    #atributos
    fecha_hemograma = models.DateTimeField( )
    nombre_hemograma = models.CharField( max_length=100, default ='Examen de Hemograma')
    eritrocito = models.DecimalField(max_digits= 2,decimal_places=1, )
    leucocitos = models.DecimalField(max_digits= 2,decimal_places=1, )
    hemoglobina = models.DecimalField(max_digits= 2,decimal_places=1, )
    hematocrito = models.DecimalField(max_digits= 2,decimal_places=1, )
    vcm = models.DecimalField( max_digits= 2,decimal_places=1, )
    chcm = models.DecimalField( max_digits= 2,decimal_places=1, )
    plaquetas = models.DecimalField(max_digits= 2,decimal_places=1, )
    observaciones_hemograma = models.CharField( max_length=100,  default="Parametros normales")


class Coagulacion(models.Model):

    #pk
    id_coagulacion = models.AutoField(primary_key=True,default=None)
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None,)
    #atributos
    fecha_solicitud = models.DateTimeField()
    nombre_examen = models.CharField(max_length =50,default='Examen de Coagulacion')
    tiempo_protrombina = models.DecimalField(max_digits=2, decimal_places=2)
    porc_protrombina = models.DecimalField(max_digits=2, decimal_places=2)
    observaciones_coagulacion = models.CharField(max_length=100)


                

class Glicemia(models.Model):
     
    #pk
    id_glicemia = models.AutoField(primary_key=True,default=None, )
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None,)
    #atributos
    fecha_glicemia = models.DateTimeField()
    nombre_examen = models.CharField(max_length=50, default='Examen de Glicemia')
    glicemia_basal = models.DecimalField(max_digits=2, decimal_places=2 )
    glicemia_120min= models.DecimalField( max_digits=2, decimal_places=1)
    observaciones_glicemia = models.CharField(max_length=100, default="Parametros normales")

                     	  

class Orina(models.Model):

    #pk
    id_orina = models.AutoField(primary_key=True,default=None, )
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None,)
    #atributos
    fecha_orina = models.DateTimeField( )
    nombre_orina = models.CharField(max_length =15, default="Examen de Orina")
    color = models.CharField(max_length=25, )
    densidad = models.DecimalField(max_digits= 2,decimal_places=1, )
    glucosa = models.DecimalField(max_digits= 2,decimal_places=1, )
    cetonas = models.DecimalField(max_digits= 2,decimal_places=1, )
    urobilinogeno = models.DecimalField(max_digits= 2,decimal_places=1, )
    billirubina = models.DecimalField(max_digits= 2,decimal_places=1, )
    observaciones_orina = models.CharField( max_length=100,  default="Parametros normales")


class PerfilLipidico(models.Model):

    #pk
    id_plipidico = models.AutoField(primary_key=True,default=None, )
    #fk
    fk_rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None,)
    #atributos
    fecha_plipidico = models.DateTimeField( )
    nombre_plipidico = models.CharField(max_length =15,default="Examen de Perfil Lipidico")
    colesterol = models.DecimalField(max_digits= 2, decimal_places=1, )
    colesterol_ldl = models.DecimalField(max_digits= 2, decimal_places=1, )
    colesterol_hdl = models.DecimalField(max_digits= 2, decimal_places=1, )
    trigliceridos = models.DecimalField(max_digits= 2,decimal_places=1, )
    observacion_plipidico = models.CharField( max_length=100,  default="Parametros normales")


