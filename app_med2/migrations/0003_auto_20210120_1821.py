# Generated by Django 3.1.4 on 2021-01-20 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_med2', '0002_auto_20210120_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostico',
            name='fk_rutUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_med2.usuario'),
        ),
    ]
