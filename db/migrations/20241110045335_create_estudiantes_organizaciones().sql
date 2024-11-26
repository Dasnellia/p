-- database: ../proyect.db
-- migrate:up
CREATE TABLE estudiantes_organizaciones (

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    estudiante_id INTEGER NOT NULL,

    organizacion_id INTEGER NOT NULL,

    FOREIGN KEY (estudiante_id) REFERENCES estudiantes (id),

    FOREIGN KEY (organizacion_id) REFERENCES organizaciones (id)

);


-- migrate:down

DROP TABLE estudiantes_organizaciones;