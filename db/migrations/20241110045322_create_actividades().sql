-- database: :memory:
-- migrate:up
CREATE TABLE actividades(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    nombre VARCHAR(25) NOT NULL,
    
    detalles VARCHAR(255) NOT NULL,

    fecha_publicacion DATE NOT NULL,

    fecha_entrega DATE NOT NULL,

    tipo VARCHAR(25) NOT NULL

);


-- migrate:down

DROP TABLE actividades;