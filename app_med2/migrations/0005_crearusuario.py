# Generated by Django 3.1.4 on 2021-01-21 03:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_med2', '0004_auto_20210120_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrearUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rutUsuario', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(4, 'Marca debe tener 4 caracteres mínimo!')])),
                ('edad', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'El modelo no puede ser de menos de 2 letras')])),
                ('direccion', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'El modelo no puede ser de menos de 2 letras')])),
                ('staff', models.BooleanField(null=True)),
                ('usuario1', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
            ],
        ),
    ]
