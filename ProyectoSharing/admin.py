from django.contrib import admin

# Register your models here.
from ProyectoSharing.models import *

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Genero)
admin.site.register(Intercambio)
admin.site.register(Usuario)
admin.site.register(Calificacion)
admin.site.register(Autor_Libro)
admin.site.register(Libros_subidos)
