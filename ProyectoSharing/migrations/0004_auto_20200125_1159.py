# Generated by Django 2.2 on 2020-01-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoSharing', '0003_auto_20200119_0419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id_usuario',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo_electronico',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]