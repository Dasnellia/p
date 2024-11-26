-- database: :memory:
-- migrate:up
CREATE TABLE contenidos_curso(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    zoom VARCHAR(100) NOT NULL,

    seccion_id INTEGER NOT NULL,

    FOREIGN KEY (seccion_id) REFERENCES secciones (id)

);


-- migrate:down

DROP TABLE contenidos_curso;