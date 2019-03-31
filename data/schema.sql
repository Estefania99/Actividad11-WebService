
CREATE TABLE clientes( 
    id_cliente integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(30) NOT NULL,
    apellido_paterno varchar(40) NOT NULL,
    apellido_materno varchar(40) NOT NULL,
    telefono varchar(10) NOT NULL,
    email varchar(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO clientes(nombre,apellido_paterno,apellido_materno,telefono,email)VALUES
('Alexis','Hernandez','Perez', '7714563289','alexisher@hotmail.com'),
('Estefania','Garcia','Resendiz', '5512369850','fannygarcia14@gmail.com'),
('Carlos','Dominguez','Omania', '7751235698','carlitosdom12@gmail.com');



