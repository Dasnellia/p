-- database: :memory:
-- migrate:up
CREATE TABLE estudiantes_secciones(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    estudiante_id INTEGER NOT NULL,

    seccion_id INTEGER NOT NULL,

    FOREIGN KEY (estudiante_id) REFERENCES estudiantes (id),

    FOREIGN KEY (seccion_id) REFERENCES secciones (id)

);


-- migrate:down

DROP TABLE estudiantes_secciones;