create database clinica1;
use clinica1;
create table pacientes(
	id_paciente int auto_increment primary key,
	nombre varchar(100),
	edad int,
	genero varchar(10),
	diagnostico varchar(150)
);
insert into pacientes(nombre,edad,genero,diagnostico) values('Edmand Lara',54,'Masculino','Esclerosis');
select * from pacientes;
