#!/usr/bin/env python3

import os
import sys
import time


def limpiar():
    os.system("clear" if os.name == "posix" else "cls")


def pausa():
    try:
        input("\nPresiona ENTER para continuar...")
    except KeyboardInterrupt:
        print("\n\nInterrumpido por el usuario.")
        sys.exit(0)


def titulo(texto):
    print("\n" + "=" * 50)
    print(texto)
    print("=" * 50 + "\n")


def seccion(texto):
    print("\n" + "-" * 50)
    print(texto)
    print("-" * 50 + "\n")


def codigo(texto):
    print("Código:")
    print(texto)


def salida():
    print("Salida:")


try:

    limpiar()
    titulo("ARCHIVOS EN PYTHON")

    print("Python permite leer y escribir archivos del sistema.")
    print("Es una de las operaciones más comunes en programación.\n")

    print("Casos de uso frecuentes:\n")
    print("• leer configuraciones")
    print("• guardar resultados")
    print("• procesar datos de texto")
    print("• llevar registros o logs")

    pausa()
    limpiar()

    titulo("MODOS DE APERTURA")

    print("""
┌──────┬───────────────────────────────────────────────────┐
│  r   │  lectura (el archivo debe existir)                │
│  w   │  escritura (crea el archivo o lo sobreescribe)    │
│  a   │  agregar al final (no borra el contenido)         │
│  r+  │  lectura y escritura                              │
└──────┴───────────────────────────────────────────────────┘
""")

    pausa()
    limpiar()

    titulo("ESCRIBIR UN ARCHIVO")

    print("Se usa open() con el modo 'w' para escribir.\n")

    codigo("""
archivo = open("notas.txt", "w")
archivo.write("Primera línea\\n")
archivo.write("Segunda línea\\n")
archivo.close()
""")

    archivo = open("notas.txt", "w")
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")
    archivo.close()

    print("Archivo creado correctamente.")

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("open() abre o crea el archivo.")
    print("write() escribe texto en él.")
    print("close() cierra el archivo y guarda los cambios.")
    print("\nSiempre hay que cerrar el archivo después de usarlo.")

    pausa()
    limpiar()

    titulo("LEER UN ARCHIVO")

    print("Se usa open() con el modo 'r' para leer.\n")

    codigo("""
archivo = open("notas.txt", "r")
contenido = archivo.read()
archivo.close()

print(contenido)
""")

    salida()

    archivo = open("notas.txt", "r")
    contenido = archivo.read()
    archivo.close()

    print(contenido)

    pausa()
    limpiar()

    titulo("USO DE WITH")

    print("'with' cierra el archivo automáticamente.")
    print("Es la forma recomendada de trabajar con archivos.\n")

    codigo("""
with open("notas.txt", "r") as archivo:
    contenido = archivo.read()

print(contenido)
""")

    salida()

    with open("notas.txt", "r") as archivo:
        contenido = archivo.read()

    print(contenido)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("El bloque 'with' garantiza que el archivo se cierra")
    print("aunque ocurra un error dentro del bloque.")
    print("\nNo hace falta llamar a close() manualmente.")

    pausa()
    limpiar()

    titulo("LEER LÍNEA POR LÍNEA")

    print("Se puede recorrer el archivo como si fuera una lista.\n")

    codigo("""
with open("notas.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
""")

    salida()

    with open("notas.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())
            time.sleep(0.3)

    pausa()
    limpiar()

    seccion("readlines()")

    print("readlines() devuelve todas las líneas como una lista.\n")

    codigo("""
with open("notas.txt", "r") as archivo:
    lineas = archivo.readlines()

print(lineas)
""")

    salida()

    with open("notas.txt", "r") as archivo:
        lineas = archivo.readlines()

    print(lineas)

    pausa()
    limpiar()

    titulo("AGREGAR CONTENIDO")

    print("El modo 'a' agrega texto al final sin borrar lo anterior.\n")

    codigo("""
with open("notas.txt", "a") as archivo:
    archivo.write("Tercera línea\\n")

with open("notas.txt", "r") as archivo:
    print(archivo.read())
""")

    salida()

    with open("notas.txt", "a") as archivo:
        archivo.write("Tercera línea\n")

    with open("notas.txt", "r") as archivo:
        print(archivo.read())

    pausa()
    limpiar()

    titulo("VERIFICAR SI UN ARCHIVO EXISTE")

    print("Se puede comprobar si un archivo existe antes de abrirlo.\n")

    codigo("""
import os

if os.path.exists("notas.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")
""")

    salida()

    if os.path.exists("notas.txt"):
        print("El archivo existe")
    else:
        print("El archivo no existe")

    pausa()
    limpiar()

    titulo("MANEJAR ERRORES CON ARCHIVOS")

    print("Es buena práctica manejar errores al trabajar con archivos.\n")

    codigo("""
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error: el archivo no existe")
""")

    salida()

    try:
        with open("archivo_inexistente.txt", "r") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("Error: el archivo no existe")

    pausa()
    limpiar()

    # limpieza del archivo de ejemplo
    if os.path.exists("notas.txt"):
        os.remove("notas.txt")

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea un archivo llamado lista.txt
y escribe tres tareas pendientes, una por línea.

Ejercicio 2
Lee el archivo lista.txt e imprime
cada línea numerada.

Ejercicio 3
Agrega una tarea más al archivo usando
el modo 'a' y vuelve a leer el contenido.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ modos de apertura: r, w, a")
    print("✓ escribir archivos con write()")
    print("✓ leer archivos con read()")
    print("✓ usar with para abrir archivos")
    print("✓ leer línea por línea")
    print("✓ agregar contenido con modo a")
    print("✓ verificar si un archivo existe")
    print("✓ manejar errores con FileNotFoundError")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)
