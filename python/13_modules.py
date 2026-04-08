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
    titulo("MÓDULOS EN PYTHON")

    print("Un módulo es un archivo .py que contiene código reutilizable.")
    print("Permite organizar el programa en partes separadas.\n")

    print("Ventajas:\n")
    print("• evitar tener todo el código en un solo archivo")
    print("• reutilizar funciones en distintos programas")
    print("• usar código escrito por otros")

    pausa()
    limpiar()

    titulo("IMPORTAR UN MÓDULO")

    print("Se usa 'import' para cargar un módulo.\n")

    codigo("""
import math

print(math.pi)
print(math.sqrt(16))
""")

    salida()

    import math

    print(math.pi)
    time.sleep(0.3)
    print(math.sqrt(16))

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("math es un módulo de la librería estándar de Python.")
    print("Se accede a sus funciones con math.nombre_funcion()")

    pausa()
    limpiar()

    titulo("IMPORTAR CON FROM")

    print("Se puede importar solo lo que se necesita.\n")

    codigo("""
from math import pi, sqrt

print(pi)
print(sqrt(25))
""")

    salida()

    from math import pi, sqrt

    print(pi)
    time.sleep(0.3)
    print(sqrt(25))

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("Con 'from' se importa directamente el nombre.")
    print("No hace falta escribir math. antes de cada uso.")

    pausa()
    limpiar()

    titulo("IMPORTAR CON ALIAS")

    print("Se puede dar un nombre corto a un módulo con 'as'.\n")

    codigo("""
import math as m

print(m.pi)
print(m.floor(3.7))
""")

    salida()

    import math as m

    print(m.pi)
    time.sleep(0.3)
    print(m.floor(3.7))

    pausa()
    limpiar()

    titulo("MÓDULOS DE LA LIBRERÍA ESTÁNDAR")

    print("""
Python incluye muchos módulos listos para usar:

┌────────────┬──────────────────────────────────────────┐
│  math      │  operaciones matemáticas                 │
│  os        │  interactuar con el sistema operativo    │
│  sys       │  información del intérprete              │
│  random    │  generación de números aleatorios        │
│  datetime  │  manejo de fechas y horas                │
│  time      │  funciones de tiempo                     │
│  json      │  leer y escribir JSON                    │
└────────────┴──────────────────────────────────────────┘
""")

    pausa()
    limpiar()

    seccion("Ejemplo: random")

    codigo("""
import random

print(random.randint(1, 10))
print(random.choice(["rojo", "verde", "azul"]))
""")

    salida()

    import random

    print(random.randint(1, 10))
    time.sleep(0.3)
    print(random.choice(["rojo", "verde", "azul"]))

    pausa()
    limpiar()

    seccion("Ejemplo: datetime")

    codigo("""
from datetime import datetime

ahora = datetime.now()

print(ahora)
print(ahora.year)
print(ahora.strftime("%d/%m/%Y"))
""")

    salida()

    from datetime import datetime

    ahora = datetime.now()

    print(ahora)
    time.sleep(0.3)
    print(ahora.year)
    time.sleep(0.3)
    print(ahora.strftime("%d/%m/%Y"))

    pausa()
    limpiar()

    seccion("Ejemplo: os")

    codigo("""
import os

print(os.getcwd())
print(os.name)
""")

    salida()

    print(os.getcwd())
    time.sleep(0.3)
    print(os.name)

    pausa()
    limpiar()

    titulo("CREAR TU PROPIO MÓDULO")

    print("Cualquier archivo .py puede usarse como módulo.\n")

    codigo("""
# archivo: saludos.py

def hola(nombre):
    print(f"Hola, {nombre}")

def adios(nombre):
    print(f"Hasta luego, {nombre}")
""")

    print("\nDesde otro archivo:")

    codigo("""
import saludos

saludos.hola("José")
saludos.adios("José")
""")

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("El archivo saludos.py se convierte en un módulo.")
    print("Se importa usando su nombre sin la extensión .py")
    print("\nAmbos archivos deben estar en la misma carpeta.")

    pausa()
    limpiar()

    titulo("EL BLOQUE __main__")

    print("Cada archivo Python tiene una variable especial: __name__")
    print("\nSi el archivo se ejecuta directamente su valor es '__main__'.")
    print("Si se importa como módulo su valor es el nombre del archivo.\n")

    codigo("""
def saludar():
    print("Hola desde el módulo")

if __name__ == "__main__":
    saludar()
""")

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("El bloque if __name__ == '__main__' permite")
    print("que el código dentro solo se ejecute cuando")
    print("el archivo se corre directamente.")
    print("\nSi se importa desde otro archivo, ese bloque se ignora.")
    print("\nEs una buena práctica incluirlo en todos tus módulos.")

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Usa el módulo random para simular
el lanzamiento de un dado (número entre 1 y 6).

Ejercicio 2
Usa datetime para imprimir
el día, mes y año actuales por separado.

Ejercicio 3
Crea un archivo operaciones.py con funciones
sumar(), restar() y multiplicar().
Impórtalo desde otro archivo y úsalas.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es un módulo")
    print("✓ importar con import")
    print("✓ importar con from")
    print("✓ usar alias con as")
    print("✓ módulos de la librería estándar")
    print("✓ crear tus propios módulos")
    print("✓ el bloque if __name__ == '__main__'")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)
