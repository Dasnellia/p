-- migrate:up
CREATE TABLE sexos(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(10) NOT NULL

);



-- migrate:down

DROP TABLE sexos;