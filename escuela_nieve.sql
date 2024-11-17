-- CREACION DE TABLAS

use EscuelaNieve;

CREATE TABLE login (
    correo NVARCHAR(100) PRIMARY KEY,
    contrasena NVARCHAR(255) NOT NULL
);


CREATE TABLE actividades (
    id INT PRIMARY KEY IDENTITY(1,1),
    descripcion NVARCHAR(100) NOT NULL,
    costo DECIMAL(10, 2) NOT NULL
);

CREATE TABLE equipamiento (
    id INT PRIMARY KEY IDENTITY(1,1),
    id_actividad INT NOT NULL,
    descripcion NVARCHAR(100) NOT NULL,
    costo DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_actividad) REFERENCES actividades(id)
);

CREATE TABLE instructores (
    ci CHAR(8) PRIMARY KEY,
    nombre NVARCHAR(50) NOT NULL,
    apellido NVARCHAR(50) NOT NULL
);

CREATE TABLE turnos (
    id INT PRIMARY KEY IDENTITY(1,1),
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL
);

CREATE TABLE alumnos (
    ci CHAR(8) PRIMARY KEY,
    nombre NVARCHAR(50) NOT NULL,
    apellido NVARCHAR(50) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    telefono NVARCHAR(20),
    correo NVARCHAR(100) NOT NULL
);

CREATE TABLE clase (
    id INT PRIMARY KEY IDENTITY(1,1),
    ci_instructor CHAR(8) NOT NULL,
    id_actividad INT NOT NULL,
    id_turno INT NOT NULL,
    dictada BIT DEFAULT 0,
    FOREIGN KEY (ci_instructor) REFERENCES instructores(ci),
    FOREIGN KEY (id_actividad) REFERENCES actividades(id),
    FOREIGN KEY (id_turno) REFERENCES turnos(id),
    CONSTRAINT unique_instructor_turno UNIQUE (ci_instructor, id_turno) --Esto evita que el mismo instructor tenga dos clases en el mismo turno
);

CREATE TABLE alumno_clase (
    id_clase INT NOT NULL,
    ci_alumno CHAR(8) NOT NULL,
    id_equipamiento INT NULL, -- Esto sera NULL si usa equipo propio
    alquiler BIT NOT NULL DEFAULT 0, -- 0 = equipo propio, 1 = alquilo equipo
    PRIMARY KEY (id_clase, ci_alumno),
    FOREIGN KEY (id_clase) REFERENCES clase(id),
    FOREIGN KEY (ci_alumno) REFERENCES alumnos(ci),
    FOREIGN KEY (id_equipamiento) REFERENCES equipamiento(id),
    CONSTRAINT unique_alumno_clase UNIQUE (ci_alumno, id_clase) --Esto evita que un alumno este inscrito en dos clases en el mismo turno
);

-- INSERCION DE DATOS

INSERT INTO actividades (descripcion, costo)
VALUES ('Snowboard', 1500.00),
       ('Ski', 1300.00),
       ('Moto de nieve', 2000.00);

INSERT INTO equipamiento (id_actividad, descripcion, costo)
VALUES (1, 'Tabla de Snowboard', 300.00),
       (1, 'Botas de Snowboard', 200.00),
       (2, 'Esquis', 350.00),
       (2, 'Botas de Ski', 250.00),
       (3, 'Moto de nieve', 500.00);

INSERT INTO instructores (ci, nombre, apellido)
VALUES ('12345678', 'Juan', 'Perez'),
       ('87654321', 'Maria', 'Gonzalez'),
       ('11223344', 'Carlos', 'Rodriguez');

INSERT INTO turnos (hora_inicio, hora_fin)
VALUES ('09:00', '11:00'),
       ('12:00', '14:00'),
       ('16:00', '18:00');

INSERT INTO alumnos (ci, nombre, apellido, telefono, correo)
VALUES ('55555555', 'Ana', 'Lopez', '091234567', 'ana.lopez@gmail.com'),
       ('66666666', 'Luis', 'Martinez', '098765432', 'luis.martinez@hotmail.com'),
       ('77777777', 'Sofia', 'Gomez', '099876543', 'sofia.gomez@gmail.com');

INSERT INTO clase (ci_instructor, id_actividad, id_turno, dictada)
VALUES ('12345678', 1, 1, 0), -- Snowboard con Juan en el turno de 9:00 a 11:00
       ('87654321', 2, 2, 0), -- Ski con Maria en el turno de 12:00 a 14:00
       ('11223344', 3, 3, 0); -- Moto de nieve con Carlos en el turno de 16:00 a 18:00

INSERT INTO alumno_clase (id_clase, ci_alumno, id_equipamiento, alquiler)
VALUES (1, '55555555', 1, 1), -- Ana en Snowboard, alquilo tabla
       (2, '66666666', NULL, 0), -- Luis en Ski, equipo propio
       (3, '77777777', 5, 1); -- Sofia en Moto de nieve, alquilo moto

ALTER TABLE alumno_clase
ADD CONSTRAINT FK__alumno_cl__id_cl__72C60C4A
FOREIGN KEY (id_clase) REFERENCES clase(id)
ON DELETE CASCADE;

ALTER TABLE clase
ADD CONSTRAINT FK_clase_instructor
FOREIGN KEY (ci_instructor) REFERENCES instructores(ci)
ON DELETE CASCADE;

ALTER TABLE clase
ADD CONSTRAINT FK_clase_actividad
FOREIGN KEY (id_actividad) REFERENCES actividades(id)
ON DELETE CASCADE;

ALTER TABLE clase
ADD CONSTRAINT FK_clase_turno
FOREIGN KEY (id_turno) REFERENCES turnos(id)
ON DELETE CASCADE;

ALTER TABLE equipamiento
ADD CONSTRAINT FK_Equipamiento_Actividad
FOREIGN KEY (id_actividad) REFERENCES actividades(id)
ON DELETE CASCADE;