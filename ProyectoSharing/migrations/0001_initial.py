# Generated by Django 3.0.1 on 2020-01-16 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_autor', models.IntegerField(primary_key=True, serialize=False)),
                ('nomb_autor', models.CharField(max_length=30)),
                ('nacionalidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_genero', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=50)),
                ('total_libros', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_libro', models.IntegerField(primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=30)),
                ('isbn', models.CharField(max_length=15)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ProyectoSharing.Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom_usuario', models.CharField(max_length=30)),
                ('Apellido_usuario', models.CharField(max_length=30)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
                ('num_libros', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Libros_subidos',
            fields=[
                ('id_libro_subido', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion_estado', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('id_Libro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ProyectoSharing.Libro')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ProyectoSharing.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Intercambio',
            fields=[
                ('id_intercambio', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_prestamo', models.CharField(max_length=50)),
                ('fecha_entrega', models.CharField(max_length=50)),
                ('calificacion1', models.CharField(max_length=50)),
                ('calificacion2', models.CharField(max_length=50)),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ProyectoSharing.Libro')),
                ('id_usuario1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='intercambio_requests_created', to='ProyectoSharing.Usuario')),
                ('id_usuario2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ProyectoSharing.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id_calificacion', models.IntegerField(primary_key=True, serialize=False)),
                ('calificacion', models.IntegerField()),
                ('comentarios', models.CharField(max_length=10)),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ProyectoSharing.Libro')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ProyectoSharing.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Autor_Libro',
            fields=[
                ('id_autor_libro', models.IntegerField(primary_key=True, serialize=False)),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ProyectoSharing.Autor')),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ProyectoSharing.Libro')),
            ],
        ),
    ]
