from faker import Faker
from datetime import datetime
import random
from datetime import timedelta

fake = Faker() # Faker fake = new Faker();

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
        nombre = fake.first_name()
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

gruposeccion = {}

def llenar_grupos():
    i = 0
    contenido = ''
    seccionyausadas = set()
    id = 0

    while i < 30:
        gruposporseccion = 4
        k = 0
        gruposparaseccion = []

        while k < gruposporseccion:
            gruposparaseccion.append(id + 1)
            id += 1
            k += 1

        # Asegurarse de que cada sección se use solo una vez
        seccion_id = random.randint(1, 100)
        while seccion_id in seccionyausadas:
            seccion_id = random.randint(1, 100)
        seccionyausadas.add(seccion_id)

        for grupoid in gruposparaseccion:
            codigo = random.randint(10000, 50000)
            nombre = fake.language_name()
            tmp = f"INSERT INTO grupos (id, codigo, nombre, seccion_id) VALUES ({grupoid}, {codigo}, '{nombre}', {seccion_id});\n"
            contenido += tmp

        # Asignar los grupos generados a la sección
        gruposeccion[seccion_id] = gruposparaseccion

        # Incrementar el contador fuera del bucle `for`
        i += 1

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

actividadesporseccion = {}

def llenar_actividades():
    count_secciones = 100
    i = 0
    contenido = ''
    actividadesyausadas = set()
    id = 0
    while i < count_secciones:
        cantidadactivdadporseccion = 4
        k = 0
        listaactividadesid = []
        while k < cantidadactivdadporseccion:
            tmp = random.randint(1, 400)
            while tmp in actividadesyausadas:
                tmp = random.randint(1, 400)
            actividadesyausadas.add(tmp)
            if tmp not in listaactividadesid:
                listaactividadesid.append(tmp)
            k += 1
        actividadesporseccion[i + 1] = listaactividadesid
        for actividad_id in listaactividadesid:
            seccion_id = i + 1
            nombre = fake.job()
            fecha_publicacion = fake.date_time_between(start_date=datetime(2020, 1, 1), end_date='now')
            fecha_entrega = fecha_publicacion + timedelta(days=15)
            detalles = fake.paragraph()
            tipo_id = random.randint(1, 2)
            if tipo_id == 2:
                idactividadesgrupales.append(actividad_id)
            else:
                idactividadesindividuales.append(actividad_id)
            tmp = f"INSERT INTO actividades (id, nombre, fecha_publicacion, fecha_entrega, detalles, tipo_id, seccion_id) VALUES ({actividad_id}, '{nombre}', '{fecha_publicacion}', '{fecha_entrega}', '{detalles}', {tipo_id}, {seccion_id});\n"
            contenido += tmp
        i += 1
    with open('inserts_actividades_secciones.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)


def llenar_estudiantes():
    i = 0
    contenido = ''
    while i < 1000:
        id = 1 +i
        nombre = fake.first_name()
        apellidos = fake.last_name()
        direccion = fake.address()
        foto = fake.image_url()
        codigo_institucional = random.randint(10000000,99999999)
        usuario_id = id 
        sexo_id = random.randint(1,5)
        correo = str(codigo_institucional) + '@aloe.ulima.edu.pe'
        telefono = fake.phone_number()
        dni = random.randint(70000000,79999999)
        tmp = f"INSERT INTO estudiantes (id, nombre, apellidos, direccion, foto, codigo_institucional, usuario_id, sexo_id, correo, telefono, dni) VALUES ({id}, '{nombre}', '{apellidos}', '{direccion}', '{foto}', {codigo_institucional}, {usuario_id}, {sexo_id}, '{correo}', '{telefono}', {dni});\n"
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
        lista_estudiantes_ids = []
        while len(lista_estudiantes_ids) < n_estudiantes:
            tmp = random.randint(1, count_estudiantes)
            if tmp not in lista_estudiantes_ids:
                lista_estudiantes_ids.append(tmp)
        listaestudianteseccion = []
        for estudiante_id in lista_estudiantes_ids:
            seccion_id = i + 1
            tmp = f"INSERT INTO estudiantes_secciones (id, estudiante_id, seccion_id) VALUES ({id}, {estudiante_id}, {seccion_id});\n"
            contenido += tmp
            listaestudianteseccion.append(id)
            id += 1
        estudiantes_por_seccion[seccion_id] = listaestudianteseccion
        i += 1
    with open('inserts_estudiantes_secciones.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)



estdiantes_por_grupo = {}


def llenar_estudiantes_seccion_grupo():
    count_seccioncongrupos = len(gruposeccion)
    contenido = ''
    id = 1
    secciones_usadas = set()

    for _ in range(count_seccioncongrupos):
        seccion_id = random.choice(list(gruposeccion.keys()))
        
        while seccion_id in secciones_usadas:
            seccion_id = random.choice(list(gruposeccion.keys()))
        
        secciones_usadas.add(seccion_id)
        gruposenlaseccion = gruposeccion[seccion_id]
        estudiantes_disponibles = estudiantes_por_seccion[seccion_id]

        for grupo_id in gruposenlaseccion:
            idestudiantesparaelgrupo = []
            
            while len(idestudiantesparaelgrupo) < 5:
                tmp = random.choice(estudiantes_disponibles)
                if tmp not in idestudiantesparaelgrupo:
                    idestudiantesparaelgrupo.append(tmp)
            ideestudiantesgruapl = []	

            for estudiante_seccion_id in idestudiantesparaelgrupo:
                tmp = f"INSERT INTO estudiantes_seccion_grupo (id, estudiante_seccion_id, grupo_id) VALUES ({id}, {estudiante_seccion_id}, {grupo_id});\n"
                contenido += tmp
                id += 1
                ideestudiantesgruapl.append(id)
            estdiantes_por_grupo[grupo_id] = ideestudiantesgruapl
        
    with open('inserts_estudiantes_secciones_grupo.sql', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def encontrar_llave_por_elemento(diccionario, elemento): 
    for clave, lista in diccionario.items():
        if elemento in lista:
            return clave 
    return None


def llenar_calificaciones_grupales():
    count_actividadesgrupales = 100
    count_actividades = 400
    contenido = ''
    id = 1
    i=0
    gruposyarellenos = []
    while i < 120:
        grupo_id = i+1
        gruposyarellenos.append(grupo_id)
        n_estudiantes = 4
        k = 0
        lista_estudiantes_seccion_grupo_ids = estdiantes_por_grupo[grupo_id]
        seccion_id = encontrar_llave_por_elemento(gruposeccion, grupo_id)
        actividadesdisponibles = actividadesporseccion[seccion_id]
        actividadesgrupalesseccion = [actividad for actividad in actividadesdisponibles if actividad in idactividadesgrupales]
        for actividad_id in actividadesgrupalesseccion: #4
            for estudiante_seccion_grupo_id in lista_estudiantes_seccion_grupo_ids: #4
                nota = random.randint(0, 20)
                tmp = f"INSERT INTO calificaciones_grupales (id, estudiante_seccion_grupo_id, actividad_id, nota) VALUES ({id}, {estudiante_seccion_grupo_id}, {actividad_id}, {nota});\n"
                contenido += tmp
                print(tmp)
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
        seccion_id = (i % len(estudiantes_por_seccion)) + 1
        estudiantes_disponibles = estudiantes_por_seccion[seccion_id]
        actividadesdisponibles = actividadesporseccion[seccion_id]
        actividadesindividualesseccion = [actividad for actividad in actividadesdisponibles if actividad in idactividadesindividuales] 
        for actividad_id in actividadesindividualesseccion:
            for estudiante_id in estudiantes_disponibles:
                nota = random.randint(0, 20)
                tmp = f"INSERT INTO calificaciones_individuales (id, estudiante_seccion_id, actividad_id, nota) VALUES ({id}, {estudiante_id}, {actividad_id}, {nota});\n"
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
        fecha = fake.date_time_between(start_date=datetime(2020, 1, 1), end_date='now')
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
        seccion_id = id
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
#llenar_actividades_tipo()


#llenar_calificaciones_grupales()
#llenar_calificaciones_individuales()

#llenar_anuncios()
#llenar_mensajes()
#llenar_destinatarios_mensajes()
llenar_contenidos_curso()
#llenar_informacion_recursos_comunes()
#llenar_documentos()
#llenar_estudiantes_organizaciones()

