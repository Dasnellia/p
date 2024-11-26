from faker import Faker
from datetime import datetime
import random

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

def llenar_clientes():
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

def llenar_facturas():
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
def llenar_facturas_productos():
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
llenar_facturas_productos()
#llenar_facturas()
print(fake.passport_gender())