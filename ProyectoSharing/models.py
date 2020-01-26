from django.db import models


# Create your models here.


class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nom_genero = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    total_libros = models.IntegerField(default=0)
    def __str__(self):
        return self.nom_genero
    
    
class Usuario(models.Model):
    #id_usuario = models.AutoField(primary_key=True)
    correo_electronico = models.CharField(primary_key=True, max_length=30)
    usuario = models.CharField(max_length=30)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)    
    contrasena = models.CharField(max_length=128)  #hash
    telefono = models.CharField(max_length=10)
    num_libros = models.IntegerField(default=0)
    def __str__(self):
        return self.usuario 


class Libro(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13)
    titulo = models.CharField(max_length=120)
    id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo_libro
    
    
class Libros_subidos(models.Model):
    id_libro_subido = models.AutoField(primary_key=True)
    descripcion_estado = models.CharField(max_length=500)
    disponibilidad = models.BooleanField(default=True)
    correo_electronico = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    isbn = models.ForeignKey('Libro', on_delete=models.CASCADE)
    


class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nom_autor = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=50)
    def __str__(self):
        return self.nom_autor
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        

class Autor_Libro(models.Model):
    id_autor_libro = models.AutoField(primary_key=True)
    isbn = models.ForeignKey('Libro', on_delete=models.CASCADE)
    id_autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    def __str__(self):
        return self.id_autor,self.isbn
    class Meta:
        verbose_name = "Autor_Libro"
        verbose_name_plural = "Autores_Libros"    


class Intercambio(models.Model):
    SOLICITADO = 'SOL'
    PRESTADO = 'PRE'
    DEVUELTO = 'DEV'
    NEGADO = 'NEG'
    ESTADO_CHOICES = [
        (SOLICITADO, 'Solicitado'),
        (PRESTADO, 'Prestado'),
        (DEVUELTO, 'Devuelto'),
        (NEGADO, 'Negado'),
    ]
    
    id_intercambio = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES, default=SOLICITADO)
    fecha_solicitud = models.DateTimeField(auto_now=True)
    fecha_prestamo = models.DateTimeField(blank=True)
    fecha_devolucion = models.DateTimeField(blank=True)
    calificacion1 = models.FloatField(blank=True)
    calificacion2 = models.FloatField(blank=True)
    comentario1 = models.CharField(max_length=500, blank=True)
    comentario2 = models.CharField(max_length=500, blank=True)
    correo_electronico1 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="correo_electronico1")
    correo_electronico2 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="correo_electronico2")
    id_libro_subido1 = models.ForeignKey('Libros_subidos', on_delete=models.CASCADE, related_name="id_libro_subido1", blank=True)
    id_libro_subido2 = models.ForeignKey('Libros_subidos', on_delete=models.CASCADE, related_name="id_libro_subido2")
    def __str__(self):
        return self.id_libro_subido2, self.fecha_solicitud
    class Meta:
        verbose_name = "Intercambio"
        verbose_name_plural = "Intercambios"


class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    calificacion = models.FloatField()
    comentario = models.CharField(max_length=500)
    id_libro_subido = models.ForeignKey('Libros_subidos', on_delete=models.CASCADE)
    correo_electronico = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"
    def __str__(self):
        return self.correo_electronico + "(" + self.id_libro + ": " + self.calificacion + ")"