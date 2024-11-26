-- database: :memory:
-- migrate:up
CREATE TABLE destinatarios_mensajes(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    mensaje_id INTEGER NOT NULL,

    estudiante_id INTEGER NOT NULL,

    FOREIGN KEY (mensaje_id) REFERENCES mensajes (id),

    FOREIGN KEY (estudiante_id) REFERENCES estudiantes (id)

);


-- migrate:down

DROP TABLE destinatarios_mensajes;