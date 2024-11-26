-- database: :memory:
-- migrate:up
CREATE TABLE usuarios(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    contrasena VARCHAR(50) NOT NULL,
    nombre_usuario VARCHAR(50) NOT NULL
);


-- migrate:down

DROP TABLE usuarios;