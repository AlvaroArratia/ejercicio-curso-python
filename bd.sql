-- Se crea la base de datos
CREATE DATABASE IF NOT EXISTS master_python;

-- Se crean las tablas de la base de datos
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER auto_increment NOT NULL,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    pass VARCHAR(255) NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email) -- CONSTRAINT sirve para poner restricciones
) ENGINE = InnoDb;

CREATE TABLE IF NOT EXISTS notas(
    id INTEGER auto_increment NOT NULL,
    id_usuario INTEGER NOT NULL,
    titulo VARCHAR(255),
    nota MEDIUMTEXT,
    fecha DATE NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
) ENGINE = InnoDb;

-- ENGINE = InnoDb define el motor de almacenamiento del servidor mysql