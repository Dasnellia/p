-- database: :memory:
-- migrate:up
CREATE TABLE informacion_recursos_comunes (

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    nombre VARCHAR(100) NOT NULL,

    silabo VARCHAR(100) NOT NULL,

    descripcion VARCHAR(100) NOT NULL,

    curso_id INTEGER NOT NULL,

    FOREIGN KEY (curso_id) REFERENCES cursos (id)

);


-- migrate:down

DROP TABLE informacion_recursos_comunes;