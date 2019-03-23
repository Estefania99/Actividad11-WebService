CREATE DATABASE ferreteria_egr;

USE ferreteria_egr;

CREATE TABLE clientes(
    id_cliente int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_cliente varchar(30) NOT NULL,
    apellido_paterno varchar(30) NOT NULL,
    apellido_materno varchar(30)  NOT NULL,
    telefono char(10)  NOT NULl,
    email varchar(50) NOT NULl
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into clientes (nombre_cliente,apellido_paterno,apellido_materno,telefono,email)values
('Alexis','Hernandez','Perez','7751233201','alexishpmail.com'),
('Estefania', 'Garcia','Resendiz','7751374752','fannygarciar@gmail.com'),
('Carlos','Domiguez','Omania','5512305173','carlosdominguez@hotmail.com');


SHOW TABLES;

SELECT * FROM clientes;

DESCRIBE clientes;

CREATE USER 'elle'@'localhost' IDENTIFIED BY 'elle.2019';
GRANT ALL PRIVILEGES ON ferreteria_egr.* TO 'elle'@'localhost';
FLUSH PRIVILEGES;
