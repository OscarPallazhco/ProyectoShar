Para levantar el servidor:
	python manage.py runserver

Intentará conectarse a la base de datos postgres, por lo que se deberá levantar previamente el acceso a la base de datos en pgAdmin4, la contraseña para ingresar se la debe poner 'root', usuario: 'postgres'(por defecto) y crear una base de datos que se llame: 'ProyectoShar', las tablas y columnas se crearán automáticamente cuando se conecte con django.