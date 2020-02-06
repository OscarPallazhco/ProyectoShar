SELECT * FROM "ProyectoSharing_calificacion";
SELECT * FROM "ProyectoSharing_intercambio";
SELECT * FROM "ProyectoSharing_libros_subidos";
SELECT * FROM "ProyectoSharing_usuario";
SELECT * FROM "ProyectoSharing_libro";
SELECT * FROM "ProyectoSharing_genero";


DELETE FROM "ProyectoSharing_calificacion";
DELETE FROM "ProyectoSharing_intercambio";
DELETE FROM "ProyectoSharing_libros_subidos";
DELETE FROM "ProyectoSharing_usuario";
DELETE FROM "ProyectoSharing_libro";
DELETE FROM "ProyectoSharing_genero";

INSERT INTO public."ProyectoSharing_genero"(id_genero, nom_genero, descripcion, total_libros ) 
VALUES 
(1, 'Clásico', 'Libros que han perdurado en el tiempo.', 2),
(2, 'Suspenso', 'Libros que generan intriga en los lectores', 1),
(3, 'Terror', 'Libros que generan miedo', 1),
(4, 'Romance', 'Libros romáticos', 1),
(5, 'Juvenil', 'Libros enfocados al público juvenil', 1),
(6, 'Comedia', 'Libros que divierten a sus lectores', 1);

INSERT INTO public."ProyectoSharing_usuario"(correo_electronico, usuario, nombres, apellidos, contrasena, telefono, num_libros) 
VALUES 
('email1@gmail.com', 'usuario1', 'nombres1', 'apellidos1', 'contrasena1', '0999999991',3),
('email2@gmail.com', 'usuario2', 'nombres2', 'apellidos2', 'contrasena2', '0999999992',1),
('email3@gmail.com', 'usuario3', 'nombres3', 'apellidos3', 'contrasena3', '0999999993',1),
('email4@gmail.com', 'usuario4', 'nombres4', 'apellidos4', 'contrasena4', '0999999994',1),
('email5@gmail.com', 'usuario5', 'nombres5', 'apellidos5', 'contrasena5', '0999999995',2),
('email6@gmail.com', 'usuario6', 'nombres6', 'apellidos6', 'contrasena6', '0999999996',0);


INSERT INTO public."ProyectoSharing_libro"(isbn, titulo, id_genero_id) 
VALUES 
('9788498721805', 'El Psicoanalista',2),
('9789585957022', 'El diario de Noah',1),
('9788478085569', 'Yo visité Ganímedes',3),
('9788483656266', 'Yo antes de tí',4),
('9788408146544', 'Días de perros',6),
('9788498387926', 'Quidditch a través de los tiempos',5),
('9788478887231', 'Orgullo y Prejuicio',1);

INSERT INTO public."ProyectoSharing_libros_subidos"(id_libro_subido, descripcion_estado, disponibilidad, correo_electronico_id, isbn_id) 
VALUES 
(1,'En perfecto estado',True,'email1@gmail.com','9788498721805'),
(2,'Tiene 5 años guardado',True,'email1@gmail.com','9789585957022'),
(3,'Páginas marcadas',True,'email1@gmail.com','9788478085569'),
(4,'Páginas dobladas',True,'email2@gmail.com','9788478887231'),
(5,'Páginas con dibujos',True,'email3@gmail.com','9788478887231'),
(6,'En perfecto estado',True,'email4@gmail.com','9788498387926'),
(7,'Aún le saco el plástico protector',True,'email5@gmail.com','9788408146544'),
(8,'100/100',True,'email5@gmail.com','9788408146544');


INSERT INTO public."ProyectoSharing_intercambio"(
	id_intercambio, estado, fecha_solicitud,correo_electronico1_id, correo_electronico2_id, id_libro_subido2_id)
	VALUES 
	(1, 'SOL',now(), 'email1@gmail.com','email2@gmail.com',4),
	(2, 'SOL',now(), 'email2@gmail.com','email3@gmail.com',5),
	(3, 'SOL',now(), 'email1@gmail.com','email3@gmail.com',5),
	(4, 'SOL',now(), 'email2@gmail.com','email4@gmail.com',6),
	(5, 'SOL',now(), 'email1@gmail.com','email5@gmail.com',7),
	(6, 'SOL',now(), 'email2@gmail.com','email4@gmail.com',6),
	(7, 'SOL',now(), 'email3@gmail.com','email1@gmail.com',1),
	(8, 'SOL',now(), 'email3@gmail.com','email2@gmail.com',4);
