-- database: :memory:
-- migrate:up
CREATE TABLE periodos(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    fecha_inicio DATE NOT NULL,

    fecha_fin DATE NOT NULL

);


-- migrate:down

DROP TABLE periodos;