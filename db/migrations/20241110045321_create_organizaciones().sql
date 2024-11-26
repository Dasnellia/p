-- database: :memory:
-- migrate:up
CREATE TABLE organizaciones(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    nombre VARCHAR(25) NOT NULL,

    profesor_id INTEGER NOT NULL,

    FOREIGN KEY (profesor_id) REFERENCES profesores (id)

);


-- migrate:down

DROP TABLE organizaciones;