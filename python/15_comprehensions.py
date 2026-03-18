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
    titulo("COMPREHENSIONS EN PYTHON")

    print("Las comprehensions son una forma compacta de crear colecciones.")
    print("Permiten reemplazar bucles for de una manera más directa.\n")

    print("Existen tres tipos:\n")
    print("• list comprehension   → crea listas")
    print("• dict comprehension   → crea diccionarios")
    print("• set comprehension    → crea conjuntos")

    pausa()
    limpiar()

    titulo("LIST COMPREHENSION")

    print("Sintaxis básica:\n")

    codigo("""
nueva_lista = [expresion for elemento in coleccion]
""")

    pausa()
    limpiar()

    seccion("Sin comprehension")

    codigo("""
numeros = [1, 2, 3, 4, 5]
dobles = []

for n in numeros:
    dobles.append(n * 2)

print(dobles)
""")

    salida()

    numeros = [1, 2, 3, 4, 5]
    dobles = []

    for n in numeros:
        dobles.append(n * 2)

    print(dobles)

    pausa()
    limpiar()

    seccion("Con list comprehension")

    codigo("""
numeros = [1, 2, 3, 4, 5]

dobles = [n * 2 for n in numeros]

print(dobles)
""")

    salida()

    numeros = [1, 2, 3, 4, 5]

    dobles = [n * 2 for n in numeros]

    print(dobles)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("Ambos ejemplos hacen exactamente lo mismo.")
    print("La comprehension es más corta y directa.\n")
    print("Se lee como:")
    print("'toma n de numeros y guarda n * 2'")

    pausa()
    limpiar()

    titulo("LIST COMPREHENSION CON CONDICIÓN")

    print("Se puede agregar un filtro con 'if' al final.\n")

    codigo("""
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

pares = [n for n in numeros if n % 2 == 0]

print(pares)
""")

    salida()

    numeros = [1, 2, 3, 4, 5, 6, 7, 8]

    pares = [n for n in numeros if n % 2 == 0]

    print(pares)

    pausa()
    limpiar()

    seccion("Otro ejemplo con condición")

    codigo("""
palabras = ["hola", "mundo", "python", "es", "genial"]

largas = [p for p in palabras if len(p) > 4]

print(largas)
""")

    salida()

    palabras = ["hola", "mundo", "python", "es", "genial"]

    largas = [p for p in palabras if len(p) > 4]

    print(largas)

    pausa()
    limpiar()

    titulo("LIST COMPREHENSION CON IF/ELSE")

    print("También se puede usar if/else dentro de la expresión.\n")

    codigo("""
numeros = [1, 2, 3, 4, 5]

resultado = ["par" if n % 2 == 0 else "impar" for n in numeros]

print(resultado)
""")

    salida()

    numeros = [1, 2, 3, 4, 5]

    resultado = ["par" if n % 2 == 0 else "impar" for n in numeros]

    print(resultado)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("""
┌────────────────────────────────────────────────────┐
│  [expresion for x in lista if condicion]           │
│   → filtra elementos de la colección               │
│                                                    │
│  [a if condicion else b for x in lista]            │
│   → transforma todos los elementos                 │
└────────────────────────────────────────────────────┘
""")

    pausa()
    limpiar()

    titulo("DICT COMPREHENSION")

    print("Crea un diccionario a partir de una colección.\n")

    codigo("""
nombres = ["José", "Gonzalo", "Ignacio"]

longitudes = {nombre: len(nombre) for nombre in nombres}

print(longitudes)
""")

    salida()

    nombres = ["José", "Gonzalo", "Ignacio"]

    longitudes = {nombre: len(nombre) for nombre in nombres}

    print(longitudes)

    pausa()
    limpiar()

    seccion("Otro ejemplo")

    codigo("""
precios = {"manzana": 500, "pera": 800, "uva": 1200}

caros = {k: v for k, v in precios.items() if v > 600}

print(caros)
""")

    salida()

    precios = {"manzana": 500, "pera": 800, "uva": 1200}

    caros = {k: v for k, v in precios.items() if v > 600}

    print(caros)

    pausa()
    limpiar()

    titulo("SET COMPREHENSION")

    print("Crea un conjunto sin elementos duplicados.\n")

    codigo("""
numeros = [1, 2, 2, 3, 3, 3, 4]

unicos = {n for n in numeros}

print(unicos)
""")

    salida()

    numeros = [1, 2, 2, 3, 3, 3, 4]

    unicos = {n for n in numeros}

    print(unicos)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("Un set no guarda duplicados.")
    print("El orden puede variar, los sets no son ordenados.")
    print("\nEs útil para eliminar repetidos de una colección.")

    pausa()
    limpiar()

    titulo("RESUMEN DE SINTAXIS")

    print("""
┌─────────────────────┬─────────────────────────────────────────┐
│  list comprehension │  [expr for x in col if cond]            │
│  dict comprehension │  {k: v for k, v in col if cond}         │
│  set comprehension  │  {expr for x in col if cond}            │
└─────────────────────┴─────────────────────────────────────────┘
""")

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea una lista con los cuadrados
de los números del 1 al 10.

Ejercicio 2
Filtra una lista de números
y quédate solo con los mayores a 5.

Ejercicio 3
Crea un diccionario donde la clave sea un número
del 1 al 5 y el valor sea su cuadrado.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es una comprehension")
    print("✓ list comprehension básica")
    print("✓ list comprehension con condición")
    print("✓ list comprehension con if/else")
    print("✓ dict comprehension")
    print("✓ set comprehension")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)

