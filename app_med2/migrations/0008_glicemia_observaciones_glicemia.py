# Generated by Django 3.1.4 on 2021-01-22 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_med2', '0007_auto_20210121_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='glicemia',
            name='observaciones_glicemia',
            field=models.CharField(default='Parametros normales', max_length=100),
        ),
    ]
