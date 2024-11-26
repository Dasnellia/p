-- database: :memory:
-- migrate:up
CREATE TABLE anuncios(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    autor VARCHAR(25) NOT NULL,

    contenido VARCHAR(250) NOT NULL,

    fecha DATETIME NOT NULL,

    seccion_id INTEGER NOT NULL,

    FOREIGN KEY (seccion_id) REFERENCES secciones (id)

);


-- migrate:down

DROP TABLE anuncios;