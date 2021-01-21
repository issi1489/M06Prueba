from django.db import models
#acceder a rutUsuario con rutUsuario_id
from django.db.models.fields import BooleanField, CharField
from django.core import validators


<<<<<<< HEAD


'''
=======
"""
>>>>>>> ffdfb6d1889422f4adbbe25c9858f2ab1e059a94
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
<<<<<<< HEAD
'''


=======
"""
>>>>>>> ffdfb6d1889422f4adbbe25c9858f2ab1e059a94

class Usuario(models.Model):
    #pk
    rutUsuario = models.CharField(max_length =10, primary_key=True, default=None,
                    validators=[validators.MinLengthValidator(9, "Ingresar dni en el siguiente formato 77111666-5"), 
                                validators.MaxLengthValidator(10, "Ingresar dni en el siguiente formato 77111666-5")]
                    )

    #atributos
    nombre = models.CharField(max_length =45,
                    validators=[validators.MinLengthValidator(10, "El nombre debe tener minimo 10 caracteres"), 
                                validators.MaxLengthValidator(45, "El nombre puede tener hasta 45 caracteres")]
                    )

    edad = models.IntegerField(
                    validators=[validators.MinValueValidator(1, "Error, la edad no puede ser menor a 1 "),
                                validators.MaxValueValidator(99, "Error, la edad no puede tener menos más de 3 números")]
                    )

    direccion = models.CharField(max_length =45,
                    validators=[validators.MinLengthValidator(10, "Error, la dirección debe contener más de 10 caracteres"),
                                validators.MaxLengthValidator(45, "Error, la dirección puede contener hasta 45 caracteres ")]
                    )
    staff = models.BooleanField()
    
    usuario = models.CharField(max_length =15,
                    validators=[validators.MinLengthValidator(5, "Error, el usuario debe tener mínimo 5 caracteres"),
                    validators.MaxLengthValidator(15, "Error, el usuario debe contener hasta 15 caracteres ")]
                    )
    password = models.CharField(max_length =15,
                    validators=[validators.MinLengthValidator(6, "Error, la contraseña debe contener más de 6 caracteres"),
                    validators.MaxLengthValidator(15, "Error, la dirección puede contener hasta 15 caracteres ")]
                    )


class Diagnostico(models.Model):
    #pk
<<<<<<< HEAD
    fecha_diagnostico = models.DateTimeField(primary_key=True, default=None,)
    #fk no se hacer
    fk_rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None,)
    #atributos
    diagnostico = models.CharField(max_length=40,
                        validators=[validators.MinLengthValidator(5, "Error, el diagnostico debe contar con mas de 10 caracteres"),
                        validators.MaxLengthValidator(40, "Error, el diagnostico debe contar con menos de 10 caracteres")]
                        )
=======
    fecha_diagnostico = models.DateField(primary_key=True, default=None)
    #fk
    rutUsuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, default=None)
    #atributos
    diagnostico = models.CharField(max_length=100)
    fecha_diagnostico = models.DateTimeField(primary_key=True, default=None)
>>>>>>> ffdfb6d1889422f4adbbe25c9858f2ab1e059a94


class PerfilBioquimico(models.Model):

    #pk
    id_pbioquimico = models.AutoField(primary_key=True,default=None)
    #fk
    rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    #atributos
<<<<<<< HEAD
    fecha_pbioquimico = models.DateTimeField( )
    nombre_pbioquimico = models.CharField(max_length=100,
                        validators=[validators.MinLengthValidator(3, "Error, el nombre pbioquimico debe contar con mas de 10 caracteres"),
                        validators.MaxLengthValidator(10, "Error, el nombre pbioquimico debe contar con menos de 10 caracteres")]
                        ) 
    glucosa = models.DecimalField(max_digits= 2,decimal_places=1)
    nitrogeno_ureico = models.DecimalField(max_digits= 2, decimal_places=1 )
    calcio = models.DecimalField(max_digits= 2,decimal_places=1)
    fosforo = models.DecimalField(max_digits= 2,decimal_places=1)
    proteinas_totales = models.DecimalField( max_digits= 2,decimal_places=1)
    albumina = models.DecimalField(max_digits= 2,decimal_places=1, )
    colesterol_total = models.DecimalField( max_digits= 2,decimal_places=1, )
    acido_urico = models.DecimalField( max_digits= 2,decimal_places=1, )
    fosfatas_alcalinas = models.DecimalField(max_digits= 2, decimal_places=1, )
    bilirrubina_total = models.DecimalField( max_digits= 2,decimal_places=1, )
    ldh = models.DecimalField(max_digits= 2,decimal_places=1, )
    got_ast = models.DecimalField(max_digits= 2,decimal_places=1, )
    creatinina = models.DecimalField(max_digits= 2,decimal_places=1, )
    observaciones_pbioquimico = models.CharField(max_length=150,
                        validators=[validators.MinLengthValidator(10, "Error, la observacion debe contar con mas de 10 caracteres"),
                        validators.MaxLengthValidator(150, "Error, la observacion debe contar con menos de 150 caracteres")]
                        ) 
=======
    fecha_pbioquimico = models.DateField()
    nombre_pbioquimico = models.CharField(max_length=30,default='Examen de Perfil Bioquimico')
    glucosa = models.DecimalField(max_digits=4, decimal_places=1 )
    nitrogeno_ureico = models.DecimalField(max_digits=4, decimal_places=1)
    calcio = models.DecimalField(max_digits=4, decimal_places=1)
    fosforo = models.DecimalField(max_digits=4, decimal_places=1)
    proteinas_totales = models.DecimalField(max_digits=4, decimal_places=1)
    albumina = models.DecimalField(max_digits=4, decimal_places=1)
    colesterol_total = models.DecimalField(max_digits=4, decimal_places=1)
    acido_urico = models.DecimalField(max_digits=4, decimal_places=1)
    fosfatas_alcalinas = models.DecimalField(max_digits=4, decimal_places=1)
    bilirrubina_total = models.DecimalField(max_digits=4, decimal_places=1)
    ldh = models.DecimalField(max_digits=4, decimal_places=1)
    got_ast = models.DecimalField(max_digits=4, decimal_places=1)
    creatinina = models.DecimalField(max_digits=4, decimal_places=1)
    observaciones_pbioquimico = models.CharField(max_length=100, default="Parametros normales")
>>>>>>> ffdfb6d1889422f4adbbe25c9858f2ab1e059a94


class Hemograma(models.Model):

    #pk
    id_hemograma = models.AutoField(primary_key=True,default=None)
    #fk
    rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    #atributos
<<<<<<< HEAD
    fecha_hemograma = models.DateTimeField( )
    nombre_hemograma = models.CharField(max_length=100,
                        validators=[validators.MinLengthValidator(5, "Error, el nombre hemograma debe contar con mas de 5 caracteres"),
                        validators.MaxLengthValidator(15, "Error, el nombre hemogram debe contar con menos de 15 caracteres")]
                        ) 
    eritrocito = models.DecimalField(max_digits= 2,decimal_places=1, )
    leucocitos = models.DecimalField(max_digits= 2,decimal_places=1, )
    hemoglobina = models.DecimalField(max_digits= 2,decimal_places=1, )
    hematocrito = models.DecimalField(max_digits= 2,decimal_places=1, )
    vcm = models.DecimalField( max_digits= 2,decimal_places=1, )
    chcm = models.DecimalField( max_digits= 2,decimal_places=1, )
    plaquetas = models.DecimalField(max_digits= 2,decimal_places=1, )
    observaciones_hemograma = models.CharField(max_length=150,
                        validators=[validators.MinLengthValidator(10, "Error, la observacion debe contar con mas de 10 caracteres"),
                        validators.MaxLengthValidator(150, "Error, la observacion debe contar con menos de 150 caracteres")]
                        ) 

=======
    fecha_hemograma = models.DateField()
    nombre_hemograma = models.CharField(max_length=30,default='Examen de Hemograma')
    eritrocito = models.DecimalField(max_digits=4, decimal_places=1)
    leucocitos = models.DecimalField(max_digits=4, decimal_places=1)
    hemoglobina = models.DecimalField(max_digits=4, decimal_places=1)
    hematocrito = models.DecimalField(max_digits=4, decimal_places=1)
    vcm = models.DecimalField(max_digits=4, decimal_places=1)
    chcm = models.DecimalField(max_digits=4, decimal_places=1)
    plaquetas = models.DecimalField(max_digits=4, decimal_places=1)
    observaciones_hemograma = models.CharField(max_length=100, default="Parametros normales")
    
>>>>>>> ffdfb6d1889422f4adbbe25c9858f2ab1e059a94

class Coagulacion(models.Model):

    #pk
    id_coagulacion = models.AutoField(primary_key=True,default=None)
    #fk
    rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    #atributos
<<<<<<< HEAD
    fecha_solicitud = models.DateTimeField()
    nombre_examen = models.CharField(max_length=15,
                        validators=[validators.MinLengthValidator(5, "Error, el nombre del examen debe contar con mas de 5 caracteres"),
                        validators.MaxLengthValidator(15, "Error, el nombre del examen debe contar con menos de 15 caracteres")]
                        ) 
    tiempo_protrombina = models.DecimalField(max_digits=2, decimal_places=2)
    porc_protrombina = models.DecimalField(max_digits=2, decimal_places=2)
    observaciones_coagulacion = models.CharField(max_length=150,
                        validators=[validators.MinLengthValidator(10, "Error, la observacion debe contar con mas de 10 caracteres"),
                        validators.MaxLengthValidator(150, "Error, la observacion debe contar con menos de 150 caracteres")]
                        ) 


=======
    fecha_coagulacion = models.DateField()
    nombre_coagulacion = models.CharField(max_length=30,default='Examen de Coagulacion')
    tiempo_protrombina = models.DecimalField(max_digits=4, decimal_places=1)
    porc_protrombina = models.DecimalField(max_digits=4, decimal_places=1)
    observaciones_coagulacion = models.CharField(max_length=100, default="Parametros normales")
>>>>>>> ffdfb6d1889422f4adbbe25c9858f2ab1e059a94
                

class Glicemia(models.Model):
     
    #pk
    id_glicemia = models.AutoField(primary_key=True,default=None)
    #fk
    rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    #atributos
<<<<<<< HEAD
    fecha_glicemia = models.DateTimeField()
    nombre_examen = models.CharField(max_length=15,
                        validators=[validators.MinLengthValidator(10, "Error, la observacion debe contar con mas de 10 caracteres"),
                        validators.MaxLengthValidator(15, "Error, la observacion debe contar con menos de 15 caracteres")]
                        ) 
    glicemia_basal = models.DecimalField(max_digits=2, decimal_places=2 )
    glicemia_120min= models.DecimalField( max_digits=2, decimal_places=1)
    observaciones_glicemia = models.CharField(max_length=100,
                        validators=[validators.MinLengthValidator(10, "Error, la observacion debe contar con mas de 10 caracteres"),
                        validators.MaxLengthValidator(150, "Error, la observacion debe contar con menos de 150 caracteres")]
                        ) 

                     	  
=======
    fecha_glicemia = models.DateField()
    nombre_glicemia = models.CharField(max_length=30,default='Examen de Glicemia')
    glicemia_basal = models.DecimalField(max_digits=4, decimal_places=1)
    glicemia_120min= models.DecimalField(max_digits=4, decimal_places=1)
                       	  
>>>>>>> ffdfb6d1889422f4adbbe25c9858f2ab1e059a94

class Orina(models.Model):

    #pk
    id_orina = models.AutoField(primary_key=True,default=None)
    #fk
    rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    #atributos
<<<<<<< HEAD
    fecha_orina = models.DateTimeField( )
    nombre_orina = models.CharField(max_length=15,
                        validators=[validators.MinLengthValidator(10, "Error, el nombre de la orina debe contar con mas de 10 caracteres"),
                        validators.MaxLengthValidator(15, "Error, el nombre de la orina debe contar con menos de 15 caracteres")]
                        ) 
    color = models.CharField(max_length=15,
                        validators=[validators.MinLengthValidator(5, "Error, el color debe contar con mas de 10 caracteres"),
                        validators.MaxLengthValidator(15, "Error, el color debe contar con menos de 15 caracteres")]
                        ) 
    densidad = models.DecimalField(max_digits= 2,decimal_places=1, )
    glucosa = models.DecimalField(max_digits= 2,decimal_places=1, )
    cetonas = models.DecimalField(max_digits= 2,decimal_places=1, )
    urobilinogeno = models.DecimalField(max_digits= 2,decimal_places=1, )
    billirubina = models.DecimalField(max_digits= 2,decimal_places=1, )
    observaciones_orina = models.CharField(max_length=100,
                        validators=[validators.MinLengthValidator(10, "Error, la observacion debe contar con mas de 10 caracteres"),
                        validators.MaxLengthValidator(150, "Error, la observacion debe contar con menos de 150 caracteres")]
                        ) 

=======
    fecha_orina = models.DateField()
    nombre_orina = models.CharField(max_length=30,default="Examen de Orina")
    color = models.CharField(max_length=25)
    densidad = models.DecimalField(max_digits=4, decimal_places=1)
    glucosa = models.DecimalField(max_digits=4, decimal_places=1)
    cetonas = models.DecimalField(max_digits=4, decimal_places=1)
    urobilinogeno = models.DecimalField(max_digits=4, decimal_places=1)
    billirubina = models.DecimalField(max_digits=4, decimal_places=1)
    observaciones_orina = models.CharField(max_length=100, default="Parametros normales")
    
>>>>>>> ffdfb6d1889422f4adbbe25c9858f2ab1e059a94

class PerfilLipidico(models.Model):

    #pk
    id_plipidico = models.AutoField(primary_key=True,default=None)
    #fk
    rutUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    #atributos
<<<<<<< HEAD
    fecha_plipidico = models.DateTimeField( )
    nombre_plipidico = models.CharField(max_length=15,
                        validators=[validators.MinLengthValidator(5, "Error, el nombre plipidico debe contar con mas de 10 caracteres"),
                        validators.MaxLengthValidator(15, "Error, el nombre plipidico debe contar con menos de 15 caracteres")]
                        ) 
    colesterol = models.DecimalField(max_digits= 2, decimal_places=1, )
    colesterol_ldl = models.DecimalField(max_digits= 2, decimal_places=1, )
    colesterol_hdl = models.DecimalField(max_digits= 2, decimal_places=1, )
    trigliceridos = models.DecimalField(max_digits= 2,decimal_places=1, )
    observacion_plipidico = models.CharField(max_length=100,
                        validators=[validators.MinLengthValidator(10, "Error, la observacion debe contar con mas de 10 caracteres"),
                        validators.MaxLengthValidator(150, "Error, la observacion debe contar con menos de 150 caracteres")]
                        ) 


=======
    fecha_plipidico = models.DateField()
    nombre_plipidico = models.CharField(max_length=30,default="Examen de Perfil Lipidico")
    colesterol = models.DecimalField(max_digits=4, decimal_places=1)
    colesterol_ldl = models.DecimalField(max_digits=4, decimal_places=1)
    colesterol_hdl = models.DecimalField(max_digits=4, decimal_places=1)
    trigliceridos = models.DecimalField(max_digits=4, decimal_places=1)
    observacion_plipidico = models.CharField(max_length=100, default="Parametros normales")
>>>>>>> ffdfb6d1889422f4adbbe25c9858f2ab1e059a94
