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
    titulo("TUPLAS Y SETS EN PYTHON")

    print("Python tiene cuatro colecciones nativas principales:\n")

    print("""
┌────────────────┬──────────────┬───────────────┬────────────┐
│  Colección     │  Ordenada    │  Duplicados   │  Mutable   │
├────────────────┼──────────────┼───────────────┼────────────┤
│  list []       │  sí          │  sí           │  sí        │
│  tuple ()      │  sí          │  sí           │  no        │
│  set {}        │  no          │  no           │  sí        │
│  dict {}       │  sí          │  claves: no   │  sí        │
└────────────────┴──────────────┴───────────────┴────────────┘
""")

    print("En esta lección veremos tuplas y sets.")

    pausa()
    limpiar()

    titulo("TUPLAS")

    print("Una tupla es como una lista pero inmutable.")
    print("Una vez creada, no se puede modificar.\n")

    print("Se usa cuando los datos no deben cambiar:\n")
    print("• coordenadas")
    print("• días de la semana")
    print("• colores RGB")

    pausa()
    limpiar()

    titulo("CREAR UNA TUPLA")

    print("Las tuplas se crean con paréntesis ().\n")

    codigo("""
colores = ("rojo", "verde", "azul")

print(colores)
""")

    salida()

    colores = ("rojo", "verde", "azul")

    print(colores)

    pausa()
    limpiar()

    seccion("Tupla de un solo elemento")

    print("Para crear una tupla con un solo elemento")
    print("se necesita una coma al final.\n")

    codigo("""
solo = ("Python",)

print(solo)
print(type(solo))
""")

    salida()

    solo = ("Python",)

    print(solo)
    time.sleep(0.3)
    print(type(solo))

    pausa()
    limpiar()

    titulo("ACCEDER A ELEMENTOS")

    print("Se accede igual que en las listas, con índices.\n")

    codigo("""
colores = ("rojo", "verde", "azul")

print(colores[0])
print(colores[-1])
""")

    salida()

    colores = ("rojo", "verde", "azul")

    print(colores[0])
    time.sleep(0.3)
    print(colores[-1])

    pausa()
    limpiar()

    titulo("TUPLAS SON INMUTABLES")

    print("No se puede cambiar, agregar ni eliminar elementos.\n")

    codigo("""
colores = ("rojo", "verde", "azul")

colores[0] = "amarillo"
""")

    salida()

    try:
        colores = ("rojo", "verde", "azul")
        colores[0] = "amarillo"
    except TypeError as e:
        print(f"Error: {e}")

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("Las tuplas protegen datos que no deben cambiar.")
    print("Si intentas modificarlas, Python lanza un TypeError.")

    pausa()
    limpiar()

    titulo("DESEMPAQUETAR TUPLAS")

    print("Se pueden asignar los valores de una tupla")
    print("a varias variables a la vez.\n")

    codigo("""
coordenada = (10, 25)

x, y = coordenada

print(f"x = {x}")
print(f"y = {y}")
""")

    salida()

    coordenada = (10, 25)

    x, y = coordenada

    print(f"x = {x}")
    time.sleep(0.3)
    print(f"y = {y}")

    pausa()
    limpiar()

    seccion("Otro ejemplo")

    codigo("""
persona = ("José", 20, "Santiago")

nombre, edad, ciudad = persona

print(nombre)
print(edad)
print(ciudad)
""")

    salida()

    persona = ("José", 20, "Santiago")

    nombre, edad, ciudad = persona

    print(nombre)
    time.sleep(0.3)
    print(edad)
    time.sleep(0.3)
    print(ciudad)

    pausa()
    limpiar()

    titulo("SETS")

    print("Un set es una colección sin duplicados y sin orden fijo.")
    print("Es útil cuando solo importa si un elemento está o no.\n")

    print("Se usa para:\n")
    print("• eliminar duplicados de una lista")
    print("• verificar pertenencia rápidamente")
    print("• operaciones matemáticas de conjuntos")

    pausa()
    limpiar()

    titulo("CREAR UN SET")

    print("Los sets se crean con llaves {} o con set().\n")

    codigo("""
numeros = {1, 2, 3, 4, 5}

print(numeros)
""")

    salida()

    numeros = {1, 2, 3, 4, 5}

    print(numeros)

    pausa()
    limpiar()

    seccion("Eliminar duplicados")

    codigo("""
repetidos = [1, 2, 2, 3, 3, 3, 4]

unicos = set(repetidos)

print(unicos)
""")

    salida()

    repetidos = [1, 2, 2, 3, 3, 3, 4]

    unicos = set(repetidos)

    print(unicos)

    pausa()
    limpiar()

    titulo("AGREGAR Y ELIMINAR")

    codigo("""
frutas = {"manzana", "plátano"}

frutas.add("pera")
frutas.discard("plátano")

print(frutas)
""")

    salida()

    frutas = {"manzana", "plátano"}

    frutas.add("pera")
    frutas.discard("plátano")

    print(frutas)

    pausa()
    limpiar()

    titulo("OPERACIONES DE CONJUNTOS")

    print("""
┌──────────────────┬──────────────────────────────────────┐
│  union()         │  elementos de ambos sets             │
│  intersection()  │  elementos que están en los dos      │
│  difference()    │  elementos que están en uno y no en  │
│                  │  el otro                             │
└──────────────────┴──────────────────────────────────────┘
""")

    pausa()
    limpiar()

    seccion("Ejemplo operaciones")

    codigo("""
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
""")

    salida()

    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    print(a.union(b))
    time.sleep(0.3)
    print(a.intersection(b))
    time.sleep(0.3)
    print(a.difference(b))

    pausa()
    limpiar()

    titulo("VERIFICAR PERTENENCIA")

    print("Se usa 'in' para saber si un elemento está en el set.\n")

    codigo("""
frutas = {"manzana", "plátano", "pera"}

print("plátano" in frutas)
print("uva" in frutas)
""")

    salida()

    frutas = {"manzana", "plátano", "pera"}

    print("plátano" in frutas)
    time.sleep(0.3)
    print("uva" in frutas)

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea una tupla con los meses del año.
Imprime el primero y el último usando índices.

Ejercicio 2
Desempaqueta una tupla con nombre, edad y país
en tres variables separadas.

Ejercicio 3
Toma la lista [4, 2, 4, 1, 3, 2, 1]
y usa un set para eliminar los duplicados.

Ejercicio 4
Crea dos sets con números.
Imprime su intersección y su unión.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ diferencias entre list, tuple, set y dict")
    print("✓ crear y acceder a tuplas")
    print("✓ por qué las tuplas son inmutables")
    print("✓ desempaquetar tuplas")
    print("✓ crear y modificar sets")
    print("✓ eliminar duplicados con set()")
    print("✓ operaciones de conjuntos")
    print("✓ verificar pertenencia con in")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)
