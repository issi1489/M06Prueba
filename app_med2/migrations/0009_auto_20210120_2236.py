# Generated by Django 2.2.17 on 2021-01-21 01:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_med2', '0008_auto_20210120_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariocbv',
            name='rutUsuario',
            field=models.CharField(default=None, max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(8, 'el rut debe tener entre 9 y 10 caracteres incluido el guion')]),
        ),
    ]
