CREATE TABLE IF NOT EXISTS "schema_migrations" (version varchar(128) primary key);
CREATE TABLE sexos(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(10) NOT NULL

);
CREATE TABLE usuarios(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    contrasena VARCHAR(50) NOT NULL,
    nombre_usuario VARCHAR(50) NOT NULL
);
CREATE TABLE cursos (

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    nombre VARCHAR(25) NOT NULL,

    codigo INTEGER NOT NULL,

    descripcion VARCHAR(100) NOT NULL

);
CREATE TABLE periodos(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    fecha_inicio DATE NOT NULL,

    fecha_fin DATE NOT NULL

);
CREATE TABLE profesores(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    nombre VARCHAR(25) NOT NULL,

    apellidos VARCHAR(50) NOT NULL,

    direccion VARCHAR(100) NOT NULL,

    foto VARCHAR(100) NOT NULL,

    codigo_institucional INTEGER NOT NULL,

    contrasena VARCHAR(50) NOT NULL,

    id_usuario INTEGER NOT NULL,

    FOREIGN KEY (id_usuario) REFERENCES usuarios (id)

);
CREATE TABLE secciones(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    codigo INTEGER NOT NULL,

    curso_id INTEGER NOT NULL,

    profesor_id INTEGER NOT NULL,

    periodo_id INTEGER NOT NULL,

    FOREIGN KEY (curso_id) REFERENCES cursos (id),

    FOREIGN KEY (profesor_id) REFERENCES profesores (id),

    FOREIGN KEY (periodo_id) REFERENCES periodos (id)

);
CREATE TABLE grupos(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    codigo INTEGER NOT NULL,

    nombre VARCHAR(25) NOT NULL,

    seccion_id INTEGER NOT NULL,

    FOREIGN KEY (seccion_id) REFERENCES secciones (id)

);
CREATE TABLE organizaciones(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    nombre VARCHAR(25) NOT NULL,

    profesor_id INTEGER NOT NULL,

    FOREIGN KEY (profesor_id) REFERENCES profesores (id)

);
CREATE TABLE actividades(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    nombre VARCHAR(25) NOT NULL,

    detalles VARCHAR(255) NOT NULL,

    fecha_publicacion DATE NOT NULL,

    fecha_entrega DATE NOT NULL,

    tipo VARCHAR(25) NOT NULL

);
CREATE TABLE estudiantes(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    nombre VARCHAR(25) NOT NULL,

    apellidos VARCHAR(50) NOT NULL,

    direccion VARCHAR(100) NOT NULL,

    foto VARCHAR(100) NOT NULL,

    usuario_id INTEGER NOT NULL,

    sexo_id INTEGER NOT NULL,

    codigo_institucional INTEGER NOT NULL,

    correo VARCHAR(100) NOT NULL,

    telefono VARCHAR(15) NOT NULL,

    dni INTEGER NOT NULL,

    FOREIGN KEY (sexo_id) REFERENCES sexos (id),

    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)

);
CREATE TABLE estudiantes_secciones(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    estudiante_id INTEGER NOT NULL,

    seccion_id INTEGER NOT NULL,

    FOREIGN KEY (estudiante_id) REFERENCES estudiantes (id),

    FOREIGN KEY (seccion_id) REFERENCES secciones (id)

);
CREATE TABLE estudiantes_seccion_grupo(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    estudiante_seccion_id INTEGER NOT NULL,

    grupo_id INTEGER NOT NULL,

    FOREIGN KEY (estudiante_seccion_id) REFERENCES estudiantes_secciones (id),

    FOREIGN KEY (grupo_id) REFERENCES grupos (id)

);
CREATE TABLE calificaciones(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

	actividad_id INTEGER NOT NULL,

    estudiante_seccion_grupo_id INTEGER NOT NULL,

    nota INTEGER NOT NULL,

    FOREIGN KEY (estudiante_seccion_grupo_id) REFERENCES estudiantes_seccion_grupo (id),

    FOREIGN KEY (actividad_id) REFERENCES actividades (id)

);
CREATE TABLE anuncios(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    autor VARCHAR(25) NOT NULL,

    contenido VARCHAR(250) NOT NULL,

    fecha DATETIME NOT NULL,

    seccion_id INTEGER NOT NULL,

    FOREIGN KEY (seccion_id) REFERENCES secciones (id)

);
CREATE TABLE mensajes(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    remitente_id INTEGER NOT NULL,

    redacto VARCHAR(250) NOT NULL,

    fecha_envio DATETIME NOT NULL,

    seccion_id INTEGER NOT NULL,

    FOREIGN KEY (remitente_id) REFERENCES estudiantes (id),

    FOREIGN KEY (seccion_id) REFERENCES secciones (id)

);
CREATE TABLE destinatarios_mensajes(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    mensaje_id INTEGER NOT NULL,

    estudiante_id INTEGER NOT NULL,

    FOREIGN KEY (mensaje_id) REFERENCES mensajes (id),

    FOREIGN KEY (estudiante_id) REFERENCES estudiantes (id)

);
CREATE TABLE contenidos_curso(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    zoom VARCHAR(100) NOT NULL,

    seccion_id INTEGER NOT NULL,

    FOREIGN KEY (seccion_id) REFERENCES secciones (id)

);
CREATE TABLE informacion_recursos_comunes (

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    nombre VARCHAR(100) NOT NULL,

    silabo VARCHAR(100) NOT NULL,

    descripcion VARCHAR(100) NOT NULL,

    curso_id INTEGER NOT NULL,

    FOREIGN KEY (curso_id) REFERENCES cursos (id)

);
CREATE TABLE documentos(

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    fecha_publicacion DATE NOT NULL,

    contenidos_curso_id INTEGER NOT NULL,

    informacion_recursos_comunes_id INTEGER NOT NULL,

    FOREIGN KEY (contenidos_curso_id) REFERENCES contenidos_curso (id),

    FOREIGN KEY (informacion_recursos_comunes_id) REFERENCES informacion_recursos_comunes (id)

);
CREATE TABLE estudiantes_organizaciones (

    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

    estudiante_id INTEGER NOT NULL,

    organizacion_id INTEGER NOT NULL,

    FOREIGN KEY (estudiante_id) REFERENCES estudiantes (id),

    FOREIGN KEY (organizacion_id) REFERENCES organizaciones (id)

);
-- Dbmate schema migrations
INSERT INTO "schema_migrations" (version) VALUES
  ('20241110045313'),
  ('20241110045314'),
  ('20241110045315'),
  ('20241110045317'),
  ('20241110045318'),
  ('20241110045319'),
  ('20241110045320'),
  ('20241110045321'),
  ('20241110045322'),
  ('20241110045323'),
  ('20241110045324'),
  ('20241110045325'),
  ('20241110045327'),
  ('20241110045328'),
  ('20241110045329'),
  ('20241110045330'),
  ('20241110045331'),
  ('20241110045332'),
  ('20241110045333'),
  ('20241110045335'),
  ('20241110161501'),
  ('20241110161503'),
  ('20241110161504'),
  ('20241110161505'),
  ('20241110161506'),
  ('20241110161507'),
  ('20241110161508'),
  ('20241110161509'),
  ('20241110161511'),
  ('20241110161512'),
  ('20241110161513'),
  ('20241110161514'),
  ('20241110161515'),
  ('20241110161516'),
  ('20241110161517'),
  ('20241110161519'),
  ('20241110161520'),
  ('20241110161521'),
  ('20241110161522'),
  ('20241110162204');
