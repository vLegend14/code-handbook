#!/usr/bin/env python3

import os
import sys
import time
import array


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
    titulo("ARREGLOS EN PYTHON")

    print("En muchos lenguajes los arreglos son la estructura")
    print("principal para guardar colecciones de datos.\n")

    print("En Python ese rol lo cumplen las listas.")
    print("Sin embargo, Python también tiene un módulo 'array'")
    print("para casos donde se necesita más control y eficiencia.")

    pausa()
    limpiar()

    titulo("LISTAS VS ARREGLOS")

    print("""
┌──────────────────┬───────────────────────┬───────────────────────┐
│                  │  list                 │  array                │
├──────────────────┼───────────────────────┼───────────────────────┤
│  Tipos de dato   │  cualquier mezcla     │  un solo tipo         │
│  Memoria         │  más                  │  menos                │
│  Velocidad       │  uso general          │  mejor en numéricos   │
│  Flexibilidad    │  muy alta             │  limitada             │
│  Uso común       │  siempre              │  datos numéricos      │
└──────────────────┴───────────────────────┴───────────────────────┘

En la mayoría de casos las listas son suficientes.
Los arreglos se usan cuando se trabaja con muchos
números y se necesita eficiencia en memoria.
""")

    pausa()
    limpiar()

    titulo("EL MÓDULO ARRAY")

    print("Para usar arreglos se importa el módulo 'array'.\n")

    codigo("""
import array
""")

    print("Cada arreglo solo puede contener un tipo de dato.")
    print("Al crearlo se especifica con un código de tipo.\n")

    print("""
┌────────┬───────────────────────────────┐
│  'i'   │  enteros                      │
│  'f'   │  decimales (float)            │
│  'd'   │  decimales doble precisión    │
│  'u'   │  caracteres unicode           │
└────────┴───────────────────────────────┘
""")

    pausa()
    limpiar()

    titulo("CREAR UN ARREGLO")

    codigo("""
import array

numeros = array.array('i', [1, 2, 3, 4, 5])

print(numeros)
""")

    salida()

    numeros = array.array('i', [1, 2, 3, 4, 5])

    print(numeros)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("'i' indica que el arreglo solo acepta enteros.")
    print("El segundo argumento es la lista de valores iniciales.")
    print("\nSi intentas agregar un tipo distinto, Python lanza un error.")

    pausa()
    limpiar()

    titulo("ACCEDER A ELEMENTOS")

    print("Se accede igual que en las listas, con índices.\n")

    codigo("""
numeros = array.array('i', [10, 20, 30, 40])

print(numeros[0])
print(numeros[-1])
""")

    salida()

    numeros = array.array('i', [10, 20, 30, 40])

    print(numeros[0])
    time.sleep(0.3)
    print(numeros[-1])

    pausa()
    limpiar()

    titulo("AGREGAR Y ELIMINAR ELEMENTOS")

    codigo("""
numeros = array.array('i', [1, 2, 3])

numeros.append(4)
numeros.remove(2)

print(numeros)
""")

    salida()

    numeros = array.array('i', [1, 2, 3])

    numeros.append(4)
    numeros.remove(2)

    print(numeros)

    pausa()
    limpiar()

    titulo("RECORRER UN ARREGLO")

    print("Se recorre igual que una lista con for.\n")

    codigo("""
numeros = array.array('i', [10, 20, 30, 40, 50])

for n in numeros:
    print(n)
""")

    salida()

    numeros = array.array('i', [10, 20, 30, 40, 50])

    for n in numeros:
        print(n)
        time.sleep(0.3)

    pausa()
    limpiar()

    titulo("CONVERTIR ENTRE LISTA Y ARREGLO")

    print("Se puede convertir fácilmente entre los dos tipos.\n")

    codigo("""
# lista a arreglo
lista = [1, 2, 3, 4, 5]
arreglo = array.array('i', lista)

# arreglo a lista
de_vuelta = list(arreglo)

print(arreglo)
print(de_vuelta)
""")

    salida()

    lista = [1, 2, 3, 4, 5]
    arreglo = array.array('i', lista)

    de_vuelta = list(arreglo)

    print(arreglo)
    time.sleep(0.3)
    print(de_vuelta)

    pausa()
    limpiar()

    titulo("ARREGLO DE DECIMALES")

    codigo("""
precios = array.array('f', [9.99, 14.50, 3.75])

for p in precios:
    print(f"${p:.2f}")
""")

    salida()

    precios = array.array('f', [9.99, 14.50, 3.75])

    for p in precios:
        print(f"${p:.2f}")
        time.sleep(0.3)

    pausa()
    limpiar()

    titulo("CUÁNDO USAR CADA UNO")

    print("""
Usa una lista cuando:

• los datos son de tipos distintos
• necesitas flexibilidad
• es un programa de uso general

Usa un arreglo cuando:

• todos los datos son del mismo tipo numérico
• trabajas con grandes cantidades de números
• el uso de memoria importa
""")

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea un arreglo de enteros con los números del 1 al 5.
Agrega el número 6 e imprime el arreglo.

Ejercicio 2
Crea un arreglo de decimales con tres precios.
Recórrelo e imprime cada precio con dos decimales.

Ejercicio 3
Convierte una lista de números a un arreglo
y luego conviértelo de vuelta a lista.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ diferencia entre lista y arreglo en Python")
    print("✓ importar el módulo array")
    print("✓ códigos de tipo: 'i', 'f', 'd'")
    print("✓ crear arreglos")
    print("✓ acceder, agregar y eliminar elementos")
    print("✓ recorrer arreglos con for")
    print("✓ convertir entre lista y arreglo")
    print("✓ cuándo usar lista y cuándo arreglo")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)
