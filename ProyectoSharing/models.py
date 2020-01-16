from django.db import models


# Create your models here.


class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nom_autor = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=50)
    def __str__(self):
        return self.nom_autor
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nom_genero = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    total_libros = models.IntegerField(default=0)
    def __str__(self):
        return self.nom_genero


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=15)
    Titulo = models.CharField(max_length=30)
    id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo_libro


class Autor_Libro(models.Model):
    id_autor_libro = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey('Libro', on_delete=models.CASCADE)
    id_autor = models.ForeignKey('Autor', on_delete=models.CASCADE)


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    Nom_usuario = models.CharField(max_length=30)
    Apellido_usuario = models.CharField(max_length=30)
    correo_electronico = models.EmailField()
    Telefono = models.CharField(max_length=10)
    num_libros = models.IntegerField(default=0)
    def __str__(self):
        return self.nom_usuario + self.apellido_usuario


class Intercambio(models.Model):
    id_intercambio = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey('Libro', on_delete=models.CASCADE)
    id_usuario1 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="id_usuario1")
    id_usuario2 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="id_usuario2")
    fecha_prestamo = models.CharField(max_length=50)
    fecha_entrega = models.CharField(max_length=50)
    calificacion1 = models.CharField(max_length=50)
    calificacion2 = models.CharField(max_length=50)
    def __str__(self):
        return self.id_libro, self.fecha_prestamo


class Libros_subidos(models.Model):
    id_libro_subido = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    id_libro = models.ForeignKey('Libro', on_delete=models.CASCADE)
    descripcion_estado = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)


class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    calificacion = models.FloatField()
    comentario = models.CharField(max_length=50)
    id_libro = models.ForeignKey('Libro', on_delete=models.CASCADE)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"
    def __str__(self):
        return self.id_usuario + "(" + self.id_libro + ": " + self.calificacion + ")"
