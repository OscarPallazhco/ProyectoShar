# Generated by Django 2.2 on 2020-02-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoSharing', '0006_auto_20200205_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intercambio',
            name='fecha_devolucion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intercambio',
            name='fecha_prestamo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intercambio',
            name='fecha_solicitud',
            field=models.DateField(auto_now=True),
        ),
    ]