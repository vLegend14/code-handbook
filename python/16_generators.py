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
    titulo("GENERADORES EN PYTHON")

    print("Los generadores producen valores de uno en uno.")
    print("No guardan todos los valores en memoria a la vez.\n")

    print("Son útiles cuando:\n")
    print("• la secuencia es muy larga o infinita")
    print("• solo se necesita un valor a la vez")
    print("• se quiere ahorrar memoria")

    pausa()
    limpiar()

    titulo("LISTAS VS GENERADORES")

    print("""
┌────────────────┬──────────────────────────────────────────┐
│  Lista         │  guarda todos los elementos en memoria   │
│  Generador     │  produce un elemento a la vez            │
└────────────────┴──────────────────────────────────────────┘

Una lista con un millón de números ocupa mucha memoria.
Un generador solo tiene en memoria el número actual.
""")

    pausa()
    limpiar()

    titulo("CREAR UN GENERADOR CON YIELD")

    print("Una función generadora usa 'yield' en lugar de 'return'.")
    print("yield entrega un valor y pausa la función.\n")

    codigo("""
def contar():
    yield 1
    yield 2
    yield 3

gen = contar()

print(next(gen))
print(next(gen))
print(next(gen))
""")

    salida()

    def contar():
        yield 1
        yield 2
        yield 3

    gen = contar()

    print(next(gen))
    time.sleep(0.3)
    print(next(gen))
    time.sleep(0.3)
    print(next(gen))

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("yield pausa la función y entrega el valor.")
    print("next() reanuda la función desde donde se pausó.")
    print("Cuando no hay más valores, lanza StopIteration.")

    pausa()
    limpiar()

    titulo("RECORRER UN GENERADOR CON FOR")

    print("Un generador se puede recorrer directamente con for.\n")

    codigo("""
def numeros(n):
    for i in range(n):
        yield i

for num in numeros(5):
    print(num)
""")

    salida()

    def numeros(n):
        for i in range(n):
            yield i

    for num in numeros(5):
        print(num)
        time.sleep(0.3)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("El for llama a next() automáticamente.")
    print("Cuando el generador se agota, el bucle termina.")

    pausa()
    limpiar()

    titulo("GENERADOR CON LÓGICA")

    print("Los generadores pueden tener condiciones y cálculos.\n")

    codigo("""
def pares(limite):
    for i in range(limite):
        if i % 2 == 0:
            yield i

for n in pares(10):
    print(n)
""")

    salida()

    def pares(limite):
        for i in range(limite):
            if i % 2 == 0:
                yield i

    for n in pares(10):
        print(n)
        time.sleep(0.2)

    pausa()
    limpiar()

    titulo("GENERATOR EXPRESSION")

    print("Al igual que las list comprehensions, existen")
    print("generator expressions usando paréntesis.\n")

    codigo("""
cuadrados = (n ** 2 for n in range(5))

for c in cuadrados:
    print(c)
""")

    salida()

    cuadrados = (n ** 2 for n in range(5))

    for c in cuadrados:
        print(c)
        time.sleep(0.3)

    pausa()
    limpiar()

    seccion("List comprehension vs Generator expression")

    print("""
┌──────────────────────────┬──────────────────────────────────┐
│  [n * 2 for n in lista]  │  crea toda la lista en memoria   │
│  (n * 2 for n in lista)  │  produce un valor a la vez       │
└──────────────────────────┴──────────────────────────────────┘

Si solo vas a recorrer la colección una vez,
un generador es más eficiente que una lista.
""")

    pausa()
    limpiar()

    titulo("GENERADOR INFINITO")

    print("Un generador puede producir valores sin límite.")
    print("Hay que controlar cuándo se detiene.\n")

    codigo("""
def contador():
    n = 0
    while True:
        yield n
        n += 1

gen = contador()

for _ in range(5):
    print(next(gen))
""")

    salida()

    def contador():
        n = 0
        while True:
            yield n
            n += 1

    gen = contador()

    for _ in range(5):
        print(next(gen))
        time.sleep(0.3)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("El generador nunca termina por sí solo.")
    print("El for con range(5) limita cuántos valores se toman.")
    print("\nEsto sería imposible de hacer con una lista normal.")

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea un generador que produzca
los números del 1 al 10 usando yield.

Ejercicio 2
Crea un generador que reciba un límite
y produzca los múltiplos de 3 hasta ese límite.

Ejercicio 3
Usa una generator expression para obtener
los cuadrados de los números del 1 al 8.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es un generador")
    print("✓ diferencia entre lista y generador")
    print("✓ usar yield en una función")
    print("✓ usar next() para avanzar")
    print("✓ recorrer generadores con for")
    print("✓ generator expressions")
    print("✓ generadores infinitos")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)

