-- database: :memory:
-- migrate:up
CREATE TABLE mensajes(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    remitente_id INTEGER NOT NULL,

    redacto VARCHAR(250) NOT NULL,

    fecha_envio DATETIME NOT NULL,

    seccion_id INTEGER NOT NULL,

    FOREIGN KEY (remitente_id) REFERENCES estudiantes (id),

    FOREIGN KEY (seccion_id) REFERENCES secciones (id)

);


-- migrate:down

DROP TABLE mensajes;