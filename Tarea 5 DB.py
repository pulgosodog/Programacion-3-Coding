# Ejercicio #2
# Indica de qué forma se puede conectar una base de datos a una aplicación en Python, proporciona ejemplo.
# SQLite:
# SQLite es una base de datos ligera que se almacena en un solo archivo y es ideal para aplicaciones pequeñas y prototipos.
# No requiere instalación de servidor y se puede usar directamente con el módulo sqlite3 que está incluido en la biblioteca estándar de Python.

import sqlite3

def iniciar_sqlite():
    # Conectar a una base de datos (o crearla si no existe)
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()

    # Crear una tabla si no existe
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT)')

    # Insertar datos
    cursor.execute('INSERT INTO usuarios (nombre) VALUES (?)', ('Juan',))

    # Guardar (commit) y cerrar la conexión
    conn.commit()
    conn.close()


# PostgreSQL:
# PostgreSQL es un sistema de gestión de bases de datos relacional poderoso y de código abierto.
# Es ideal para aplicaciones web y sistemas de producción que requieren características avanzadas y escalabilidad.
# Para usarlo, se necesita instalar el paquete psycopg2: pip install psycopg2

import psycopg2

def iniciar_postgresql():
    # Conectar a la base de datos
    conn = psycopg2.connect(database="mi_db", user="usuario", password="contraseña", host="localhost", port="5432")
    cursor = conn.cursor()

    # Crear una tabla si no existe
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id SERIAL PRIMARY KEY, nombre VARCHAR(100))')

    # Insertar datos
    cursor.execute('INSERT INTO usuarios (nombre) VALUES (%s)', ('Juan',))

    # Guardar (commit) y cerrar la conexión
    conn.commit()
    conn.close()


# MySQL:
# MySQL es un sistema de gestión de bases de datos relacional muy usado en aplicaciones web.
# Es ideal para manejar grandes volúmenes de datos y se puede usar con el conector mysql-connector: pip install mysql-connector-python

import mysql.connector

def iniciar_mysql():
    # Conectar a la base de datos
    conn = mysql.connector.connect(user='usuario', password='contraseña', host='localhost', database='mi_db')
    cursor = conn.cursor()

    # Crear una tabla si no existe
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100))')

    # Insertar datos
    cursor.execute('INSERT INTO usuarios (nombre) VALUES (%s)', ('Juan',))

    # Guardar (commit) y cerrar la conexión
    conn.commit()
    conn.close()
match(input('''Escribe el numero aosicado a la funcion que quieres correr:
1.iniciar_sqlite
2.iniciar_postgresql
3.iniciar_mysql()
''')):
    case("1"):
        iniciar_sqlite()
    case('2'):
        iniciar_postgresql()
    case('3'):
        iniciar_mysql()
    case _:
        print("Ingresa un valor correcto")
