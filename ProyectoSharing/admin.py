from django.contrib import admin

# Register your models here.
from ProyectoSharing.models import Autor, Libro, Genero, Intercambio, Usuario, Calificacion, Autor_Libro, Libros_subidos 
# Register your models here.

class AutorAdmin(admin.ModelAdmin):
	list_display=("id_autor","nom_autor","nacionalidad")

class LibroAdmin(admin.ModelAdmin):
	list_display=("id_libro","Titulo","id_genero", "isbn")

class GeneroAdmin(admin.ModelAdmin):
	list_display=("id_genero","nom_genero","descripcion", "total_libros")

class IntercambioAdmin(admin.ModelAdmin):
	list_display=("id_intercambio", "id_libro","id_usuario1","id_usuario2","fecha_prestamo", "fecha_entrega","calificacion1","calificacion2")

class UsuarioAdmin(admin.ModelAdmin):
	list_display=("id_usuario","Nom_usuario", "Apellido_usuario", "correo_electronico", "Telefono","num_libros")

class CalificacionAdmin(admin.ModelAdmin):
	list_display=("id_calificacion","id_libro", "calificacion","comentario","id_usuario")

class Autor_LibroAdmin(admin.ModelAdmin):
	list_display=("id_autor_libro","id_libro", "id_autor")

class Libros_subidosAdmin(admin.ModelAdmin):
	list_display=("id_libro_subido","id_usuario", "id_libro","descripcion_estado","estado")







admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Intercambio, IntercambioAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Calificacion, CalificacionAdmin)
admin.site.register(Autor_Libro, Autor_LibroAdmin)
admin.site.register(Libros_subidos, Libros_subidosAdmin)
