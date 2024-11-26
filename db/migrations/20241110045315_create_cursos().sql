-- database: :memory:
-- migrate:up
CREATE TABLE cursos (

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    nombre VARCHAR(25) NOT NULL,

    codigo INTEGER NOT NULL,

    descripcion VARCHAR(100) NOT NULL

);

-- migrate:down

DROP TABLE cursos;