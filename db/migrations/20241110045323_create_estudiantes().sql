-- database: :memory:
-- migrate:up
CREATE TABLE estudiantes(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    nombre VARCHAR(25) NOT NULL,

    apellidos VARCHAR(50) NOT NULL,

    direccion VARCHAR(100) NOT NULL,

    foto VARCHAR(100) NOT NULL,

    usuario_id INTEGER NOT NULL,

    sexo_id INTEGER NOT NULL,

    codigo_institucional INTEGER NOT NULL,

    correo VARCHAR(100) NOT NULL,

    telefono VARCHAR(15) NOT NULL,

    dni INTEGER NOT NULL,

    FOREIGN KEY (sexo_id) REFERENCES sexos (id),

    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)

);


-- migrate:down

DROP TABLE estudiantes;