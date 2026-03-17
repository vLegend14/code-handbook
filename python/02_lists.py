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
    titulo("LISTAS EN PYTHON")

    print("Las listas permiten guardar múltiples valores en una sola variable.\n")

    print("Son una de las estructuras más usadas en Python.")

    pausa()
    limpiar()

    titulo("CREAR UNA LISTA")

    print("Una lista se crea usando corchetes [].\n")

    codigo("""
frutas = ["manzana", "banana", "pera"]

print(frutas)
""")

    salida()

    frutas = ["manzana", "banana", "pera"]

    print(frutas)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("Cada elemento de la lista está separado por comas.")
    print("Una lista puede contener cualquier tipo de dato.")

    pausa()
    limpiar()

    titulo("ACCEDER A ELEMENTOS")

    print("Cada elemento tiene una posición llamada índice.\n")

    print("Los índices comienzan en 0.\n")

    codigo("""
frutas = ["manzana", "banana", "pera"]

print(frutas[0])
print(frutas[1])
""")

    salida()

    frutas = ["manzana", "banana", "pera"]

    print(frutas[0])
    print(frutas[1])

    pausa()
    limpiar()

    titulo("AGREGAR ELEMENTOS")

    print("Podemos agregar elementos con append().\n")

    codigo("""
frutas = ["manzana", "banana"]

frutas.append("naranja")

print(frutas)
""")

    salida()

    frutas = ["manzana", "banana"]

    frutas.append("naranja")

    print(frutas)

    pausa()
    limpiar()

    titulo("RECORRER UNA LISTA")

    print("Las listas se recorren comúnmente usando for.\n")

    codigo("""
frutas = ["manzana", "banana", "pera"]

for fruta in frutas:
    print(fruta)
""")

    salida()

    frutas = ["manzana", "banana", "pera"]

    for fruta in frutas:
        print(fruta)
        time.sleep(0.3)

    pausa()
    limpiar()

    titulo("LONGITUD DE UNA LISTA")

    print("Podemos saber cuántos elementos tiene una lista.\n")

    codigo("""
frutas = ["manzana", "banana", "pera"]

print(len(frutas))
""")

    salida()

    frutas = ["manzana", "banana", "pera"]

    print(len(frutas))

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea una lista con tres nombres.

Ejercicio 2
Imprime el primer elemento.

Ejercicio 3
Recorre la lista usando un bucle for.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es una lista")
    print("✓ cómo crear listas")
    print("✓ acceder a elementos")
    print("✓ agregar elementos")
    print("✓ recorrer listas")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)