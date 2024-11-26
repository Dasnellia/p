-- database: :memory:
-- migrate:up
CREATE TABLE estudiantes_seccion_grupo(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    estudiante_seccion_id INTEGER NOT NULL,

    grupo_id INTEGER NOT NULL,

    FOREIGN KEY (estudiante_seccion_id) REFERENCES estudiantes_secciones (id),

    FOREIGN KEY (grupo_id) REFERENCES grupos (id)

);


-- migrate:down

DROP TABLE estudiantes_seccion_grupo;