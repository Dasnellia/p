-- database: :memory:
-- migrate:up

CREATE TABLE calificaciones(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

	actividad_id INTEGER NOT NULL,

    estudiante_seccion_grupo_id INTEGER NOT NULL,

    nota INTEGER NOT NULL,

    FOREIGN KEY (estudiante_seccion_grupo_id) REFERENCES estudiantes_seccion_grupo (id),

    FOREIGN KEY (actividad_id) REFERENCES actividades (id)

);


-- migrate:down

DROP TABLE calificaciones;