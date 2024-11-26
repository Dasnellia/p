-- database: :memory:
-- migrate:up
CREATE TABLE secciones(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    codigo INTEGER NOT NULL,

    curso_id INTEGER NOT NULL,

    profesor_id INTEGER NOT NULL,

    periodo_id INTEGER NOT NULL,

    FOREIGN KEY (curso_id) REFERENCES cursos (id),

    FOREIGN KEY (profesor_id) REFERENCES profesores (id),

    FOREIGN KEY (periodo_id) REFERENCES periodos (id)

);


-- migrate:down
DROP TABLE secciones;
