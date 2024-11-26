-- database: :memory:
-- migrate:up

CREATE TABLE documentos(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    fecha_publicacion DATE NOT NULL,

    contenidos_curso_id INTEGER NOT NULL,

    informacion_recursos_comunes_id INTEGER NOT NULL,

    FOREIGN KEY (contenidos_curso_id) REFERENCES contenidos_curso (id),

    FOREIGN KEY (informacion_recursos_comunes_id) REFERENCES informacion_recursos_comunes (id)

);


-- migrate:down

DROP TABLE documentos;