-- database: :memory:
-- migrate:up


CREATE TABLE grupos(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    codigo INTEGER NOT NULL,

    nombre VARCHAR(25) NOT NULL,

    seccion_id INTEGER NOT NULL,

    FOREIGN KEY (seccion_id) REFERENCES secciones (id)

);

-- migrate:down

DROP TABLE grupos;  