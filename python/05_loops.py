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
    titulo("BUCLES EN PYTHON")

    print("Los bucles permiten repetir código varias veces.")
    print("Son una de las herramientas más importantes en programación.\n")

    print("Python tiene principalmente dos tipos de bucles:\n")

    print("""
┌──────────┬─────────────────────────────────────────┐
│  for     │  Itera sobre una secuencia conocida     │
│  while   │  Repite mientras una condición sea True │
└──────────┴─────────────────────────────────────────┘
""")

    pausa()
    limpiar()

    titulo("¿PARA QUÉ SIRVEN LOS BUCLES?")

    print("Los bucles se usan cuando necesitas repetir algo.\n")

    print("Ejemplos comunes:\n")
    print("• recorrer listas")
    print("• procesar datos")
    print("• repetir cálculos")
    print("• automatizar tareas")
    print("• recorrer archivos")
    print("• iterar sobre caracteres de un texto")

    pausa()
    limpiar()

    titulo("BUCLE FOR")

    print("El bucle 'for' se usa para recorrer colecciones de datos.\n")

    print("Sintaxis básica:\n")

    codigo("""
for elemento in coleccion:
    hacer_algo()
""")

    pausa()
    limpiar()

    seccion("EJEMPLO: contar números")

    codigo("""
for i in range(5):
    print("Iteración:", i)
""")

    salida()

    for i in range(5):
        print("Iteración:", i)
        time.sleep(0.3)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("range(5) genera los números:")
    print("0 1 2 3 4")
    print("\nEl bucle se ejecuta una vez por cada número.")

    pausa()
    limpiar()

    titulo("RECORRER LISTAS")

    frutas = ["manzana", "plátano", "pera", "naranja"]

    print("Lista de frutas:")
    print(frutas)

    pausa()

    seccion("EJEMPLO")

    codigo("""
frutas = ["manzana", "plátano", "pera", "naranja"]

for fruta in frutas:
    print("fruta:", fruta)
""")

    salida()

    for fruta in frutas:
        print("fruta:", fruta)
        time.sleep(0.3)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("El bucle toma cada elemento de la lista.")
    print("En cada iteración la variable contiene un elemento distinto.")

    pausa()
    limpiar()

    seccion("Usando range()")

    print("""
range() genera una secuencia de números.

range(inicio, fin, paso)

inicio → donde comienza
fin    → límite (NO incluido)
paso   → cuánto avanza cada iteración

Ejemplos:

range(5)
→ 0 1 2 3 4

range(2, 6)
→ 2 3 4 5

range(0, 10, 2)
→ 0 2 4 6 8
""")

    pausa()
    limpiar()

    seccion("Ejemplo range(1, 6)")

    codigo("""
for i in range(1, 6):
    print(i)
""")

    salida()

    for i in range(1, 6):
        print(i)
        time.sleep(0.3)

    pausa()
    limpiar()

    seccion("range() — contador inverso")

    codigo("""
for i in range(5, 0, -1):
    print(i)
""")

    salida()

    for i in range(5, 0, -1):
        print(i)
        time.sleep(0.3)

    pausa()
    limpiar()

    seccion("Usando enumerate()")

    print("""
enumerate() permite recorrer una colección
obteniendo índice y valor al mismo tiempo.

Devuelve pares:

(indice, valor)
""")

    pausa()
    limpiar()

    seccion("enumerate() — índice automático")

    codigo("""
idiomas = ["Español", "Inglés", "Japonés"]

for i, lang in enumerate(idiomas):
    print(i, lang)
""")

    salida()

    idiomas = ["Español", "Inglés", "Japonés"]

    for i, lang in enumerate(idiomas):
        print(i, lang)
        time.sleep(0.3)

    pausa()
    limpiar()

    seccion("enumerate() — empezando desde 1")

    codigo("""
idiomas = ["Español", "Inglés", "Japonés"]

for i, lang in enumerate(idiomas, start=1):
    print(i, lang)
""")

    salida()

    for i, lang in enumerate(idiomas, start=1):
        print(i, lang)
        time.sleep(0.3)

    pausa()
    limpiar()

    seccion("Usando zip()")

    print("""
zip() combina varias colecciones elemento por elemento.

zip(coleccion1, coleccion2, ...)

coleccion1 → primera colección
coleccion2 → segunda colección
...        → se pueden añadir más colecciones

En cada iteración devuelve una tupla con los elementos
de cada colección en la misma posición.

Ejemplos:

nombres = ["José", "Gonzalo", "Ignacio"]
edades  = [20, 25, 30]

zip(nombres, edades)
→ (José", 20)
→ (Gonzalo", 25)
→ (Ignacio", 30)

Si las colecciones tienen distinto tamaño,
zip() se detiene cuando termina la más corta.
""")

    pausa()
    limpiar()

    seccion("zip() — iterar listas en paralelo")

    codigo("""
nombres = ["José", "Gonzalo", "Ignacio"]
notas   = [6.5, 3.0, 5.8]

for nombre, nota in zip(nombres, notas):
    estado = "✔ Aprobado" if nota >= 4 else "✘ Reprobado"
    print(f"{nombre} → {nota}  {estado}")
""")

    salida()

    nombres = ["José", "Gonzalo", "Ignacio"]
    notas = [6.5, 3.0, 5.8]

    for nombre, nota in zip(nombres, notas):

        estado = "✔ Aprobado" if nota >= 4 else "✘ Reprobado"

        print(f"{nombre} → {nota}  {estado}")
        time.sleep(0.3)

    pausa()
    limpiar()

    titulo("BUCLE WHILE")

    print("while ejecuta código mientras una condición sea verdadera.\n")

    print("Sintaxis básica:\n")

    codigo("""
while condición:
    hacer_algo()
""")

    pausa()
    limpiar()

    seccion("Ejemplo contador")
    codigo("""
    contador = 0

    while contador < 5:
        print("contador =", contador)
        contador += 1
""")

    salida()

    contador = 0

    while contador < 5:
        print("contador =", contador)
        contador += 1
        time.sleep(0.3)

    pausa()
    limpiar()

    titulo("CONTROL DE BUCLES")

    print("break   → termina el bucle")
    print("continue → salta a la siguiente iteración")

    pausa()
    limpiar()

    seccion("Ejemplo break")

    codigo("""
for i in range(10):

    if i == 5:
        print("Se detuvo el bucle")
        break

    print(i)
""")

    salida()

    for i in range(10):

        if i == 5:
            print("Se detuvo el bucle")
            break

        print(i)
        time.sleep(0.3)

    pausa()
    limpiar()

    seccion("Ejemplo continue")

    codigo("""
for i in range(5):

    if i == 2:
        continue

    print(i)
""")

    salida()

    for i in range(5):

        if i == 2:
            continue

        print(i)
        time.sleep(0.3)

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
    Practica lo que aprendiste resolviendo estos ejercicios.

    Ejercicio 1
    Imprime los números del 1 al 10 usando un bucle for.

    Ejercicio 2
    Crea una lista de nombres y recórrela con un for
    imprimiendo cada nombre.

    Ejercicio 3
    Usa un bucle while para contar desde 0 hasta 5.
    """)

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es un bucle")
    print("✓ cómo usar for")
    print("✓ cómo usar while")
    print("✓ range")
    print("✓ enumerate")
    print("✓ zip")
    print("✓ break y continue")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)