from faker import Faker
from datetime import datetime
import random
from datetime import timedelta

fake = Faker() # Faker fake = new Faker();

def llenar_productos():
    i = 1
    contenido = ''
    with open('productos.txt', mode='r', newline='', encoding='utf-8') as archivo:
        for fila in archivo:
            fila = fila.strip().split('::')
            id = fila[0]
            nombre = fila[1].capitalize()
            categoria_id = fila[2]
            descripcion = fake.paragraph()
            codigo = random.randint(1000,5000)
            valor_unitario = random.randint(5,200)/100.0
            tmp = f"INSERT INTO productos (id, nombre, codigo, descripcion, valor_unitario, categoria_id) VALUES ({id}, '{nombre}', {codigo}, '{descripcion}', {valor_unitario}, {categoria_id});\n"
            contenido = contenido + tmp
    with open('inserts_productos.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)




#def llenar_clientes():
    i = 0
    contenido = ''
    while i < 100:
        id = i + 1
        nombre = fake.name()
        direccion = fake.address()
        rif = random.randint(10000000,99999999)
        ciudad_id = random.randint(1,4)
        tmp = f"INSERT INTO clientes (id, nombre, direccion, rif, ciudad_id) VALUES ({id}, '{nombre}', '{direccion}', {rif}, {ciudad_id});\n"
        contenido = contenido + tmp
        i = i + 1
    with open('inserts_clientes.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

#def llenar_facturas():
    i = 0
    contenido = ''
    fecha_inicio = datetime(2022, 1, 1)
    fecha_fin = datetime(2023, 12, 31)
    while i < 1000:
        id = i + 1
        numero = 100000 + id
        cliente_id = random.randint(1,100)
        fecha_aleatoria = fake.date_time_between(start_date=fecha_inicio, end_date=fecha_fin)
        fecha = fecha_aleatoria.strftime('%Y-%m-%d %H:%M:%S')
        tmp = f"INSERT INTO facturas (id, fecha, cliente_id, numero) VALUES ({id}, '{str(fecha)}', {cliente_id}, {numero});\n"
        contenido = contenido + tmp
        i = i + 1
    with open('inserts_facturas.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

# llenar_productos()
#def llenar_facturas_productos():
    count_facturas =1000
    count_productos = 32
    i = 1
    contenido = ''
    i = 0
    id = 1

    while i < count_facturas:
        n_productos = random.randint(1,32)
        k = 0
        
        lista_productos_ids = []

        while k < n_productos:
            tmp = random.randint(1,count_productos)
            if tmp not in lista_productos_ids:
                lista_productos_ids.append(tmp)
            k = k+1
        for producto_id in lista_productos_ids:
            cantidad = random.randint(1,20)
            factura_id = i+1
            tmp = f" INSERT INTO facturas_productos (id,cantidad, producto_id, factura_id) VALUES ({id}, '{cantidad}', '{producto_id}','{factura_id}');\n"
            contenido = contenido + tmp
        i = i+1
    with open('inserts_facturas_productos.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

# llenar_clientes()
#llenar_facturas_productos()
#llenar_facturas()

periodosinicioporseccion = [] #la posicion del periodo es la id de la seccion +1}

idactividadesgrupales = []
idactividadesindividuales = []

def llenar_sexos():
    i = 0
    contenido = ''
    c = ['MASCULINO', 'FEMENINO', 'OTRO', 'NO ESPECIFICADO','NO BINARIO']
    while i < 5:
        id = 1 +i
        nombre = c[i]
        tmp = f"INSERT INTO sexos (id, nombre) VALUES ({id}, '{nombre}');\n"
        contenido= contenido+tmp
        i = i + 1
    with open('inserts_sexos.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def llenar_usuarios():
    id = 0
    i = 0
    contenido = ''
    while i < 1100:
        id = i + 1
        nombre_usuario = fake.user_name()
        contrasena = fake.password()
        tmp = f"INSERT INTO usuarios (id, nombre_usuario, contrasena) VALUES ({id}, '{nombre_usuario}', '{contrasena}');\n"
        contenido = contenido + tmp
        i = i + 1
    with open('inserts_usuarios.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def llenar_cursos():
    contenido = ''
    with open('cursos.txt', mode='r', newline='', encoding='utf-8') as archivo:
        i = 1
        for fila in archivo:
            fila = fila.strip().split('::')
            id = i
            nombre = fila[1].capitalize()
            descripcion = fake.paragraph()
            codigo = fila[0]
            i = i+1
            tmp = f"INSERT INTO cursos (id, nombre, codigo, descripcion) VALUES ({id}, '{nombre}', {codigo}, '{descripcion}');\n"
            contenido = contenido + tmp
    with open('inserts_cursos.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def llenar_periodos():
    i = 0
    contenido = ''
    while i < 100:
        id = i + 1
        fecha_inicio = fake.date_time_between(start_date=datetime(2020, 1, 1), end_date='now')
        fecha_fin = fecha_inicio + timedelta(days=6*30)
        tmp = f"INSERT INTO periodos (id, fecha_inicio, fecha_fin) VALUES ({id}, '{fecha_inicio}', '{fecha_fin}');\n"
        contenido = contenido + tmp
        i = i + 1
    with open('inserts_periodos.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def llenar_profesores():
    i = 0
    contenido = ''
    while i < 100:
        id = i + 1
        nombre = fake.name()
        apellidos = fake.last_name()
        direccion = fake.address()
        foto = fake.image_url()
        codigo_institucional = random.randint(10000000,99999999)
        contrasena = fake.password()
        id_usuario = id +1000
        tmp = f"INSERT INTO profesores (id, nombre, apellidos, direccion, foto, codigo_institucional, contrasena, id_usuario) VALUES ({id}, '{nombre}', '{apellidos}', '{direccion}', '{foto}', {codigo_institucional}, '{contrasena}', {id_usuario});\n"
        contenido = contenido + tmp
        i = i + 1
    with open('inserts_profesores.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def llenar_secciones():
    i = 0
    contenido = ''
    while i < 100:
        id = 1 +i
        codigo = random.randint(10000,50000)
        curso_id = random.randint(1,20)
        profesor_id = random.randint(1,100)
        periodo_id = random.randint(1,100)
        tmp = f"INSERT INTO secciones (id, codigo, curso_id, profesor_id, periodo_id) VALUES ({id}, {codigo}, {curso_id}, {profesor_id}, {periodo_id});\n"
        contenido= contenido+tmp
        i = i + 1
    with open('inserts_secciones.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)    

def llenar_grupos():
    i = 0
    contenido = ''
    while i < 100:
        id = 1 +i
        codigo = random.randint(10000,50000)
        nombre = fake.language_name()
        seccion_id = random.randint(1,100)
        tmp = f"INSERT INTO grupos (id, codigo, nombre, seccion_id) VALUES ({id}, {codigo}, '{nombre}', {seccion_id});\n"
        contenido= contenido+tmp
        i = i + 1
    with open('inserts_grupos.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def llenar_organizaciones():
    i = 0
    contenido = ''
    profesor_ids_usados = set()
    while i < 100:
        id = 1 +i
        nombre = fake.company()
        profesor_id = random.randint(1,100)
        while profesor_id in profesor_ids_usados:
            profesor_id = random.randint(1,100)
        profesor_ids_usados.add(profesor_id)
        tmp = f"INSERT INTO organizaciones (id, nombre, profesor_id) VALUES ({id}, '{nombre}', {profesor_id});\n"
        contenido= contenido+tmp
        i = i + 1
    with open('inserts_organizaciones.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def llenar_actividades_tipo():
    i = 0
    contenido = ''
    c = ['Individual','Grupal']
    while i < 2:
        id = 1 +i
        nombre = c[i]
        tmp = f"INSERT INTO actividades_tipo (id, nombre) VALUES ({id}, '{nombre}');\n"
        contenido= contenido+tmp
        i = i + 1
    with open('inserts_actividades_tipo.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def llenar_actividades():
    i = 0
    contenido = ''
    while i < 100:
        id = 1 +i
        nombre = fake.job()
        fecha_publicacion = fake.date_time_between(start_date=datetime(2020, 1, 1), end_date='now')
        fecha_entrega = fecha_publicacion + timedelta(days=15)
        detalles = fake.paragraph()
        tipo_id = random.randint(1,2) 
        if (tipo_id ==2): {
            idactividadesgrupales.append(id)
        }
        else:{
            idactividadesindividuales.append(id)
        }
        tmp = f"INSERT INTO actividades (id, nombre, fecha_publicacion, fecha_entrega, detalles, tipo_id) VALUES ({id}, '{nombre}', '{fecha_publicacion}', '{fecha_entrega}', '{detalles}', {tipo_id});\n"
        contenido= contenido+tmp
        i = i + 1
    with open('inserts_actividades.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def llenar_estudiantes():
    i = 0
    contenido = ''
    while i < 1000:
        id = 1 +i
        nombre = fake.name()
        apellidos = fake.last_name()
        direccion = fake.address()
        foto = fake.image_url()
        codigo_institucional = random.randint(10000000,99999999)
        usuario_id = id 
        sexo_id = random.randint(1,5)
        correo = str(codigo_institucional) + '@aloe.ulima.edu.pe'
        telefono = fake.phone_number()
        dni = random.randint(70000000,79999999)
        tmp = f"INSERT INTO estudiantes (id, nombre, apellidos, direccion, foto, codigo_institucional, usuario_id, sexo_id, correo, telefono, dni) VALUES ({id}, '{nombre}', '{apellidos}', '{direccion}', '{foto}', {codigo_institucional}, {id_usuario}, {sexo_id}, '{correo}', '{telefono}', {dni});\n"
        contenido= contenido+tmp
        i = i + 1
    with open('inserts_estudiantes.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

estudiantes_por_seccion = {}

def llenar_estudiantes_secciones():
    count_estudiantes = 1000
    count_secciones = 100
    i = 0
    contenido = ''
    id = 1
    while i < count_secciones:
        n_estudiantes = random.randint(10, 30)
        k = 0
        lista_estudiantes_ids = []
        while k < n_estudiantes:
            tmp = random.randint(1, count_estudiantes)
            if tmp not in lista_estudiantes_ids:
                lista_estudiantes_ids.append(tmp)
            k += 1
        estudiantes_por_seccion[i + 1] = lista_estudiantes_ids
        for estudiante_id in lista_estudiantes_ids:
            seccion_id = i + 1
            tmp = f"INSERT INTO estudiantes_secciones (id, estudiante_id, seccion_id) VALUES ({id}, {estudiante_id}, {seccion_id});\n"
            contenido += tmp
            id += 1
        i += 1
    with open('inserts_estudiantes_secciones.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)



def llenar_estudiantes_seccion_grupo():
    count_estudiantes_seccion = 1000
    count_grupos = 100
    i = 0
    contenido = ''
    id = 1
    while i < count_grupos:
        seccion_id = (i % len(estudiantes_por_seccion)) + 1
        n_estudiantes = 5  
        k = 0
        lista_estudiantes_seccion_ids = []
        estudiantes_disponibles = estudiantes_por_seccion[seccion_id]
        while k < n_estudiantes:
            tmp = random.choice(estudiantes_disponibles)
            if tmp not in lista_estudiantes_seccion_ids:
                lista_estudiantes_seccion_ids.append(tmp)
            k += 1
        for estudiante_seccion_id in lista_estudiantes_seccion_ids:
            grupo_id = i + 1
            tmp = f"INSERT INTO estudiantes_seccion_grupo (id, estudiante_seccion_id,grupo_id) VALUES ({id},{estudiante_seccion_id},  {grupo_id});\n"
            contenido += tmp
            id += 1
        i += 1
    with open('inserts_estudiantes_secciones_grupo.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)


def llenar_calificaciones_grupales():
    count_estudiantes_seccion_grupo= 100
    count_actividades = len(idactividadesgrupales)-1
    i = 0
    contenido = ''
    id = 1
    while i < count_actividades:
        n_estudiantes = 4
        k = 0
        lista_estudiantes_seccion_grupo_ids = []
        while k < n_estudiantes:
            tmp = random.randint(1, count_estudiantes_seccion_grupo)
            if tmp not in lista_estudiantes_seccion_grupo_ids:
                lista_estudiantes_seccion_grupo_ids.append(tmp)
            k += 1
        for estudiante_seccion_grupo_id in lista_estudiantes_seccion_grupo_ids:
            actividad_id = idactividadesgrupales[i]
            nota = random.randint(0, 20)
            tmp = f"INSERT INTO calificaciones_grupales (id, estudiante_seccion_grupo_id, actividad_id, nota) VALUES ({id}, {estudiante_seccion_grupo_id}, {actividad_id}, {nota});\n"
            contenido += tmp
            id += 1
        i += 1
    with open('inserts_calificaciones_grupales.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)
        
def llenar_calificaciones_individuales():
    count_estudiantes_seccion= 1000
    count_actividades = len(idactividadesindividuales)
    i = 0
    contenido = ''
    id = 1
    while i < count_actividades:
        n_estudiantes = random.randint(1, 1)
        k = 0
        lista_estudiantes_seccion_ids = []
        while k < n_estudiantes:
            tmp = random.randint(1, count_estudiantes_seccion)
            if tmp not in lista_estudiantes_seccion_ids:
                lista_estudiantes_seccion_ids.append(tmp)
            k += 1
        for estudiante_seccion_id in lista_estudiantes_seccion_ids:
            actividad_id = idactividadesgrupales[i]
            nota = random.randint(0, 20)
            tmp = f"INSERT INTO calificaciones_individuales (id, estudiante_seccion_id, actividad_id, nota) VALUES ({id}, {estudiante_seccion_id}, {actividad_id}, {nota});\n"
            contenido += tmp
            id += 1
        i += 1
    with open('inserts_calificaciones_individuales.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def llenar_anuncios():
    i = 0
    contenido = ''
    while i < 100:
        id = 1 +i
        autor = fake.name_nonbinary()
        redacto = fake.sentence()
        seccion_id = random.randint(1,100)
        fecha = fake.date_time_between(start_date=periodosinicioporseccion[seccion_id+1], end_date=periodosfinalporseccion[seccion_id+1])
        tmp = f"INSERT INTO anuncios (id, autor, fecha, contenido, seccion_id) VALUES ({id}, '{autor}', '{fecha}', '{redacto}', {seccion_id});\n"
        contenido= contenido+tmp
        i = i + 1
    with open('inserts_anuncios.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def llenar_mensajes():
    id = 0
    contenido = ''
    while id < 100:
        id += 1
        remitente_id = random.randint(1, 100)
        redacto = fake.paragraph()
        fecha_envio = fake.date_time_between(start_date=datetime(2020, 1, 1), end_date='now')
        seccion_id = random.randint(1, 100)
        tmp = f"INSERT INTO mensajes (id, remitente_id, redacto, fecha_envio, seccion_id) VALUES ({id}, {remitente_id}, '{redacto}', '{fecha_envio}', {seccion_id});\n"
        contenido += tmp
    with open('inserts_mensajes.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)
    
def llenar_destinatarios_mensajes():
    count_mensajes = 100
    count_estudiantes = 400
    i = 0
    contenido = ''
    id = 1
    while i < count_mensajes:
        n_estudiantes = random.randint(1, 4)
        k = 0
        lista_estudiantes_ids = []
        while k < n_estudiantes:
            tmp = random.randint(1, count_estudiantes)
            if tmp not in lista_estudiantes_ids:
                lista_estudiantes_ids.append(tmp)
            k += 1
        for estudiante_id in lista_estudiantes_ids:
            mensaje_id = i + 1
            tmp = f"INSERT INTO destinatarios_mensajes (id, mensaje_id, estudiante_id) VALUES ({id}, {mensaje_id}, {estudiante_id});\n"
            contenido += tmp
            id += 1
        i += 1
    with open('inserts_destinatarios_mensajes.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def llenar_contenidos_curso():
    id = 0
    contenido = ''
    while id < 100:
        id = id + 1
        seccion_id = random.randint(1, 100)
        
        zoom = "https://zoom.us/join?confno=" + str(random.randint(1000000000, 9999999999))
        tmp = f"INSERT INTO contenidos_curso (id, seccion_id, zoom) VALUES ({id}, {seccion_id}, '{zoom}');\n"
        contenido += tmp
    with open('inserts_contenidos_curso.sql', 'w', encoding='utf-8') as archivo:    
        archivo.write(contenido)

def llenar_informacion_recursos_comunes():
    i = 0
    id = 0
    contenido = ''
    while i < 100:
        id = id + 1
        nombre = fake.sentence()
        silabo = fake.bs()
        descripcion = fake.paragraph()
        curso_id = random.randint(1, 20)
        tmp = f"INSERT INTO informacion_recursos_comunes (id, nombre, silabo, descripcion, curso_id) VALUES ({id}, '{nombre}', '{silabo}', '{descripcion}', {curso_id});\n"
        contenido =contenido + tmp
        i = i + 1
    with open('inserts_informacion_recursos_comunes.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def llenar_documentos():
    id = 0
    contenido = ''
    while id < 100:
        id = id + 1
        fecha_publicacion = fake.date_time_between(start_date=datetime(2020, 1, 1), end_date='now')
        contenidos_curso_id = random.randint(1, 100)
        informacion_recursos_comunes_id = random.randint(1, 100)
        tmp = f"INSERT INTO documentos (id, fecha_publicacion, contenidos_curso_id, informacion_recursos_comunes_id) VALUES ({id}, '{fecha_publicacion}', {contenidos_curso_id}, {informacion_recursos_comunes_id});\n"
        contenido += tmp
    with open('inserts_documentos.sql', 'w', encoding='utf-8') as archivo:    
        archivo.write(contenido)


def llenar_estudiantes_organizaciones():
    count_estudiantes = 700
    count_organizaciones = 100
    i = 0  
    contenido = ''
    id = 1
    while i < count_organizaciones:
        n_estudiantes = random.randint(2, 5)
        k = 0
        lista_estudiantes_ids = []
        while k < n_estudiantes:
            tmp = random.randint(1, count_estudiantes)
            if tmp not in lista_estudiantes_ids:
                lista_estudiantes_ids.append(tmp)
            k += 1
        for estudiante_id in lista_estudiantes_ids:
            organizacion_id = i + 1
            tmp = f"INSERT INTO estudiantes_organizaciones (id, estudiante_id, organizacion_id) VALUES ({id}, {estudiante_id}, {organizacion_id});\n"
            contenido += tmp
            id += 1
        i += 1
    with open('inserts_estudiantes_organizaciones.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

#llenar_sexos()
#llenar_usuarios()
#llenar_cursos()
#llenar_periodos()
#llenar_profesores()
#llenar_secciones()
#llenar_grupos()
#llenar_organizaciones()
#llenar_actividades()
#llenar_estudiantes()
#llenar_estudiantes_secciones()
#llenar_estudiantes_seccion_grupo()
#llenar_calificaciones()
#llenar_anuncios()
#llenar_mensajes()
#llenar_destinatarios_mensajes()
#llenar_contenidos_curso()
#llenar_informacion_recursos_comunes()
#llenar_documentos()
llenar_estudiantes_organizaciones()

