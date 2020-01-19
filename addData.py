from django_seed import Seed
from ProyectoSharing.models import *

seeder = Seed.seeder()


seeder.add_entity(Genero, 5)
seeder.add_entity(Usuario, 5)
seeder.add_entity(Libro, 5)
seeder.add_entity(Libros_subidos, 5)
seeder.add_entity(Autor, 5)
seeder.add_entity(Autor_Libro, 5)
seeder.add_entity(Intercambio, 5)
seeder.add_entity(Calificacion, 5)



inserted_pks = seeder.execute()