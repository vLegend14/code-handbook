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
    titulo("TIPOS DE DATOS EN PYTHON")

    print("Todo valor en Python tiene un tipo de dato.")
    print("El tipo define qué clase de información representa")
    print("y qué operaciones se pueden hacer con ella.\n")

    print("Python tiene tipos de datos integrados:")

    print("""
┌──────────┬─────────────────────────────────────────┐
│  int     │  números enteros                        │
│  float   │  números con decimales                  │
│  str     │  texto                                  │
│  bool    │  verdadero o falso                      │
│  None    │  ausencia de valor                      │
└──────────┴─────────────────────────────────────────┘
""")

    pausa()
    limpiar()

    titulo("INT — NÚMEROS ENTEROS")

    print("Los enteros son números sin parte decimal.")
    print("Pueden ser positivos, negativos o cero.\n")

    codigo("""
edad = 25
temperatura = -3
cero = 0

print(edad)
print(temperatura)
print(cero)
""")

    salida()

    edad = 25
    temperatura = -3
    cero = 0

    print(edad)
    time.sleep(0.3)
    print(temperatura)
    time.sleep(0.3)
    print(cero)

    pausa()
    limpiar()

    seccion("Operaciones con int")

    codigo("""
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
""")

    salida()

    a = 10
    b = 3

    print(a + b)
    time.sleep(0.2)
    print(a - b)
    time.sleep(0.2)
    print(a * b)
    time.sleep(0.2)
    print(a // b)
    time.sleep(0.2)
    print(a % b)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("""
┌──────┬─────────────────────────────────┐
│  +   │  suma                           │
│  -   │  resta                          │
│  *   │  multiplicación                 │
│  //  │  división entera (sin decimal)  │
│  %   │  módulo (resto de la división)  │
│  **  │  potencia                       │
└──────┴─────────────────────────────────┘
""")

    pausa()
    limpiar()

    titulo("FLOAT — NÚMEROS DECIMALES")

    print("Los float son números con parte decimal.")
    print("Se escriben con punto, no con coma.\n")

    codigo("""
precio = 9.99
pi = 3.14159
negativo = -0.5

print(precio)
print(pi)
print(negativo)
""")

    salida()

    precio = 9.99
    pi = 3.14159
    negativo = -0.5

    print(precio)
    time.sleep(0.3)
    print(pi)
    time.sleep(0.3)
    print(negativo)

    pausa()
    limpiar()

    seccion("División y float")

    print("La división con '/' siempre devuelve un float.\n")

    codigo("""
print(10 / 2)
print(7 / 2)
""")

    salida()

    print(10 / 2)
    time.sleep(0.3)
    print(7 / 2)

    pausa()
    limpiar()

    seccion("Redondear decimales")

    codigo("""
numero = 3.14159

print(round(numero, 2))
""")

    salida()

    print(round(3.14159, 2))

    pausa()
    limpiar()

    titulo("STR — TEXTO")

    print("Los strings guardan texto.")
    print("Se escriben entre comillas simples o dobles.\n")

    codigo("""
nombre = "José"
mensaje = 'Hola mundo'

print(nombre)
print(mensaje)
""")

    salida()

    nombre = "José"
    mensaje = 'Hola mundo'

    print(nombre)
    time.sleep(0.3)
    print(mensaje)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("En Python no existe el tipo 'char' de otros lenguajes.")
    print("Un carácter solo es un str de longitud 1.\n")

    codigo("""
letra = "A"

print(letra)
print(type(letra))
print(len(letra))
""")

    salida()

    letra = "A"

    print(letra)
    time.sleep(0.3)
    print(type(letra))
    time.sleep(0.3)
    print(len(letra))

    pausa()
    limpiar()

    titulo("BOOL — VERDADERO O FALSO")

    print("Los booleanos solo tienen dos valores posibles:")
    print("True o False.\n")

    print("Se usan para representar condiciones y estados.\n")

    codigo("""
activo = True
terminado = False

print(activo)
print(terminado)
""")

    salida()

    activo = True
    terminado = False

    print(activo)
    time.sleep(0.3)
    print(terminado)

    pausa()
    limpiar()

    seccion("Comparaciones producen bool")

    print("Cualquier comparación devuelve un bool.\n")

    codigo("""
print(5 > 3)
print(10 == 10)
print(7 < 2)
""")

    salida()

    print(5 > 3)
    time.sleep(0.3)
    print(10 == 10)
    time.sleep(0.3)
    print(7 < 2)

    pausa()
    limpiar()

    titulo("NONE — AUSENCIA DE VALOR")

    print("None representa la ausencia de valor.")
    print("Es distinto de 0, False o un string vacío.\n")

    codigo("""
resultado = None

print(resultado)
print(type(resultado))
""")

    salida()

    resultado = None

    print(resultado)
    time.sleep(0.3)
    print(type(resultado))

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("None se usa cuando algo todavía no tiene valor")
    print("o cuando una función no devuelve nada.\n")

    print("Para verificar si algo es None se usa 'is':\n")

    codigo("""
resultado = None

if resultado is None:
    print("No hay resultado todavía")
""")

    salida()

    if resultado is None:
        print("No hay resultado todavía")

    pausa()
    limpiar()

    titulo("LA FUNCIÓN TYPE()")

    print("type() devuelve el tipo de dato de cualquier valor.\n")

    codigo("""
print(type(42))
print(type(3.14))
print(type("hola"))
print(type(True))
print(type(None))
""")

    salida()

    print(type(42))
    time.sleep(0.2)
    print(type(3.14))
    time.sleep(0.2)
    print(type("hola"))
    time.sleep(0.2)
    print(type(True))
    time.sleep(0.2)
    print(type(None))

    pausa()
    limpiar()

    titulo("CONVERTIR ENTRE TIPOS")

    print("Python permite convertir un tipo en otro.\n")

    print("""
┌──────────┬──────────────────────────────────┐
│  int()   │  convierte a entero              │
│  float() │  convierte a decimal             │
│  str()   │  convierte a texto               │
│  bool()  │  convierte a booleano            │
└──────────┴──────────────────────────────────┘
""")

    pausa()
    limpiar()

    seccion("Ejemplos de conversión")

    codigo("""
print(int("42"))
print(float("3.14"))
print(str(100))
print(bool(0))
print(bool(1))
""")

    salida()

    print(int("42"))
    time.sleep(0.2)
    print(float("3.14"))
    time.sleep(0.2)
    print(str(100))
    time.sleep(0.2)
    print(bool(0))
    time.sleep(0.2)
    print(bool(1))

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("bool(0) es False porque 0 se considera vacío.")
    print("bool(1) es True porque cualquier número distinto de 0 es True.")
    print("\nEsto aplica también a strings y listas:")

    codigo("""
print(bool(""))
print(bool("hola"))
print(bool([]))
print(bool([1, 2]))
""")

    salida()

    print(bool(""))
    time.sleep(0.2)
    print(bool("hola"))
    time.sleep(0.2)
    print(bool([]))
    time.sleep(0.2)
    print(bool([1, 2]))

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea una variable de cada tipo:
int, float, str, bool y None.
Usa type() para imprimir el tipo de cada una.

Ejercicio 2
Convierte el string "25" a int
y el número 7 a string.
Verifica los tipos antes y después.

Ejercicio 3
Prueba qué valores se convierten en True
y cuáles en False usando bool().
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es un tipo de dato")
    print("✓ int — números enteros y operaciones")
    print("✓ float — números decimales")
    print("✓ str — texto")
    print("✓ bool — True y False")
    print("✓ None — ausencia de valor")
    print("✓ usar type() para consultar el tipo")
    print("✓ convertir entre tipos")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)
