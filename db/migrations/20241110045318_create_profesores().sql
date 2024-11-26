-- database: :memory:
-- migrate:up
CREATE TABLE profesores(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    nombre VARCHAR(25) NOT NULL,

    apellidos VARCHAR(50) NOT NULL,

    direccion VARCHAR(100) NOT NULL,

    foto VARCHAR(100) NOT NULL,

    codigo_institucional INTEGER NOT NULL,

    contrasena VARCHAR(50) NOT NULL,

    id_usuario INTEGER NOT NULL,

    FOREIGN KEY (id_usuario) REFERENCES usuarios (id)

);


-- migrate:down

DROP TABLE profesores;