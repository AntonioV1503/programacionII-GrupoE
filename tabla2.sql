create database clinica1;
use clinica1;
create table pacientes(
	id_paciente int auto_increment primary key,
	nombre varchar(100),
	edad int,
	genero varchar(10),
	diagnostico varchar(150)
);
insert into pacientes(nombre,edad,genero,diagnostico) values('Evo Morales',67,'Masculino','Cancer');
select * from pacientes;
update pacientes set diagnostico='Anemia' where id_paciente=1;
delete from pacientes where id_paciente=1;
create table doctor(
	id_doctor int auto_increment primary key,
	nombre varchar(50),
	cedula varchar(10),
    correo varchar(50),
	fechaingreso date
);
insert into doctor(nombre,cedula,correo,fechaingreso) values('Paolo Guerrero','124521SC','paolog@gmail.com','2023-09-27');
select * from doctor;
delete from doctor where id_doctor=3;
update doctor set fechaingreso='2025-10-17' where id_doctor=5;

